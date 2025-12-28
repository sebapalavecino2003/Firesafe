export async function getDevices() {
  const token = localStorage.getItem("token")

  const response = await fetch("http://localhost:8080/api/v1/devices", {
    headers: {
      Authorization: `Bearer ${token}`
    }
  })

  if (!response.ok) {
    throw new Error("No autorizado")
  }

  return response.json()
}
