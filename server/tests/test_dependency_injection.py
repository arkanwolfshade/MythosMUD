"""
Tests for dependency injection system.

This module tests the dependency injection system to ensure that
services are properly injected into API endpoints.
"""

from unittest.mock import Mock

from fastapi.testclient import TestClient

from ..app.factory import create_app
from ..dependencies import get_player_service, get_room_service


class TestDependencyInjection:
    """Test the dependency injection system."""

    def test_get_player_service_creates_instance(self):
        """Test that get_player_service creates a PlayerService instance."""
        # Create a mock request with app state
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        # Get the service
        service = get_player_service(mock_request)

        # Verify it's a PlayerService instance
        from ..game.player_service import PlayerService

        assert isinstance(service, PlayerService)
        assert service.persistence == mock_persistence

    def test_get_room_service_creates_instance(self):
        """Test that get_room_service creates a RoomService instance."""
        # Create a mock request with app state
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        # Get the service
        service = get_room_service(mock_request)

        # Verify it's a RoomService instance
        from ..game.room_service import RoomService

        assert isinstance(service, RoomService)
        assert service.persistence == mock_persistence

    def test_dependency_injection_in_fastapi_app(self):
        """Test that dependency injection works in the FastAPI application."""
        # Create the app
        app = create_app()

        # Mock the persistence layer since TestClient doesn't run lifespan
        mock_persistence = Mock()
        app.state.persistence = mock_persistence

        client = TestClient(app)

        # Mock the player service methods
        mock_persistence.get_player.return_value = None
        mock_persistence.list_players.return_value = []

        # Test that the dependency injection works by making a request
        # This should not raise an import error or dependency resolution error
        response = client.get("/players/")

        # The response might be 401 (unauthorized) or 200 (success)
        # The important thing is that it doesn't fail with dependency injection errors
        assert response.status_code in [200, 401, 403]

    def test_player_service_dependency_resolution(self):
        """Test that PlayerService dependency is properly resolved."""
        # Create the app
        app = create_app()

        # Mock the persistence layer since TestClient doesn't run lifespan
        mock_persistence = Mock()
        app.state.persistence = mock_persistence

        # Test that the dependency injection works by directly calling the dependency function
        from fastapi import Request

        mock_request = Mock(spec=Request)
        mock_request.app = app

        # This should not raise an error
        service = get_player_service(mock_request)
        assert service is not None

    def test_room_service_dependency_resolution(self):
        """Test that RoomService dependency is properly resolved."""
        # Create the app
        app = create_app()

        # Mock the persistence layer since TestClient doesn't run lifespan
        mock_persistence = Mock()
        app.state.persistence = mock_persistence

        # Test that the dependency injection works by directly calling the dependency function
        from fastapi import Request

        mock_request = Mock(spec=Request)
        mock_request.app = app

        # This should not raise an error
        service = get_room_service(mock_request)
        assert service is not None
