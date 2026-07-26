from fastapi import status


def register_and_login(client):
    register_data = {
        "email": "student@test.com",
        "password": "password123"
    }

    client.post("/auth/register", json=register_data)

    response = client.post(
        "/auth/login",
        json=register_data
    )

    token = response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    return headers


def sample_student():
    return {
        "name": "Siddarth",
        "email": "student@test.com",
        "college": "RV University",
        "degree": "B.Tech",
        "branch": "Computer Science",
        "current_year": 3,
        "graduation_year": 2027,
        "cgpa": 9.1,
        "attendance": 95,
        "backlogs": 0,
        "target_role": "ML Engineer"
    }


def test_create_student_profile(client):
    headers = register_and_login(client)

    response = client.post(
        "/students/me/profile",
        json=sample_student(),
        headers=headers
    )

    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["name"] == "Siddarth"
    assert data["college"] == "RV University"
    assert data["cgpa"] == 9.1


def test_duplicate_student_profile(client):
    headers = register_and_login(client)

    payload = sample_student()

    client.post(
        "/students/me/profile",
        json=payload,
        headers=headers
    )

    response = client.post(
        "/students/me/profile",
        json=payload,
        headers=headers
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Student profile already exists"


def test_get_my_profile(client):
    headers = register_and_login(client)

    client.post(
        "/students/me/profile",
        json=sample_student(),
        headers=headers
    )

    response = client.get(
        "/students/me/profile",
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data["name"] == "Siddarth"


def test_update_profile(client):
    headers = register_and_login(client)

    client.post(
        "/students/me/profile",
        json=sample_student(),
        headers=headers
    )

    updated = sample_student()
    updated["cgpa"] = 9.8
    updated["attendance"] = 99

    response = client.put(
        "/students/me/profile",
        json=updated,
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data["cgpa"] == 9.8
    assert data["attendance"] == 99


def test_get_public_profile(client):
    headers = register_and_login(client)

    create = client.post(
        "/students/me/profile",
        json=sample_student(),
        headers=headers
    )

    student_id = create.json()["id"]

    response = client.get(
        f"/students/{student_id}/profile"
    )

    assert response.status_code == status.HTTP_200_OK


def test_public_profile_not_found(client):
    response = client.get(
        "/students/999/profile"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Student not found"


def test_get_profile_without_creation(client):
    headers = register_and_login(client)

    response = client.get(
        "/students/me/profile",
        headers=headers
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_profile_without_token(client):
    response = client.post(
        "/students/me/profile",
        json=sample_student()
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_create_profile_invalid_cgpa(client):
    headers = register_and_login(client)

    payload = sample_student()
    payload["cgpa"] = 12

    response = client.post(
        "/students/me/profile",
        json=payload,
        headers=headers
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY