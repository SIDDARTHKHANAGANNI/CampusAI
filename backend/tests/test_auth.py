from fastapi import status


def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["email"] == "test@example.com"
    assert data["is_active"] is True
    assert "id" in data


def test_duplicate_registration(client):
    payload = {
        "email": "duplicate@example.com",
        "password": "password123"
    }

    client.post("/auth/register", json=payload)

    response = client.post("/auth/register", json=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["success"] is False
    assert response.json()["message"] == "Email already registered"


def test_login_success(client):
    payload = {
        "email": "login@example.com",
        "password": "password123"
    }

    client.post("/auth/register", json=payload)

    response = client.post(
        "/auth/login",
        json=payload
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post(
        "/auth/register",
        json={
            "email": "wrong@example.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "wrong@example.com",
            "password": "incorrect123"
        }
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["success"] is False
    assert response.json()["message"] == "Invalid email or password"


def test_login_non_existing_user(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "nouser@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["success"] is False
    assert response.json()["message"] == "Invalid email or password"


def test_register_short_password(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "short@example.com",
            "password": "123"
        }
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_register_invalid_email(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "invalid-email",
            "password": "password123"
        }
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_access_me_without_token(client):
    response = client.get("/auth/me")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED