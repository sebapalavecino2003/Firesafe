from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

async def fake_reenviar_request(*args, **kwargs):
    return 200, {
        "token_acceso": "token-falso",
        "rol": "administrador"
    }

def test_login_ok(mocker):
    mocker.patch(
        "app.api.rutas_auth.reenviar_request",  # 👈 CLAVE
        fake_reenviar_request
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "admin@mail.com",
            "password": "admin"
        }
    )

    assert response.status_code == 200
    assert "token_acceso" in response.json()
