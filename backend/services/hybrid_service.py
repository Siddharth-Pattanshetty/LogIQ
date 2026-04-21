from datetime import datetime

from backend.services.rule_services_v2 import rule_predict_v2
from ai_engine.models.nlp.inference import predict_nlp
from backend.services.llm_service import predict_llm

from backend.services.cache_service import get_cache,set_cache
from backend.services.rate_limiter import can_call_llm,increment_llm_calls
from backend.services.storage_service import save_prediction
from backend.utils.logger import logger


def needs_llm(log: str):
    complex_keywords = [
        "inconsistent", "unexpected behavior", "degradation",
        "instability", "conflicting", "integrity", "drift",
        "anomaly", "partial failure", "unknown issue"
    ]

    return any(k in log.lower() for k in complex_keywords)

def format_response(result, explanation=""):
    return {
        "label": result.get("label"),
        "confidence": result.get("confidence"),
        "source": result.get("source"),
        "explanation": explanation,
        "timestamp": datetime.utcnow().isoformat()
    }

def hybrid_predict(log: str):
    logger.info(f"Input: {log}")

    cached = get_cache(log)
    if cached:
        logger.info("Cache hit")
        return cached

    rule_result = rule_predict_v2(log)
    if rule_result["confidence"] >= 0.9:
        response = format_response(rule_result, "Rule-based decision")
        set_cache(log, response)
        save_prediction(response)
        return response

    nlp_result = predict_nlp(log)
    if nlp_result["confidence"] >= 0.85:
        response = format_response(nlp_result, "NLP confident prediction")
        set_cache(log, response)
        save_prediction(response)
        return response

    if needs_llm(log) and can_call_llm():
        try:
            increment_llm_calls()
            llm_result = predict_llm(log)

            response = format_response(
                llm_result,
                llm_result.get("explanation", "LLM reasoning")
            )

            set_cache(log, response)
            save_prediction(response)
            return response

        except Exception as e:
            logger.error(f"LLM failed: {e}")

    response = format_response(nlp_result, "Fallback to NLP")
    set_cache(log, response)
    save_prediction(response)
    return response