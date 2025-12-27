from app.domain.regla import Regla
from app.domain.alerta import Alerta

class CasoUsoEvaluarDatosSensor:

    def ejecutar(self, evento):
        regla = Regla(max_temperatura=45.0, max_gas=300)

        severidad = regla.evaluar(
            temperatura=evento.temperatura,
            gas=evento.gas
        )

        if severidad:
            return Alerta(
                dispositivo_id=evento.dispositivo_id,
                severidad=severidad,
                mensaje="Riesgo detectado"
            )

        return None
