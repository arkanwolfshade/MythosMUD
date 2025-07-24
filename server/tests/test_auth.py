import os
import json
import tempfile
import pytest
from fastapi.testclient import TestClient
from server.main import app
from server.auth import get_users_file, get_invites_file


@pytest.fixture
def temp_files():
    users_fd, users_path = tempfile.mkstemp()
    invites_fd, invites_path = tempfile.mkstemp()
    os.close(users_fd)
    os.close(invites_fd)
    # Write initial data
    with open(users_path, "w", encoding="utf-8") as f:
        json.dump([], f)
    with open(invites_path, "w", encoding="utf-8") as f:
        json.dump(
            [
                {"code": "INVITE123", "used": False},
                {"code": "USEDINVITE", "used": True},
            ],
            f,
        )
    yield users_path, invites_path
    os.remove(users_path)
    os.remove(invites_path)


@pytest.fixture(autouse=True)
def override_dependencies(temp_files):
    users_path, invites_path = temp_files
    app.dependency_overrides[get_users_file] = lambda: users_path
    app.dependency_overrides[get_invites_file] = lambda: invites_path
    yield
    app.dependency_overrides = {}


def test_successful_registration():
    client = TestClient(app)
    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "password": "testpass",
            "invite_code": "INVITE123",
        },
    )
    assert response.status_code == 201
    assert "Registration successful" in response.json()["message"]
    # Check user is in users.json
    with open(app.dependency_overrides[get_users_file](), "r", encoding="utf-8") as f:
        users = json.load(f)
    assert any(u["username"] == "testuser" for u in users)
    # Check invite is marked as used
    with open(app.dependency_overrides[get_invites_file](), "r", encoding="utf-8") as f:
        invites = json.load(f)
    assert any(i["code"] == "INVITE123" and i["used"] for i in invites)


def test_duplicate_username():
    client = TestClient(app)
    # Register once
    client.post(
        "/auth/register",
        json={
            "username": "dupeuser",
            "password": "testpass",
            "invite_code": "INVITE123",
        },
    )
    # Reset invite to unused for second attempt
    with open(app.dependency_overrides[get_invites_file](), "w", encoding="utf-8") as f:
        json.dump(
            [
                {"code": "INVITE123", "used": False},
                {"code": "USEDINVITE", "used": True},
            ],
            f,
        )
    # Register again with same username
    response = client.post(
        "/auth/register",
        json={
            "username": "dupeuser",
            "password": "testpass",
            "invite_code": "INVITE123",
        },
    )
    assert response.status_code == 409
    assert "Username already exists" in response.json()["detail"]


def test_invalid_invite_code():
    client = TestClient(app)
    response = client.post(
        "/auth/register",
        json={
            "username": "badinvite",
            "password": "testpass",
            "invite_code": "INVALID",
        },
    )
    assert response.status_code == 400
    assert "Invite code is invalid" in response.json()["detail"]


def test_used_invite_code():
    client = TestClient(app)
    response = client.post(
        "/auth/register",
        json={
            "username": "usedinvite",
            "password": "testpass",
            "invite_code": "USEDINVITE",
        },
    )
    assert response.status_code == 400
    assert "Invite code is invalid" in response.json()["detail"]


def test_successful_login():
    client = TestClient(app)
    # Register user first
    client.post(
        "/auth/register",
        json={
            "username": "loginuser",
            "password": "testpass",
            "invite_code": "INVITE123",
        },
    )
    response = client.post(
        "/auth/login", json={"username": "loginuser", "password": "testpass"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password():
    client = TestClient(app)
    # Register user first
    client.post(
        "/auth/register",
        json={
            "username": "wrongpass",
            "password": "rightpass",
            "invite_code": "INVITE123",
        },
    )
    response = client.post(
        "/auth/login", json={"username": "wrongpass", "password": "wrongpass"}
    )
    assert response.status_code == 401
    assert "Invalid username or password" in response.json()["detail"]


def test_login_nonexistent_user():
    client = TestClient(app)
    response = client.post(
        "/auth/login", json={"username": "ghost", "password": "doesntmatter"}
    )
    assert response.status_code == 401
    assert "Invalid username or password" in response.json()["detail"]


def test_me_valid_token():
    client = TestClient(app)
    # Register and login
    client.post(
        "/auth/register",
        json={"username": "meuser", "password": "testpass", "invite_code": "INVITE123"},
    )
    login_resp = client.post(
        "/auth/login", json={"username": "meuser", "password": "testpass"}
    )
    token = login_resp.json()["access_token"]
    resp = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["username"] == "meuser"
    assert "password_hash" not in data


def test_me_missing_token():
    client = TestClient(app)
    resp = client.get("/auth/me")
    assert resp.status_code == 403  # FastAPI returns 403 for missing credentials


def test_me_invalid_token():
    client = TestClient(app)
    resp = client.get("/auth/me", headers={"Authorization": "Bearer invalidtoken"})
    assert resp.status_code == 401
    assert "Invalid or expired token" in resp.json()["detail"]
