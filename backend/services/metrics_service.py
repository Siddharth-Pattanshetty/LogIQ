metrics = {
    "rule": 0,
    "nlp": 0,
    "embedding": 0,
    "llm": 0
}

def update_metrics(source):
    if source in metrics:
        metrics[source] += 1

def get_metrics():
    total = sum(metrics.values()) or 1

    return {
        "rule_usage_%": round(metrics["rule"] / total * 100, 2),
        "nlp_usage_%": round(metrics["nlp"] / total * 100, 2),
        "embedding_usage_%": round(metrics["embedding"] / total * 100, 2),
        "llm_usage_%": round(metrics["llm"] / total * 100, 2),
        "total_predictions": sum(metrics.values())
    }