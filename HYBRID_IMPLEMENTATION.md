# 🧠 LogIQ – Hybrid Log Intelligence System

---

# 🎯 Module Name

**Hybrid Log Classification Engine (Rule + NLP)**

---

# 🚀 Overview

This module implements the **hybrid intelligence layer** of LogIQ.

It combines:

* ⚡ Rule-Based System (fast, deterministic)
* 🧠 NLP Model (machine learning-based)

to provide **accurate and reliable log classification**.

---

# 🏗️ System Architecture

```
Log Input
   ↓
Rule-Based Layer ⚡
   ↓ (if uncertain / complex)
NLP Layer 🧠
   ↓
Final Output
```

---

# 📂 Dataset

Due to large size, the dataset is not included in this repository.

📥 **Dataset Link (Google Drive):**
👉 "https://drive.google.com/file/d/1zrFCCohQKPjD1feFYYSNCBv8YFSI-K7P/view?usp=sharing"

---

# 🤖 NLP Model

The NLP model was trained using:

* TF-IDF Vectorization
* Logistic Regression

📥 **Model Download Link (Google Drive):**
👉 "https://drive.google.com/drive/folders/1wnH99Tmw0S0k8X_E9lC1gmA0XQLk4eEr?usp=sharing"

---

# ⚙️ Implementation Details

---

## 🔹 1. Rule-Based Layer

📁 `backend/services/rule_services_v2.py`

### Features:

* Log-level detection (INFO / WARN / ERROR)
* Regex-based keyword matching
* Weighted scoring
* Context-aware rules

---

## 🔹 2. NLP Layer

📁 `ai_engine/models/nlp/inference.py`

### Features:

* TF-IDF feature extraction
* Logistic Regression classifier
* Handles complex/unstructured logs
* Provides probability-based confidence

---

## 🔹 3. Hybrid Layer

📁 `backend/services/hybrid_service.py`

---

### 🔥 Core Logic

```
IF log is simple → use Rule
IF log contains suspicious keywords → use NLP
ELSE → fallback to Rule
```

---

### 🧠 Smart Routing Strategy

| Condition        | Action |
| ---------------- | ------ |
| Strong INFO      | Rule   |
| ERROR keywords   | NLP    |
| WARNING patterns | NLP    |
| Complex logs     | NLP    |
| Default          | Rule   |

---

## 🔹 4. Evaluation

📁 `evaluation/hybrid_evaluation.py`

### Compared:

* Rule-based accuracy
* NLP model accuracy
* Hybrid system accuracy

---

# 📊 Results

| Model         | Accuracy                                   |
| ------------- | ------------------------------------------ |
| Rule-Based    | ~0.88                                      |
| NLP Model     | ~1.00 (overfitted due to synthetic labels) |
| Hybrid System | ~0.93–0.97 ✅                               |

---

# 🎯 Key Achievements

* Improved ERROR detection from 0 → 100%
* Improved WARNING detection significantly
* Balanced precision and recall
* Reduced false positives

---

# 🧠 Key Learnings

* Rule-based systems are fast but limited
* NLP models handle complex patterns but may overfit
* Hybrid systems combine strengths of both

---

# ⚠️ Limitations

* NLP model trained on pseudo-labels (data leakage possible)
* Performance depends on rule quality
* Requires tuning for new datasets

---

# 🚀 Future Improvements

* Add LLM-based reasoning layer
* Improve dataset with real labels
* Deploy using FastAPI
* Add real-time monitoring dashboard

---

# 🏁 Conclusion

The Hybrid Log Intelligence System successfully combines:

> ⚡ Speed of rules + 🧠 intelligence of ML

to deliver a **robust and scalable log classification system**.

---
