from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

reference_logs = {
    "ERROR": [
        "system failure occurred",
        "execution failed due to error",
        "crash detected in service"
    ],
    "WARNING": [
        "performance degradation detected",
        "retry attempts increasing",
        "timeout occurred"
    ],
    "INFO": [
        "system running normally",
        "operation completed successfully"
    ]
}

ref_embeddings = {
    label: model.encode(texts)
    for label, texts in reference_logs.items()
}


def semantic_classify(log: str):
    log_emb = model.encode([log])

    best_label = None
    best_score = 0

    for label, embeddings in ref_embeddings.items():
        sim = cosine_similarity(log_emb, embeddings).max()

        if sim > best_score:
            best_score = sim
            best_label = label

    return best_label, float(best_score)