from app.infrastructure.email_adapter import enviar_email
from app.domain.canal import Canal

class CasoUsoEnviarNotificacion:

    def ejecutar(self, notificacion):
        if notificacion.canal == Canal.EMAIL:
            enviar_email(
                notificacion.destinatario,
                notificacion.mensaje
            )
