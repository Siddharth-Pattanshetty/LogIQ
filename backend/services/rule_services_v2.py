import re
from backend.rules.rule_config import RULES


def preprocess_log(log):
    log = log.lower().strip()
    return log


def calculate_score(log):
    scores = {
        "ERROR": 0,
        "WARNING": 0,
        "INFO": 0
    }

    for label, rule in RULES.items():
        for pattern in rule["patterns"]:
            if re.search(pattern, log):
                scores[label] += rule["weight"]

    return scores


def apply_context_rules(log, scores):

    if scores["ERROR"] > 0 and scores["WARNING"] > 0:
        scores["ERROR"] += 1

    if "retry" in log and "failed" in log:
        scores["ERROR"] += 2

    return scores


def get_final_label(scores):
    total = sum(scores.values())

    if total == 0:
        return "INFO", 0.5   

    label = max(scores, key=scores.get)
    confidence = scores[label] / total

    return label, round(confidence, 2)
    label = max(scores, key=scores.get)
    total = sum(scores.values())

    confidence = scores[label] / total if total > 0 else 0

    return label, round(confidence, 2)

def extract_log_level(log):
    if " error " in log:
        return "ERROR"
    elif " warn " in log:
        return "WARNING"
    elif " info " in log:
        return "INFO"
    return None

def rule_predict_v2(log):
    log = preprocess_log(log)

    level = extract_log_level(log)
    if level:
        return {
            "label": level,
            "confidence": 0.9,   
            "scores": {},
            "source": "rule_v2_level"
        }

    scores = calculate_score(log)

    scores = apply_context_rules(log, scores)

    label, confidence = get_final_label(scores)

    return {
        "label": label,
        "confidence": confidence,
        "scores": scores,
        "source": "rule_v2"
    }