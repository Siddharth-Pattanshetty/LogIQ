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
   ↓ (if complex / low confidence)
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
👉 "https://drive.google.com/file/d/1F6Hn3XQ1B_GDlPHky9Ekddrk-JnaEMd9/view?usp=sharing"

---

# 🤖 LLM Integration (Gemini API)

The system uses:

* Google Gemini API (`gemini-3-flash-preview`)
* Secure API key stored in `.env`
* Prompt-based reasoning for classification

### Features:

* Handles ambiguous/unseen logs
* Provides explanations
* Used selectively to reduce cost

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
* Called only for complex cases

---

## 🔹 4. Hybrid Layer

📁 `backend/services/hybrid_service.py`

---

### 🔥 Updated Core Logic (Production-Ready)

```
1. Apply Rule-Based Classification
2. If rule confidence ≥ 0.9 → return rule result
3. Else apply NLP model
4. If NLP confidence ≥ 0.85 → return NLP result
5. Else check if log is complex (semantic keywords)
6. If complex → call LLM
7. If LLM fails → fallback to NLP
8. Return final result
```

---

### 🧠 Smart Routing Strategy

| Condition                 | Action       |
| ------------------------- | ------------ |
| Strong rule match         | Rule ⚡       |
| Moderate / structured log | NLP 🧠       |
| Complex / ambiguous log   | LLM 🤖       |
| LLM failure / quota issue | NLP fallback |
| Default                   | NLP          |

---

### 🧩 Hybrid Code Logic (Improved)

```python
def needs_llm(log: str):
    log = log.lower()

    keywords = [
        "inconsistent", "instability", "degradation",
        "conflicting", "integrity", "drift",
        "anomaly", "unexpected", "partial failure"
    ]

    return any(k in log for k in keywords)


def hybrid_predict(log: str):
    rule_result = rule_predict_v2(log)

    if rule_result["confidence"] >= 0.9:
        return rule_result

    nlp_result = predict_nlp(log)

    if nlp_result["confidence"] >= 0.85:
        return nlp_result

    if needs_llm(log):
        try:
            return predict_llm(log)
        except:
            return nlp_result

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
| NLP Model     | ~1.00 (synthetic bias possible) |
| Hybrid System | ~0.92–0.97 ✅                    |

---

# 🎯 Key Achievements

* Improved ERROR detection significantly
* Improved WARNING classification accuracy
* Reduced unnecessary LLM calls (~70–80%)
* Stable fallback system (no crashes on API failure)
* Balanced precision and recall

---

# 🧠 Key Learnings

* Rule-based systems are fast but limited
* NLP models capture patterns but lack deep reasoning
* LLMs provide reasoning but are costly and unstable
* Smart routing is critical for real-world systems

---

# ⚠️ Limitations

* LLM depends on API quota and availability
* NLP trained on limited dataset (may overfit)
* Rule-based logic requires manual tuning

---

# 🚀 Future Improvements

* Add caching layer (L1/L2)
* Use embeddings for semantic similarity
* Improve dataset with real-world labels
* Deploy with FastAPI
* Build frontend dashboard for monitoring

---

# 🏁 Conclusion

The Hybrid Log Intelligence System successfully combines:

> ⚡ Rule-based speed + 🧠 NLP learning + 🤖 LLM reasoning

to deliver a **robust, efficient, and scalable log classification system** suitable for real-world applications.

---
