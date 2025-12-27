from fastapi import APIRouter, Depends, Request
from app.seguridad.jwt_middleware import validar_token
from app.infraestructura.proxy_http import reenviar_request

router = APIRouter()

DEVICE_SERVICE_URL = "http://device-service:8000"

@router.get("/devices", dependencies=[Depends(validar_token)])
async def listar_dispositivos(request: Request):
    headers = {
        "X-Usuario-Id": request.state.usuario_id
    }
    status, data = await reenviar_request(
        "GET",
        f"{DEVICE_SERVICE_URL}/api/v1/devices",
        headers=headers
    )
    return data
