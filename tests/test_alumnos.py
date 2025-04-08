# test/test_alumnos.py
from fastapi.testclient import TestClient
from main import app
from utils.dependencies import get_current_user  # o donde hayas definido la dependencia real
from dependencies_override import fake_get_current_user

# Sobrescribe la dependencia get_current_user con la fake
app.dependency_overrides[get_current_user] = fake_get_current_user

client = TestClient(app)

def test_read_alumnos():
    response = client.get("/api/v2/alumnos")
    assert response.status_code == 200
