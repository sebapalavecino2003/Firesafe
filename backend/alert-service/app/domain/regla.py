from app.domain.severidad import Severidad

class Regla:
    def __init__(self, max_temperatura: float, max_gas: int):
        self.max_temperatura = max_temperatura
        self.max_gas = max_gas

    def evaluar(self, temperatura: float, gas: int) -> Severidad | None:
        if gas > self.max_gas:
            return Severidad.CRITICA
        if temperatura > self.max_temperatura:
            return Severidad.ALTA
        return None
