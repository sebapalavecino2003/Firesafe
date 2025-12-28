from fastapi import FastAPI
from app.api.rutas import router

app = FastAPI(title="Alert Service")
app.include_router(router, prefix="/api/v1")
