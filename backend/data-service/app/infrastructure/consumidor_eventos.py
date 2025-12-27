from datetime import datetime
from app.domain.lectura_sensor import LecturaSensor
from app.application.guardar_lectura import CasoUsoGuardarLectura

class ConsumidorEventos:
    def procesar(self, evento):
        lectura = LecturaSensor(
            dispositivo_id=evento["dispositivo_id"],
            temperatura=evento["temperatura"],
            gas=evento["gas"],
            timestamp=datetime.utcnow()
        )
        CasoUsoGuardarLectura().ejecutar(lectura)
