import { useEffect, useState } from "react"

export default function Dashboard() {
  const [devices, setDevices] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem("token")

    fetch("http://localhost:8080/api/v1/devices", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
      .then(res => {
        if (!res.ok) {
          throw new Error("No autorizado")
        }
        return res.json()
      })
      .then(data => setDevices(data))
      .catch(err => {
        console.error(err)
        localStorage.removeItem("token")
        location.reload()
      })
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return <p style={{ padding: 40 }}>Cargando dispositivos...</p>
  }

  return (
    <div style={{ padding: 40 }}>
      <h2>Dashboard (devices-mf)</h2>

      <ul>
        {devices.map(device => (
          <li key={device.id}>
            {device.nombre ?? device.name ?? "Dispositivo"}
          </li>
        ))}
      </ul>

      <button
        onClick={() => {
          localStorage.removeItem("token")
          location.reload()
        }}
      >
        Cerrar sesión
      </button>
    </div>
  )
}
