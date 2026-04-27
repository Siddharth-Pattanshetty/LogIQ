from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = None
reference_vectors = None

REFERENCE_LOGS = {
    "ERROR": [
        "system failure occurred",
        "execution failed",
        "crash detected",
        "exception occurred"
    ],
    "WARNING": [
        "high latency detected",
        "retry attempts increasing",
        "timeout occurred",
        "performance degradation"
    ],
    "INFO": [
        "system running normally",
        "operation completed successfully",
        "service started"
    ]
}


def load_embeddings():
    global vectorizer, reference_vectors

    if vectorizer is None:
        vectorizer = TfidfVectorizer()

        all_texts = []
        labels = []

        for label, texts in REFERENCE_LOGS.items():
            for text in texts:
                all_texts.append(text)
                labels.append(label)

        vectors = vectorizer.fit_transform(all_texts)

        reference_vectors = {
            label: vectors[i]
            for i, label in enumerate(labels)
        }


def semantic_classify(log: str):
    load_embeddings()

    log_vec = vectorizer.transform([log])

    best_label = None
    best_score = 0

    for label, ref_vec in reference_vectors.items():
        score = cosine_similarity(log_vec, ref_vec).max()

        if score > best_score:
            best_score = score
            best_label = label

    return best_label, float(best_score)