import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def predict_llm(log: str):
    prompt = f"""
You are an expert in system log analysis.

Classify the following log into one of:
INFO, WARNING, ERROR

Also give a short reason.

Log:
{log}

Output format:
Label: <INFO/WARNING/ERROR>
Reason: <short explanation>
"""

    try:
        response = model.generate_content(prompt)
        output = response.text

        label = "INFO"
        if "ERROR" in output:
            label = "ERROR"
        elif "WARNING" in output:
            label = "WARNING"

        return {
            "label": label,
            "confidence": 0.85,
            "source": "llm_gemini",
            "explanation": output.strip()
        }

    except Exception as e:
        return {
            "label": "INFO",
            "confidence": 0.5,
            "source": "llm_fallback",
            "error": str(e)
        }

