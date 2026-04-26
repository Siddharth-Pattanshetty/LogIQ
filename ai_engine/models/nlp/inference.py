import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "logiq_model.pkl")


if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = pickle.load(open(MODEL_PATH, "rb"))


def preprocess_log(log: str):
    log = log.lower()
    log = log.strip()
    return log


def predict_nlp(log: str):
    processed_log = preprocess_log(log)

    pred = model.predict([processed_log])[0]

    try:
        prob = max(model.predict_proba([processed_log])[0])
    except:
        prob = 0.85  # fallback if not supported

    return {
        "label": pred,
        "confidence": round(float(prob), 2),
        "source": "nlp_model"
    }