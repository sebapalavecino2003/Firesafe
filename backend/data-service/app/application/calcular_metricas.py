class CasoUsoCalcularMetricas:
    def ejecutar(self, lecturas):
        temperaturas = [l.temperatura for l in lecturas]
        return {
            "promedio": sum(temperaturas) / len(temperaturas) if temperaturas else 0,
            "maximo": max(temperaturas) if temperaturas else 0
        }
