from pydantic import BaseModel
from typing import Optional


class LogRequest(BaseModel):
    log: str


class LogResponse(BaseModel):
    label: str
    confidence: float
    source: str
    explanation: Optional[str] = None