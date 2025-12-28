from app.domain.usuario import Usuario

class CasoUsoIniciarSesion:
    def ejecutar(self, email: str, password: str) -> Usuario:
        if email == "admin@mail.com" and password == "admin":
            return Usuario(
                id="1",
                email=email,
                rol="administrador"
            )
        raise Exception("Credenciales invalidas")
