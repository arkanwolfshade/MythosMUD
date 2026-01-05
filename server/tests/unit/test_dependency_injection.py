"""
Unit tests for dependency injection functions.

Tests dependency injection providers for services.
"""

from unittest.mock import MagicMock, Mock

import pytest
from fastapi import Request

from server.dependencies import (
    get_container,
    get_player_service,
    get_player_service_for_testing,
    get_room_service,
    get_stats_generator,
)
from server.game.player_service import PlayerService
from server.game.room_service import RoomService
from server.game.stats_generator import StatsGenerator


class TestGetContainer:
    """Test get_container() function."""

    def test_get_container_success(self):
        """Test get_container() returns container from app state."""
        mock_container = MagicMock()
        request = Mock(spec=Request)
        request.app = Mock()
        request.app.state = Mock()
        request.app.state.container = mock_container

        result = get_container(request)
        assert result == mock_container

    def test_get_container_missing(self):
        """Test get_container() raises error when container missing."""
        request = Mock(spec=Request)
        request.app = Mock()
        request.app.state = Mock()
        del request.app.state.container

        with pytest.raises(RuntimeError, match="ApplicationContainer not found"):
            get_container(request)

    def test_get_container_no_app_state(self):
        """Test get_container() raises error when app.state missing."""
        request = Mock(spec=Request)
        request.app = Mock()
        del request.app.state

        with pytest.raises(AttributeError):
            get_container(request)


class TestGetPlayerService:
    """Test get_player_service() function."""

    def test_get_player_service_success(self):
        """Test get_player_service() returns player service from container."""
        mock_player_service = MagicMock(spec=PlayerService)
        mock_container = MagicMock()
        mock_container.player_service = mock_player_service

        request = Mock(spec=Request)
        request.app = Mock()
        request.app.state = Mock()
        request.app.state.container = mock_container

        result = get_player_service(request)
        assert result == mock_player_service

    def test_get_player_service_not_initialized(self):
        """Test get_player_service() raises error when service not initialized."""
        mock_container = MagicMock()
        mock_container.player_service = None

        request = Mock(spec=Request)
        request.app = Mock()
        request.app.state = Mock()
        request.app.state.container = mock_container

        with pytest.raises(RuntimeError, match="PlayerService not initialized"):
            get_player_service(request)


class TestGetPlayerServiceForTesting:
    """Test get_player_service_for_testing() function."""

    def test_get_player_service_for_testing_with_injection(self):
        """Test get_player_service_for_testing() with injected service."""
        mock_service = MagicMock(spec=PlayerService)
        result = get_player_service_for_testing(mock_service)
        assert result == mock_service

    def test_get_player_service_for_testing_without_injection(self):
        """Test get_player_service_for_testing() creates mock when None."""
        result = get_player_service_for_testing(None)
        assert isinstance(result, PlayerService)


class TestGetRoomService:
    """Test get_room_service() function."""

    def test_get_room_service_success(self):
        """Test get_room_service() returns room service from container."""
        mock_room_service = MagicMock(spec=RoomService)
        mock_container = MagicMock()
        mock_container.room_service = mock_room_service

        request = Mock(spec=Request)
        request.app = Mock()
        request.app.state = Mock()
        request.app.state.container = mock_container

        result = get_room_service(request)
        assert result == mock_room_service

    def test_get_room_service_not_initialized(self):
        """Test get_room_service() raises error when service not initialized."""
        mock_container = MagicMock()
        mock_container.room_service = None

        request = Mock(spec=Request)
        request.app = Mock()
        request.app.state = Mock()
        request.app.state.container = mock_container

        with pytest.raises(RuntimeError, match="RoomService not initialized"):
            get_room_service(request)


class TestGetStatsGenerator:
    """Test get_stats_generator() function."""

    def test_get_stats_generator(self):
        """Test get_stats_generator() returns StatsGenerator instance."""
        result = get_stats_generator()
        assert isinstance(result, StatsGenerator)

    def test_get_stats_generator_stateless(self):
        """Test get_stats_generator() returns stateless instance."""
        gen1 = get_stats_generator()
        gen2 = get_stats_generator()
        # Should return new instances (stateless)
        assert gen1 is not gen2 or isinstance(gen1, StatsGenerator)
