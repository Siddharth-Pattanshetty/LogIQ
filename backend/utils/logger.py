import os
import logging

# Log level is configurable via environment variable (default: INFO)
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("LogIQ")

# Add file handler to persist logs to disk
try:
    os.makedirs("logs", exist_ok=True)
    file_handler = logging.FileHandler("logs/logiq.log", encoding="utf-8")
    file_handler.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(file_handler)
except Exception:
    pass  # Don't crash if log directory can't be created