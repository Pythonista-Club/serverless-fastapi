from fastapi.testclient import TestClient
from mangum import Mangum

from api import api

client = TestClient(api)
handler = Mangum(api)

def test_api_root():
    response = client.get("/")
    assert response.status_code == 200 
    assert response.json() == {"resp":"Welcome for the Pythonista Club! "} 