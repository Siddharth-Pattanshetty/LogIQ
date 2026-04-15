# 🧠 LogIQ – Advanced Rule-Based Log Intelligence

---

# 🎯 Project Module

**Rule-Based Log Categorization Engine**

This module is the **first layer** of the LogIQ system and is responsible for fast, interpretable log classification.

---

# 🚀 Objective

To classify system logs into:

* **INFO**
* **WARNING**
* **ERROR**

using an **intelligent rule-based architecture** that mimics real-world log monitoring systems.

---

# 🏗️ System Role in LogIQ

```
Log Input
   ↓
Rule-Based Layer 
   ↓
NLP Layer 🧠 (future)
   ↓
LLM Layer 🤖 (future)
   ↓
Final Output
```

---

# 📂 Dataset

Due to large size, the dataset is **not included in this repository**.

📥 **Dataset Source:** Hadoop Log Dataset
📥 **Dataset Location (Google Drive):**
👉 ""https://drive.google.com/file/d/1zrFCCohQKPjD1feFYYSNCBv8YFSI-K7P/view?usp=sharing""


---

# 📁 Dataset Structure

```
Dataset/
   ├── application_*/
   │     ├── log files
```

Each file contains real-world distributed system logs.

---

# ⚙️ Implementation Pipeline

## 🔹 Step 1: Log Loading

📁 `ai_engine/utils/load_logs.py`

* Recursively reads all files
* Extracts raw log lines
* Removes empty or invalid entries

---

## 🔹 Step 2: Log Filtering

Only valid logs are retained:

```
YYYY-MM-DD HH:MM:SS
```

### ✔ Removes:

* Metadata
* Headers
* Noise
* Descriptions

---

## 🔹 Step 3: Preprocessing

* Convert to lowercase
* Strip unnecessary spaces
* Normalize log format

---

# 🧠 Core Engine 

📁 `backend/services/rule_service_v2.py`
📁 `backend/rules/rule_config.py`

---

# 🔥 Key Innovations 
---

## ✅ 1. Log Level Extraction (Highest Priority)

Logs already contain severity:

```
INFO / WARN / ERROR
```

### ✔ Behavior:

* Direct classification
* Skips pattern matching
* High confidence (0.9)

### 💡 Example:

```
INFO ... starting server
→ Label: INFO
```

---

## ✅ 2. Regex-Based Pattern Matching

Instead of simple keywords, **regex patterns** are used.

### 🔴 ERROR Patterns

* exception
* failed
* error
* denied
* segmentation fault
* nullpointer

---

### 🟡 WARNING Patterns

* warn
* retry
* slow
* timeout
* deprecated

---

### 🔵 INFO Patterns

* info
* start / starting / started
* running
* progress
* launch
* connected
* listening

---

## ✅ 3. Weighted Scoring System

Each category contributes differently:

| Label   | Weight |
| ------- | ------ |
| ERROR   | 3      |
| WARNING | 2      |
| INFO    | 1      |

### ✔ How it works:

* Each matched pattern adds weight
* Multiple matches increase confidence

---

## ✅ 4. Context-Aware Intelligence

Rules consider combinations of words:

### ✔ Examples:

* `retry + failed` → strong ERROR
* `ERROR + WARNING` → boost ERROR

This mimics real-world system reasoning.

---

## ✅ 5. Smart Fallback Mechanism (Critical Fix)

If no rule matches:

```
Label      : INFO
Confidence : 0.5
```

### ✔ Why:

* Prevents incorrect ERROR classification
* Ensures system stability

---

# 🔄 Full Classification Flow

```
Raw Log
   ↓
Preprocessing
   ↓
Log Level Detection 
   ↓
Regex Matching
   ↓
Score Calculation
   ↓
Context Adjustment
   ↓
Final Label + Confidence
```

---

# 📊 Output Format

```json
{
  "label": "INFO",
  "confidence": 0.9,
  "scores": {
    "ERROR": 0,
    "WARNING": 0,
    "INFO": 1
  },
  "source": "rule_v2_level"
}
```

---

# 🧪 Testing

📁 `scripts/test_rule.py`

### ✔ Features:

* Loads dataset
* Random sampling of logs
* Applies rule engine
* Displays predictions

---

# 🧪 Sample Output

```
Log:
2015-10-17 INFO IPC Server starting

Prediction:
Label      : INFO
Confidence : 0.9
Source     : rule_v2_level
```

---

# 🎯 Key Features

* ⚡ Fast (no training required)
* 🧠 Context-aware classification
* 🎯 High accuracy using log-level extraction
* 🔍 Regex-based intelligent matching
* 🧩 Modular design
* 🔄 Easily extendable rules

---

# ⚠️ Limitations

* Cannot fully understand semantic meaning
* Dependent on rule coverage
* Needs updates for new log formats
* Less effective for unseen patterns



# 🏁 Final Summary

The **Rule-Based Engine** transforms a basic keyword system into an:

> ⚡ Intelligent, context-aware, production-ready log classification engine

It serves as the **foundation layer** of LogIQ and ensures:

* Fast processing
* Reliable baseline predictions
* Strong support for advanced AI layers

---
