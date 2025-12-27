from fastapi import APIRouter
from app.api.dtos import AlertaResponse

router = APIRouter()

@router.get("/alertas")
def listar_alertas():
    # mock inicial
    return [
        AlertaResponse(
            dispositivo_id="ESP32-001",
            severidad="critica",
            mensaje="Gas elevado"
        )
    ]
