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


def _bind_get_stats(mock_player: MagicMock, return_value: object) -> MagicMock:
    get_stats: MagicMock = MagicMock(return_value=return_value)
    mock_player.get_stats = get_stats
    return get_stats


def _app_with_container(container: MagicMock) -> MagicMock:
    app_state: MagicMock = MagicMock()
    app_state.container = container
    app: MagicMock = MagicMock()
    app.state = app_state
    return app


def _connection_manager_with_app(app: MagicMock | None) -> MagicMock:
    connection_manager: MagicMock = MagicMock()
    connection_manager.app = app
    return connection_manager


def _persistence_with_room(room: MagicMock | None) -> MagicMock:
    mock_persistence: MagicMock = MagicMock()
    get_room_by_id: MagicMock = MagicMock(return_value=room)
    mock_persistence.get_room_by_id = get_room_by_id
    return mock_persistence


def _room_with_has_player(has_player_value: bool, room_id: str) -> MagicMock:
    mock_room: MagicMock = MagicMock()
    has_player: MagicMock = MagicMock(return_value=has_player_value)
    mock_room.has_player = has_player
    mock_room.id = room_id
    return mock_room


def test_get_player_service_from_connection_manager_success():
    """Test get_player_service_from_connection_manager() returns player service."""
    mock_player_service: MagicMock = MagicMock()
    container: MagicMock = MagicMock()
    container.player_service = mock_player_service
    mock_connection_manager = _connection_manager_with_app(_app_with_container(container))

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
    _ = _bind_get_stats(mock_player, {"hp": 100, "mp": 50})

    result = get_player_stats_data(mock_player)
    assert result == {"hp": 100, "mp": 50}


def test_get_player_stats_data_string_stats():
    """Test get_player_stats_data() parses JSON string stats."""
    mock_player = MagicMock()
    _ = _bind_get_stats(mock_player, '{"hp": 100, "mp": 50}')

    result = get_player_stats_data(mock_player)
    assert result == {"hp": 100, "mp": 50}


def test_get_player_stats_data_adds_health():
    """Test get_player_stats_data() adds health from current_dp."""
    mock_player = MagicMock()
    _ = _bind_get_stats(mock_player, {"current_dp": 80})

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
    _ = _bind_get_stats(mock_player, {"hp": 100, "mp": 50})

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
    _ = _bind_get_stats(mock_player, {})

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
    model_dump: MagicMock = MagicMock(return_value={"name": "TestPlayer", "experience_points": 1000})
    mock_complete_data.model_dump = model_dump
    mock_player_service.convert_player_to_schema = AsyncMock(return_value=mock_complete_data)

    container: MagicMock = MagicMock()
    container.player_service = mock_player_service
    mock_connection_manager = _connection_manager_with_app(_app_with_container(container))

    result = await prepare_player_data(mock_player, player_id, mock_connection_manager)
    assert result["name"] == "TestPlayer"
    assert result["xp"] == 1000


@pytest.mark.asyncio
async def test_prepare_player_data_no_service():
    """Test prepare_player_data() uses basic data when service unavailable."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    _ = _bind_get_stats(mock_player, {"hp": 100})
    player_id = uuid.uuid4()

    mock_connection_manager = _connection_manager_with_app(None)

    result = await prepare_player_data(mock_player, player_id, mock_connection_manager)
    assert result["name"] == "TestPlayer"
    assert "stats" in result


@pytest.mark.asyncio
async def test_prepare_player_data_service_error():
    """Test prepare_player_data() falls back to basic data on error."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    _ = _bind_get_stats(mock_player, {"hp": 100})
    player_id = uuid.uuid4()

    mock_player_service = AsyncMock()
    mock_player_service.convert_player_to_schema = AsyncMock(side_effect=RuntimeError("Service error"))

    container: MagicMock = MagicMock()
    container.player_service = mock_player_service
    mock_connection_manager = _connection_manager_with_app(_app_with_container(container))

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
    mock_room = _room_with_has_player(True, room_id)

    mock_connection_manager = AsyncMock()
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

    with patch("server.container.async_persistence_access.get_container_async_persistence") as mock_get_persistence:
        mock_persistence = _persistence_with_room(mock_room)
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

    with patch("server.container.async_persistence_access.get_container_async_persistence") as mock_get_persistence:
        mock_persistence = _persistence_with_room(None)
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
    mock_room = _room_with_has_player(False, room_id)
    player_entered: MagicMock = MagicMock()
    mock_room.player_entered = player_entered

    mock_connection_manager = AsyncMock()
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

    with patch("server.container.async_persistence_access.get_container_async_persistence") as mock_get_persistence:
        mock_persistence = _persistence_with_room(mock_room)
        mock_get_persistence.return_value = mock_persistence

        player, room, canonical_room_id = await get_player_and_room(player_id, player_id_str, mock_connection_manager)
        assert player == mock_player
        assert room == mock_room
        assert canonical_room_id == room_id
        player_entered.assert_called_once_with(player_id_str)
