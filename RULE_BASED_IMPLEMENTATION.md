# 🧠 LogIQ – Rule-Based Log Categorization

## 📌 Overview

This module implements the **Rule-Based Layer** of the LogIQ system.
It classifies logs into:

* INFO
* WARNING
* ERROR

based on predefined regex patterns.

---

## 📂 Dataset

Due to large size, the dataset is **not included in this repository**.

📥 Dataset Location (Google Drive):
👉"https://drive.google.com/file/d/1zrFCCohQKPjD1feFYYSNCBv8YFSI-K7P/view?usp=sharing"

---

## 📁 Dataset Structure

The dataset contains Hadoop logs organized as:

```
Dataset/
   ├── application_*/
   │     ├── log files
```

Each file contains raw system logs generated from distributed Hadoop applications.

---

## ⚙️ Implementation Steps

### 1️⃣ Load Logs

Logs are loaded recursively from all files using:

```
ai_engine/utils/load_logs.py
```

* Traverses dataset directory
* Reads all log files
* Filters valid log lines

---

### 2️⃣ Log Filtering

Only logs starting with a timestamp are selected:

```
YYYY-MM-DD ...
```

This removes:

* Dataset descriptions
* Headers
* Application IDs
* Empty or irrelevant lines

---

### 3️⃣ Rule-Based Classification

Implemented in:

```
backend/services/rule_service.py
```

#### Classification Rules:

* **ERROR**

  * error
  * exception
  * failed
  * fatal
  * denied

* **WARNING**

  * warn
  * retry
  * slow
  * deprecated

* **INFO**

  * info
  * default fallback

Each log is converted to lowercase and matched using regex patterns.

---

### 4️⃣ Testing

Testing is performed using:

```
scripts/test_rule.py
```

* Loads dataset
* Randomly samples logs
* Applies rule-based classification
* Prints predictions

---

## 🧪 Example Output

```
Log:
2015-10-17 15:40:12,123 ERROR Task failed due to disk issue

Prediction:
Label      : ERROR
Confidence : 0.9
Source     : rule
```

---

## 🎯 Key Features

* Fast and lightweight classification
* No training required
* Handles majority of common log patterns
* Simple and interpretable logic
* Forms the first layer of hybrid system

---

## ⚠️ Limitations

* Cannot handle unseen or complex logs
* Limited to predefined patterns
* Accuracy depends on rule coverage

---

## 🚀 Next Steps

* Add NLP-based classification layer
* Integrate embedding similarity search
* Introduce LLM-based reasoning
* Build hybrid decision pipeline

---

## 🏁 Summary

This module completes the **Rule-Based Layer** of LogIQ, providing a fast and effective baseline for log classification.
It serves as the foundation for building a scalable AI-powered log intelligence system.
