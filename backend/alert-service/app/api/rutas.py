from fastapi import APIRouter

router = APIRouter()

@router.get("/alertas")
def listar_alertas():
    return [
        {
            "dispositivo_id": "ESP32-001",
            "severidad": "critica",
            "mensaje": "Gas elevado"
        }
    ]
