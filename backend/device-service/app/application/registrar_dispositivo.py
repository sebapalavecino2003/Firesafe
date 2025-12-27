from app.domain.dispositivo import Dispositivo

class CasoUsoRegistrarDispositivo:
    def ejecutar(self, datos):
        return Dispositivo(
            id=datos.id,
            nombre=datos.nombre,
            ubicacion=datos.ubicacion
        )
