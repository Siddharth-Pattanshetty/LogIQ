# 🧠 LogIQ – Hybrid Log Intelligence System (Rule + NLP + LLM)

---

# 🎯 Module Name

**Hybrid Log Classification Engine**

---

# 🚀 Overview

LogIQ is a **multi-layer intelligent log classification system** that combines:

* ⚡ Rule-Based System (fast, deterministic)
* 🧠 NLP Model (machine learning-based)
* 🤖 LLM (Gemini API for reasoning)

to classify logs into:

```text
INFO | WARNING | ERROR
```

---

# 🏗️ System Architecture

```
Log Input
   ↓
Rule-Based Layer ⚡
   ↓ (if uncertain)
NLP Layer 🧠
   ↓ (if complex / low confidence)
LLM Layer 🤖
   ↓
Final Output
```

---

# 📂 Dataset

Dataset is not included due to size.

📥 **Dataset (Hadoop Logs):**
👉 https://drive.google.com/file/d/1zrFCCohQKPjD1feFYYSNCBv8YFSI-K7P/view

---

# 🤖 NLP Model

📥 **Download Model Files:**
👉 https://drive.google.com/file/d/1F6Hn3XQ1B_GDlPHky9Ekddrk-JnaEMd9/view

### Required Files:

```text
logiq_model.pkl
vectorizer.pkl
```

### 📥 Place them here:

```
ai_engine/models/nlp/
```

---

# ⚙️ Installation & Setup

## 🔹 Step 1: Clone Project

```bash
git clone https://github.com/Siddharth-Pattanshetty/LogIQ.git
cd LogIQ
```

---

## 🔹 Step 2: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 🔹 Step 3: Install Dependencies

```bash
pip install fastapi uvicorn scikit-learn python-dotenv google-genai
```

---

# 🔐 Gemini API Setup

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# 🧠 Implementation Details

---

## 🔹 1. Rule-Based Layer ⚡

📁 `backend/services/rule_services_v2.py`

### Features:

* Log-level extraction (INFO / WARN / ERROR)
* Regex-based pattern matching
* Weighted scoring:

  * ERROR → 3
  * WARNING → 2
  * INFO → 1
* Context-aware logic:

  * `retry + failed → ERROR`
* Fallback:

  * Default → INFO (0.5)

---

### ✔ Example Rules

| Pattern           | Label   |
| ----------------- | ------- |
| exception, failed | ERROR   |
| timeout, retry    | WARNING |
| started, running  | INFO    |

---

---

## 🔹 2. NLP Layer 🧠

📁 `ai_engine/models/nlp/inference.py`

### Features:

* TF-IDF vectorization
* Logistic Regression model
* Confidence-based prediction

---

## 🔹 3. LLM Layer 🤖

📁 `backend/services/llm_service.py`

### Features:

* Gemini API (`gemini-3-flash-preview`)
* Prompt-based classification
* Returns label + explanation
* Used only for complex logs

---

## 🔹 4. Hybrid Layer 🔥

📁 `backend/services/hybrid_service.py`

---

### 🧠 Core Logic

```
1. Apply Rule-Based Classification
2. If confidence ≥ 0.9 → RETURN
3. Else apply NLP
4. If confidence ≥ 0.85 → RETURN
5. Else check complexity
6. If complex → call LLM
7. If LLM fails → fallback to NLP
```

---

### 🧩 Code Logic

```python
def hybrid_predict(log: str):
    rule = rule_predict_v2(log)

    if rule["confidence"] >= 0.9:
        return rule

    nlp = predict_nlp(log)

    if nlp["confidence"] >= 0.85:
        return nlp

    if needs_llm(log):
        try:
            return predict_llm(log)
        except:
            return nlp

    return nlp
```

---

### 🧠 Smart Routing

| Condition   | Action |
| ----------- | ------ |
| Strong rule | Rule   |
| Moderate    | NLP    |
| Complex     | LLM    |
| Failure     | NLP    |

---

# ⚡ Advanced Features (Production)

---

## ✅ Caching

* Avoid recomputation
* Faster response

---

## ✅ Rate Limiting

* Controls LLM usage
* Prevents quota exhaustion

---

## ✅ Logging

* Tracks inputs and outputs
* Helps debugging

---

## ✅ Batch API

* Multiple logs in one request

---

## ✅ Storage

* Saves predictions to:

```
logs/predictions.json
```

---

# 🌐 API Endpoints

---

## 🔹 1. Single Log

```http
POST /predict-log
```

### Request:

```json
{
  "log": "execution halted due to conflicting states"
}
```

---

## 🔹 2. Batch Logs

```http
POST /predict-batch
```

```json
{
  "logs": [
    "timeout occurred",
    "system stable",
    "execution failed"
  ]
}
```

---

# 🚀 Run the Project

```bash
uvicorn backend.main:app --reload
```

---

# 🌐 Open API Docs

```
http://127.0.0.1:8000/docs
```

---

# 📊 Results

| Model      | Accuracy     |
| ---------- | ------------ |
| Rule-Based | ~0.88        |
| NLP        | ~1.00        |
| Hybrid     | ~0.92–0.97 ✅ |

---

# 🎯 Key Achievements

* Reduced LLM usage by ~70–80%
* Improved ERROR detection significantly
* Balanced precision and recall
* Stable fallback system

---

# ⚠️ Limitations

* LLM depends on API quota
* NLP may overfit
* Rules need tuning

---

# 🚀 Future Improvements

* Redis caching
* Real dataset labeling
* Deployment (Render/Docker)
* Monitoring dashboard

---

# 🏁 Conclusion

LogIQ successfully combines:

> ⚡ Speed (Rules) + 🧠 Learning (NLP) + 🤖 Reasoning (LLM)

to build a **robust, scalable log intelligence system**.

---
