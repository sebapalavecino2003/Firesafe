import jwt
from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

CLAVE_SECRETA = "clave-super-secreta"
ALGORITMO = "HS256"

security = HTTPBearer()

def validar_token(
    request: Request,
    credenciales: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        token = credenciales.credentials
        payload = jwt.decode(token, CLAVE_SECRETA, algorithms=[ALGORITMO])
        request.state.usuario_id = payload["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="Token invalido")
