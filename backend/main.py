from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router
from backend.utils.logger import logger

app = FastAPI(
    title="LogIQ API",
    description="Hybrid Log Intelligence System — Rule + NLP + Embedding + LLM",
    version="1.0.0"
)

# CORS middleware for cross-origin frontend support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routes with API version prefix
app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
def startup_event():
    """Pre-load models and embeddings on startup instead of first request."""
    logger.info("LogIQ starting up...")

    try:
        from ai_engine.models.nlp.inference import predict_nlp
        logger.info("NLP model loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load NLP model: {e}")

    try:
        from backend.services.embedding_service import load_embeddings
        load_embeddings()
        logger.info("Embedding vectors loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load embeddings: {e}")

    logger.info("LogIQ ready 🚀")


@app.get("/")
def home():
    return {"message": "LogIQ running 🚀", "version": "1.0.0", "docs": "/docs"}