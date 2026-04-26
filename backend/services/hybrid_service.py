from datetime import datetime

from backend.services.rule_services_v2 import rule_predict_v2
from ai_engine.models.nlp.inference import predict_nlp
from backend.services.embedding_service import semantic_classify
from backend.services.llm_service import predict_llm


from backend.services.cache_service import get_cache, set_cache
from backend.services.rate_limiter import can_call_llm, increment_llm_calls
from backend.services.metrics_service import update_metrics
from backend.services.storage_service import save_prediction
from backend.utils.logger import logger


def format_response(result, explanation=None):
    return {
        "label": result.get("label"),
        "confidence": round(float(result.get("confidence", 0)), 2),
        "source": result.get("source"),
        "explanation": explanation,
        "timestamp": datetime.utcnow().isoformat()
    }

def hybrid_predict(log: str):
    try:
        logger.info(f"Incoming log: {log}")

        cached = get_cache(log)
        if cached:
            logger.info("Cache hit")
            return cached

        rule_result = rule_predict_v2(log)

        if rule_result["confidence"] >= 0.9:
            update_metrics("rule")

            response = format_response(
                rule_result,
                "High confidence rule-based classification"
            )

            set_cache(log, response)
            save_prediction(response)
            return response

        nlp_result = predict_nlp(log)

        if nlp_result["confidence"] >= 0.7:
            update_metrics("nlp")

            response = format_response(
                nlp_result,
                "NLP confident prediction"
            )

            set_cache(log, response)
            save_prediction(response)
            return response

        label, score = semantic_classify(log)

        if score > 0.65:
            update_metrics("embedding")

            response = format_response(
                {
                    "label": label,
                    "confidence": score,
                    "source": "embedding"
                },
                f"Semantic similarity match (score={round(score,2)})"
            )

            set_cache(log, response)
            save_prediction(response)
            return response

        if can_call_llm() and score < 0.6:
            try:
                increment_llm_calls()

                llm_result = predict_llm(log)
                update_metrics("llm")

                response = format_response(
                    llm_result,
                    llm_result.get("explanation", "LLM reasoning")
                )

                set_cache(log, response)
                save_prediction(response)
                return response

            except Exception as e:
                logger.error(f"LLM failed: {e}")

        # =========================
        # 🔹 STEP 5: FINAL FALLBACK
        # =========================
        update_metrics("nlp")

        response = format_response(
            nlp_result,
            "Fallback to NLP (LLM unavailable or low confidence)"
        )

        set_cache(log, response)
        save_prediction(response)
        return response

    except Exception as e:
        logger.error(f"System error: {e}")

        return format_response(
            {"label": "INFO", "confidence": 0.5, "source": "system"},
            str(e)
        )