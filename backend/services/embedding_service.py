from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = None

REFERENCE = {
    "ERROR": [
        "system failure occurred",
        "execution failed",
        "crash detected"
    ],
    "WARNING": [
        "high latency detected",
        "retry attempts increasing",
        "timeout occurred"
    ],
    "INFO": [
        "system running normally",
        "operation successful"
    ]
}

ref_emb = None


def load_model():
    global model, ref_emb

    if model is None:
        model = SentenceTransformer('all-MiniLM-L6-v2')

        ref_emb = {
            k: model.encode(v)
            for k, v in REFERENCE.items()
        }


def semantic_classify(log):
    load_model()  # 🔥 LAZY LOAD

    emb = model.encode([log])

    best_label = None
    best_score = 0

    for label, vectors in ref_emb.items():
        score = cosine_similarity(emb, vectors).max()

        if score > best_score:
            best_score = score
            best_label = label

    return best_label, float(best_score)