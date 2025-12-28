from fastapi.testclient import TestClient
from fastapi import Request, Header
from app.main import app
from app.api import rutas_devices

client = TestClient(app)

# ---------- FAKES ----------

async def fake_reenviar_request(*args, **kwargs):
    return 200, [
        {
            "id": "ESP32-001",
            "nombre": "Sensor Cocina",
            "ubicacion": "Cocina"
        }
    ]

async def fake_validar_token(
    request: Request,
    authorization: str = Header(None)   # 👈 CLAVE ABSOLUTA
):
    request.state.usuario_id = "admin"
    return True

# ---------- TEST ----------

def test_devices_con_token(mocker):
    # Mock del proxy HTTP
    mocker.patch(
        "app.api.rutas_devices.reenviar_request",
        fake_reenviar_request
    )

    # Override del dependency CON FIRMA COMPATIBLE
    app.dependency_overrides[rutas_devices.validar_token] = fake_validar_token

    response = client.get(
        "/api/v1/devices",
        headers={
            "Authorization": "Bearer token-falso"
        }
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)

    # Limpieza
    app.dependency_overrides = {}
