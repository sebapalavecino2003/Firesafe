class Dispositivo:
    def __init__(self, id: str, nombre: str, ubicacion: str, activo: bool = True):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.activo = activo
