"""
Tests for game API endpoints, specifically the broadcast functionality.

This module tests the game API endpoints including the broadcast message feature
which requires authenticated users.
"""

from unittest.mock import Mock

from fastapi.testclient import TestClient

from server.main import app


class TestGameApiBroadcast:
    """Test game API broadcast endpoint."""

    def setup_method(self):
        """Set up test fixtures."""
        self.client = TestClient(app)

    def test_broadcast_endpoint_authenticated(self):
        """Test broadcast endpoint with authenticated user.

        AI: Tests the broadcast message endpoint body (lines 53-61 in api/game.py).
        Covers the TODO path for admin verification where we log a warning about
        sending broadcast without admin verification. This is the primary uncovered
        path in the broadcast_message endpoint.
        """
        # Mock the authentication dependency to return a user
        from server.auth.users import get_current_user

        # Create a mock user object with required attributes
        mock_user = Mock()
        mock_user.id = "test-user-id"
        mock_user.username = "testuser"

        async def mock_get_current_user():
            return mock_user

        # Override the dependency
        app.dependency_overrides[get_current_user] = mock_get_current_user

        try:
            # Send broadcast message - message is a query parameter in POST
            response = self.client.post(
                "/game/broadcast",
                params={"message": "Test broadcast message"},
            )

            # Verify response
            assert response.status_code == 200
            data = response.json()
            assert "message" in data
            assert "Test broadcast message" in data["message"]
        finally:
            # Clean up dependency override
            app.dependency_overrides.clear()
