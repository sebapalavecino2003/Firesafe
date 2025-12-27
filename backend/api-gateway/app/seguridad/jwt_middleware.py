import jwt
from fastapi import Request, HTTPException

CLAVE_SECRETA = "clave-super-secreta"
ALGORITMO = "HS256"

def validar_token(request: Request):
    auth = request.headers.get("Authorization")
    if not auth:
        raise HTTPException(status_code=401, detail="Token requerido")

    try:
        token = auth.replace("Bearer ", "")
        payload = jwt.decode(token, CLAVE_SECRETA, algorithms=[ALGORITMO])
        request.state.usuario_id = payload["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="Token invalido")
