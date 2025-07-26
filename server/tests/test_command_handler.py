import pytest
from fastapi.testclient import TestClient
from server.main import app
from server.auth import get_users_file, get_invites_file
from server.tests.mock_data import MockPlayerManager
from server.auth_utils import decode_access_token


# Patch the PersistenceLayer class to use the test database
@pytest.fixture(autouse=True)
def patch_persistence_layer(monkeypatch):
    """Patch the PersistenceLayer class to use the test database."""
    # Use the test database that was created with init_test_db.py
    from pathlib import Path

    test_db_path = Path(__file__).parent / "data" / "players" / "test_players.db"
    test_log_path = Path(__file__).parent / "data" / "test_persistence.log"

    # Ensure the test database exists
    if not test_db_path.exists():
        raise FileNotFoundError(
            f"Test database not found at {test_db_path}. Run init_test_db.py first."
        )

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


# Patch get_current_user to always reflect the mock player's current room
@pytest.fixture(autouse=True)
def patch_get_current_user(monkeypatch):
    def get_current_user_mock(credentials=None, users_file=None):
        print(f"[get_current_user_mock] Called with credentials: {credentials}")
        # Extract token from credentials
        token = None
        if credentials and hasattr(credentials, "credentials"):
            token = credentials.credentials
        elif isinstance(credentials, str):
            token = credentials

        print(f"[get_current_user_mock] Extracted token: {token}")

        # Handle mock token for testing
        if token == "mock_token_for_cmduser":
            print("[get_current_user_mock] Using mock token")
            return {"username": "cmduser", "current_room_id": "arkham_001"}

        if not token:
            print("[get_current_user_mock] No token, using default")
            return {"username": "cmduser", "current_room_id": "arkham_001"}

        # Try to decode real token
        payload = decode_access_token(token)
        username = payload["sub"] if payload and "sub" in payload else "cmduser"

        # For testing, always return the mock user data instead of checking the users file
        player_manager = app.state.player_manager
        player = player_manager.get_player_by_name(username)
        if player:
            return {
                "username": player.name,
                "current_room_id": player.current_room_id,
            }
        else:
            # Fallback for testing
            return {"username": "cmduser", "current_room_id": "arkham_001"}

    # Mock the HTTPBearer dependency to accept our mock token
    def mock_bearer_scheme(credentials=None):
        if credentials and credentials.credentials == "mock_token_for_cmduser":
            return credentials
        # For real tokens, let the original HTTPBearer handle it
        from fastapi.security import HTTPBearer
        original_bearer = HTTPBearer()
        return original_bearer(credentials)

    print("[patch_get_current_user] Setting up mocks...")
    monkeypatch.setattr("server.auth.get_current_user", get_current_user_mock)
    monkeypatch.setattr("server.auth.bearer_scheme", mock_bearer_scheme)
    # Also mock it in the command_handler module where it's imported
    monkeypatch.setattr("server.command_handler.get_current_user", get_current_user_mock)
    print("[patch_get_current_user] Mocks set up successfully")
    yield


@pytest.fixture
def temp_files():
    import tempfile
    import os
    import json

    users_fd, users_path = tempfile.mkstemp()
    invites_fd, invites_path = tempfile.mkstemp()
    os.close(users_fd)
    os.close(invites_fd)
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


# Remove the debug_print_player_room autouse fixture


@pytest.fixture(scope="function")
def persistent_patch_app_state(monkeypatch):
    # No-op: patching now handled in test_client fixture
    yield


@pytest.fixture
def test_client(persistent_patch_app_state):
    with TestClient(app) as client:
        mock_player_manager = MockPlayerManager()
        # Rooms will be loaded from JSON files by the PersistenceLayer
        client.app.state.player_manager = mock_player_manager
        player = mock_player_manager.get_player_by_name("cmduser")
        if player:
            print(f"[debug] Test start: cmduser in {player.current_room_id}")
        else:
            print("[debug] Test start: cmduser not found")
        yield client


@pytest.fixture
def auth_token(test_client):
    # Try to register the user, but don't fail if they already exist
    reg_resp = test_client.post(
        "/auth/register",
        json={
            "username": "cmduser",
            "password": "testpass",
            "invite_code": "INVITE123",
        },
    )
    print(f"[auth_token] Registration response status: {reg_resp.status_code}")
    print(f"[auth_token] Registration response: {reg_resp.json()}")

    # Registration should succeed (201) or user already exists (409)
    assert reg_resp.status_code in [201, 409], f"Unexpected registration status: {reg_resp.status_code}"

    pm = test_client.app.state.player_manager
    print(
        f"[auth_token] After registration: {pm.get_player_by_name('cmduser').current_room_id}"
    )
    resp = test_client.post(
        "/auth/login", json={"username": "cmduser", "password": "testpass"}
    )
    print(f"[auth_token] Login response status: {resp.status_code}")
    print(f"[auth_token] Login response: {resp.json()}")
    print(
        f"[auth_token] After login: {pm.get_player_by_name('cmduser').current_room_id}"
    )

    # Login should succeed
    assert resp.status_code == 200, f"Login failed: {resp.json()}"
    return resp.json()["access_token"]


def post_command(client, token, command):
    return client.post(
        "/command/",
        json={"command": command},
        headers={"Authorization": f"Bearer {token}"},
    )


def test_auth_required(test_client):
    resp = test_client.post("/command/", json={"command": "look"})
    assert resp.status_code == 403


def test_look_command_with_mock_auth(test_client):
    """Test look command using a valid JWT token for testing."""
    # Create a valid JWT token for testing
    from server.auth_utils import create_access_token
    from datetime import timedelta

    test_token = create_access_token(
        data={"sub": "cmduser"},
        expires_delta=timedelta(minutes=60)
    )

    print("[test] About to make request with valid JWT token")
    resp = test_client.post(
        "/command/",
        json={"command": "look"},
        headers={"Authorization": f"Bearer {test_token}"}
    )
    print(f"[test] Response status: {resp.status_code}")
    print(f"[test] Response body: {resp.json()}")

    assert resp.status_code == 200
    result = resp.json()["result"]
    assert result.startswith("Arkham Town Square")
    assert "You are standing in the bustling heart of Arkham" in result
    assert "Exits: north, south, east, west" in result


def test_empty_command(auth_token, test_client):
    resp = post_command(test_client, auth_token, "   ")
    assert resp.status_code == 200
    assert resp.json()["result"] == ""


def test_look_command(auth_token, test_client):
    resp = post_command(test_client, auth_token, "look")
    assert resp.status_code == 200
    result = resp.json()["result"]
    assert result.startswith("Arkham Town Square")
    assert "You are standing in the bustling heart of Arkham." in result
    assert "Exits: north, south, east, west" in result


def test_go_missing_direction(auth_token, test_client):
    resp = post_command(test_client, auth_token, "go")
    assert resp.status_code == 200
    assert "Go where?" in resp.json()["result"]


def test_go_extra_whitespace(auth_token, test_client):
    resp = post_command(test_client, auth_token, "go   east")
    assert resp.status_code == 200
    result = resp.json()["result"]
    assert result.startswith("East Market Bazaar")
    assert "Colorful tents and exotic wares fill the lively bazaar" in result
    assert "Exits: west" in result


def test_say_with_message(auth_token, test_client):
    resp = post_command(test_client, auth_token, "say hello world")
    assert resp.status_code == 200
    assert resp.json()["result"] == "You say: hello world"


def test_say_empty(auth_token, test_client):
    resp = post_command(test_client, auth_token, "say   ")
    assert resp.status_code == 200
    assert resp.json()["result"] == "You open your mouth, but no words come out"


def test_unknown_command(auth_token, test_client):
    resp = post_command(test_client, auth_token, "foobar")
    assert resp.status_code == 200
    assert "Unknown command" in resp.json()["result"]


def test_case_insensitivity(auth_token, test_client):
    resp = post_command(test_client, auth_token, "LoOk")
    assert resp.status_code == 200
    result = resp.json()["result"]
    assert result.startswith("Arkham Town Square")
    assert "You are standing in the bustling heart of Arkham." in result
    assert "Exits: north, south, east, west" in result


def test_max_length(auth_token, test_client):
    valid_cmd = "a" * 50
    resp = post_command(test_client, auth_token, valid_cmd)
    assert resp.status_code == 200
    long_cmd = "a" * 51
    resp = post_command(test_client, auth_token, long_cmd)
    assert resp.status_code == 400
    assert "too long" in resp.json()["detail"].lower()


def test_command_injection(auth_token, test_client):
    # Shell injection
    malicious = "say ; rm -rf /"
    resp = post_command(test_client, auth_token, malicious)
    assert resp.status_code == 400
    assert "invalid characters" in resp.json()["detail"].lower()
    # SQL injection
    sql_inject = "say ' OR 1=1; --"
    resp = post_command(test_client, auth_token, sql_inject)
    assert resp.status_code == 400
    assert "invalid characters" in resp.json()["detail"].lower()
    # Python code injection
    py_inject = "say __import__('os').system('ls')"
    resp = post_command(test_client, auth_token, py_inject)
    assert resp.status_code == 400
    assert "invalid characters" in resp.json()["detail"].lower()
    # Format string attack
    fmt_inject = "say %x %x %x"
    resp = post_command(test_client, auth_token, fmt_inject)
    assert resp.status_code == 400
    assert "invalid characters" in resp.json()["detail"].lower()
    # Unicode/emoji (should be allowed if not dangerous)
    unicode_ok = "say hello 😊"
    resp = post_command(test_client, auth_token, unicode_ok)
    assert resp.status_code == 200
    assert "😊" in resp.json()["result"]


def test_look_direction_valid(auth_token, test_client):
    resp = post_command(test_client, auth_token, "look north")
    assert resp.status_code == 200
    result = resp.json()["result"]
    assert result.startswith("Miskatonic University Gates")
    assert "The grand wrought-iron gates of Miskatonic University loom here" in result


def test_look_direction_invalid(auth_token, test_client):
    resp = post_command(test_client, auth_token, "look up")
    assert resp.status_code == 200
    result = resp.json()["result"]
    assert (
        result == "You see nothing special that way."
        or result == "You see nothing special."
    )


def test_look_direction_extra_whitespace(auth_token, test_client):
    resp = post_command(test_client, auth_token, "look   north   ")
    assert resp.status_code == 200
    result = resp.json()["result"]
    assert result.startswith("Miskatonic University Gates")
    assert "The grand wrought-iron gates of Miskatonic University loom here" in result


def test_look_direction_case_insensitive(auth_token, test_client):
    resp = post_command(test_client, auth_token, "LOOK NorTh")
    assert resp.status_code == 200
    result = resp.json()["result"]
    assert result.startswith("Miskatonic University Gates")
    assert "The grand wrought-iron gates of Miskatonic University loom here" in result


def test_go_valid_direction(auth_token, test_client):
    resp = post_command(test_client, auth_token, "go north")
    assert resp.status_code == 200
    result = resp.json()["result"]
    assert result.startswith("Miskatonic University Gates")
    assert "The grand wrought-iron gates of Miskatonic University loom here" in result
    # After moving, look should return the new room
    resp2 = post_command(test_client, auth_token, "look")
    assert resp2.status_code == 200
    result2 = resp2.json()["result"]
    assert result2.startswith("Miskatonic University Gates")
    assert "The grand wrought-iron gates of Miskatonic University loom here" in result2


def test_go_invalid_direction(auth_token, test_client):
    resp = post_command(test_client, auth_token, "go up")
    assert resp.status_code == 200
    assert resp.json()["result"] == "You can't go that way"


def test_go_blocked_exit(auth_token, test_client):
    pm = test_client.app.state.player_manager
    # Move north first
    resp1 = post_command(test_client, auth_token, "go north")
    print(f"After first go north: {pm.get_player_by_name('cmduser').current_room_id}")
    print(f"First go north result: {resp1.json()['result']}")
    # Try to go north again
    resp2 = post_command(test_client, auth_token, "go north")
    print(f"After second go north: {pm.get_player_by_name('cmduser').current_room_id}")
    print(f"Second go north result: {resp2.json()['result']}")
    assert resp2.status_code == 200
    # The player should now be in University Quad
    assert resp2.json()["result"].startswith("University Quad")
    assert "A broad green lawn surrounded by academic halls" in resp2.json()["result"]


def test_print_rooms_and_player_manager(test_client):
    # Print loaded rooms
    rooms = test_client.app.state.rooms
    print("Loaded rooms:")
    for room_id, room in rooms.items():
        print(f"- {room_id}: {room.get('name', '')} exits={room.get('exits', {})}")
    # Print player manager data
    player_manager = test_client.app.state.player_manager
    print("Players in manager:")
    for player in player_manager.list_players():
        print(f"- {player.name} in {player.current_room_id}")
    # Ensure test user is present
    player = player_manager.get_player_by_name("cmduser")
    if not player:
        # Create the player if not present
        player_manager.create_player("cmduser", "arkham_001")
        print("Created player 'cmduser' in arkham_001")
    else:
        print(f"Player 'cmduser' already exists in {player.current_room_id}")
    assert player_manager.get_player_by_name("cmduser") is not None


def test_debug_player_room_after_move(auth_token, test_client):
    pm = test_client.app.state.player_manager
    player = pm.get_player_by_name("cmduser")
    print(f"Before move: {player.current_room_id}")
    post_command(test_client, auth_token, "go north")
    player = pm.get_player_by_name("cmduser")
    print(f"After move north: {player.current_room_id}")
    post_command(test_client, auth_token, "go north")
    player = pm.get_player_by_name("cmduser")
    print(f"After move north again: {player.current_room_id}")


def test_minimal_registration_login_room(test_client):
    test_client.post(
        "/auth/register",
        json={
            "username": "cmduser",
            "password": "testpass",
            "invite_code": "INVITE123",
        },
    )
    pm = test_client.app.state.player_manager
    print(
        f"[minimal] After registration: {pm.get_player_by_name('cmduser').current_room_id}"
    )
    test_client.post(
        "/auth/login", json={"username": "cmduser", "password": "testpass"}
    )
    print(f"[minimal] After login: {pm.get_player_by_name('cmduser').current_room_id}")


def test_no_file_io(monkeypatch):
    def fail_open(*args, **kwargs):
        raise AssertionError(f"File I/O attempted: open({args}, {kwargs})")

    monkeypatch.setattr("builtins.open", fail_open)
    # Try a simple command to trigger any accidental file I/O
    from server.tests.mock_data import MockPlayerManager

    pm = MockPlayerManager()
    pm.get_player_by_name("cmduser")
    # If no AssertionError, test passes


def test_player_room_persistence_after_go(auth_token, test_client):
    pm = test_client.app.state.player_manager
    player = pm.get_player_by_name("cmduser")
    print(f"Before move: {player.current_room_id}")  # Should be arkham_001

    # Move north
    resp = post_command(test_client, auth_token, "go north")
    assert resp.status_code == 200
    player = pm.get_player_by_name("cmduser")
    print(f"After go north: {player.current_room_id}")  # Should be arkham_002

    # Issue look
    resp2 = post_command(test_client, auth_token, "look")
    assert resp2.status_code == 200
    player = pm.get_player_by_name("cmduser")
    print(f"After look: {player.current_room_id}")  # Should still be arkham_002

    # Check the result of look
    result2 = resp2.json()["result"]
    print(f"Look result: {result2}")
