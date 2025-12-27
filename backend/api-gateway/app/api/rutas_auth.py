from fastapi import APIRouter
from app.infraestructura.proxy_http import reenviar_request

router = APIRouter()

AUTH_SERVICE_URL = "http://servicio-autenticacion:8000"

@router.post("/login")
async def login(payload: dict):
    status, data = await reenviar_request(
        "POST",
        f"{AUTH_SERVICE_URL}/api/v1/autenticacion/login",
        json=payload
    )
    return data
