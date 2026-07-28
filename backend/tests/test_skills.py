from fastapi import status


def register_login_create_student(client):
    credentials = {
        "email": "skills@test.com",
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
            "name": "Skill User",
            "email": "skills@test.com",
            "college": "RV University",
            "degree": "B.Tech",
            "branch": "Computer Science",
            "current_year": 3,
            "graduation_year": 2027,
            "cgpa": 9.2,
            "attendance": 96,
            "backlogs": 0,
            "target_role": "Backend Developer"
        },
        headers=headers
    )

    return headers


def sample_skill():
    return {
        "name": "Java",
        "category": "Programming Language",
        "proficiency": "Advanced"
    }


def test_add_skill(client):
    headers = register_login_create_student(client)

    response = client.post(
        "/students/me/skills",
        json=sample_skill(),
        headers=headers
    )

    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["name"] == "Java"
    assert data["category"] == "Programming Language"
    assert data["proficiency"] == "Advanced"


def test_get_my_skills(client):
    headers = register_login_create_student(client)

    client.post(
        "/students/me/skills",
        json=sample_skill(),
        headers=headers
    )

    response = client.get(
        "/students/me/skills",
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Java"


def test_update_skill(client):
    headers = register_login_create_student(client)

    create = client.post(
        "/students/me/skills",
        json=sample_skill(),
        headers=headers
    )

    skill_id = create.json()["id"]

    response = client.put(
        f"/students/me/skills/{skill_id}",
        json={
            "proficiency": "Expert"
        },
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data["proficiency"] == "Expert"


def test_update_non_existing_skill(client):
    headers = register_login_create_student(client)

    response = client.put(
        "/students/me/skills/999",
        json={
            "proficiency": "Expert"
        },
        headers=headers
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Skill not found"


def test_get_public_skills(client):
    headers = register_login_create_student(client)

    client.post(
        "/students/me/skills",
        json=sample_skill(),
        headers=headers
    )

    profile = client.get(
        "/students/me/profile",
        headers=headers
    )

    student_id = profile.json()["id"]

    response = client.get(
        f"/students/{student_id}/skills"
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Java"


def test_public_student_not_found(client):
    response = client.get(
        "/students/999/skills"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Student not found"


def test_add_skill_without_token(client):
    response = client.post(
        "/students/me/skills",
        json=sample_skill()
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_invalid_skill_name(client):
    headers = register_login_create_student(client)

    payload = sample_skill()
    payload["name"] = ""

    response = client.post(
        "/students/me/skills",
        json=payload,
        headers=headers
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_invalid_proficiency(client):
    headers = register_login_create_student(client)

    payload = sample_skill()
    payload["proficiency"] = ""

    response = client.post(
        "/students/me/skills",
        json=payload,
        headers=headers
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY