from app.infrastructure.repositorio_ts import RepositorioTS

class CasoUsoConsultarHistorico:
    def ejecutar(self, dispositivo_id: str, desde, hasta):
        return RepositorioTS().consultar(dispositivo_id, desde, hasta)
