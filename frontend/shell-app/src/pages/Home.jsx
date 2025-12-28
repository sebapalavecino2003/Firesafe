import { lazy, Suspense } from "react";
import { obtenerToken, logout } from "../app/auth";

const DevicesMF = lazy(() => import("devicesMF/Devices"));

export default function Home() {
  const token = obtenerToken();

  return (
    <div>
      <h1>FireSafe Dashboard</h1>

      <button onClick={logout}>Cerrar sesión</button>

      <Suspense fallback={<div>Cargando dispositivos…</div>}>
        <DevicesMF token={token} />
      </Suspense>
    </div>
  );
}
