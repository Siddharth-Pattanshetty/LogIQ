import random
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

from ai_engine.utils.load_logs import load_logs
from backend.services.rule_services_v2 import rule_predict_v2
from ai_engine.models.nlp.inference import predict_nlp
from backend.services.hybrid_service import hybrid_predict


# 🔧 CONFIG
DATASET_PATH = "Dataset"
SAMPLE_SIZE = 500


def create_labeled_data(logs):
    """
    Create pseudo-labels (independent from rule logic)
    """
    data = []

    for log in logs:
        log_lower = log.lower()

        # Remove log-level bias
        clean_log = log_lower.replace("info", "").replace("warn", "").replace("error", "")

        if any(word in clean_log for word in ["exception", "failed", "denied", "crash", "fatal"]):
            label = "ERROR"
        elif any(word in clean_log for word in ["retry", "slow", "timeout", "latency"]):
            label = "WARNING"
        else:
            label = "INFO"

        data.append((log, label))

    return data


def evaluate():
    print("🚀 Loading logs...")
    logs = load_logs(DATASET_PATH)

    print(f"📊 Total logs: {len(logs)}")

    labeled_data = create_labeled_data(logs)

    samples = random.sample(labeled_data, SAMPLE_SIZE)

    y_true = []
    y_rule = []
    y_nlp = []
    y_hybrid = []

    print("\n🧪 Running evaluation...\n")

    for log, true_label in samples:
        y_true.append(true_label)

        # Rule prediction
        rule_pred = rule_predict_v2(log)["label"]
        y_rule.append(rule_pred)

        # NLP prediction
        nlp_pred = predict_nlp(log)["label"]
        y_nlp.append(nlp_pred)

        # Hybrid prediction
        hybrid_pred = hybrid_predict(log)["label"]
        y_hybrid.append(hybrid_pred)

    # ---------------- RESULTS ---------------- #

    print("📊 ACCURACY COMPARISON")
    print("----------------------------")
    print("Rule Accuracy   :", round(accuracy_score(y_true, y_rule), 4))
    print("NLP Accuracy    :", round(accuracy_score(y_true, y_nlp), 4))
    print("Hybrid Accuracy :", round(accuracy_score(y_true, y_hybrid), 4))

    print("\n📄 CLASSIFICATION REPORT (HYBRID)\n")
    print(classification_report(y_true, y_hybrid))

    print("\n📉 CONFUSION MATRIX (HYBRID)\n")
    print(confusion_matrix(y_true, y_hybrid))


if __name__ == "__main__":
    evaluate()