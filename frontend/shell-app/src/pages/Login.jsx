import { lazy, Suspense } from "react";
import { guardarToken } from "../app/auth";

const LoginMF = lazy(() => import("authMF/Login"));

export default function Login() {
  const onLogin = async (credenciales) => {
    const res = await fetch("http://localhost:8080/api/v1/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(credenciales)
    });

    const data = await res.json();
    guardarToken(data.token_acceso);
    window.location.href = "/";
  };

  return (
    <Suspense fallback={<div>Cargando login…</div>}>
      <LoginMF onLogin={onLogin} />
    </Suspense>
  );
}
