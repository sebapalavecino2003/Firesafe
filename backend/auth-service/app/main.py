from fastapi import FastAPI
from app.api.rutas import router

app = FastAPI(title="Servicio de Autenticacion")

app.include_router(router, prefix="/api/v1/autenticacion")
