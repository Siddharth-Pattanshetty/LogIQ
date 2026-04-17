from backend.services.rule_services_v2 import rule_predict_v2
from ai_engine.models.nlp.inference import predict_nlp


def hybrid_predict(log: str):
    log_lower = log.lower()

    rule_result = rule_predict_v2(log)

    if rule_result["label"] == "INFO" and rule_result["confidence"] > 0.85:
        # BUT check if suspicious words exist
        if any(word in log_lower for word in [
            "retry", "timeout", "slow", "latency", "delay"
        ]):
            return predict_nlp(log)
        return rule_result

    if any(word in log_lower for word in [
        "exception", "failed", "error", "denied", "crash", "fatal"
    ]):
        return predict_nlp(log)

    if any(word in log_lower for word in [
        "retry", "timeout"
    ]):
        return predict_nlp(log)

    return rule_result