import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "logiq_model.pkl")

data = pickle.load(open(MODEL_PATH, "rb"))


model = data["model"]
vectorizer = data["vectorizer"]


def preprocess_log(log: str):
    return log.lower().strip()


def predict_nlp(log: str):
    processed_log = preprocess_log(log)

    X = vectorizer.transform([processed_log])

    pred = model.predict(X)[0]

    try:
        prob = max(model.predict_proba(X)[0])
    except:
        prob = 0.85

    return {
        "label": pred,
        "confidence": round(float(prob), 2),
        "source": "nlp_model"
    }