import random
from ai_engine.utils.load_logs import load_logs
from backend.services.hybrid_service import hybrid_predict

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

            if result.get("source") in ["llm_gemini", "llm"]:
                print("\n💡 Explanation:")
                print(result.get("explanation", "No explanation available"))

        except Exception as e:
            print("❌ Error during prediction:", str(e))

        print("-" * 80)


def test_custom_logs():
  
    print("\n🧪 Testing Custom Logs...\n")

    test_logs = [
        "disk failure occurred during read operation",
        "connection timeout while fetching data",
        "retrying request due to slow response",
        "null pointer exception in module",
        "system running normally"
    ]

    for i, log in enumerate(test_logs, 1):
        print(f"🔹 Custom Log {i}:")
        print(log)

        try:
            result = hybrid_predict(log)

            print("🧠 Prediction:")
            print(f"  Label      : {result.get('label', 'N/A')}")
            print(f"  Confidence : {result.get('confidence', 'N/A')}")
            print(f"  Source     : {result.get('source', 'N/A')}")

            if result.get("source") in ["llm_gemini", "llm"]:
                print("\n💡 Explanation:")
                print(result.get("explanation", "No explanation available"))

        except Exception as e:
            print("❌ Error:", str(e))

        print("-" * 80)


if __name__ == "__main__":
    test_hybrid()

    test_custom_logs()