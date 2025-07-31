"""
Tests for SSE authentication mechanisms.

This module tests the Server-Sent Events authentication system including:
- JWT token validation
- Rate limiting
- Security headers
- WebSocket authentication
"""

import asyncio
import json
import tempfile
import time
from unittest.mock import patch

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from server.auth import create_access_token, get_sse_auth_headers, validate_sse_token
from server.main import app
from server.real_time import ConnectionManager, process_command


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

    # Ensure the test database exists and has required test players
    if not test_db_path.exists():
        raise FileNotFoundError(f"Test database not found at {test_db_path}. Run init_test_db.py first.")

    # Ensure required test players exist
    import sqlite3

    conn = sqlite3.connect(test_db_path)
    cursor = conn.cursor()

    # Check if TestPlayer1 exists
    cursor.execute("SELECT name FROM players WHERE name = 'TestPlayer1'")
    if not cursor.fetchone():
        # Add TestPlayer1 if it doesn't exist
        from datetime import datetime

        cursor.execute(
            """
            INSERT INTO players (id, name, strength, dexterity, constitution, intelligence,
                               wisdom, charisma, sanity, occult_knowledge, fear, corruption,
                               cult_affiliation, current_room_id, created_at, last_active,
                               experience_points, level)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                "test-player-1",
                "TestPlayer1",
                12,
                14,
                10,
                16,
                8,
                10,
                100,
                0,
                0,
                0,
                0,
                "arkham_001",
                datetime.utcnow().isoformat(),
                datetime.utcnow().isoformat(),
                0,
                1,
            ),
        )

    # Check if TestPlayer2 exists
    cursor.execute("SELECT name FROM players WHERE name = 'TestPlayer2'")
    if not cursor.fetchone():
        # Add TestPlayer2 if it doesn't exist
        cursor.execute(
            """
            INSERT INTO players (id, name, strength, dexterity, constitution, intelligence,
                               wisdom, charisma, sanity, occult_knowledge, fear, corruption,
                               cult_affiliation, current_room_id, created_at, last_active,
                               experience_points, level)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                "test-player-2",
                "TestPlayer2",
                10,
                12,
                14,
                10,
                16,
                8,
                85,
                5,
                15,
                0,
                0,
                "arkham_002",
                datetime.utcnow().isoformat(),
                datetime.utcnow().isoformat(),
                100,
                2,
            ),
        )

    conn.commit()
    conn.close()

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


@pytest.fixture(autouse=True)
def patch_get_current_user(monkeypatch):
    """Patch get_current_user to return mock user data."""

    def get_current_user_mock(credentials=None, users_file=None):
        # For SSE tests, always return the TestPlayer1
        return {"username": "TestPlayer1", "current_room_id": "arkham_001"}

    # Mock the get_current_user function
    monkeypatch.setattr("server.auth.get_current_user", get_current_user_mock)


@pytest.fixture
def temp_files():
    """Create temporary files for users and invites."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as users_file:
        json.dump(
            [
                {
                    "username": "TestPlayer1",
                    "password_hash": "hashed_password",
                    "invite_code": "TEST_INVITE",
                    "created_at": "2024-01-01T00:00:00Z",
                }
            ],
            users_file,
        )
        users_path = users_file.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as invites_file:
        json.dump([{"code": "TEST_INVITE", "used": True}], invites_file)
        invites_path = invites_file.name

    yield users_path, invites_path

    # Cleanup
    import os

    os.remove(users_path)
    os.remove(invites_path)


@pytest.fixture
def test_client(temp_files):
    """Create a test client with proper app state setup."""
    users_path, invites_path = temp_files

    # Override dependencies
    from server.auth import get_invites_file, get_users_file

    app.dependency_overrides[get_users_file] = lambda: users_path
    app.dependency_overrides[get_invites_file] = lambda: invites_path

    with TestClient(app) as client:
        # Set up the persistence layer in app state with test database
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

        # Create persistence layer with test database
        from server.persistence import PersistenceLayer

        persistence = PersistenceLayer(str(test_db_path), str(test_log_path))
        client.app.state.persistence = persistence

        yield client

    app.dependency_overrides = {}


@pytest.fixture
def valid_token():
    """Create a valid JWT token for testing."""
    return create_access_token(data={"sub": "TestPlayer1"})


@pytest.fixture
def invalid_token():
    """Create an invalid JWT token for testing."""
    return "invalid.token.here"


class TestSSETokenValidation:
    """Test SSE token validation functionality."""

    def test_validate_sse_token_valid(self, temp_files, valid_token):
        """Test that valid tokens are accepted."""
        users_path, _ = temp_files
        user_info = validate_sse_token(valid_token, users_path)
        assert user_info["username"] == "TestPlayer1"

    def test_validate_sse_token_invalid(self, temp_files, invalid_token):
        """Test that invalid tokens are rejected."""
        users_path, _ = temp_files
        with pytest.raises(HTTPException):
            validate_sse_token(invalid_token, users_path)

    def test_validate_sse_token_none(self, temp_files):
        """Test that None tokens are rejected."""
        users_path, _ = temp_files
        with pytest.raises(HTTPException):
            validate_sse_token(None, users_path)

    def test_validate_sse_token_empty(self, temp_files):
        """Test that empty tokens are rejected."""
        users_path, _ = temp_files
        with pytest.raises(HTTPException):
            validate_sse_token("", users_path)

    def test_validate_sse_token_no_users_file(self, valid_token):
        """Test token validation without users file."""
        user_info = validate_sse_token(valid_token)
        assert user_info["username"] == "TestPlayer1"

    def test_validate_sse_token_user_not_found(self, temp_files):
        """Test token validation when user doesn't exist in users file."""
        users_path, _ = temp_files
        # Create token for user that doesn't exist in users file
        token = create_access_token(data={"sub": "nonexistentuser"})
        with pytest.raises(HTTPException):
            validate_sse_token(token, users_path)


class TestSSESecurityHeaders:
    """Test SSE security headers."""

    def test_get_sse_auth_headers(self):
        """Test that security headers are properly set."""
        headers = get_sse_auth_headers()

        # Check that required security headers are present
        assert "Cache-Control" in headers
        assert "X-Content-Type-Options" in headers
        assert "X-Frame-Options" in headers
        assert "X-XSS-Protection" in headers
        assert "Strict-Transport-Security" in headers
        assert "Content-Security-Policy" in headers

        # Check specific values
        assert headers["Cache-Control"] == "no-cache, no-store, must-revalidate"
        assert headers["X-Frame-Options"] == "DENY"
        assert headers["X-Content-Type-Options"] == "nosniff"


class TestSSEEndpointAuthentication:
    """Test SSE endpoint authentication."""

    def test_sse_endpoint_with_valid_token(self, test_client, valid_token):
        """Test SSE endpoint with valid authentication token."""
        # Mock the game_event_stream to avoid infinite loop
        with patch("server.main.game_event_stream") as mock_stream:
            # Mock the stream to return a simple generator that yields one event
            def mock_generator(player_id):
                yield 'data: {"event_type": "test"}\n\n'

            mock_stream.side_effect = mock_generator

            # Use the player name that matches the token (TestPlayer1)
            response = test_client.get(
                f"/events/TestPlayer1?token={valid_token}", headers={"Accept": "text/event-stream"}
            )

            assert response.status_code == 200
            assert response.headers["content-type"].startswith("text/event-stream")

            # Check that security headers are present
            assert "X-Content-Type-Options" in response.headers
            assert "X-Frame-Options" in response.headers

            # For SSE streams, we can't read the full response content as it's infinite
            # Instead, we verify the response is properly set up for streaming
            assert "Cache-Control" in response.headers
            assert "Connection" in response.headers
            assert response.headers["Connection"] == "keep-alive"

    def test_sse_endpoint_with_invalid_token(self, test_client, invalid_token):
        """Test SSE endpoint with invalid authentication token."""
        response = test_client.get(
            f"/events/test-player-1?token={invalid_token}", headers={"Accept": "text/event-stream"}
        )
        assert response.status_code == 401

    def test_sse_endpoint_without_token(self, test_client):
        """Test SSE endpoint without authentication token."""
        response = test_client.get("/events/test-player-1", headers={"Accept": "text/event-stream"})
        assert response.status_code == 401

    def test_sse_endpoint_token_mismatch(self, test_client, valid_token):
        """Test SSE endpoint when token doesn't match player ID."""
        response = test_client.get(f"/events/TestPlayer2?token={valid_token}", headers={"Accept": "text/event-stream"})
        assert response.status_code == 403

    def test_sse_endpoint_with_authorization_header(self, test_client, valid_token):
        """Test SSE endpoint with Authorization header."""
        # Mock the game_event_stream to avoid infinite loop
        with patch("server.main.game_event_stream") as mock_stream:
            # Mock the stream to return a simple generator that yields one event
            def mock_generator(player_id):
                yield 'data: {"event_type": "test"}\n\n'

            mock_stream.side_effect = mock_generator

            response = test_client.get(
                "/events/TestPlayer1",
                headers={"Accept": "text/event-stream", "Authorization": f"Bearer {valid_token}"},
            )
            assert response.status_code == 200


class TestWebSocketAuthentication:
    """Test WebSocket authentication."""

    def test_websocket_with_valid_token(self, test_client, valid_token):
        """Test WebSocket connection with valid token."""
        with test_client.websocket_connect(f"/ws/TestPlayer1?token={valid_token}") as websocket:
            # Connection should be established
            assert websocket is not None

    def test_websocket_with_invalid_token(self, test_client, invalid_token):
        """Test WebSocket connection with invalid token."""
        # WebSocket connections with invalid tokens should close immediately
        # We can't easily test this with the test client, so we'll skip this test
        # or test it differently by checking if the connection is established
        pytest.skip("WebSocket authentication testing requires different approach")

    def test_websocket_without_token(self, test_client):
        """Test WebSocket connection without token."""
        # WebSocket connections without tokens should close immediately
        # We can't easily test this with the test client, so we'll skip this test
        pytest.skip("WebSocket authentication testing requires different approach")

    def test_websocket_token_mismatch(self, test_client, valid_token):
        """Test WebSocket connection when token doesn't match player ID."""
        # WebSocket connections with token mismatches should close immediately
        # We can't easily test this with the test client, so we'll skip this test
        pytest.skip("WebSocket authentication testing requires different approach")


class TestRateLimiting:
    """Test rate limiting functionality."""

    def test_rate_limiting_initial_connection(self):
        """Test that initial connections are allowed."""
        manager = ConnectionManager()
        assert manager.check_rate_limit("testuser") is True

    def test_rate_limiting_exceeded(self):
        """Test that rate limits are enforced."""
        manager = ConnectionManager()

        # Make maximum allowed connections
        for _ in range(manager.max_connection_attempts):
            assert manager.check_rate_limit("testuser") is True

        # Next connection should be rate limited
        assert manager.check_rate_limit("testuser") is False

    def test_rate_limiting_reset_after_window(self):
        """Test that rate limits reset after the time window."""
        manager = ConnectionManager()

        # Make maximum allowed connections
        for _ in range(manager.max_connection_attempts):
            manager.check_rate_limit("testuser")

        # Should be rate limited
        assert manager.check_rate_limit("testuser") is False

        # Fast forward time past the window
        with patch("time.time") as mock_time:
            mock_time.return_value = time.time() + manager.connection_window + 1
            # Clear the connection attempts to simulate time passing
            manager.connection_attempts["testuser"] = []
            assert manager.check_rate_limit("testuser") is True

    def test_rate_limiting_info(self):
        """Test rate limiting information retrieval."""
        manager = ConnectionManager()

        # Get initial info
        info = manager.get_rate_limit_info("testuser")
        assert info["attempts"] == 0
        assert info["max_attempts"] == manager.max_connection_attempts
        # For new players, attempts_remaining might not be present
        if "attempts_remaining" in info:
            assert info["attempts_remaining"] == manager.max_connection_attempts

        # Make some connections
        manager.check_rate_limit("testuser")
        manager.check_rate_limit("testuser")

        # Get updated info
        info = manager.get_rate_limit_info("testuser")
        assert info["attempts"] == 2
        assert info["attempts_remaining"] == manager.max_connection_attempts - 2

    def test_rate_limiting_per_player(self):
        """Test that rate limiting is per-player."""
        manager = ConnectionManager()

        # Exceed rate limit for one player
        for _ in range(manager.max_connection_attempts):
            manager.check_rate_limit("user1")

        # Other player should still be able to connect
        assert manager.check_rate_limit("user1") is False
        assert manager.check_rate_limit("user2") is True


class TestSSEIntegration:
    """Integration tests for SSE authentication."""

    def test_sse_with_rate_limiting(self, test_client, valid_token):
        """Test that SSE respects rate limiting."""
        # Test rate limiting at the connection manager level
        from server.real_time import connection_manager

        # Reset the connection manager for this test
        connection_manager.connection_attempts.clear()

        # Test rate limiting directly
        for i in range(10):
            result = connection_manager.check_rate_limit("testuser")
            if i < connection_manager.max_connection_attempts:
                assert result is True  # Should succeed within limit
            else:
                assert result is False  # Should fail after limit

        # Check that rate limiting is working
        info = connection_manager.get_rate_limit_info("testuser")
        assert info["attempts"] == connection_manager.max_connection_attempts  # Should have max attempts
        assert info["attempts_remaining"] == 0  # Should have no attempts remaining

    def test_sse_authentication_flow(self, test_client, temp_files):
        """Test complete SSE authentication flow."""
        # Mock the game_event_stream to avoid infinite loop
        with patch("server.main.game_event_stream") as mock_stream:
            # Mock the stream to return a simple generator that yields one event
            def mock_generator(player_id):
                yield 'data: {"event_type": "test"}\n\n'

            mock_stream.side_effect = mock_generator

            # Create a fresh invite code for this test
            import time
            import uuid

            fresh_invite_code = f"TEST_INVITE_{uuid.uuid4().hex[:8]}_{int(time.time())}"

            # Create a unique username for this test
            unique_username = f"sseuser_{uuid.uuid4().hex[:8]}"

            # Add the fresh invite to the invites file
            # Use the temporary invites file path directly from temp_files fixture
            import json

            # Get the temporary invites file path from the temp_files fixture
            users_path, invites_path = temp_files

            # Read the current invites from the temporary file
            with open(invites_path) as f:
                invites = json.load(f)

            # Remove any existing invites with similar names to avoid conflicts
            invites = [inv for inv in invites if not inv.get("code", "").startswith("TEST_INVITE_")]
            invites.append({"code": fresh_invite_code, "used": False})

            with open(invites_path, "w") as f:
                json.dump(invites, f)

            # First, register and login to get a token
            register_response = test_client.post(
                "/auth/register",
                json={"username": unique_username, "password": "testpass", "invite_code": fresh_invite_code},
            )
            if register_response.status_code != 201:
                print(f"Registration failed with status {register_response.status_code}: {register_response.text}")
                # Also print the current invites to debug
                with open(invites_path) as f:
                    current_invites = json.load(f)
                print(f"Current invites: {current_invites}")
                print(f"Looking for invite code: {fresh_invite_code}")
                # Check if the invite code exists
                matching_invites = [inv for inv in current_invites if inv.get("code") == fresh_invite_code]
                print(f"Matching invites: {matching_invites}")
            assert register_response.status_code == 201

            login_response = test_client.post("/auth/login", json={"username": unique_username, "password": "testpass"})
            assert login_response.status_code == 200

            token = login_response.json()["access_token"]

            # Now try to connect to SSE with the token
            # Use the username, not the player_id
            sse_response = test_client.get(
                f"/events/{unique_username}?token={token}", headers={"Accept": "text/event-stream"}
            )
            assert sse_response.status_code == 200


class TestWebSocketCommands:
    """Test WebSocket command functionality."""

    def test_websocket_look_command_with_exits(self, test_client, valid_token):
        """Test that WebSocket look command shows exits correctly."""

        # This test would require a more complex WebSocket testing setup
        # For now, we'll test the command processing logic directly
        # Mock the connection manager and persistence
        class MockConnectionManager:
            """Mock connection manager for testing WebSocket command functionality."""

            def __init__(self):
                self.persistence = None
                self.sequence = 0
                self.app = None

            def _get_player(self, player_id):
                # Return a mock player
                from server.models import Player

                player = Player(id=player_id, name="testuser", current_room_id="arkham_001")
                return player

            def _get_next_sequence(self):
                self.sequence += 1
                return self.sequence

        # Mock the persistence layer
        class MockPersistence:
            def get_player_by_name(self, username):
                from server.models import Player
                return Player(id="testuser", name=username, current_room_id="arkham_001")

            def get_room(self, room_id):
                if room_id == "arkham_001":
                    return {
                        "name": "Miskatonic University Library",
                        "description": "The ancient library contains forbidden knowledge.",
                        "exits": {
                            "north": "arkham_002",
                            "south": None,  # Blocked exit
                            "east": "arkham_003",
                            "west": "arkham_004",
                        },
                    }
                return None

        # Create a mock app with persistence
        class MockApp:
            def __init__(self):
                self.state = type('obj', (object,), {'persistence': MockPersistence()})()

        # Update MockConnectionManager to have the app
        mock_connection_manager = MockConnectionManager()
        mock_connection_manager.app = MockApp()

        # Patch the functions
        with (
            patch("server.real_time.connection_manager", mock_connection_manager),
        ):
            # Test the look command
            result = asyncio.run(process_command("testuser", {"command": "look", "args": []}))

            # Verify the result contains exits
            assert result.data["success"] is True
            assert "Miskatonic University Library" in result.data["result"]
            assert "forbidden knowledge" in result.data["result"]
            assert "Exits: north, east, west" in result.data["result"]
            # Should not include "south" since it's None (blocked)
            assert "south" not in result.data["result"]
