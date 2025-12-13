"""
Tests for dependency injection system.

This module tests the dependency injection system to ensure that
services are properly injected into API endpoints.
"""

from unittest.mock import Mock

from fastapi import Request

from server.dependencies import get_player_service, get_room_service
from server.game.player_service import PlayerService
from server.game.room_service import RoomService


class TestDependencyInjection:
    """Test the dependency injection system."""

    def test_get_player_service_creates_instance(self, container_test_client):
        """
        Test that get_player_service returns PlayerService from container.

        AI: ARCHITECTURE CHANGE - Updated to use container-based DI
        """

        # Create mock request with real container
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        # Get the service
        service = get_player_service(mock_request)

        # Verify it's the real PlayerService from container
        assert isinstance(service, PlayerService)
        assert service is container_test_client.app.state.container.player_service

    def test_get_room_service_creates_instance(self, container_test_client):
        """
        Test that get_room_service returns RoomService from container.

        AI: ARCHITECTURE CHANGE - Updated to use container-based DI
        """

        # Create mock request with real container
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        # Get the service
        service = get_room_service(mock_request)

        # Verify it's the real RoomService from container
        assert isinstance(service, RoomService)
        assert service is container_test_client.app.state.container.room_service

    def test_dependency_injection_in_fastapi_app(self, container_test_client):
        """
        Test that dependency injection works in the FastAPI application with container.

        AI: ARCHITECTURE CHANGE - Updated to use container-based TestClient
        """
        # Test that the dependency injection works by making a request
        # This should not raise an import error or dependency resolution error
        response = container_test_client.get("/api/players/")

        # The response might be 401 (unauthorized), 422 (validation error), or 200 (success)
        # The important thing is that it doesn't fail with dependency injection errors
        assert response.status_code in [200, 401, 403, 422]

    def test_player_service_dependency_resolution(self, container_test_client):
        """
        Test that PlayerService dependency is properly resolved with container.

        AI: ARCHITECTURE CHANGE - Updated to use container-based TestClient
        """

        # Create mock request with real container
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        # This should not raise an error
        service = get_player_service(mock_request)
        assert service is not None
        assert isinstance(service, PlayerService)
        assert service is container_test_client.app.state.container.player_service

    def test_room_service_dependency_resolution(self, container_test_client):
        """
        Test that RoomService dependency is properly resolved with container.

        AI: ARCHITECTURE CHANGE - Updated to use container-based TestClient
        """

        # Create mock request with real container
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        # This should not raise an error
        service = get_room_service(mock_request)
        assert service is not None
        assert isinstance(service, RoomService)
        assert service is container_test_client.app.state.container.room_service
