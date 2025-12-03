def test_signup(client):
    response = client.post(
        "/signup",
        json={
            "email": "novo@example.com",
            "password": "123456"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data or "user" in data
