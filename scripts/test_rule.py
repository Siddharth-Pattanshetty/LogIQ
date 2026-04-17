# import sys
# import os
# import random

# # Fix import path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from ai_engine.utils.load_logs import load_logs
# from backend.services.rule_services_v2 import rule_predict_v2 as rule_predict


# if __name__ == "__main__":
#     dataset_path = "D:/Softwares/LogIQ/Dataset"

#     print("Loading logs...")
#     logs = load_logs(dataset_path)

#     print(f"Total logs loaded: {len(logs)}\n")

#     # Pick 10 random logs
#     sample_size = 10
#     sample_logs = random.sample(logs, sample_size) if len(logs) >= sample_size else logs

#     # Predict and print
#     for i, log in enumerate(sample_logs):
#         result = rule_predict(log)

#         print(f"\n🔹 Log {i+1}:")
#         print(log)

#         print("🧠 Prediction:")
#         print(f"  Label      : {result['label']}")
#         print(f"  Confidence : {result['confidence']}")
#         print(f"  Source     : {result['source']}")

#         print("-" * 70)

import random
from ai_engine.utils.load_logs import load_logs
from backend.services.hybrid_service import hybrid_predict

# 🔧 CONFIG
DATASET_PATH = "Dataset"
SAMPLE_SIZE = 10


def test_hybrid():
    print("🚀 Loading logs...")
    logs = load_logs(DATASET_PATH)

    print(f"📊 Total logs loaded: {len(logs)}")

    # Select random logs
    samples = random.sample(logs, SAMPLE_SIZE)

    print("\n🧪 Running Hybrid Predictions...\n")

    for i, log in enumerate(samples, 1):
        print(f"🔹 Log {i}:")
        print(log)

        try:
            result = hybrid_predict(log)

            print("🧠 Prediction:")
            print(f"  Label      : {result.get('label', 'N/A')}")
            print(f"  Confidence : {result.get('confidence', 'N/A')}")
            print(f"  Source     : {result.get('source', 'N/A')}")

        except Exception as e:
            print("❌ Error during prediction:", str(e))

        print("-" * 80)


if __name__ == "__main__":
    test_hybrid()