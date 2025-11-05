"""
Test the actual dependency injection functions.

This module tests that the get_player_service and get_room_service functions
work correctly and return the expected service instances.
"""

from unittest.mock import AsyncMock, Mock

import pytest
from fastapi import Request

from server.dependencies import get_player_service, get_room_service
from server.game.player_service import PlayerService
from server.game.room_service import RoomService


class TestDependencyInjectionFunctions:
    """Test the dependency injection functions."""

    @pytest.fixture
    def mock_persistence(self):
        """Create mock persistence layer."""
        mock_persistence = AsyncMock()
        mock_persistence.async_list_players.return_value = []
        mock_persistence.async_get_player.return_value = None
        mock_persistence.async_get_room.return_value = None
        mock_persistence.async_save_player.return_value = None
        mock_persistence.delete_player.return_value = True
        # Also mock synchronous methods for backward compatibility
        mock_persistence.list_players.return_value = []
        mock_persistence.get_player.return_value = None
        mock_persistence.get_room.return_value = None
        mock_persistence.save_player.return_value = None
        mock_persistence.delete_player.return_value = True
        return mock_persistence

    @pytest.fixture
    def mock_request(self, mock_persistence):
        """Create mock request with app state."""
        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence
        return mock_request

    def test_get_player_service_function(self, container_test_client):
        """
        Test that get_player_service function works correctly with container.

        AI: ARCHITECTURE CHANGE - Updated to use container-based DI
        """
        # Create mock request with container
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        service = get_player_service(mock_request)

        # ARCHITECTURE FIX: Service comes from container
        assert isinstance(service, PlayerService)
        assert hasattr(service, "persistence")
        assert service.persistence is container_test_client.app.state.container.persistence

    def test_get_room_service_function(self, container_test_client):
        """
        Test that get_room_service function works correctly with container.

        AI: ARCHITECTURE CHANGE - Updated to use container-based DI
        """
        # Create mock request with container
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        service = get_room_service(mock_request)

        # ARCHITECTURE FIX: Service comes from container
        assert isinstance(service, RoomService)
        assert hasattr(service, "persistence")
        assert service.persistence is container_test_client.app.state.container.persistence

    def test_dependency_functions_return_same_instances(self, container_test_client):
        """
        Test that dependency functions return SAME instances from container (singleton).

        AI: ARCHITECTURE CHANGE - Container uses singleton pattern
        Old behavior: Each call created new service instance
        New behavior: Container returns same service instance (singleton)
        """
        # Create mock request with container
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        player_service1 = get_player_service(mock_request)
        player_service2 = get_player_service(mock_request)
        room_service1 = get_room_service(mock_request)
        room_service2 = get_room_service(mock_request)

        # ARCHITECTURE FIX: Container uses singleton pattern
        assert player_service1 is player_service2  # Same instance
        assert room_service1 is room_service2  # Same instance
        assert player_service1 is not room_service1  # Different services

    def test_dependency_functions_with_container_persistence(self, container_test_client):
        """
        Test dependency functions use container's persistence layer.

        AI: ARCHITECTURE CHANGE - All services use same persistence from container
        """
        # Create mock requests with container
        mock_request1 = Mock(spec=Request)
        mock_request1.app = container_test_client.app

        mock_request2 = Mock(spec=Request)
        mock_request2.app = container_test_client.app

        player_service = get_player_service(mock_request1)
        room_service = get_room_service(mock_request2)

        # ARCHITECTURE FIX: Both services use SAME persistence from container
        container_persistence = container_test_client.app.state.container.persistence
        assert player_service.persistence is container_persistence
        assert room_service.persistence is container_persistence
        assert player_service.persistence is room_service.persistence

    def test_dependency_function_error_handling(self):
        """
        Test that dependency functions handle missing container gracefully.

        AI: ARCHITECTURE CHANGE - Requires container to be initialized
        """
        # Test with request that has no container
        bad_request = Mock(spec=Request)
        bad_request.app = Mock()
        bad_request.app.state = Mock()
        # Simulate missing container
        bad_request.app.state.container = None

        with pytest.raises((AttributeError, RuntimeError)):
            get_player_service(bad_request)

    def test_dependency_functions_require_container(self):
        """
        Test dependency functions require ApplicationContainer.

        AI: ARCHITECTURE CHANGE - Container must be initialized
        """
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        # Simulate missing container
        mock_request.app.state.container = None

        # ARCHITECTURE FIX: Missing container raises error
        with pytest.raises((AttributeError, RuntimeError)):
            get_player_service(mock_request)

    def test_dependency_functions_consistency(self, container_test_client):
        """
        Test that dependency functions behave consistently (return same instance).

        AI: ARCHITECTURE CHANGE - Container uses singleton pattern
        """
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        # Call the function multiple times
        services = []
        for _ in range(5):
            service = get_player_service(mock_request)
            services.append(service)

        # ARCHITECTURE FIX: All services are SAME instance (singleton)
        for service in services:
            assert isinstance(service, PlayerService)
            assert service is services[0]  # All are same instance

    def test_dependency_functions_use_container_persistence(self, container_test_client):
        """
        Test dependency functions use container's persistence layer.

        AI: ARCHITECTURE CHANGE - All services use container persistence
        """
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        service = get_player_service(mock_request)

        # ARCHITECTURE FIX: Service uses container's persistence
        container_persistence = container_test_client.app.state.container.persistence
        assert service.persistence is container_persistence

    def test_dependency_functions_with_different_service_types(self, container_test_client):
        """
        Test that different dependency functions return different service types.

        AI: ARCHITECTURE CHANGE - Uses container for both services
        """
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        player_service = get_player_service(mock_request)
        room_service = get_room_service(mock_request)

        # Verify they are different service types
        assert isinstance(player_service, PlayerService)
        assert isinstance(room_service, RoomService)
        # ARCHITECTURE FIX: Both from container
        assert player_service is container_test_client.app.state.container.player_service
        assert room_service is container_test_client.app.state.container.room_service
        assert not isinstance(player_service, RoomService)
        assert not isinstance(room_service, PlayerService)
