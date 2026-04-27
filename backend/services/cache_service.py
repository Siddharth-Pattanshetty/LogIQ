import time
import threading

# In-memory cache with TTL and max size
_cache = {}
_cache_timestamps = {}
_lock = threading.Lock()

# Configuration
MAX_CACHE_SIZE = 1000
CACHE_TTL_SECONDS = 3600  # 1 hour

# Stats
_hits = 0
_misses = 0


def _evict_expired():
    """Remove entries older than TTL."""
    now = time.time()
    expired_keys = [
        key for key, ts in _cache_timestamps.items()
        if now - ts > CACHE_TTL_SECONDS
    ]
    for key in expired_keys:
        _cache.pop(key, None)
        _cache_timestamps.pop(key, None)


def _evict_lru():
    """If cache is full, remove the oldest entry."""
    if len(_cache) >= MAX_CACHE_SIZE:
        oldest_key = min(_cache_timestamps, key=_cache_timestamps.get)
        _cache.pop(oldest_key, None)
        _cache_timestamps.pop(oldest_key, None)


def get_cache(log: str) -> dict | None:
    global _hits, _misses

    with _lock:
        _evict_expired()

        if log in _cache:
            _hits += 1
            # Refresh timestamp on access (LRU behavior)
            _cache_timestamps[log] = time.time()
            return _cache[log]

        _misses += 1
        return None


def set_cache(log: str, result: dict):
    with _lock:
        _evict_lru()
        _cache[log] = result
        _cache_timestamps[log] = time.time()


def get_cache_stats() -> dict:
    total = _hits + _misses
    return {
        "cache_size": len(_cache),
        "max_size": MAX_CACHE_SIZE,
        "ttl_seconds": CACHE_TTL_SECONDS,
        "hits": _hits,
        "misses": _misses,
        "hit_rate_%": round(_hits / total * 100, 2) if total > 0 else 0.0
    }