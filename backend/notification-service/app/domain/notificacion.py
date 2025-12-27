from app.domain.canal import Canal

class Notificacion:
    def __init__(self, destinatario: str, mensaje: str, canal: Canal):
        self.destinatario = destinatario
        self.mensaje = mensaje
        self.canal = canal
