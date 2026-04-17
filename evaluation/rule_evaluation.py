import random
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
from ai_engine.utils.load_logs import load_logs
from backend.services.rule_services_v2 import rule_predict_v2

SAMPLE_SIZE=500

def create_labeled_data(logs):
    data = []

    for log in logs:
        log_lower = log.lower()

        log_clean = log_lower.replace("info", "").replace("warn", "").replace("error", "")

        if any(word in log_clean for word in ["exception", "failed", "denied"]):
            label = "ERROR"
        elif any(word in log_clean for word in ["retry", "slow", "timeout"]):
            label = "WARNING"
        else:
            label = "INFO"

        data.append((log, label))

    return data

def evaluate_rule_engine():
    print("Loading logs...")
    dataset_path = "D:/Softwares/LogIQ/Dataset"
    logs = load_logs(dataset_path)

    print(f"Total logs: {len(logs)}")

    labeled_data = create_labeled_data(logs)

    sampled_data = random.sample(labeled_data, min(SAMPLE_SIZE, len(labeled_data)))

    y_true = []
    y_pred = []

    for log, true_label in sampled_data:
        result = rule_predict_v2(log)
        pred_label = result["label"]

        y_true.append(true_label)
        y_pred.append(pred_label)

    print("\n📊 Evaluation Results\n")

    print("Accuracy:", accuracy_score(y_true, y_pred))

    print("\nClassification Report:\n")
    print(classification_report(y_true, y_pred))

    print("\nConfusion Matrix:\n")
    print(confusion_matrix(y_true, y_pred))


if __name__ == "__main__":
    evaluate_rule_engine()