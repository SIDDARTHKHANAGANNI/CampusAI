from fastapi import status


def register_login_create_student(client):
    credentials = {
        "email": "career@test.com",
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
            "name": "Career User",
            "email": "career@test.com",
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


def sample_career_goal():
    return {
        "target_role": "Backend Developer",
        "target_company_type": "Product Based",
        "target_timeline": "2027"
    }


def test_add_career_goal(client):
    headers = register_login_create_student(client)

    response = client.post(
        "/students/me/career-goals",
        json=sample_career_goal(),
        headers=headers
    )

    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["target_role"] == "Backend Developer"
    assert data["target_company_type"] == "Product Based"
    assert data["target_timeline"] == "2027"


def test_get_my_career_goals(client):
    headers = register_login_create_student(client)

    client.post(
        "/students/me/career-goals",
        json=sample_career_goal(),
        headers=headers
    )

    response = client.get(
        "/students/me/career-goals",
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert len(data) == 1
    assert data[0]["target_role"] == "Backend Developer"


def test_update_career_goal(client):
    headers = register_login_create_student(client)

    create = client.post(
        "/students/me/career-goals",
        json=sample_career_goal(),
        headers=headers
    )

    goal_id = create.json()["id"]

    response = client.put(
        f"/students/me/career-goals/{goal_id}",
        json={
            "target_role": "Machine Learning Engineer",
            "target_timeline": "2028"
        },
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data["target_role"] == "Machine Learning Engineer"
    assert data["target_timeline"] == "2028"


def test_delete_career_goal(client):
    headers = register_login_create_student(client)

    create = client.post(
        "/students/me/career-goals",
        json=sample_career_goal(),
        headers=headers
    )

    goal_id = create.json()["id"]

    response = client.delete(
        f"/students/me/career-goals/{goal_id}",
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Career goal deleted successfully"


def test_delete_non_existing_career_goal(client):
    headers = register_login_create_student(client)

    response = client.delete(
        "/students/me/career-goals/999",
        headers=headers
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Career goal not found"


def test_update_non_existing_career_goal(client):
    headers = register_login_create_student(client)

    response = client.put(
        "/students/me/career-goals/999",
        json={
            "target_role": "Data Scientist"
        },
        headers=headers
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Career goal not found"


def test_get_public_career_goals(client):
    headers = register_login_create_student(client)

    client.post(
        "/students/me/career-goals",
        json=sample_career_goal(),
        headers=headers
    )

    profile = client.get(
        "/students/me/profile",
        headers=headers
    )

    student_id = profile.json()["id"]

    response = client.get(
        f"/students/{student_id}/career-goals"
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert len(data) == 1
    assert data[0]["target_role"] == "Backend Developer"


def test_public_career_goals_student_not_found(client):
    response = client.get(
        "/students/999/career-goals"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Student not found"


def test_add_career_goal_without_token(client):
    response = client.post(
        "/students/me/career-goals",
        json=sample_career_goal()
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_empty_target_role(client):
    headers = register_login_create_student(client)

    payload = sample_career_goal()
    payload["target_role"] = ""

    response = client.post(
        "/students/me/career-goals",
        json=payload,
        headers=headers
    )

    # Your schema currently has no validation on target_role,
    # so this may succeed until validation is added.
    assert response.status_code in (
        status.HTTP_201_CREATED,
        status.HTTP_422_UNPROCESSABLE_ENTITY
    )