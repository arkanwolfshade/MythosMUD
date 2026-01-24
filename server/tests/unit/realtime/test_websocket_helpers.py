"""
Unit tests for WebSocket helpers.

Tests the websocket_helpers module functions. Player-related tests are in
test_websocket_helpers_player.py.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.websocket_helpers import (
    check_shutdown_and_reject,
    convert_schema_to_dict,
    convert_uuids_to_strings,
    get_npc_name_from_instance,
    get_occupant_names,
    load_player_mute_data,
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
    del mock_npc.name

    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {npc_id: mock_npc}
        mock_get_service.return_value = mock_service

        result = get_npc_name_from_instance(npc_id)
        assert result is None


def test_get_npc_name_from_instance_import_error():
    """Test get_npc_name_from_instance() handles ImportError."""
    npc_id = "npc_123"

    with patch(
        "server.services.npc_instance_service.get_npc_instance_service",
        side_effect=ImportError("No module"),
    ):
        result = get_npc_name_from_instance(npc_id)
        assert result is None


def test_get_npc_name_from_instance_runtime_error():
    """Test get_npc_name_from_instance() handles RuntimeError."""
    npc_id = "npc_123"

    with patch(
        "server.services.npc_instance_service.get_npc_instance_service",
        side_effect=RuntimeError("Not initialized"),
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
            "server.commands.admin_shutdown_command.get_shutdown_blocking_message",
            return_value="Server shutting down",
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
            "server.commands.admin_shutdown_command.get_shutdown_blocking_message",
            return_value="Server shutting down",
        ),
    ):
        result = await check_shutdown_and_reject(mock_websocket, player_id)
        assert result is False


@pytest.mark.asyncio
async def test_load_player_mute_data_success():
    """Test load_player_mute_data() successfully loads mute data."""
    player_id_str = "player_123"

    with patch("server.services.user_manager.user_manager") as mock_user_manager:
        mock_user_manager.load_player_mutes_async = AsyncMock(return_value=True)
        await load_player_mute_data(player_id_str)
        mock_user_manager.load_player_mutes_async.assert_called_once_with(player_id_str)


@pytest.mark.asyncio
async def test_load_player_mute_data_import_error():
    """Test load_player_mute_data() handles ImportError."""
    import sys

    player_id_str = "player_123"
    original_module = sys.modules.pop("server.services.user_manager", None)
    try:
        await load_player_mute_data(player_id_str)
    finally:
        if original_module is not None:
            sys.modules["server.services.user_manager"] = original_module


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
    assert validate_occupant_name(123) is False  # type: ignore[arg-type]  # Reason: Intentionally testing non-string input


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
        {"player_name": uuid_str},
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
    result = await get_occupant_names(None, "room_123")  # type: ignore[arg-type]  # Reason: Intentionally testing None input
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
