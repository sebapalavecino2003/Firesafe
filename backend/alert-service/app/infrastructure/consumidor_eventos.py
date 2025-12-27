from app.application.evaluar_datos_sensor import CasoUsoEvaluarDatosSensor

class ConsumidorEventos:

    def procesar(self, evento):
        alerta = CasoUsoEvaluarDatosSensor().ejecutar(evento)
        if alerta:
            print("ALERTA GENERADA:", alerta.severidad.value)
