"""
Unit tests for WebSocket helpers (player-related).

Tests get_player_service_from_connection_manager, get_player_stats_data,
build_basic_player_data, prepare_player_data, and get_player_and_room.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.websocket_helpers import (
    build_basic_player_data,
    get_player_and_room,
    get_player_service_from_connection_manager,
    get_player_stats_data,
    prepare_player_data,
)


def test_get_player_service_from_connection_manager_success():
    """Test get_player_service_from_connection_manager() returns player service."""
    mock_player_service = MagicMock()
    mock_app_state = MagicMock()
    mock_app_state.container = MagicMock()
    mock_app_state.container.player_service = mock_player_service
    mock_app = MagicMock()
    mock_app.state = mock_app_state
    mock_connection_manager = MagicMock()
    mock_connection_manager.app = mock_app

    result = get_player_service_from_connection_manager(mock_connection_manager)
    assert result == mock_player_service


def test_get_player_service_from_connection_manager_no_app():
    """Test get_player_service_from_connection_manager() returns None when no app."""
    mock_connection_manager = MagicMock()
    mock_connection_manager.app = None

    result = get_player_service_from_connection_manager(mock_connection_manager)
    assert result is None


def test_get_player_service_from_connection_manager_no_state():
    """Test get_player_service_from_connection_manager() returns None when no state."""
    mock_app = MagicMock()
    mock_app.state = None
    mock_connection_manager = MagicMock()
    mock_connection_manager.app = mock_app

    result = get_player_service_from_connection_manager(mock_connection_manager)
    assert result is None


def test_get_player_stats_data_with_get_stats():
    """Test get_player_stats_data() uses get_stats() method."""
    mock_player = MagicMock()
    mock_player.get_stats.return_value = {"hp": 100, "mp": 50}

    result = get_player_stats_data(mock_player)
    assert result == {"hp": 100, "mp": 50}


def test_get_player_stats_data_string_stats():
    """Test get_player_stats_data() parses JSON string stats."""
    mock_player = MagicMock()
    mock_player.get_stats.return_value = '{"hp": 100, "mp": 50}'

    result = get_player_stats_data(mock_player)
    assert result == {"hp": 100, "mp": 50}


def test_get_player_stats_data_adds_health():
    """Test get_player_stats_data() adds health from current_dp."""
    mock_player = MagicMock()
    mock_player.get_stats.return_value = {"current_dp": 80}

    result = get_player_stats_data(mock_player)
    assert result["health"] == 80
    assert result["current_dp"] == 80


def test_get_player_stats_data_no_get_stats():
    """Test get_player_stats_data() returns empty dict when no get_stats."""
    mock_player = MagicMock()
    del mock_player.get_stats

    result = get_player_stats_data(mock_player)
    assert result == {}


def test_build_basic_player_data():
    """Test build_basic_player_data() builds player data dictionary."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_player.experience_points = 1000
    mock_player.get_stats.return_value = {"hp": 100, "mp": 50}

    result = build_basic_player_data(mock_player)
    assert result["name"] == "TestPlayer"
    assert result["level"] == 5
    assert result["xp"] == 1000
    assert result["stats"] == {"hp": 100, "mp": 50}


def test_build_basic_player_data_defaults():
    """Test build_basic_player_data() uses defaults when attributes missing."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    del mock_player.level
    del mock_player.experience_points
    mock_player.get_stats.return_value = {}

    result = build_basic_player_data(mock_player)
    assert result["name"] == "TestPlayer"
    assert result["level"] == 1
    assert result["xp"] == 0


@pytest.mark.asyncio
async def test_prepare_player_data_with_service():
    """Test prepare_player_data() uses player service when available."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    player_id = uuid.uuid4()

    mock_player_service = AsyncMock()
    mock_complete_data = MagicMock()
    mock_complete_data.model_dump.return_value = {"name": "TestPlayer", "experience_points": 1000}
    mock_player_service.convert_player_to_schema = AsyncMock(return_value=mock_complete_data)

    mock_connection_manager = MagicMock()
    mock_connection_manager.app = MagicMock()
    mock_connection_manager.app.state = MagicMock()
    mock_connection_manager.app.state.container = MagicMock()
    mock_connection_manager.app.state.container.player_service = mock_player_service

    result = await prepare_player_data(mock_player, player_id, mock_connection_manager)
    assert result["name"] == "TestPlayer"
    assert result["xp"] == 1000


@pytest.mark.asyncio
async def test_prepare_player_data_no_service():
    """Test prepare_player_data() uses basic data when service unavailable."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.get_stats.return_value = {"hp": 100}
    player_id = uuid.uuid4()

    mock_connection_manager = MagicMock()
    mock_connection_manager.app = None

    result = await prepare_player_data(mock_player, player_id, mock_connection_manager)
    assert result["name"] == "TestPlayer"
    assert "stats" in result


@pytest.mark.asyncio
async def test_prepare_player_data_service_error():
    """Test prepare_player_data() falls back to basic data on error."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.get_stats.return_value = {"hp": 100}
    player_id = uuid.uuid4()

    mock_player_service = AsyncMock()
    mock_player_service.convert_player_to_schema = AsyncMock(side_effect=RuntimeError("Service error"))

    mock_connection_manager = MagicMock()
    mock_connection_manager.app = MagicMock()
    mock_connection_manager.app.state = MagicMock()
    mock_connection_manager.app.state.container = MagicMock()
    mock_connection_manager.app.state.container.player_service = mock_player_service

    result = await prepare_player_data(mock_player, player_id, mock_connection_manager)
    assert result["name"] == "TestPlayer"
    assert "stats" in result


@pytest.mark.asyncio
async def test_get_player_and_room_success():
    """Test get_player_and_room() returns player, room, and canonical_room_id."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    room_id = "room_123"

    mock_player = MagicMock()
    mock_player.current_room_id = room_id
    mock_room = MagicMock()
    mock_room.has_player.return_value = True
    mock_room.id = room_id

    mock_connection_manager = AsyncMock()
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id.return_value = mock_room
        mock_get_persistence.return_value = mock_persistence

        player, room, canonical_room_id = await get_player_and_room(player_id, player_id_str, mock_connection_manager)
        assert player == mock_player
        assert room == mock_room
        assert canonical_room_id == room_id


@pytest.mark.asyncio
async def test_get_player_and_room_player_not_found():
    """Test get_player_and_room() returns None when player not found."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)

    mock_connection_manager = AsyncMock()
    mock_connection_manager.get_player = AsyncMock(return_value=None)

    player, room, canonical_room_id = await get_player_and_room(player_id, player_id_str, mock_connection_manager)
    assert player is None
    assert room is None
    assert canonical_room_id is None


@pytest.mark.asyncio
async def test_get_player_and_room_room_not_found():
    """Test get_player_and_room() returns None when room not found."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    room_id = "room_123"

    mock_player = MagicMock()
    mock_player.current_room_id = room_id

    mock_connection_manager = AsyncMock()
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id.return_value = None
        mock_get_persistence.return_value = mock_persistence

        player, room, canonical_room_id = await get_player_and_room(player_id, player_id_str, mock_connection_manager)
        assert player is None
        assert room is None
        assert canonical_room_id is None


@pytest.mark.asyncio
async def test_get_player_and_room_adds_player_to_room():
    """Test get_player_and_room() adds player to room if not present."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    room_id = "room_123"

    mock_player = MagicMock()
    mock_player.current_room_id = room_id
    mock_room = MagicMock()
    mock_room.has_player.return_value = False
    mock_room.id = room_id

    mock_connection_manager = AsyncMock()
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id.return_value = mock_room
        mock_get_persistence.return_value = mock_persistence

        player, room, canonical_room_id = await get_player_and_room(player_id, player_id_str, mock_connection_manager)
        assert player == mock_player
        assert room == mock_room
        assert canonical_room_id == room_id
        mock_room.player_entered.assert_called_once_with(player_id_str)
