from app.infrastructure.repositorio_ts import RepositorioTS

class CasoUsoGuardarLectura:
    def ejecutar(self, lectura):
        RepositorioTS().guardar(lectura)
