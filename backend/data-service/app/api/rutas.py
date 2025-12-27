from fastapi import APIRouter
from app.api.dtos import RangoRequest
from app.application.consultar_historico import CasoUsoConsultarHistorico
from app.application.calcular_metricas import CasoUsoCalcularMetricas

router = APIRouter()

@router.post("/historico")
def historico(rango: RangoRequest):
    lecturas = CasoUsoConsultarHistorico().ejecutar(
        rango.dispositivo_id, rango.desde, rango.hasta
    )
    return CasoUsoCalcularMetricas().ejecutar(lecturas)
