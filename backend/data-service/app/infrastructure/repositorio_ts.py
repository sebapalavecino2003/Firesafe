class RepositorioTS:
    def guardar(self, lectura):
        print("Guardando lectura:", lectura.dispositivo_id, lectura.temperatura)

    def consultar(self, dispositivo_id, desde, hasta):
        return []
