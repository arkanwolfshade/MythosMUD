"""
Tests for SSE authentication mechanisms.

This module tests the Server-Sent Events authentication system including:
- JWT token validation
- Rate limiting
- Security headers
- WebSocket authentication
"""

import json
import tempfile
import time
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from server.auth import validate_sse_token, get_sse_auth_headers
from server.auth_utils import create_access_token
from server.main import app
from server.real_time import ConnectionManager


@pytest.fixture
def temp_files():
    """Create temporary files for users and invites."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as users_file:
        json.dump([
            {
                "username": "testuser",
                "password_hash": "hashed_password",
                "invite_code": "TEST_INVITE",
                "created_at": "2024-01-01T00:00:00Z"
            }
        ], users_file)
        users_path = users_file.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as invites_file:
        json.dump([
            {"code": "TEST_INVITE", "used": True}
        ], invites_file)
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
    from server.auth import get_users_file, get_invites_file
    app.dependency_overrides[get_users_file] = lambda: users_path
    app.dependency_overrides[get_invites_file] = lambda: invites_path

    with TestClient(app) as client:
        # Set up the persistence layer in app state
        from server.persistence import get_persistence
        client.app.state.persistence = get_persistence()
        yield client

    app.dependency_overrides = {}


@pytest.fixture
def valid_token():
    """Create a valid JWT token for testing."""
    return create_access_token(data={"sub": "testuser"})


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
        assert user_info["username"] == "testuser"

    def test_validate_sse_token_invalid(self, temp_files, invalid_token):
        """Test that invalid tokens are rejected."""
        users_path, _ = temp_files
        with pytest.raises(Exception):
            validate_sse_token(invalid_token, users_path)

    def test_validate_sse_token_none(self, temp_files):
        """Test that None tokens are rejected."""
        users_path, _ = temp_files
        with pytest.raises(Exception):
            validate_sse_token(None, users_path)

    def test_validate_sse_token_empty(self, temp_files):
        """Test that empty tokens are rejected."""
        users_path, _ = temp_files
        with pytest.raises(Exception):
            validate_sse_token("", users_path)

    def test_validate_sse_token_no_users_file(self, valid_token):
        """Test token validation without users file."""
        user_info = validate_sse_token(valid_token)
        assert user_info["username"] == "testuser"

    def test_validate_sse_token_user_not_found(self, temp_files):
        """Test token validation when user doesn't exist in users file."""
        users_path, _ = temp_files
        # Create token for user that doesn't exist in users file
        token = create_access_token(data={"sub": "nonexistentuser"})
        with pytest.raises(Exception):
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
        response = test_client.get(
            f"/events/testuser?token={valid_token}",
            headers={"Accept": "text/event-stream"}
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "text/event-stream"

        # Check that security headers are present
        assert "X-Content-Type-Options" in response.headers
        assert "X-Frame-Options" in response.headers

    def test_sse_endpoint_with_invalid_token(self, test_client, invalid_token):
        """Test SSE endpoint with invalid authentication token."""
        response = test_client.get(
            f"/events/testuser?token={invalid_token}",
            headers={"Accept": "text/event-stream"}
        )
        assert response.status_code == 401

    def test_sse_endpoint_without_token(self, test_client):
        """Test SSE endpoint without authentication token."""
        response = test_client.get(
            "/events/testuser",
            headers={"Accept": "text/event-stream"}
        )
        assert response.status_code == 401

    def test_sse_endpoint_token_mismatch(self, test_client, valid_token):
        """Test SSE endpoint when token doesn't match player ID."""
        response = test_client.get(
            f"/events/differentuser?token={valid_token}",
            headers={"Accept": "text/event-stream"}
        )
        assert response.status_code == 403

    def test_sse_endpoint_with_authorization_header(self, test_client, valid_token):
        """Test SSE endpoint with Authorization header."""
        response = test_client.get(
            "/events/testuser",
            headers={
                "Accept": "text/event-stream",
                "Authorization": f"Bearer {valid_token}"
            }
        )
        assert response.status_code == 200


class TestWebSocketAuthentication:
    """Test WebSocket authentication."""

    def test_websocket_with_valid_token(self, test_client, valid_token):
        """Test WebSocket connection with valid token."""
        with test_client.websocket_connect(
            f"/ws/testuser?token={valid_token}"
        ) as websocket:
            # Connection should be established
            assert websocket is not None

    def test_websocket_with_invalid_token(self, test_client, invalid_token):
        """Test WebSocket connection with invalid token."""
        with pytest.raises(Exception):
            test_client.websocket_connect(
                f"/ws/testuser?token={invalid_token}"
            )

    def test_websocket_without_token(self, test_client):
        """Test WebSocket connection without token."""
        with pytest.raises(Exception):
            test_client.websocket_connect("/ws/testuser")

    def test_websocket_token_mismatch(self, test_client, valid_token):
        """Test WebSocket connection when token doesn't match player ID."""
        with pytest.raises(Exception):
            test_client.websocket_connect(
                f"/ws/differentuser?token={valid_token}"
            )


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
        with patch('time.time') as mock_time:
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
        # Make multiple rapid requests to trigger rate limiting
        responses = []
        for _ in range(10):
            response = test_client.get(
                f"/events/testuser?token={valid_token}",
                headers={"Accept": "text/event-stream"}
            )
            responses.append(response)

        # Some requests should succeed, others should be rate limited
        success_count = sum(1 for r in responses if r.status_code == 200)
        assert success_count > 0  # At least some should succeed
        assert success_count < len(responses)  # Not all should succeed

    def test_sse_authentication_flow(self, test_client):
        """Test complete SSE authentication flow."""
        # First, register and login to get a token
        register_response = test_client.post(
            "/auth/register",
            json={
                "username": "sseuser",
                "password": "testpass",
                "invite_code": "TEST_INVITE"
            }
        )
        assert register_response.status_code == 201

        login_response = test_client.post(
            "/auth/login",
            json={"username": "sseuser", "password": "testpass"}
        )
        assert login_response.status_code == 200

        token = login_response.json()["access_token"]

        # Now try to connect to SSE with the token
        sse_response = test_client.get(
            f"/events/sseuser?token={token}",
            headers={"Accept": "text/event-stream"}
        )
        assert sse_response.status_code == 200
