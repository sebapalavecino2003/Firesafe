from fastapi import APIRouter
from app.api.dtos import DispositivoRequest
from app.application.registrar_dispositivo import CasoUsoRegistrarDispositivo
from app.application.listar_dispositivos import CasoUsoListarDispositivos

router = APIRouter()

@router.post("/devices")
def registrar(dispositivo: DispositivoRequest):
    return CasoUsoRegistrarDispositivo().ejecutar(dispositivo)

@router.get("/devices")
def listar():
    return CasoUsoListarDispositivos().ejecutar()
