from fastapi import FastAPI
from app.api import rutas_auth, rutas_devices

app = FastAPI(title="API Gateway")

app.include_router(rutas_auth.router, prefix="/api/v1/auth")
app.include_router(rutas_devices.router, prefix="/api/v1")
