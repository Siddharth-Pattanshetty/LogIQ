from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas.log_schema import LogRequest, LogResponse
from backend.services.hybrid_service import hybrid_predict

app = FastAPI(
    title="LogIQ API",
    description="AI-Powered Hybrid Log Intelligence System",
    version="1.0"
)

# ✅ Enable CORS (important for frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "LogIQ API is running 🚀"}


@app.post("/predict", response_model=LogResponse)
def predict_log(request: LogRequest):
    result = hybrid_predict(request.log)

    # Ensure explanation exists
    if "explanation" not in result:
        result["explanation"] = None

    return result