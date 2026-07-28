from fastapi import status


def register_login_create_student(client):
    credentials = {
        "email": "projects@test.com",
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
            "name": "Project User",
            "email": "projects@test.com",
            "college": "RV University",
            "degree": "B.Tech",
            "branch": "Computer Science",
            "current_year": 3,
            "graduation_year": 2027,
            "cgpa": 9.1,
            "attendance": 95,
            "backlogs": 0,
            "target_role": "Backend Developer"
        },
        headers=headers
    )

    return headers


def sample_project():
    return {
        "title": "CampusAI",
        "description": "AI powered student platform",
        "technologies": "FastAPI, PostgreSQL, React",
        "github_url": "https://github.com/test/campusai"
    }


def test_add_project(client):
    headers = register_login_create_student(client)

    response = client.post(
        "/students/me/projects",
        json=sample_project(),
        headers=headers
    )

    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["title"] == "CampusAI"
    assert data["description"] == "AI powered student platform"


def test_get_my_projects(client):
    headers = register_login_create_student(client)

    client.post(
        "/students/me/projects",
        json=sample_project(),
        headers=headers
    )

    response = client.get(
        "/students/me/projects",
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "CampusAI"


def test_update_project(client):
    headers = register_login_create_student(client)

    create = client.post(
        "/students/me/projects",
        json=sample_project(),
        headers=headers
    )

    project_id = create.json()["id"]

    response = client.put(
        f"/students/me/projects/{project_id}",
        json={
            "title": "CampusAI V2",
            "technologies": "FastAPI, React, Docker"
        },
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data["title"] == "CampusAI V2"
    assert data["technologies"] == "FastAPI, React, Docker"


def test_delete_project(client):
    headers = register_login_create_student(client)

    create = client.post(
        "/students/me/projects",
        json=sample_project(),
        headers=headers
    )

    project_id = create.json()["id"]

    response = client.delete(
        f"/students/me/projects/{project_id}",
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Project deleted successfully"


def test_delete_non_existing_project(client):
    headers = register_login_create_student(client)

    response = client.delete(
        "/students/me/projects/999",
        headers=headers
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Project not found"


def test_update_non_existing_project(client):
    headers = register_login_create_student(client)

    response = client.put(
        "/students/me/projects/999",
        json={
            "title": "Updated"
        },
        headers=headers
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Project not found"


def test_get_public_projects(client):
    headers = register_login_create_student(client)

    client.post(
        "/students/me/projects",
        json=sample_project(),
        headers=headers
    )

    profile = client.get(
        "/students/me/profile",
        headers=headers
    )

    student_id = profile.json()["id"]

    response = client.get(
        f"/students/{student_id}/projects"
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "CampusAI"


def test_public_projects_student_not_found(client):
    response = client.get(
        "/students/999/projects"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Student not found"


def test_add_project_without_token(client):
    response = client.post(
        "/students/me/projects",
        json=sample_project()
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_empty_project_title(client):
    headers = register_login_create_student(client)

    payload = sample_project()
    payload["title"] = ""

    response = client.post(
        "/students/me/projects",
        json=payload,
        headers=headers
    )

    # Current schema has no validation on title length,
    # so adjust this assertion if you later add constraints.
    assert response.status_code in (
        status.HTTP_201_CREATED,
        status.HTTP_422_UNPROCESSABLE_ENTITY
    )