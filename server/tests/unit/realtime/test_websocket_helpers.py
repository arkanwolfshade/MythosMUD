"""
Unit tests for WebSocket helpers.

Tests the websocket_helpers module functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.websocket_helpers import (
    build_basic_player_data,
    check_shutdown_and_reject,
    convert_schema_to_dict,
    convert_uuids_to_strings,
    get_npc_name_from_instance,
    get_occupant_names,
    get_player_and_room,
    get_player_service_from_connection_manager,
    get_player_stats_data,
    load_player_mute_data,
    prepare_player_data,
    validate_occupant_name,
)


def test_get_npc_name_from_instance_success():
    """Test get_npc_name_from_instance() returns NPC name when found."""
    npc_id = "npc_123"
    npc_name = "Test NPC"
    mock_npc = MagicMock()
    mock_npc.name = npc_name

    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {npc_id: mock_npc}
        mock_get_service.return_value = mock_service

        result = get_npc_name_from_instance(npc_id)
        assert result == npc_name


def test_get_npc_name_from_instance_not_found():
    """Test get_npc_name_from_instance() returns None when NPC not found."""
    npc_id = "npc_123"

    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {}
        mock_get_service.return_value = mock_service

        result = get_npc_name_from_instance(npc_id)
        assert result is None


def test_get_npc_name_from_instance_no_name_attribute():
    """Test get_npc_name_from_instance() returns None when NPC has no name."""
    npc_id = "npc_123"
    mock_npc = MagicMock()
    del mock_npc.name  # Remove name attribute

    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {npc_id: mock_npc}
        mock_get_service.return_value = mock_service

        result = get_npc_name_from_instance(npc_id)
        assert result is None


def test_get_npc_name_from_instance_import_error():
    """Test get_npc_name_from_instance() handles ImportError."""
    npc_id = "npc_123"

    with patch("server.services.npc_instance_service.get_npc_instance_service", side_effect=ImportError("No module")):
        result = get_npc_name_from_instance(npc_id)
        assert result is None


def test_get_npc_name_from_instance_runtime_error():
    """Test get_npc_name_from_instance() handles RuntimeError."""
    npc_id = "npc_123"

    with patch(
        "server.services.npc_instance_service.get_npc_instance_service", side_effect=RuntimeError("Not initialized")
    ):
        result = get_npc_name_from_instance(npc_id)
        assert result is None


@pytest.mark.asyncio
async def test_check_shutdown_and_reject_not_shutting_down():
    """Test check_shutdown_and_reject() returns False when not shutting down."""
    mock_websocket = AsyncMock()
    player_id = uuid.uuid4()

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        result = await check_shutdown_and_reject(mock_websocket, player_id)
        assert result is False


@pytest.mark.asyncio
async def test_check_shutdown_and_reject_shutting_down():
    """Test check_shutdown_and_reject() returns True and closes connection when shutting down."""
    mock_websocket = AsyncMock()
    mock_websocket.app = MagicMock()
    player_id = uuid.uuid4()

    with (
        patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True),
        patch(
            "server.commands.admin_shutdown_command.get_shutdown_blocking_message", return_value="Server shutting down"
        ),
    ):
        result = await check_shutdown_and_reject(mock_websocket, player_id)
        assert result is True
        mock_websocket.send_json.assert_called_once()
        mock_websocket.close.assert_called_once()


@pytest.mark.asyncio
async def test_check_shutdown_and_reject_websocket_disconnect():
    """Test check_shutdown_and_reject() handles WebSocketDisconnect."""
    from fastapi import WebSocketDisconnect

    mock_websocket = AsyncMock()
    mock_websocket.app = MagicMock()
    mock_websocket.close.side_effect = WebSocketDisconnect()
    player_id = uuid.uuid4()

    with (
        patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True),
        patch(
            "server.commands.admin_shutdown_command.get_shutdown_blocking_message", return_value="Server shutting down"
        ),
    ):
        # The function catches WebSocketDisconnect and returns False (not True)
        # because the exception is caught in the except block and the function returns False
        result = await check_shutdown_and_reject(mock_websocket, player_id)
        assert result is False


def test_load_player_mute_data_success():
    """Test load_player_mute_data() successfully loads mute data."""
    player_id_str = "player_123"

    with patch("server.services.user_manager.user_manager") as mock_user_manager:
        load_player_mute_data(player_id_str)
        mock_user_manager.load_player_mutes.assert_called_once_with(player_id_str)


def test_load_player_mute_data_import_error():
    """Test load_player_mute_data() handles ImportError."""
    player_id_str = "player_123"

    with patch("server.services.user_manager.user_manager", side_effect=ImportError("No module")):
        # Should not raise
        load_player_mute_data(player_id_str)


def test_validate_occupant_name_valid():
    """Test validate_occupant_name() returns True for valid name."""
    assert validate_occupant_name("PlayerName") is True
    assert validate_occupant_name("Test NPC") is True
    assert validate_occupant_name("player-123") is True


def test_validate_occupant_name_uuid():
    """Test validate_occupant_name() returns False for UUID string."""
    uuid_str = str(uuid.uuid4())
    assert validate_occupant_name(uuid_str) is False


def test_validate_occupant_name_empty():
    """Test validate_occupant_name() returns False for empty string."""
    assert validate_occupant_name("") is False


def test_validate_occupant_name_none():
    """Test validate_occupant_name() returns False for None."""
    assert validate_occupant_name(None) is False


def test_validate_occupant_name_not_string():
    """Test validate_occupant_name() returns False for non-string."""
    assert validate_occupant_name(123) is False


@pytest.mark.asyncio
async def test_get_occupant_names_success():
    """Test get_occupant_names() extracts valid occupant names."""
    room_occupants = [
        {"player_name": "Player1"},
        {"name": "Player2"},
        {"player_name": "NPC1"},
    ]
    room_id = "room_123"

    result = await get_occupant_names(room_occupants, room_id)
    assert "Player1" in result
    assert "Player2" in result
    assert "NPC1" in result


@pytest.mark.asyncio
async def test_get_occupant_names_filters_uuid():
    """Test get_occupant_names() filters out UUID strings."""
    uuid_str = str(uuid.uuid4())
    room_occupants = [
        {"player_name": "Player1"},
        {"player_name": uuid_str},  # Should be filtered
    ]
    room_id = "room_123"

    result = await get_occupant_names(room_occupants, room_id)
    assert "Player1" in result
    assert uuid_str not in result


@pytest.mark.asyncio
async def test_get_occupant_names_empty():
    """Test get_occupant_names() returns empty list for empty occupants."""
    result = await get_occupant_names([], "room_123")
    assert result == []


@pytest.mark.asyncio
async def test_get_occupant_names_none():
    """Test get_occupant_names() handles None occupants."""
    result = await get_occupant_names(None, "room_123")
    assert result == []


def test_convert_uuids_to_strings_dict():
    """Test convert_uuids_to_strings() converts UUIDs in dictionary."""
    test_uuid = uuid.uuid4()
    obj = {"id": test_uuid, "name": "Test"}
    result = convert_uuids_to_strings(obj)
    assert result["id"] == str(test_uuid)
    assert result["name"] == "Test"


def test_convert_uuids_to_strings_list():
    """Test convert_uuids_to_strings() converts UUIDs in list."""
    test_uuid = uuid.uuid4()
    obj = [test_uuid, "string", 123]
    result = convert_uuids_to_strings(obj)
    assert result[0] == str(test_uuid)
    assert result[1] == "string"
    assert result[2] == 123


def test_convert_uuids_to_strings_nested():
    """Test convert_uuids_to_strings() converts UUIDs in nested structures."""
    test_uuid = uuid.uuid4()
    obj = {"data": {"id": test_uuid, "items": [test_uuid]}}
    result = convert_uuids_to_strings(obj)
    assert result["data"]["id"] == str(test_uuid)
    assert result["data"]["items"][0] == str(test_uuid)


def test_convert_uuids_to_strings_no_uuid():
    """Test convert_uuids_to_strings() returns unchanged for non-UUID objects."""
    obj = {"name": "Test", "value": 123}
    result = convert_uuids_to_strings(obj)
    assert result == obj


def test_get_player_service_from_connection_manager_success():
    """Test get_player_service_from_connection_manager() returns player service."""
    mock_player_service = MagicMock()
    mock_app_state = MagicMock()
    mock_app_state.player_service = mock_player_service
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


def test_convert_schema_to_dict_with_model_dump():
    """Test convert_schema_to_dict() uses model_dump() when available."""
    mock_schema = MagicMock()
    mock_schema.model_dump.return_value = {"key": "value"}

    result = convert_schema_to_dict(mock_schema)
    assert result == {"key": "value"}
    mock_schema.model_dump.assert_called_once_with(mode="json")


def test_convert_schema_to_dict_with_dict():
    """Test convert_schema_to_dict() uses dict() when model_dump() not available."""
    mock_schema = MagicMock()
    del mock_schema.model_dump
    mock_schema.dict.return_value = {"key": "value"}

    result = convert_schema_to_dict(mock_schema)
    assert result == {"key": "value"}
    mock_schema.dict.assert_called_once()


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

    mock_player_service = MagicMock()
    mock_complete_data = MagicMock()
    mock_complete_data.model_dump.return_value = {"name": "TestPlayer", "experience_points": 1000}
    mock_player_service.convert_player_to_schema = AsyncMock(return_value=mock_complete_data)

    mock_connection_manager = MagicMock()
    mock_connection_manager.app = MagicMock()
    mock_connection_manager.app.state = MagicMock()
    mock_connection_manager.app.state.player_service = mock_player_service

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

    mock_player_service = MagicMock()
    mock_player_service.convert_player_to_schema = AsyncMock(side_effect=RuntimeError("Service error"))

    mock_connection_manager = MagicMock()
    mock_connection_manager.app = MagicMock()
    mock_connection_manager.app.state = MagicMock()
    mock_connection_manager.app.state.player_service = mock_player_service

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
    mock_room.id = room_id  # Set room.id for canonical_room_id

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
        mock_room.player_entered.assert_called_once_with(player_id_str)
