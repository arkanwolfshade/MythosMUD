"""
Unit tests for NPC event handlers helper functions.

Tests the helper functions in npc_event_handlers.py.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.npc_event_handlers import NPCEventHandler


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.async_persistence = MagicMock()
    manager.room_manager = MagicMock()
    manager.send_personal_message = AsyncMock()
    return manager


@pytest.fixture
def mock_message_builder():
    """Create a mock message builder."""
    builder = MagicMock()
    builder.create_npc_movement_message = MagicMock(return_value="NPC moves north")
    return builder


@pytest.fixture
def npc_event_handler(mock_connection_manager, mock_message_builder):
    """Create an NPCEventHandler instance."""
    return NPCEventHandler(
        connection_manager=mock_connection_manager,
        task_registry=None,
        message_builder=mock_message_builder,
        send_occupants_update=AsyncMock(),
    )


def test_extract_spawn_message_from_config(npc_event_handler):
    """Test _extract_spawn_message_from_config() extracts spawn message."""
    config = {"spawn_message": "A mysterious figure appears."}
    result = npc_event_handler._extract_spawn_message_from_config(config)
    assert result == "A mysterious figure appears."


def test_extract_spawn_message_from_config_none(npc_event_handler):
    """Test _extract_spawn_message_from_config() returns None when not found."""
    config = {"type": "passive"}
    result = npc_event_handler._extract_spawn_message_from_config(config)
    assert result is None


def test_get_npc_spawn_message(npc_event_handler):
    """Test _get_npc_spawn_message() returns spawn message."""
    with patch.object(npc_event_handler, "_get_npc_instance") as mock_get_instance:
        mock_npc = MagicMock()
        mock_npc.name = "TestNPC"
        mock_get_instance.return_value = mock_npc
        with patch.object(npc_event_handler, "_get_behavior_config_from_instance", return_value=None):
            result = npc_event_handler._get_npc_spawn_message("npc_001")
            assert result == "TestNPC appears."


def test_get_npc_spawn_message_custom(npc_event_handler):
    """Test _get_npc_spawn_message() returns custom spawn message."""
    with patch.object(npc_event_handler, "_get_npc_instance") as mock_get_instance:
        mock_npc = MagicMock()
        mock_npc.name = "TestNPC"
        mock_get_instance.return_value = mock_npc
        with patch.object(
            npc_event_handler, "_get_behavior_config_from_instance", return_value={"spawn_message": "Custom message"}
        ):
            with patch.object(
                npc_event_handler, "_parse_behavior_config", return_value={"spawn_message": "Custom message"}
            ):
                result = npc_event_handler._get_npc_spawn_message("npc_001")
                assert result == "Custom message"


def test_get_npc_name(npc_event_handler):
    """Test _get_npc_name() returns NPC name."""
    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_lifecycle = MagicMock()
        mock_npc = MagicMock()
        mock_npc.name = "TestNPC"
        mock_lifecycle.active_npcs = {"npc_001": mock_npc}
        mock_service.lifecycle_manager = mock_lifecycle
        mock_get_service.return_value = mock_service
        result = npc_event_handler._get_npc_name("npc_001")
        assert result == "TestNPC"


@pytest.mark.asyncio
async def test_determine_direction_from_rooms(npc_event_handler, mock_connection_manager):
    """Test _determine_direction_from_rooms() determines direction."""
    mock_room = MagicMock()
    mock_room.exits = {"north": "room_002"}
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = await npc_event_handler._determine_direction_from_rooms("room_001", "room_002")
    assert result == "north"


@pytest.mark.asyncio
async def test_determine_direction_from_rooms_not_found(npc_event_handler, mock_connection_manager):
    """Test _determine_direction_from_rooms() returns None when direction not found."""
    mock_room = MagicMock()
    mock_room.exits = {"north": "room_003"}
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = await npc_event_handler._determine_direction_from_rooms("room_001", "room_002")
    assert result is None


def test_get_npc_departure_message(npc_event_handler):
    """Test _get_npc_departure_message() returns departure message."""
    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_lifecycle = MagicMock()
        mock_npc = MagicMock()
        mock_npc.name = "TestNPC"
        # Set both _behavior_config and behavior_config to None to trigger default message
        type(mock_npc)._behavior_config = None
        type(mock_npc).behavior_config = None
        mock_lifecycle.active_npcs = {"npc_001": mock_npc}
        mock_service.lifecycle_manager = mock_lifecycle
        mock_get_service.return_value = mock_service
        result = npc_event_handler._get_npc_departure_message("npc_001")
        assert result == "TestNPC leaves."
