from fastapi import APIRouter

router = APIRouter()

@router.post("/test-email")
def test_email():
    print("Email de prueba enviado")
    return {"status": "ok"}
