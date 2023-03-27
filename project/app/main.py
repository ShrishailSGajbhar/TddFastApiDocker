from fastapi import FastAPI, Depends
from app.config import get_settings, Settings
app = FastAPI()


@app.get("/")
def index():
    return {"message": "Learning Test driven developement using FastAPI, pytest & Docker. Next try with route '/ping'."}


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!!",
        "environment": settings.environment,
        "testing": settings.testing
    }
