from app.domain.dispositivo import Dispositivo

class CasoUsoListarDispositivos:
    def ejecutar(self):
        # mock inicial
        return [
            Dispositivo("ESP32-001", "Sensor Cocina", "Cocina"),
            Dispositivo("ESP32-002", "Sensor Garage", "Garage"),
        ]
