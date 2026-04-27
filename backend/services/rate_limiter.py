import time
import os

# Configuration — can be overridden via environment variables
LLM_CALL_LIMIT = int(os.getenv("LLM_CALL_LIMIT", "5"))
LLM_WINDOW_SECONDS = int(os.getenv("LLM_WINDOW_SECONDS", "60"))

# Timestamps of recent LLM calls
_llm_call_timestamps = []


def can_call_llm() -> bool:
    """Check if LLM can be called within the current time window."""
    _cleanup_expired()
    return len(_llm_call_timestamps) < LLM_CALL_LIMIT


def increment_llm_calls():
    """Record an LLM call timestamp."""
    _llm_call_timestamps.append(time.time())


def _cleanup_expired():
    """Remove timestamps outside the current time window."""
    global _llm_call_timestamps
    now = time.time()
    _llm_call_timestamps = [
        t for t in _llm_call_timestamps
        if now - t < LLM_WINDOW_SECONDS
    ]


def reset_rate_limiter():
    """Reset the rate limiter — useful for testing."""
    global _llm_call_timestamps
    _llm_call_timestamps = []