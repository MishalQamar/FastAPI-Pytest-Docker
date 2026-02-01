def test_ping(test_app):
    # GIVEN
    # test_app is a fixture that returns a TestClient

    # WHEN
    response = test_app.get("/ping")

    # THEN
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong", "testing": True}
