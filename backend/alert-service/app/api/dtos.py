from pydantic import BaseModel

class AlertaResponse(BaseModel):
    dispositivo_id: str
    severidad: str
    mensaje: str
