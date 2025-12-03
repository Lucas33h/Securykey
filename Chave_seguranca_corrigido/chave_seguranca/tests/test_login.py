def test_login(client):
    response = client.post(
        "/login",
        json={
            "email": "teste@example.com",
            "password": "123456"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
