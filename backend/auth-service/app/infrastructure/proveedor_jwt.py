import jwt
from datetime import datetime, timedelta

CLAVE_SECRETA = "clave-super-secreta"
ALGORITMO = "HS256"

def generar_token(id_usuario: str) -> str:
    payload = {
        "sub": id_usuario,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, CLAVE_SECRETA, algorithm=ALGORITMO)
