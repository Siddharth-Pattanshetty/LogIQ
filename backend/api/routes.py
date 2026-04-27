from fastapi import APIRouter, HTTPException
from backend.schemas.log_schema import LogRequest, BatchRequest, PredictionResponse, BatchResponse
from backend.services.hybrid_service import hybrid_predict
from backend.services.metrics_service import get_metrics
from backend.utils.logger import logger

router = APIRouter()


@router.post("/predict-log", response_model=PredictionResponse)
def predict_log(req: LogRequest):
    try:
        return hybrid_predict(req.log)
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


@router.post("/predict-batch", response_model=BatchResponse)
def predict_batch(req: BatchRequest):
    try:
        return {
            "results": [hybrid_predict(log) for log in req.logs]
        }
    except Exception as e:
        logger.error(f"Batch prediction failed: {e}")
        raise HTTPException(status_code=500, detail=f"Batch prediction failed: {str(e)}")


@router.get("/metrics")
def metrics():
    return get_metrics()