from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from backend.services.hybrid_service import hybrid_predict

router = APIRouter()

class LogRequest(BaseModel):
    log: str


class BatchRequest(BaseModel):
    logs: List[str]

@router.post("/predict-log")
def predict_log(req: LogRequest):
    return hybrid_predict(req.log)

@router.post("/predict-batch")
def predict_batch(req: BatchRequest):
    return {
        "results": [hybrid_predict(log) for log in req.logs]
    }