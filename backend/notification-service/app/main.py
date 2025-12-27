from fastapi import FastAPI
from app.api.rutas import router

app = FastAPI(title="Notification Service")
app.include_router(router, prefix="/api/v1")
