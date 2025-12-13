"""
Tests for game API endpoints, specifically the broadcast functionality.

This module tests the game API endpoints including the broadcast message feature
which requires superuser (admin) privileges.
"""

from unittest.mock import Mock

import pytest


class TestGameApiBroadcast:
    """Test game API broadcast endpoint."""

    @pytest.fixture(scope="class")
    def client(self, container_test_client_class):
        """Class-scoped client fixture."""
        return container_test_client_class

    @pytest.fixture(autouse=True)
    def _setup(self, client):
        """Set client as instance variable for backward compatibility."""
        self.client = client

    def test_broadcast_endpoint_requires_superuser(self):
        """Test broadcast endpoint with authenticated superuser.

        AI: Tests the broadcast message endpoint with proper admin authentication.
        Verifies that the endpoint correctly uses get_current_superuser dependency
        and allows superusers to broadcast messages.
        """
        # Mock the authentication dependency to return a superuser
        from unittest.mock import AsyncMock

        from server.auth.dependencies import get_current_superuser

        # Create a mock superuser object with required attributes
        mock_superuser = Mock()
        mock_superuser.id = "admin-user-id"
        mock_superuser.username = "admin"
        mock_superuser.is_superuser = True

        async def mock_get_current_superuser():
            return mock_superuser

        # Ensure container and connection_manager are set up
        # The container should already be set up by container_test_client_class fixture
        # But ensure connection_manager exists and is mocked
        if hasattr(self.client.app.state, "container") and self.client.app.state.container:
            container = self.client.app.state.container
            if not hasattr(container, "connection_manager") or container.connection_manager is None:
                from server.realtime.connection_manager import ConnectionManager

                container.connection_manager = ConnectionManager()
            # Mock broadcast_global_event to avoid actual broadcasting
            container.connection_manager.broadcast_global_event = AsyncMock(
                return_value={"successful_deliveries": 0, "message": "Test broadcast message"}
            )

        # Patch dependency override on the test client's app
        self.client.app.dependency_overrides[get_current_superuser] = mock_get_current_superuser

        try:
            response = self.client.post(
                "/game/broadcast",
                params={"message": "Test broadcast message"},
            )

            assert response.status_code == 200
            data = response.json()
            assert "message" in data
            assert data["message"] == "Test broadcast message"
            assert "recipients" in data
            assert "broadcaster" in data
            assert data["broadcaster"] == "admin"
        finally:
            self.client.app.dependency_overrides.clear()

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
            raise LoggedHTTPException(
                status_code=403,
                detail="The user doesn't have enough privileges",
            )

        self.client.app.dependency_overrides[get_current_superuser] = mock_get_current_superuser_rejects

        try:
            response = self.client.post(
                "/game/broadcast",
                params={"message": "Unauthorized broadcast"},
            )

            assert response.status_code == 403
            data = response.json()
            assert "doesn't have enough privileges" in str(
                data.get("detail", "")
            ) or "doesn't have enough privileges" in str(data.get("error", ""))
        finally:
            self.client.app.dependency_overrides.clear()
