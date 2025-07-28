import json
import os
import tempfile

import pytest
from fastapi.testclient import TestClient

from server.auth import get_invites_file, get_users_file
from server.main import app

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
                {"code": "ARKHAM_ACCESS", "used": False},
                {"code": "USEDINVITE", "used": True},
            ],
            invites_file,
        )
        invites_path = invites_file.name

    yield users_path, invites_path

    # Cleanup
    os.remove(users_path)
    os.remove(invites_path)


@pytest.fixture(autouse=True)
def override_dependencies(temp_files):
    """Override dependencies to use temporary files."""
    users_path, invites_path = temp_files
    print(f"Setting up dependency overrides:")
    print(f"  users_file: {users_path}")
    print(f"  invites_file: {invites_path}")
    app.dependency_overrides[get_users_file] = lambda: users_path
    app.dependency_overrides[get_invites_file] = lambda: invites_path

    # Debug: Check what's in the invites file
    with open(invites_path, 'r') as f:
        invites_content = f.read()
        print(f"Invites file content: {invites_content}")

    yield
    app.dependency_overrides = {}


@pytest.fixture(autouse=True)
def patch_persistence_layer(monkeypatch):
    """Patch the PersistenceLayer class to use the test database."""
    # Use the test configuration to get the test database path
    from pathlib import Path
    from server.config_loader import get_config

    # Load test configuration
    test_config_path = Path(__file__).parent.parent / "test_server_config.yaml"
    config = get_config(str(test_config_path))

    # Resolve paths relative to the project root (server directory)
    project_root = Path(__file__).parent.parent
    # Remove the "server/" prefix from the config paths since we're already in the server directory
    db_path = config["db_path"].replace("server/", "")
    log_path = config["log_path"].replace("server/", "")
    test_db_path = project_root / db_path
    test_log_path = project_root / log_path

    # Ensure the test database exists
    if not test_db_path.exists():
        raise FileNotFoundError(f"Test database not found at {test_db_path}. Run init_test_db.py first.")

    # Patch the PersistenceLayer constructor to use our test database
    original_init = None

    def mock_init(self, db_path=None, log_path=None):
        # Use our test database instead of the default
        if db_path is None:
            db_path = str(test_db_path)
        if log_path is None:
            log_path = str(test_log_path)

        # Call the original __init__ with our modified paths
        original_init(self, db_path, log_path)

    # Store the original __init__ method
    from server.persistence import PersistenceLayer
    original_init = PersistenceLayer.__init__

    # Patch the __init__ method
    monkeypatch.setattr(PersistenceLayer, "__init__", mock_init)

    yield

    # Restore the original __init__ method
    monkeypatch.setattr(PersistenceLayer, "__init__", original_init)


@pytest.fixture
def test_client():
    """Create a test client with proper app state setup."""
    with TestClient(app) as client:
        # Set up the persistence layer in app state
        from server.persistence import get_persistence
        client.app.state.persistence = get_persistence()
        yield client


def test_successful_registration(test_client):
    response = test_client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "password": "testpass",
            "invite_code": "ARKHAM_ACCESS",
        },
    )
    print(f"Response status: {response.status_code}")
    print(f"Response content: {response.json()}")
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
