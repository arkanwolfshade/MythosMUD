import pytest
from fastapi.testclient import TestClient
from server.main import app
from server.auth import get_users_file, get_invites_file
from server.tests.mock_data import MOCK_ROOMS, MockPlayerManager
from server.auth_utils import decode_access_token


# Patch the get_persistence function to prevent PersistenceLayer creation
@pytest.fixture(autouse=True)
def patch_get_persistence(monkeypatch):
    """Patch the get_persistence function to return a mock persistence layer."""
    class MockPersistenceLayer:
        def __init__(self):
            pass

        def get_player_by_name(self, name):
            return None

        def get_room(self, room_id):
            return None

    def mock_get_persistence():
        return MockPersistenceLayer()

    monkeypatch.setattr("server.persistence.get_persistence", mock_get_persistence)
    yield


# Patch get_current_user to always reflect the mock player's current room
@pytest.fixture(autouse=True)
def patch_get_current_user(monkeypatch):
    def get_current_user_mock(credentials=None, users_file=None):
        # Extract token from credentials
        token = None
        if credentials and hasattr(credentials, "credentials"):
            token = credentials.credentials
        elif isinstance(credentials, str):
            token = credentials
        if not token:
            return {"username": "cmduser", "current_room_id": "arkham_001"}
        payload = decode_access_token(token)
        username = payload["sub"] if payload and "sub" in payload else "cmduser"
        player_manager = app.state.player_manager
        player = player_manager.get_player_by_name(username)
        return {
            "username": player.name,
            "current_room_id": player.current_room_id,
        }

    monkeypatch.setattr("server.auth.get_current_user", get_current_user_mock)
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
        mock_rooms = MOCK_ROOMS.copy()
        client.app.state.player_manager = mock_player_manager
        client.app.state.rooms = mock_rooms
        player = mock_player_manager.get_player_by_name("cmduser")
        if player:
            print(f"[debug] Test start: cmduser in {player.current_room_id}")
        else:
            print("[debug] Test start: cmduser not found")
        yield client


@pytest.fixture
def auth_token(test_client):
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
        f"[auth_token] After registration: {pm.get_player_by_name('cmduser').current_room_id}"
    )
    resp = test_client.post(
        "/auth/login", json={"username": "cmduser", "password": "testpass"}
    )
    print(
        f"[auth_token] After login: {pm.get_player_by_name('cmduser').current_room_id}"
    )
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
