"""
Unit tests for NPC event handlers.

Tests the NPCEventHandler class.
"""

from unittest.mock import AsyncMock, MagicMock

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
