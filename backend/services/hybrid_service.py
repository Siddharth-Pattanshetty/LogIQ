from backend.services.rule_services_v2 import rule_predict_v2
from ai_engine.models.nlp.inference import predict_nlp
from backend.services.llm_service import predict_llm


def needs_llm(log: str):
    log = log.lower()

    # Complex semantic indicators
    complex_keywords = [
        "inconsistent", "unexpected behavior", "degradation",
        "instability", "conflicting", "integrity", "drift",
        "anomaly", "partial failure", "unknown issue"
    ]

    return any(word in log for word in complex_keywords)


def hybrid_predict(log: str):
    try:
        # 🔹 Step 1: Rule-based
        rule_result = rule_predict_v2(log)

        if rule_result["confidence"] >= 0.9:
            return rule_result

        # 🔹 Step 2: NLP
        nlp_result = predict_nlp(log)

        # If NLP is strong → trust it
        if nlp_result["confidence"] >= 0.85:
            return nlp_result

        # 🔹 Step 3: Decide if LLM is really needed
        if not needs_llm(log):
            return nlp_result

        # 🔹 Step 4: LLM call (controlled)
        try:
            llm_result = predict_llm(log)

            if llm_result and llm_result.get("confidence", 0) >= 0.7:
                return llm_result

        except Exception as e:
            return {
                "label": nlp_result["label"],
                "confidence": nlp_result["confidence"],
                "source": "nlp_fallback",
                "explanation": f"LLM failed: {str(e)}"
            }

        # 🔹 Final fallback
        return nlp_result

    except Exception as e:
        return {
            "label": "INFO",
            "confidence": 0.5,
            "source": "system_fallback",
            "explanation": str(e)
        }