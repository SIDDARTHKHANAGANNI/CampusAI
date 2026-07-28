from fastapi import status


def register_login_create_student(client):
    credentials = {
        "email": "academic@test.com",
        "password": "password123"
    }

    client.post("/auth/register", json=credentials)

    login = client.post(
        "/auth/login",
        json=credentials
    )

    token = login.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    client.post(
        "/students/me/profile",
        json={
            "name": "Academic User",
            "email": "academic@test.com",
            "college": "RV University",
            "degree": "B.Tech",
            "branch": "Computer Science",
            "current_year": 3,
            "graduation_year": 2027,
            "cgpa": 9.0,
            "attendance": 95,
            "backlogs": 0,
            "target_role": "Software Engineer"
        },
        headers=headers
    )

    return headers


def sample_academic():
    return {
        "semester": 5,
        "semester_gpa": 9.25,
        "attendance": 94,
        "backlogs": 0
    }


def test_add_academic_record(client):
    headers = register_login_create_student(client)

    response = client.post(
        "/students/me/academics",
        json=sample_academic(),
        headers=headers
    )

    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["semester"] == 5
    assert data["semester_gpa"] == 9.25
    assert data["attendance"] == 94
    assert data["backlogs"] == 0


def test_get_my_academic_records(client):
    headers = register_login_create_student(client)

    client.post(
        "/students/me/academics",
        json=sample_academic(),
        headers=headers
    )

    response = client.get(
        "/students/me/academics",
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert len(data) == 1
    assert data[0]["semester"] == 5


def test_update_academic_record(client):
    headers = register_login_create_student(client)

    create = client.post(
        "/students/me/academics",
        json=sample_academic(),
        headers=headers
    )

    academic_id = create.json()["id"]

    response = client.put(
        f"/students/me/academics/{academic_id}",
        json={
            "semester_gpa": 9.80,
            "attendance": 99
        },
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data["semester_gpa"] == 9.80
    assert data["attendance"] == 99


def test_delete_academic_record(client):
    headers = register_login_create_student(client)

    create = client.post(
        "/students/me/academics",
        json=sample_academic(),
        headers=headers
    )

    academic_id = create.json()["id"]

    response = client.delete(
        f"/students/me/academics/{academic_id}",
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    assert response.json()["message"] == "Academic record deleted successfully"


def test_delete_non_existing_record(client):
    headers = register_login_create_student(client)

    response = client.delete(
        "/students/me/academics/999",
        headers=headers
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Academic record not found"


def test_public_academic_records(client):
    headers = register_login_create_student(client)

    client.post(
        "/students/me/academics",
        json=sample_academic(),
        headers=headers
    )

    profile = client.get(
        "/students/me/profile",
        headers=headers
    )

    student_id = profile.json()["id"]

    response = client.get(
        f"/students/{student_id}/academics"
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert len(data) == 1


def test_add_academic_without_token(client):
    response = client.post(
        "/students/me/academics",
        json=sample_academic()
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_invalid_semester(client):
    headers = register_login_create_student(client)

    payload = sample_academic()
    payload["semester"] = 13

    response = client.post(
        "/students/me/academics",
        json=payload,
        headers=headers
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_invalid_gpa(client):
    headers = register_login_create_student(client)

    payload = sample_academic()
    payload["semester_gpa"] = 11

    response = client.post(
        "/students/me/academics",
        json=payload,
        headers=headers
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY