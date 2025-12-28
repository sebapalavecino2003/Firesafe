export default function Login() {
  async function ingresar() {
    try {
      const response = await fetch("http://localhost:8080/api/v1/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          email: "admin@mail.com",
          password: "admin"
        })
      })

      if (!response.ok) {
        throw new Error("Credenciales invalidas")
      }

      const data = await response.json()

      // 🔐 Guardamos JWT real
      localStorage.setItem("token", data.access_token)

      // 🔄 Forzamos al shell a re-evaluar
      window.location.reload()

    } catch (error) {
      alert("Error al iniciar sesion")
      console.error(error)
    }
  }

  return (
    <div style={{ padding: 40 }}>
      <h2>Login (auth-mf)</h2>
      <button onClick={ingresar}>Ingresar</button>
    </div>
  )
}
