import json
import os
import sqlite3
import tempfile

import pytest
from fastapi.testclient import TestClient

from server.auth import get_invites_file, get_users_file
from server.main import app
from server.persistence import PersistenceLayer

# Database schema for tests
TEST_SCHEMA = """
CREATE TABLE IF NOT EXISTS players (
    id TEXT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    strength INTEGER,
    dexterity INTEGER,
    constitution INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    sanity INTEGER,
    occult_knowledge INTEGER,
    fear INTEGER,
    corruption INTEGER,
    cult_affiliation INTEGER,
    current_room_id TEXT,
    created_at TEXT,
    last_active TEXT,
    experience_points INTEGER,
    level INTEGER
);

CREATE TABLE IF NOT EXISTS rooms (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    exits TEXT,
    zone TEXT
);
"""


@pytest.fixture
def temp_files():
    """Create temporary files for users and invites."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as users_file:
        json.dump([], users_file)
        users_path = users_file.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as invites_file:
        json.dump(
            [
                {"code": "INVITE123", "used": False},
                {"code": "USEDINVITE", "used": True},
            ],
            invites_file,
        )
        invites_path = invites_file.name

    yield users_path, invites_path

    # Cleanup
    os.remove(users_path)
    os.remove(invites_path)


@pytest.fixture
def temp_log_file():
    """Create a temporary log file for the persistence layer."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as log_file:
        log_path = log_file.name

    yield log_path

    # Cleanup - don't try to remove if it's still in use
    try:
        if os.path.exists(log_path):
            os.remove(log_path)
    except PermissionError:
        pass  # File might still be in use by logger


@pytest.fixture
def temp_db():
    """Create a temporary database with schema."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".db", delete=False) as db_file:
        db_path = db_file.name

    # Initialize the database with schema
    with sqlite3.connect(db_path) as conn:
        conn.executescript(TEST_SCHEMA)
        conn.commit()

    yield db_path

    # Cleanup
    try:
        if os.path.exists(db_path):
            os.remove(db_path)
    except PermissionError:
        pass  # File might still be in use


@pytest.fixture(autouse=True)
def override_dependencies(temp_files):
    """Override dependencies to use temporary files."""
    users_path, invites_path = temp_files
    app.dependency_overrides[get_users_file] = lambda: users_path
    app.dependency_overrides[get_invites_file] = lambda: invites_path
    yield
    app.dependency_overrides = {}


@pytest.fixture(autouse=True)
def setup_test_persistence(temp_log_file, temp_db, monkeypatch):
    """Set up test persistence layer."""
    # Create a test persistence layer with temporary database and log file
    test_persistence = PersistenceLayer(db_path=temp_db, log_path=temp_log_file)

    # Patch get_persistence to return our test persistence layer
    monkeypatch.setattr("server.persistence.get_persistence", lambda: test_persistence)

    # Also set it on the app state
    app.state.persistence = test_persistence
    yield


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
    users_path = app.dependency_overrides[get_users_file]()
    with open(users_path, encoding="utf-8") as f:
        users = json.load(f)
    assert any(u["username"] == "testuser" for u in users)

    # Check invite is marked as used
    invites_path = app.dependency_overrides[get_invites_file]()
    with open(invites_path, encoding="utf-8") as f:
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
    invites_path = app.dependency_overrides[get_invites_file]()
    with open(invites_path, "w", encoding="utf-8") as f:
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
    response = client.post("/auth/login", json={"username": "loginuser", "password": "testpass"})
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
    response = client.post("/auth/login", json={"username": "wrongpass", "password": "wrongpass"})
    assert response.status_code == 401
    assert "Invalid username or password" in response.json()["detail"]


def test_login_nonexistent_user():
    client = TestClient(app)
    response = client.post("/auth/login", json={"username": "ghost", "password": "doesntmatter"})
    assert response.status_code == 401
    assert "Invalid username or password" in response.json()["detail"]


def test_me_valid_token():
    client = TestClient(app)
    # Register and login
    client.post(
        "/auth/register",
        json={"username": "meuser", "password": "testpass", "invite_code": "INVITE123"},
    )
    login_resp = client.post("/auth/login", json={"username": "meuser", "password": "testpass"})
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
