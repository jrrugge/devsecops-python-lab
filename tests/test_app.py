import pytest

from app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)

    with app.test_client() as test_client:
        yield test_client


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_default_greeting(client):
    response = client.get("/greet")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, world!"}


def test_named_greeting(client):
    response = client.get("/greet?name=John")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, John!"}


def test_long_name_is_limited(client):
    long_name = "A" * 100

    response = client.get(f"/greet?name={long_name}")
    message = response.get_json()["message"]

    assert response.status_code == 200
    assert message == f"Hello, {'A' * 50}!"