import os
from backend.utils.logger import logger

_client = None


def _get_client():
    """Lazy-initialize the Gemini client to avoid crash on import if API key is missing."""
    global _client
    if _client is None:
        from google import genai
        from dotenv import load_dotenv
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            logger.error("GEMINI_API_KEY not found in environment variables")
            raise RuntimeError("GEMINI_API_KEY not configured")

        _client = genai.Client(api_key=api_key)
    return _client


def predict_llm(log: str):
    prompt = f"""
You are an expert log analysis system.

Classify the log into one of:
INFO, WARNING, ERROR

Also provide:
- Confidence score between 0 and 1
- Short explanation

Log:
{log}

Respond STRICTLY in this format:

Label: <INFO/WARNING/ERROR>
Confidence: <0-1>
Reason: <short explanation>
"""

    try:
        client = _get_client()
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        text = response.text.strip()

        # Line-based parsing for robustness
        label = "INFO"
        confidence = 0.5
        reason = ""

        for line in text.split("\n"):
            stripped = line.strip()

            if stripped.lower().startswith("label:"):
                raw_label = stripped.split(":", 1)[1].strip().upper()
                if raw_label in ("ERROR", "WARNING", "INFO"):
                    label = raw_label

            elif stripped.lower().startswith("confidence:"):
                try:
                    confidence = float(stripped.split(":", 1)[1].strip())
                    confidence = max(0.0, min(1.0, confidence))  # Clamp to [0, 1]
                except (ValueError, IndexError):
                    confidence = 0.5

            elif stripped.lower().startswith("reason:"):
                reason = stripped.split(":", 1)[1].strip()

        return {
            "label": label,
            "confidence": round(confidence, 2),
            "source": "llm_gemini",
            "explanation": reason or text
        }

    except Exception as e:
        logger.error(f"LLM prediction failed: {e}")

        return {
            "label": "INFO",
            "confidence": 0.5,
            "source": "llm_fallback",
            "explanation": str(e)
        }