from pydantic import BaseModel

class DispositivoRequest(BaseModel):
    id: str
    nombre: str
    ubicacion: str
