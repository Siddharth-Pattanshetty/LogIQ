from backend.services.rule_services_v2 import rule_predict_v2
from ai_engine.models.nlp.inference import predict_nlp
from backend.services.llm_service import predict_llm


def hybrid_predict(log: str):
    from backend.services.rule_services_v2 import rule_predict_v2
    from ai_engine.models.nlp.inference import predict_nlp
    from backend.services.llm_service import predict_llm

    rule_result = rule_predict_v2(log)

    if rule_result["confidence"] > 0.9:
        return rule_result

    nlp_result = predict_nlp(log)

    if nlp_result["confidence"] < 0.95:
        return predict_llm(log)

    return nlp_result