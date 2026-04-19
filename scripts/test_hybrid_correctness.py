from backend.services.hybrid_service import hybrid_predict

test_cases = [
    # RULE
    ("INFO system initialized successfully", "INFO"),
    ("ERROR failed to connect to database", "ERROR"),
    ("WARN memory usage exceeded threshold", "WARNING"),
    ("INFO user login completed", "INFO"),

    # NLP
    ("connection timeout occurred while accessing remote service", "ERROR"),
    ("retry attempts increasing due to unstable network", "WARNING"),
    ("operation completed but response latency was high", "WARNING"),
    ("failed to process request due to invalid configuration", "ERROR"),

    # LLM
    ("system exhibited inconsistent behavior under normal conditions", "WARNING"),
    ("execution could not proceed due to conflicting internal states", "ERROR"),
    ("performance degradation observed without clear root cause", "WARNING"),
    ("data integrity cannot be ensured after partial transaction rollback", "ERROR"),
]

correct = 0

print("\n🧪 Running Full Hybrid Test\n")

for i, (log, expected) in enumerate(test_cases, 1):
    result = hybrid_predict(log)

    print(f"🔹 Test Case {i}")
    print(f"Log       : {log}")
    print(f"Expected  : {expected}")
    print(f"Predicted : {result['label']}")
    print(f"Source    : {result['source']}")
    print("-" * 60)

    if result["label"] == expected:
        correct += 1

accuracy = correct / len(test_cases)
print(f"\n📊 Final Accuracy: {round(accuracy, 2)}")