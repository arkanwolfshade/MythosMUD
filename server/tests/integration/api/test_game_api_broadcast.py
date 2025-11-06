"""
Tests for game API endpoints, specifically the broadcast functionality.

This module tests the game API endpoints including the broadcast message feature
which requires superuser (admin) privileges.
"""

from unittest.mock import Mock

from fastapi.testclient import TestClient

from server.main import app


class TestGameApiBroadcast:
    """Test game API broadcast endpoint."""

    def setup_method(self):
        """Set up test fixtures."""
        self.client = TestClient(app)

    def test_broadcast_endpoint_requires_superuser(self):
        """Test broadcast endpoint with authenticated superuser.

        AI: Tests the broadcast message endpoint with proper admin authentication.
        Verifies that the endpoint correctly uses get_current_superuser dependency
        and allows superusers to broadcast messages.
        """
        # Mock the authentication dependency to return a superuser
        from server.auth.dependencies import get_current_superuser

        # Create a mock superuser object with required attributes
        mock_superuser = Mock()
        mock_superuser.id = "admin-user-id"
        mock_superuser.username = "admin"
        mock_superuser.is_superuser = True

        async def mock_get_current_superuser():
            return mock_superuser

        # AI Agent: Mock the broadcast endpoint's dependency injection
        #           The endpoint uses `container.connection_manager` from request state
        async def mock_broadcast_global(*args, **kwargs):
            return {
                "successful_deliveries": 5,
                "failed_deliveries": 0,
                "total_players": 5,
            }

        # Override the dependency
        app.dependency_overrides[get_current_superuser] = mock_get_current_superuser

        try:
            # Send broadcast message - message is a query parameter in POST
            # The endpoint will work with container.connection_manager if app is started
            response = self.client.post(
                "/game/broadcast",
                params={"message": "Test broadcast message"},
            )

            # Verify response
            assert response.status_code == 200
            data = response.json()
            assert "message" in data
            assert data["message"] == "Test broadcast message"
            # Note: actual broadcast results depend on the connection_manager state in the app
            assert "recipients" in data
            assert "broadcaster" in data
            assert data["broadcaster"] == "admin"
        finally:
            # Clean up dependency override
            app.dependency_overrides.clear()

    def test_broadcast_endpoint_rejects_non_superuser(self):
        """Test broadcast endpoint rejects non-superuser with 403.

        AI: Tests that the endpoint correctly rejects non-admin users
        and returns a 403 Forbidden error as per security requirements.
        """
        from server.auth.dependencies import get_current_superuser
        from server.exceptions import LoggedHTTPException

        # Create a mock non-superuser
        mock_user = Mock()
        mock_user.id = "regular-user-id"
        mock_user.username = "regularuser"
        mock_user.is_superuser = False

        async def mock_get_current_superuser_rejects():
            # Simulate the actual get_current_superuser behavior for non-superusers
            raise LoggedHTTPException(
                status_code=403,
                detail="The user doesn't have enough privileges",
            )

        # Override the dependency
        app.dependency_overrides[get_current_superuser] = mock_get_current_superuser_rejects

        try:
            # Attempt to send broadcast message as non-admin
            response = self.client.post(
                "/game/broadcast",
                params={"message": "Unauthorized broadcast"},
            )

            # Verify rejection
            assert response.status_code == 403
            data = response.json()
            # The error response might be in either format depending on error handling middleware
            assert "doesn't have enough privileges" in str(
                data.get("detail", "")
            ) or "doesn't have enough privileges" in str(data.get("error", ""))
        finally:
            # Clean up dependency override
            app.dependency_overrides.clear()
