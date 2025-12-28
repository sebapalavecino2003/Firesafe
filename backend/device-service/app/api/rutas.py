from fastapi import APIRouter
from typing import List
from app.application.listar_dispositivos import CasoUsoListarDispositivos
from app.api.dtos import DispositivoRequest
router = APIRouter()

@router.get(
    "/devices",
    response_model=List[DispositivoRequest]
)
def listar():
    return CasoUsoListarDispositivos().ejecutar()