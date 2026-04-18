# 🧠 LogIQ – Hybrid Log Intelligence System (Rule + NLP + LLM)

---

# 🎯 Module Name

**Hybrid Log Classification Engine (Rule + NLP + LLM)**

---

# 🚀 Overview

This module implements the **multi-layer hybrid intelligence system** of LogIQ.

It combines:

* ⚡ Rule-Based System (fast, deterministic)
* 🧠 NLP Model (machine learning-based)
* 🤖 LLM (Gemini API for reasoning)

to provide **accurate, scalable, and intelligent log classification**.

---

# 🏗️ System Architecture

```
Log Input
   ↓
Rule-Based Layer ⚡
   ↓ (if uncertain)
NLP Layer 🧠
   ↓ (if still uncertain)
LLM Layer 🤖 (Gemini)
   ↓
Final Output
```

---

# 📂 Dataset

Due to large size, the dataset is not included in this repository.

📥 **Dataset Link (Google Drive):**
👉 "https://drive.google.com/file/d/1zrFCCohQKPjD1feFYYSNCBv8YFSI-K7P/view"

---

# 🤖 NLP Model

The NLP model was trained using:

* TF-IDF Vectorization
* Logistic Regression
* Class balancing (`class_weight='balanced'`)

📥 **Model Download Link (Google Drive):**
👉 "https://drive.google.com/drive/folders/1wnH99Tmw0S0k8X_E9lC1gmA0XQLk4eEr"
---

# 🤖 LLM Integration (Gemini API)

The system uses:

* Google Gemini API (`gemini-1.5-flash`)
* Secure API key stored in `.env`
* Prompt-based reasoning for classification

### Features:

* Handles ambiguous/unseen logs
* Provides explanations
* Acts as fallback layer

---

# ⚙️ Implementation Details

---

## 🔹 1. Rule-Based Layer

📁 `backend/services/rule_services_v2.py`

### Features:

* Log-level detection (INFO / WARN / ERROR)
* Regex-based keyword matching
* Weighted scoring system
* Context-aware classification
* Fast execution (no computation overhead)

---

## 🔹 2. NLP Layer

📁 `ai_engine/models/nlp/inference.py`

### Features:

* TF-IDF feature extraction
* Logistic Regression classifier
* Handles semi-structured logs
* Probability-based confidence scoring

---

## 🔹 3. LLM Layer (Gemini)

📁 `backend/services/llm_service.py`

### Features:

* Prompt-based classification
* Semantic understanding of logs
* Generates reasoning/explanation
* Used only when rule + NLP are insufficient

---

## 🔹 4. Hybrid Layer

📁 `backend/services/hybrid_service.py`

---

### 🔥 Core Logic (Actual Implementation)

```
1. Apply Rule-Based Classification
2. If rule confidence > 0.9 → return rule result
3. Else apply NLP model
4. If NLP confidence < 0.95 → use LLM (Gemini)
5. Else → return NLP result
```

---

### 🧠 Smart Routing Strategy

| Condition                      | Action |
| ------------------------------ | ------ |
| High confidence rule           | Rule ⚡ |
| Moderate complexity            | NLP 🧠 |
| Low NLP confidence / ambiguous | LLM 🤖 |
| Default fallback               | NLP    |

---

### 🧩 Hybrid Code Logic

```python
rule_result = rule_predict_v2(log)

if rule_result["confidence"] > 0.9:
    return rule_result

nlp_result = predict_nlp(log)

if nlp_result["confidence"] < 0.95:
    return predict_llm(log)

return nlp_result
```

---

## 🔹 5. Evaluation

📁 `evaluation/hybrid_evaluation.py`

### Compared:

* Rule-based accuracy
* NLP model accuracy
* Hybrid system accuracy

---

# 📊 Results

| Model         | Accuracy                        |
| ------------- | ------------------------------- |
| Rule-Based    | ~0.88                           |
| NLP Model     | ~1.00 (due to synthetic labels) |
| Hybrid System | ~0.92–0.97 ✅                    |

---

# 🎯 Key Achievements

* Improved ERROR detection from 0 → near 100%
* Improved WARNING detection significantly
* Balanced precision and recall
* Reduced false positives using hybrid routing
* Integrated LLM for reasoning-based classification

---

# 🧠 Key Learnings

* Rule-based systems are fast but limited
* NLP models capture patterns but may overfit
* LLMs provide reasoning but are costly
* Hybrid systems combine all strengths effectively

---


# 🏁 Conclusion

The Hybrid Log Intelligence System successfully combines:

> ⚡ Speed of rules + 🧠 pattern learning + 🤖 reasoning

to deliver a **robust, scalable, and intelligent log classification system**.

---
