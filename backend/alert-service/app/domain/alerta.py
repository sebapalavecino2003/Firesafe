from app.domain.severidad import Severidad

class Alerta:
    def __init__(self, dispositivo_id: str, severidad: Severidad, mensaje: str):
        self.dispositivo_id = dispositivo_id
        self.severidad = severidad
        self.mensaje = mensaje
        self.confirmada = False
