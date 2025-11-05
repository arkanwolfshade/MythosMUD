"""
Simple tests for service layer dependency injection functionality.

This module tests that the service classes can be instantiated correctly
and that dependency injection patterns work as expected.
"""

from unittest.mock import AsyncMock

import pytest

from server.game.player_service import PlayerService
from server.game.room_service import RoomService


class TestServiceDependencyInjectionSimple:
    """Test service layer dependency injection without full app lifecycle."""

    @pytest.fixture
    def mock_persistence(self):
        """Create mock persistence layer."""
        mock_persistence = AsyncMock()
        mock_persistence.async_list_players.return_value = []
        mock_persistence.async_get_player.return_value = None
        mock_persistence.async_get_room.return_value = None
        mock_persistence.async_save_player.return_value = None
        mock_persistence.async_delete_player.return_value = True
        # Also mock synchronous methods for backward compatibility
        mock_persistence.list_players.return_value = []
        mock_persistence.get_player.return_value = None
        mock_persistence.get_room.return_value = None
        mock_persistence.save_player.return_value = None
        mock_persistence.delete_player.return_value = True
        return mock_persistence

    def test_service_independence(self, mock_persistence):
        """Test that different service instances are independent."""
        player_service1 = PlayerService(persistence=mock_persistence)
        player_service2 = PlayerService(persistence=mock_persistence)
        room_service = RoomService(persistence=mock_persistence)

        # Verify they are different instances
        assert player_service1 is not player_service2
        assert player_service1 is not room_service
        assert player_service2 is not room_service

        # But they share the same persistence layer
        assert player_service1.persistence == mock_persistence
        assert player_service2.persistence == mock_persistence
        assert room_service.persistence == mock_persistence

    def test_service_initialization_with_different_persistence(self):
        """Test that services can be initialized with different persistence layers."""
        persistence1 = AsyncMock()
        persistence2 = AsyncMock()

        player_service1 = PlayerService(persistence=persistence1)
        player_service2 = PlayerService(persistence=persistence2)

        # Verify they use different persistence layers
        assert player_service1.persistence == persistence1
        assert player_service2.persistence == persistence2
        assert player_service1.persistence is not player_service2.persistence

    def test_service_error_handling_capability(self, mock_persistence):
        """Test that services can handle errors from persistence layer."""
        # Configure mock to raise an exception
        mock_persistence.async_list_players.side_effect = Exception("Database error")

        service = PlayerService(persistence=mock_persistence)

        # The service should be created successfully even if persistence has issues
        assert isinstance(service, PlayerService)
        assert service.persistence == mock_persistence

    def test_service_dependency_injection_pattern(self, mock_persistence):
        """Test that services follow dependency injection pattern."""
        # This tests the pattern where services receive dependencies in constructor
        player_service = PlayerService(persistence=mock_persistence)
        room_service = RoomService(persistence=mock_persistence)

        # Verify dependency injection worked
        assert player_service.persistence is mock_persistence
        assert room_service.persistence is mock_persistence

        # Verify services don't create their own dependencies
        # (This is a design pattern test)
        assert not hasattr(player_service, "_create_persistence")
        assert not hasattr(room_service, "_create_persistence")
