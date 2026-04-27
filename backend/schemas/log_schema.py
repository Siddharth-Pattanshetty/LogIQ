from pydantic import BaseModel, Field
from typing import Optional, List


class LogRequest(BaseModel):
    log: str = Field(..., min_length=1, max_length=5000, description="The log message to classify")


class BatchRequest(BaseModel):
    logs: List[str] = Field(..., min_length=1, max_length=100, description="List of log messages to classify")


class PredictionResponse(BaseModel):
    label: str = Field(..., description="Predicted severity: INFO, WARNING, or ERROR")
    confidence: float = Field(..., ge=0, le=1, description="Prediction confidence score")
    source: str = Field(..., description="Classification layer that produced the result")
    explanation: Optional[str] = Field(None, description="Human-readable explanation of the prediction")
    timestamp: Optional[str] = Field(None, description="ISO 8601 timestamp of the prediction")


class BatchResponse(BaseModel):
    results: List[PredictionResponse]