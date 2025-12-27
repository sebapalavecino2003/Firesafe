from pydantic import BaseModel
from datetime import datetime

class RangoRequest(BaseModel):
    dispositivo_id: str
    desde: datetime
    hasta: datetime
