from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="LogIQ API")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "LogIQ running 🚀"}