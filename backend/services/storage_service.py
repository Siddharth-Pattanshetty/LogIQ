import json
import os

from backend.utils.logger import logger

FILE_PATH = "logs/predictions.jsonl"


def save_prediction(data):
    """Append a prediction to the log file in JSON Lines format (one JSON object per line).
    This is O(1) per write — much faster than read-modify-write on a JSON array."""
    try:
        os.makedirs("logs", exist_ok=True)

        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(data) + "\n")

    except Exception as e:
        logger.error(f"Failed to save prediction: {e}")


def load_predictions():
    """Load all saved predictions from the log file."""
    predictions = []

    if not os.path.exists(FILE_PATH):
        return predictions

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        predictions.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue  # Skip corrupted lines
    except Exception as e:
        logger.error(f"Failed to load predictions: {e}")

    return predictions