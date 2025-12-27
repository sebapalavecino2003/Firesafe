from datetime import datetime

class LecturaSensor:
    def __init__(self, dispositivo_id: str, temperatura: float, gas: int, timestamp: datetime):
        self.dispositivo_id = dispositivo_id
        self.temperatura = temperatura
        self.gas = gas
        self.timestamp = timestamp
