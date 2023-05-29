from tests import client

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_contacts():
    response = client.get("/contacts")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
