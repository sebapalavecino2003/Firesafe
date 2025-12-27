from app.application.enviar_notificacion import CasoUsoEnviarNotificacion
from app.domain.notificacion import Notificacion
from app.domain.canal import Canal

class ConsumidorEventos:

    def procesar_alerta(self, evento_alerta):
        notificacion = Notificacion(
            destinatario="admin@mail.com",
            mensaje=evento_alerta["mensaje"],
            canal=Canal.EMAIL
        )
        CasoUsoEnviarNotificacion().ejecutar(notificacion)
