import { Suspense } from "react"

const AuthMF = React.lazy(() => import("authMf/Login"))
const DevicesMF = React.lazy(() => import("devicesMf/Dashboard"))

export default function App() {
  const token = localStorage.getItem("token")

  return (
    <Suspense fallback={<div>Cargando aplicación...</div>}>
      {!token ? <AuthMF /> : <DevicesMF />}
    </Suspense>
  )
}
