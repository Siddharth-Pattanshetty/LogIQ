from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = None
reference_data = None  # List of (label, vector) tuples

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
    global vectorizer, reference_data

    if vectorizer is None:
        vectorizer = TfidfVectorizer()

        all_texts = []
        labels = []

        for label, texts in REFERENCE_LOGS.items():
            for text in texts:
                all_texts.append(text)
                labels.append(label)

        vectors = vectorizer.fit_transform(all_texts)

        # Store ALL vectors as (label, vector) tuples — fixes the bug where
        # the old dict approach overwrote entries with the same label key,
        # reducing 11 reference vectors down to just 3.
        reference_data = [
            (labels[i], vectors[i])
            for i in range(len(labels))
        ]


def semantic_classify(log: str):
    load_embeddings()

    log_vec = vectorizer.transform([log])

    best_label = None
    best_score = 0

    for label, ref_vec in reference_data:
        score = cosine_similarity(log_vec, ref_vec).max()

        if score > best_score:
            best_score = score
            best_label = label

    return best_label, float(best_score)