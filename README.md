<p align="center">
  <h1 align="center">🧠 LogIQ — Intelligent Log Classification System</h1>
  <p align="center">
    A multi-layer hybrid log intelligence system combining <b>Rule-Based</b>, <b>NLP</b>, <b>Semantic Embedding</b>, and <b>LLM (Gemini)</b> engines for accurate log classification.
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-frontend-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Gemini-LLM-4285F4?logo=google&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/license-Apache%202.0-green" alt="License">
</p>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Installation & Setup](#️-installation--setup)
- [Running the Project](#-running-the-project)
- [API Endpoints](#-api-endpoints)
- [How the Hybrid Engine Works](#-how-the-hybrid-engine-works)
- [Dataset](#-dataset)
- [Evaluation & Results](#-evaluation--results)
- [Tech Stack](#-tech-stack)
- [Limitations](#️-limitations)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## 🔍 Overview

**LogIQ** is a hybrid log classification system that categorizes log messages into three severity levels:

```
INFO  |  WARNING  |  ERROR
```

It intelligently routes each log through up to **four classification layers**, using confidence thresholds to determine when a more powerful (but costlier) model is needed:

| Layer | Engine | Purpose |
|-------|--------|---------|
| ⚡ Layer 1 | **Rule-Based** | Fast, deterministic keyword/regex matching |
| 🧠 Layer 2 | **NLP (ML)** | TF-IDF + Logistic Regression for pattern-based classification |
| 🔗 Layer 3 | **Semantic Embedding** | TF-IDF cosine similarity against reference logs |
| 🤖 Layer 4 | **LLM (Gemini)** | Google Gemini API for complex, ambiguous logs |

This architecture **reduces LLM usage by ~70–80%** while maintaining high accuracy, making it both cost-effective and scalable.

---

## 🏗️ System Architecture

```
                        ┌──────────────┐
                        │   Log Input  │
                        └──────┬───────┘
                               │
                        ┌──────▼───────┐
                        │  Rule-Based  │ ⚡ Confidence ≥ 0.9 → Return
                        └──────┬───────┘
                               │ (uncertain)
                        ┌──────▼───────┐
                        │   NLP Model  │ 🧠 Confidence ≥ 0.7 → Return
                        └──────┬───────┘
                               │ (low confidence)
                        ┌──────▼───────┐
                        │  Embeddings  │ 🔗 Score > 0.6 → Return
                        └──────┬───────┘
                               │ (still uncertain)
                        ┌──────▼───────┐
                        │  LLM Gemini  │ 🤖 Final reasoning layer
                        └──────┬───────┘
                               │
                        ┌──────▼───────┐
                        │ NLP Fallback │ 🔄 If LLM fails or is rate-limited
                        └──────────────┘
```

---

## 📂 Project Structure

```
LogIQ/
├── ai_engine/                      # AI/ML components
│   ├── models/
│   │   └── nlp/
│   │       ├── inference.py        # NLP prediction (TF-IDF + Logistic Regression)
│   │       ├── logiq_model.pkl     # Trained model bundle
│   │       ├── model.pkl           # Standalone model file
│   │       └── vectorizer.pkl      # TF-IDF vectorizer
│   └── utils/
│       └── load_logs.py            # Hadoop log file loader & validator
│
├── backend/                        # FastAPI backend
│   ├── main.py                     # App entry point
│   ├── api/
│   │   └── routes.py               # API endpoints (/predict-log, /predict-batch, /metrics)
│   ├── rules/
│   │   └── rule_config.py          # Regex patterns & weights for rule engine
│   ├── schemas/
│   │   └── log_schema.py           # Pydantic request/response models
│   ├── services/
│   │   ├── hybrid_service.py       # 🔥 Core hybrid routing engine
│   │   ├── rule_services.py        # Rule engine v1 (basic keyword matching)
│   │   ├── rule_services_v2.py     # Rule engine v2 (weighted scoring + context rules)
│   │   ├── llm_service.py          # Gemini LLM integration
│   │   ├── embedding_service.py    # TF-IDF semantic similarity classifier
│   │   ├── cache_service.py        # In-memory prediction cache
│   │   ├── rate_limiter.py         # LLM call rate limiter (max 5 calls)
│   │   ├── metrics_service.py      # Layer usage tracking & metrics
│   │   └── storage_service.py      # Prediction persistence (JSON)
│   └── utils/
│       └── logger.py               # Logging configuration
│
├── frontend/                       # Streamlit UI
│   └── app.py                      # Interactive log analysis dashboard
│
├── evaluation/                     # Evaluation scripts
│   ├── hybrid_evaluation.py        # Full hybrid accuracy & classification report
│   └── rule_evaluation.py          # Rule-only engine evaluation
│
├── scripts/                        # Test scripts
│   ├── test_hybrid_correctness.py  # Correctness test with known labels
│   └── test_rule.py                # Random sample + custom log testing
│
├── Dataset/                        # Hadoop log dataset (55 application dirs)
│   ├── README.md                   # Dataset documentation & citations
│   └── abnormal_label.txt          # Labeled abnormal/normal job IDs
│
├── logs/                           # Runtime output
│   └── predictions.json            # Saved prediction history
│
├── .env                            # Gemini API key (not committed)
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
├── start.sh                        # Production start script
└── LICENSE                         # Apache License 2.0
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.9+
- A Google Gemini API key ([get one here](https://aistudio.google.com/app/apikey))

### Step 1: Clone the Repository

```bash
git clone https://github.com/Siddharth-Pattanshetty/LogIQ.git
cd LogIQ
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Step 5: Download Required Files

**Dataset (Hadoop Logs):**
> 📥 [Download from Google Drive](https://drive.google.com/file/d/1zrFCCohQKPjD1feFYYSNCBv8YFSI-K7P/view)
>
> Extract into the `Dataset/` directory.

**NLP Model Files** *(if not already present)*:
> 📥 [Download from Google Drive](https://drive.google.com/file/d/1F6Hn3XQ1B_GDlPHky9Ekddrk-JnaEMd9/view)
>
> Place `logiq_model.pkl` and `vectorizer.pkl` inside `ai_engine/models/nlp/`.

---

## 🚀 Running the Project

### Start the Backend API

```bash
uvicorn backend.main:app --reload
```

The API will be available at **http://127.0.0.1:8000**

📖 Interactive API docs: **http://127.0.0.1:8000/docs**

### Start the Frontend (Streamlit)

In a separate terminal:

```bash
streamlit run frontend/app.py
```

The UI will open at **http://localhost:8501**

---

## 🌐 API Endpoints

### `GET /` — Health Check

```json
{ "message": "LogIQ running 🚀", "version": "1.0.0", "docs": "/docs" }
```

### `POST /api/v1/predict-log` — Classify a Single Log

**Request:**
```json
{
  "log": "execution halted due to conflicting states"
}
```

**Response:**
```json
{
  "label": "ERROR",
  "confidence": 0.92,
  "source": "nlp_model",
  "explanation": "NLP confident prediction",
  "timestamp": "2026-04-27T15:00:00.000000"
}
```

### `POST /api/v1/predict-batch` — Classify Multiple Logs

**Request:**
```json
{
  "logs": [
    "timeout occurred",
    "system stable",
    "execution failed"
  ]
}
```

**Response:**
```json
{
  "results": [
    { "label": "WARNING", "confidence": 0.85, "source": "rule_v2", ... },
    { "label": "INFO", "confidence": 0.70, "source": "nlp_model", ... },
    { "label": "ERROR", "confidence": 0.90, "source": "rule_v2_level", ... }
  ]
}
```

### `GET /api/v1/metrics` — Layer Usage Statistics

```json
{
  "rule_usage_%": 45.0,
  "nlp_usage_%": 40.0,
  "embedding_usage_%": 10.0,
  "llm_usage_%": 5.0,
  "total_predictions": 100
}
```

---

## 🔥 How the Hybrid Engine Works

The core intelligence lies in `backend/services/hybrid_service.py`:

```python
def hybrid_predict(log):
    # 1. Check cache → return if hit
    # 2. Rule-Based (v2) → return if confidence ≥ 0.9
    # 3. NLP Model → return if confidence ≥ 0.7
    # 4. Semantic Embedding → return if similarity > 0.6
    # 5. LLM (Gemini) → used only if rate limit allows & still uncertain
    # 6. Fallback → NLP result if all else fails
```

### Smart Routing Summary

| Condition | Action | Cost |
|-----------|--------|------|
| High-confidence keywords detected | Rule engine returns immediately | ⚡ Free |
| ML model is confident | NLP returns | ⚡ Free |
| Semantically similar to reference logs | Embedding returns | ⚡ Free |
| Complex/ambiguous log | LLM (Gemini) reasons about it | 💰 API call |
| LLM fails or rate-limited | Falls back to NLP | ⚡ Free |

### Production Features

| Feature | Description |
|---------|-------------|
| 🗄️ **Caching** | In-memory cache avoids recomputation for duplicate logs |
| 🚦 **Rate Limiting** | Caps LLM calls at 5 per session to prevent quota exhaustion |
| 📊 **Metrics** | Tracks usage % across rule, NLP, and LLM layers |
| 💾 **Storage** | Persists all predictions to `logs/predictions.json` |
| 📝 **Logging** | Structured logging for debugging and auditing |

---

## 📊 Dataset

The project uses **Hadoop YARN application logs** from the [Loghub](https://github.com/logpai/loghub) collection. The dataset contains logs from a 46-core Hadoop cluster (5 machines) running WordCount and PageRank applications under normal and failure-injected conditions.

| Property | Value |
|----------|-------|
| Source | Hadoop YARN |
| Applications | WordCount, PageRank |
| Failure types | Machine down, Network disconnect, Disk full |
| Total application runs | 55 |

---

## 📈 Evaluation & Results

Run the evaluation scripts:

```bash
# Full hybrid evaluation (Rule vs NLP vs Hybrid)
python -m evaluation.hybrid_evaluation

# Rule-only evaluation
python -m evaluation.rule_evaluation

# Correctness test with known labels
python -m scripts.test_hybrid_correctness
```

### Accuracy Comparison

| Model | Accuracy |
|-------|----------|
| Rule-Based (v2) | ~0.88 |
| NLP (TF-IDF + LR) | ~1.00 |
| **Hybrid** | **~0.92–0.97** ✅ |

### Key Achievements

- ✅ Reduced LLM API usage by **~70–80%**
- ✅ Improved ERROR detection significantly
- ✅ Balanced precision and recall across all classes
- ✅ Stable fallback system prevents classification failures

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Backend API | FastAPI + Uvicorn |
| NLP Model | scikit-learn (TF-IDF + Logistic Regression) |
| LLM | Google Gemini API (`gemini-3-flash-preview`) |
| Frontend | Streamlit |
| Embeddings | TF-IDF + Cosine Similarity |
| Data Format | JSON |
| Language | Python 3.9+ |

---

## ⚠️ Limitations

- **LLM quota**: Gemini API usage is subject to rate limits and API quotas
- **NLP overfitting**: The ML model may overfit on the training dataset patterns
- **Rule tuning**: Regex patterns and weights require manual tuning for new log formats
- **In-memory state**: Cache, metrics, and rate limiter reset on server restart
- **No authentication**: API endpoints are currently unprotected

---

## 🚀 Future Improvements

- [ ] Redis-based persistent caching
- [ ] Real-world dataset labeling with human annotators
- [ ] Deployment via Docker / Render / Cloud Run
- [ ] Monitoring dashboard with Grafana
- [ ] Authentication & API key management
- [ ] Model retraining pipeline
- [ ] WebSocket support for real-time log streaming

---

## 📄 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <b>LogIQ</b> — ⚡ Speed (Rules) + 🧠 Learning (NLP) + 🔗 Similarity (Embeddings) + 🤖 Reasoning (LLM)
</p>
