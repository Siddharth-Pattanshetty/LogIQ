import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        text = response.text.strip()

        label = "INFO"
        confidence = 0.5

        if "ERROR" in text:
            label = "ERROR"
        elif "WARNING" in text:
            label = "WARNING"

        for line in text.split("\n"):
            if "confidence" in line.lower():
                try:
                    confidence = float(line.split(":")[1].strip())
                except:
                    confidence = 0.5

        return {
            "label": label,
            "confidence": round(confidence, 2),
            "source": "llm_gemini",
            "explanation": text
        }

    except Exception as e:
        print("LLM ERROR:", e)

        return {
            "label": "INFO",
            "confidence": 0.5,
            "source": "llm_fallback",
            "explanation": str(e)
        }