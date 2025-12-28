from fastapi import APIRouter
from app.api.dtos import LoginRequest
from app.application.iniciar_sesion import CasoUsoIniciarSesion
from app.infrastructure.proveedor_jwt import generar_token

router = APIRouter()

@router.post("/login")
def login(datos: LoginRequest):
    usuario = CasoUsoIniciarSesion().ejecutar(
        datos.email,
        datos.password
    )

    token = generar_token(usuario.id)

    return {
        "token_acceso": token,
        "rol": usuario.rol
    }
