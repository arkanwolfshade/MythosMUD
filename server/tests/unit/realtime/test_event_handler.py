"""
Unit tests for event handler.

Tests the event_handler module classes and functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events.event_types import (
    NPCEnteredRoom,
    NPCLeftRoom,
    PlayerDeliriumRespawnedEvent,
    PlayerDiedEvent,
    PlayerDPDecayEvent,
    PlayerDPUpdated,
    PlayerEnteredRoom,
    PlayerLeftRoom,
    PlayerRespawnedEvent,
)
from server.realtime.event_handler import RealTimeEventHandler
from server.services.player_combat_service import PlayerXPAwardEvent


@pytest.fixture
def mock_event_bus():
    """Create a mock EventBus."""
    bus = MagicMock()
    bus.subscribe = MagicMock()
    return bus


@pytest.fixture
def mock_connection_manager():
    """Create a mock ConnectionManager."""
    manager = MagicMock()
    manager.broadcast_to_room = AsyncMock()
    return manager


@pytest.fixture
def mock_task_registry():
    """Create a mock TaskRegistry."""
    return MagicMock()


@pytest.fixture
def event_handler(mock_event_bus, mock_connection_manager, mock_task_registry):
    """Create a RealTimeEventHandler instance."""
    with patch("server.realtime.event_handler.get_room_sync_service") as mock_sync, patch(
        "server.realtime.event_handler.chat_logger"
    ) as mock_chat_logger:
        mock_sync.return_value = MagicMock()
        handler = RealTimeEventHandler(
            event_bus=mock_event_bus, task_registry=mock_task_registry, connection_manager=mock_connection_manager
        )
        return handler


def test_event_handler_init(mock_event_bus, mock_connection_manager, mock_task_registry):
    """Test RealTimeEventHandler.__init__() initializes correctly."""
    with patch("server.realtime.event_handler.get_room_sync_service") as mock_sync, patch(
        "server.realtime.event_handler.chat_logger"
    ) as mock_chat_logger:
        mock_sync.return_value = MagicMock()
        handler = RealTimeEventHandler(
            event_bus=mock_event_bus, task_registry=mock_task_registry, connection_manager=mock_connection_manager
        )

        assert handler.event_bus == mock_event_bus
        assert handler.connection_manager == mock_connection_manager
        assert handler.task_registry == mock_task_registry
        assert handler._sequence_counter == 0
        assert hasattr(handler, "name_extractor")
        assert hasattr(handler, "occupant_manager")
        assert hasattr(handler, "message_builder")
        assert hasattr(handler, "player_handler")
        assert hasattr(handler, "npc_handler")


def test_event_handler_init_no_event_bus(mock_connection_manager, mock_task_registry):
    """Test RealTimeEventHandler.__init__() creates EventBus when None."""
    with patch("server.realtime.event_handler.EventBus") as mock_event_bus_class, patch(
        "server.realtime.event_handler.get_room_sync_service"
    ) as mock_sync, patch("server.realtime.event_handler.chat_logger") as mock_chat_logger:
        mock_event_bus_instance = MagicMock()
        mock_event_bus_class.return_value = mock_event_bus_instance
        mock_sync.return_value = MagicMock()

        handler = RealTimeEventHandler(
            event_bus=None, task_registry=mock_task_registry, connection_manager=mock_connection_manager
        )

        assert handler.event_bus == mock_event_bus_instance
        mock_event_bus_class.assert_called_once()


def test_event_handler_subscribe_to_events(event_handler, mock_event_bus):
    """Test RealTimeEventHandler subscribes to all events."""
    assert mock_event_bus.subscribe.call_count >= 10  # Should subscribe to multiple events


def test_event_handler_get_next_sequence(event_handler):
    """Test RealTimeEventHandler._get_next_sequence() increments counter."""
    seq1 = event_handler._get_next_sequence()
    seq2 = event_handler._get_next_sequence()

    assert seq1 == 1
    assert seq2 == 2
    assert event_handler._sequence_counter == 2


@pytest.mark.asyncio
async def test_event_handler_handle_player_entered(event_handler):
    """Test RealTimeEventHandler._handle_player_entered() delegates to player_handler."""
    mock_event = MagicMock(spec=PlayerEnteredRoom)
    mock_event.player_id = uuid.uuid4()
    mock_event.room_id = "room_123"

    with patch.object(event_handler.player_handler, "handle_player_entered") as mock_handle:
        await event_handler._handle_player_entered(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_handle_player_left(event_handler):
    """Test RealTimeEventHandler._handle_player_left() delegates to player_handler."""
    mock_event = MagicMock(spec=PlayerLeftRoom)
    mock_event.player_id = uuid.uuid4()
    mock_event.room_id = "room_123"

    with patch.object(event_handler.player_handler, "handle_player_left") as mock_handle:
        await event_handler._handle_player_left(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_handle_npc_entered(event_handler):
    """Test RealTimeEventHandler._handle_npc_entered() delegates to npc_handler."""
    mock_event = MagicMock(spec=NPCEnteredRoom)
    mock_event.npc_id = "npc_123"
    mock_event.room_id = "room_123"

    with patch.object(event_handler.npc_handler, "handle_npc_entered") as mock_handle:
        await event_handler._handle_npc_entered(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_handle_npc_left(event_handler):
    """Test RealTimeEventHandler._handle_npc_left() delegates to npc_handler."""
    mock_event = MagicMock(spec=NPCLeftRoom)
    mock_event.npc_id = "npc_123"
    mock_event.room_id = "room_123"

    with patch.object(event_handler.npc_handler, "handle_npc_left") as mock_handle:
        await event_handler._handle_npc_left(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_handle_player_xp_awarded(event_handler):
    """Test RealTimeEventHandler._handle_player_xp_awarded() delegates to player_handler."""
    mock_event = MagicMock(spec=PlayerXPAwardEvent)
    mock_event.player_id = uuid.uuid4()
    mock_event.xp_amount = 100

    with patch.object(event_handler.player_handler, "handle_player_xp_awarded") as mock_handle:
        await event_handler._handle_player_xp_awarded(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_handle_player_dp_updated(event_handler):
    """Test RealTimeEventHandler._handle_player_dp_updated() delegates to player_handler."""
    mock_event = MagicMock(spec=PlayerDPUpdated)
    mock_event.player_id = uuid.uuid4()
    mock_event.new_dp = 50

    with patch.object(event_handler.player_handler, "handle_player_dp_updated") as mock_handle:
        await event_handler._handle_player_dp_updated(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_handle_player_died(event_handler):
    """Test RealTimeEventHandler._handle_player_died() delegates to player_handler."""
    mock_event = MagicMock(spec=PlayerDiedEvent)
    mock_event.player_id = uuid.uuid4()

    with patch.object(event_handler.player_handler, "handle_player_died") as mock_handle:
        await event_handler._handle_player_died(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_handle_player_dp_decay(event_handler):
    """Test RealTimeEventHandler._handle_player_dp_decay() delegates to player_handler."""
    mock_event = MagicMock(spec=PlayerDPDecayEvent)
    mock_event.player_id = uuid.uuid4()
    mock_event.dp_lost = 5

    with patch.object(event_handler.player_handler, "handle_player_dp_decay") as mock_handle:
        await event_handler._handle_player_dp_decay(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_handle_player_respawned(event_handler):
    """Test RealTimeEventHandler._handle_player_respawned() delegates to player_handler."""
    mock_event = MagicMock(spec=PlayerRespawnedEvent)
    mock_event.player_id = uuid.uuid4()
    mock_event.room_id = "room_123"

    with patch.object(event_handler.player_handler, "handle_player_respawned") as mock_handle:
        await event_handler._handle_player_respawned(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_handle_player_delirium_respawned(event_handler):
    """Test RealTimeEventHandler._handle_player_delirium_respawned() delegates to player_handler."""
    mock_event = MagicMock(spec=PlayerDeliriumRespawnedEvent)
    mock_event.player_id = uuid.uuid4()
    mock_event.room_id = "room_123"

    with patch.object(event_handler.player_handler, "handle_player_delirium_respawned") as mock_handle:
        await event_handler._handle_player_delirium_respawned(mock_event)

        mock_handle.assert_called_once()
        assert mock_handle.call_args[0][0] == mock_event


@pytest.mark.asyncio
async def test_event_handler_send_room_occupants_update_internal_success(event_handler):
    """Test RealTimeEventHandler._send_room_occupants_update_internal() sends update."""
    room_id = "room_123"
    exclude_player = "player_123"

    with patch.object(event_handler.occupant_manager, "get_room_occupants") as mock_get_occupants, patch.object(
        event_handler.occupant_manager, "separate_occupants_by_type"
    ) as mock_separate, patch.object(event_handler.message_builder, "build_occupants_update_message") as mock_build:
        mock_get_occupants.return_value = [{"name": "Player1"}, {"name": "NPC1"}]
        mock_separate.return_value = (["Player1"], ["NPC1"], [{"name": "Player1"}, {"name": "NPC1"}])
        mock_build.return_value = {"type": "room_occupants", "players": ["Player1"], "npcs": ["NPC1"]}

        await event_handler._send_room_occupants_update_internal(room_id, exclude_player)

        mock_get_occupants.assert_called_once_with(room_id)
        mock_separate.assert_called_once()
        mock_build.assert_called_once()
        event_handler.connection_manager.broadcast_to_room.assert_called_once()


@pytest.mark.asyncio
async def test_event_handler_send_room_occupants_update_internal_error(event_handler):
    """Test RealTimeEventHandler._send_room_occupants_update_internal() handles errors."""
    room_id = "room_123"

    with patch.object(event_handler.occupant_manager, "get_room_occupants", side_effect=ValueError("Error")):
        await event_handler._send_room_occupants_update_internal(room_id)

        # Should not raise, just log error
        event_handler.connection_manager.broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_event_handler_send_room_occupants_update(event_handler):
    """Test RealTimeEventHandler.send_room_occupants_update() calls internal method."""
    room_id = "room_123"
    exclude_player = "player_123"

    with patch.object(event_handler, "_send_room_occupants_update_internal") as mock_internal:
        await event_handler.send_room_occupants_update(room_id, exclude_player)

        mock_internal.assert_called_once_with(room_id, exclude_player)


@pytest.mark.asyncio
async def test_event_handler_get_room_occupants(event_handler):
    """Test RealTimeEventHandler._get_room_occupants() delegates to occupant_manager."""
    room_id = "room_123"
    expected_occupants = [{"name": "Player1"}, {"name": "NPC1"}]

    with patch.object(event_handler.occupant_manager, "get_room_occupants", return_value=expected_occupants):
        result = await event_handler._get_room_occupants(room_id)

        assert result == expected_occupants


def test_event_handler_create_player_entered_message(event_handler):
    """Test RealTimeEventHandler._create_player_entered_message() delegates to message_builder."""
    mock_event = MagicMock(spec=PlayerEnteredRoom)
    player_name = "TestPlayer"
    expected_message = {"type": "player_entered", "player": player_name}

    with patch.object(event_handler.message_builder, "create_player_entered_message", return_value=expected_message):
        result = event_handler._create_player_entered_message(mock_event, player_name)

        assert result == expected_message


def test_event_handler_create_player_left_message(event_handler):
    """Test RealTimeEventHandler._create_player_left_message() delegates to message_builder."""
    mock_event = MagicMock(spec=PlayerLeftRoom)
    player_name = "TestPlayer"
    expected_message = {"type": "player_left", "player": player_name}

    with patch.object(event_handler.message_builder, "create_player_left_message", return_value=expected_message):
        result = event_handler._create_player_left_message(mock_event, player_name)

        assert result == expected_message


@pytest.mark.asyncio
async def test_event_handler_send_occupants_snapshot_to_player(event_handler):
    """Test RealTimeEventHandler._send_occupants_snapshot_to_player() delegates to player_handler."""
    player_id = uuid.uuid4()
    room_id = "room_123"

    with patch.object(event_handler.player_handler, "send_occupants_snapshot_to_player") as mock_send:
        await event_handler._send_occupants_snapshot_to_player(player_id, room_id)

        mock_send.assert_called_once_with(player_id, room_id)


def test_event_handler_shutdown(event_handler):
    """Test RealTimeEventHandler.shutdown() logs shutdown."""
    with patch.object(event_handler._logger, "info") as mock_info:
        event_handler.shutdown()

        mock_info.assert_called_once()
        assert "Shutting down" in mock_info.call_args[0][0]
