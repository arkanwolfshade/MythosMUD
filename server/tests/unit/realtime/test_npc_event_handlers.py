"""
Unit tests for NPC event handlers.

Tests the NPCEventHandler class.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events.event_types import NPCEnteredRoom, NPCLeftRoom
from server.realtime.npc_event_handlers import NPCEventHandler


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    return MagicMock()


@pytest.fixture
def mock_message_builder():
    """Create a mock message builder."""
    return MagicMock()


@pytest.fixture
def mock_send_occupants_update():
    """Create a mock send_occupants_update function."""
    return AsyncMock()


@pytest.fixture
def npc_event_handler(mock_connection_manager, mock_message_builder, mock_send_occupants_update):
    """Create an NPCEventHandler instance."""
    return NPCEventHandler(
        connection_manager=mock_connection_manager,
        task_registry=None,
        message_builder=mock_message_builder,
        send_occupants_update=mock_send_occupants_update,
    )


def test_npc_event_handler_init(npc_event_handler, mock_connection_manager):
    """Test NPCEventHandler initialization."""
    assert npc_event_handler.connection_manager == mock_connection_manager
    assert npc_event_handler.task_registry is None


def test_get_npc_instance_not_found(npc_event_handler):
    """Test _get_npc_instance() when NPC is not found."""
    result = npc_event_handler._get_npc_instance("npc_001")
    assert result is None


def test_get_behavior_config_from_instance_private_attr(npc_event_handler):
    """Test _get_behavior_config_from_instance() with private attribute."""
    mock_npc = MagicMock()
    mock_npc._behavior_config = {"type": "passive"}
    result = npc_event_handler._get_behavior_config_from_instance(mock_npc)
    assert result == {"type": "passive"}


def test_get_behavior_config_from_instance_method(npc_event_handler):
    """Test _get_behavior_config_from_instance() with method."""
    mock_npc = MagicMock(spec=[])
    # Configure mock to not have _behavior_config, but have get_behavior_config method
    type(mock_npc).get_behavior_config = MagicMock(return_value={"type": "aggressive"})
    result = npc_event_handler._get_behavior_config_from_instance(mock_npc)
    assert result == {"type": "aggressive"}


def test_get_behavior_config_from_instance_public_attr(npc_event_handler):
    """Test _get_behavior_config_from_instance() with public attribute."""
    mock_npc = MagicMock(spec=[])
    # Configure mock to not have _behavior_config or get_behavior_config, but have behavior_config
    type(mock_npc).behavior_config = {"type": "shopkeeper"}
    result = npc_event_handler._get_behavior_config_from_instance(mock_npc)
    assert result == {"type": "shopkeeper"}


def test_get_behavior_config_from_instance_none(npc_event_handler):
    """Test _get_behavior_config_from_instance() when config is not found."""
    mock_npc = MagicMock(spec=[])
    # Configure mock to not have any behavior config attributes
    result = npc_event_handler._get_behavior_config_from_instance(mock_npc)
    assert result is None


def test_parse_behavior_config_dict(npc_event_handler):
    """Test _parse_behavior_config() with dict."""
    config = {"type": "passive"}
    result = npc_event_handler._parse_behavior_config(config)
    assert result == config


def test_parse_behavior_config_string(npc_event_handler):
    """Test _parse_behavior_config() with JSON string."""
    import json

    config = {"type": "passive"}
    config_str = json.dumps(config)
    result = npc_event_handler._parse_behavior_config(config_str)
    assert result == config


def test_parse_behavior_config_invalid_json(npc_event_handler):
    """Test _parse_behavior_config() with invalid JSON."""
    result = npc_event_handler._parse_behavior_config("not valid json")
    assert result is None


@pytest.mark.asyncio
async def test_handle_npc_entered_room(npc_event_handler):
    """Test handle_npc_entered_room() processes event."""
    event = NPCEnteredRoom(npc_id="npc_001", room_id="room_001")
    await npc_event_handler.handle_npc_entered(event)
    # Should not raise


@pytest.mark.asyncio
async def test_handle_npc_left_room(npc_event_handler):
    """Test handle_npc_left_room() processes event."""
    event = NPCLeftRoom(npc_id="npc_001", room_id="room_001")
    await npc_event_handler.handle_npc_left(event)
    # Should not raise


def test_get_npc_instance_found(npc_event_handler):
    """Test _get_npc_instance() when NPC is found."""
    # get_npc_instance_service is imported inside the method
    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_lifecycle_manager = MagicMock()
        mock_npc_instance = MagicMock()
        mock_lifecycle_manager.active_npcs = {"npc_001": mock_npc_instance}
        mock_service.lifecycle_manager = mock_lifecycle_manager
        mock_get_service.return_value = mock_service
        result = npc_event_handler._get_npc_instance("npc_001")
        assert result == mock_npc_instance


def test_get_npc_instance_no_service(npc_event_handler):
    """Test _get_npc_instance() when service is not available."""
    # get_npc_instance_service is imported inside the method
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        result = npc_event_handler._get_npc_instance("npc_001")
        assert result is None


def test_get_npc_instance_exception(npc_event_handler):
    """Test _get_npc_instance() handles exceptions gracefully."""
    # get_npc_instance_service is imported inside the method
    with patch("server.services.npc_instance_service.get_npc_instance_service", side_effect=Exception("test error")):
        result = npc_event_handler._get_npc_instance("npc_001")
        assert result is None


def test_parse_behavior_config_none(npc_event_handler):
    """Test _parse_behavior_config() with None."""
    result = npc_event_handler._parse_behavior_config(None)
    assert result is None


def test_parse_behavior_config_empty_string(npc_event_handler):
    """Test _parse_behavior_config() with empty string."""
    result = npc_event_handler._parse_behavior_config("")
    assert result is None


@pytest.mark.asyncio
async def test_handle_npc_entered_room_with_npc_instance(npc_event_handler):
    """Test handle_npc_entered_room() with valid NPC instance."""
    with patch.object(npc_event_handler, "_get_npc_instance", return_value=MagicMock()):
        with patch.object(npc_event_handler, "_get_behavior_config_from_instance", return_value={"type": "passive"}):
            event = NPCEnteredRoom(npc_id="npc_001", room_id="room_001")
            await npc_event_handler.handle_npc_entered(event)
            # Should not raise


@pytest.mark.asyncio
async def test_handle_npc_left_room_with_npc_instance(npc_event_handler):
    """Test handle_npc_left_room() with valid NPC instance."""
    with patch.object(npc_event_handler, "_get_npc_instance", return_value=MagicMock()):
        event = NPCLeftRoom(npc_id="npc_001", room_id="room_001")
        await npc_event_handler.handle_npc_left(event)
        # Should not raise


def test_parse_behavior_config_not_dict_or_string(npc_event_handler):
    """Test _parse_behavior_config() returns None for non-dict, non-string."""
    result = npc_event_handler._parse_behavior_config(123)
    assert result is None


def test_get_npc_spawn_message_no_config(npc_event_handler):
    """Test _get_npc_spawn_message() returns default when no config."""
    with patch.object(npc_event_handler, "_get_npc_instance") as mock_get_instance:
        mock_instance = MagicMock()
        mock_instance.name = "TestNPC"
        mock_get_instance.return_value = mock_instance
        with patch.object(npc_event_handler, "_get_behavior_config_from_instance", return_value=None):
            result = npc_event_handler._get_npc_spawn_message("npc_001")
            assert result == "TestNPC appears."


def test_get_npc_name_no_service(npc_event_handler):
    """Test _get_npc_name() returns None when service not available."""
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        result = npc_event_handler._get_npc_name("npc_001")
        assert result is None


@pytest.mark.asyncio
async def test_determine_direction_from_rooms_no_persistence(npc_event_handler, mock_connection_manager):
    """Test _determine_direction_from_rooms() returns None when persistence not available."""
    npc_event_handler.connection_manager.async_persistence = None
    result = await npc_event_handler._determine_direction_from_rooms("room_001", "room_002")
    assert result is None


@pytest.mark.asyncio
async def test_determine_direction_from_rooms_room_not_found(npc_event_handler, mock_connection_manager):
    """Test _determine_direction_from_rooms() returns None when room not found."""
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=None)
    result = await npc_event_handler._determine_direction_from_rooms("room_001", "room_002")
    assert result is None


@pytest.mark.asyncio
async def test_determine_direction_from_rooms_no_match(npc_event_handler, mock_connection_manager):
    """Test _determine_direction_from_rooms() returns None when no matching exit."""
    mock_room = MagicMock()
    mock_room.exits = {"north": "room_003"}
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = await npc_event_handler._determine_direction_from_rooms("room_001", "room_002")
    assert result is None


def test_get_npc_departure_message_no_instance(npc_event_handler):
    """Test _get_npc_departure_message() returns None when NPC not found."""
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        result = npc_event_handler._get_npc_departure_message("nonexistent_npc")
        assert result is None


def test_get_npc_departure_message_no_config(npc_event_handler):
    """Test _get_npc_departure_message() returns default when no config."""
    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_lifecycle_manager = MagicMock()
        mock_instance = MagicMock()
        mock_instance.name = "TestNPC"
        mock_instance._behavior_config = None
        del mock_instance.behavior_config
        mock_lifecycle_manager.active_npcs = {"npc_001": mock_instance}
        mock_service.lifecycle_manager = mock_lifecycle_manager
        mock_get_service.return_value = mock_service
        result = npc_event_handler._get_npc_departure_message("npc_001")
        assert result == "TestNPC leaves."


@pytest.mark.asyncio
async def test_send_room_message_no_connection_manager(npc_event_handler):
    """Test _send_room_message() handles missing connection_manager."""
    npc_event_handler.connection_manager = None
    await npc_event_handler._send_room_message("room_001", "Test message")
    # Should complete without error


@pytest.mark.asyncio
async def test_send_room_message_no_room_manager(npc_event_handler, mock_connection_manager):
    """Test _send_room_message() handles missing room_manager."""
    del mock_connection_manager.room_manager
    await npc_event_handler._send_room_message("room_001", "Test message")
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_npc_entered_no_connection_manager(npc_event_handler):
    """Test handle_npc_entered() handles missing connection_manager."""
    npc_event_handler.connection_manager = None
    event = NPCEnteredRoom(npc_id="npc_001", room_id="room_001", from_room_id=None)
    await npc_event_handler.handle_npc_entered(event)
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_npc_entered_no_persistence(npc_event_handler, mock_connection_manager):
    """Test handle_npc_entered() handles missing persistence."""
    mock_connection_manager.async_persistence = None
    event = NPCEnteredRoom(npc_id="npc_001", room_id="room_001", from_room_id=None)
    await npc_event_handler.handle_npc_entered(event)
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_npc_entered_room_not_found(npc_event_handler, mock_connection_manager):
    """Test handle_npc_entered() handles room not found."""
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=None)
    event = NPCEnteredRoom(npc_id="npc_001", room_id="room_001", from_room_id=None)
    await npc_event_handler.handle_npc_entered(event)
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_npc_left_no_connection_manager(npc_event_handler):
    """Test handle_npc_left() handles missing connection_manager."""
    npc_event_handler.connection_manager = None
    event = NPCLeftRoom(npc_id="npc_001", room_id="room_001", to_room_id=None)
    await npc_event_handler.handle_npc_left(event)
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_npc_left_no_persistence(npc_event_handler, mock_connection_manager):
    """Test handle_npc_left() handles missing persistence."""
    mock_connection_manager.async_persistence = None
    event = NPCLeftRoom(npc_id="npc_001", room_id="room_001", to_room_id=None)
    await npc_event_handler.handle_npc_left(event)
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_npc_left_room_not_found(npc_event_handler, mock_connection_manager):
    """Test handle_npc_left() handles room not found."""
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=None)
    event = NPCLeftRoom(npc_id="npc_001", room_id="room_001", to_room_id=None)
    await npc_event_handler.handle_npc_left(event)
    # Should complete without error
