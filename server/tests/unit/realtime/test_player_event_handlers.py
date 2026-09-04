"""
Unit tests for player event handlers.

Tests the PlayerEventHandler class and its delegation to specialized handlers.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.events.event_types import PlayerDPUpdated, PlayerEnteredRoom, PlayerLeftRoom
from server.realtime.player_event_handlers import PlayerEventHandler
from server.services.player_combat_service import PlayerXPAwardEvent


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    return MagicMock()


@pytest.fixture
def mock_room_sync_service():
    """Create a mock room sync service."""
    return MagicMock()


@pytest.fixture
def mock_chat_logger():
    """Create a mock chat logger."""
    return MagicMock()


@pytest.fixture
def mock_task_registry():
    """Create a mock task registry."""
    return MagicMock()


@pytest.fixture
def mock_message_builder():
    """Create a mock message builder."""
    return MagicMock()


@pytest.fixture
def mock_name_extractor():
    """Create a mock name extractor."""
    return MagicMock()


@pytest.fixture
def mock_occupant_manager():
    """Create a mock occupant manager."""
    return MagicMock()


@pytest.fixture
def player_event_handler(
    mock_connection_manager,
    mock_room_sync_service,
    mock_chat_logger,
    mock_task_registry,
    mock_message_builder,
    mock_name_extractor,
    mock_occupant_manager,
):
    """Create a PlayerEventHandler instance."""
    return PlayerEventHandler(
        connection_manager=mock_connection_manager,
        room_sync_service=mock_room_sync_service,
        chat_logger=mock_chat_logger,
        task_registry=mock_task_registry,
        message_builder=mock_message_builder,
        name_extractor=mock_name_extractor,
        occupant_manager=mock_occupant_manager,
    )


def test_player_event_handler_init(player_event_handler):
    """Test PlayerEventHandler initialization."""
    assert player_event_handler.connection_manager is not None
    assert player_event_handler.room_sync_service is not None
    assert player_event_handler.chat_logger is not None
    assert player_event_handler.task_registry is not None
    assert player_event_handler.message_builder is not None
    assert player_event_handler.name_extractor is not None
    assert player_event_handler.occupant_manager is not None
    assert hasattr(player_event_handler, "_room_handler")
    assert hasattr(player_event_handler, "_state_handler")
    assert hasattr(player_event_handler, "_respawn_handler")
    assert hasattr(player_event_handler, "_utils")


@pytest.mark.asyncio
async def test_handle_player_entered_delegates_to_room_handler(player_event_handler):
    """Test handle_player_entered() delegates to room handler."""
    event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    send_occupants_update = MagicMock()
    player_event_handler._room_handler.handle_player_entered = AsyncMock()
    await player_event_handler.handle_player_entered(event, send_occupants_update)
    player_event_handler._room_handler.handle_player_entered.assert_awaited_once_with(event, send_occupants_update)


@pytest.mark.asyncio
async def test_handle_player_entered_no_send_occupants_update(player_event_handler):
    """Test handle_player_entered() works without send_occupants_update."""
    event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    player_event_handler._room_handler.handle_player_entered = AsyncMock()
    await player_event_handler.handle_player_entered(event, None)
    player_event_handler._room_handler.handle_player_entered.assert_awaited_once_with(event, None)


@pytest.mark.asyncio
async def test_handle_player_left_delegates_to_room_handler(player_event_handler):
    """Test handle_player_left() delegates to room handler."""
    event = PlayerLeftRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    send_occupants_update = MagicMock()
    player_event_handler._room_handler.handle_player_left = AsyncMock()
    await player_event_handler.handle_player_left(event, send_occupants_update)
    player_event_handler._room_handler.handle_player_left.assert_awaited_once_with(event, send_occupants_update)


@pytest.mark.asyncio
async def test_send_occupants_snapshot_to_player_delegates_to_room_handler(player_event_handler):
    """Test send_occupants_snapshot_to_player() delegates to room handler."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    player_event_handler._room_handler.send_occupants_snapshot_to_player = AsyncMock()
    await player_event_handler.send_occupants_snapshot_to_player(player_id, room_id)
    player_event_handler._room_handler.send_occupants_snapshot_to_player.assert_awaited_once_with(player_id, room_id)


@pytest.mark.asyncio
async def test_send_occupants_snapshot_to_player_string_id(player_event_handler):
    """Test send_occupants_snapshot_to_player() handles string player_id."""
    player_id = str(uuid.uuid4())
    room_id = "room_001"
    player_event_handler._room_handler.send_occupants_snapshot_to_player = AsyncMock()
    await player_event_handler.send_occupants_snapshot_to_player(player_id, room_id)
    player_event_handler._room_handler.send_occupants_snapshot_to_player.assert_awaited_once_with(player_id, room_id)


@pytest.mark.asyncio
async def test_handle_player_xp_awarded_delegates_to_state_handler(player_event_handler):
    """Test handle_player_xp_awarded() delegates to state handler."""
    event = PlayerXPAwardEvent(player_id=uuid.uuid4(), xp_amount=100, new_level=5)
    player_event_handler._state_handler.handle_player_xp_awarded = AsyncMock()
    await player_event_handler.handle_player_xp_awarded(event)
    player_event_handler._state_handler.handle_player_xp_awarded.assert_awaited_once_with(event)


@pytest.mark.asyncio
async def test_handle_player_dp_updated_delegates_to_state_handler(player_event_handler):
    """Test handle_player_dp_updated() delegates to state handler."""
    event = PlayerDPUpdated(player_id=uuid.uuid4(), old_dp=60, new_dp=50, max_dp=100)
    player_event_handler._state_handler.handle_player_dp_updated = AsyncMock()
    await player_event_handler.handle_player_dp_updated(event)
    player_event_handler._state_handler.handle_player_dp_updated.assert_awaited_once_with(event)


@pytest.mark.asyncio
async def test_handle_player_died_delegates_to_state_handler(player_event_handler):
    """Test handle_player_died() delegates to state handler."""
    event = MagicMock()
    player_event_handler._state_handler.handle_player_died = AsyncMock()
    await player_event_handler.handle_player_died(event)
    player_event_handler._state_handler.handle_player_died.assert_awaited_once_with(event)


@pytest.mark.asyncio
async def test_handle_player_dp_decay_delegates_to_state_handler(player_event_handler):
    """Test handle_player_dp_decay() delegates to state handler."""
    event = MagicMock()
    player_event_handler._state_handler.handle_player_dp_decay = AsyncMock()
    await player_event_handler.handle_player_dp_decay(event)
    player_event_handler._state_handler.handle_player_dp_decay.assert_awaited_once_with(event)


@pytest.mark.asyncio
async def test_handle_player_respawned_delegates_to_respawn_handler(player_event_handler):
    """Test handle_player_respawned() delegates to respawn handler."""
    event = MagicMock()
    player_event_handler._respawn_handler.handle_player_respawned = AsyncMock()
    await player_event_handler.handle_player_respawned(event)
    player_event_handler._respawn_handler.handle_player_respawned.assert_awaited_once_with(event)


@pytest.mark.asyncio
async def test_handle_player_delirium_respawned_delegates_to_respawn_handler(player_event_handler):
    """Test handle_player_delirium_respawned() delegates to respawn handler."""
    event = MagicMock()
    player_event_handler._respawn_handler.handle_player_delirium_respawned = AsyncMock()
    await player_event_handler.handle_player_delirium_respawned(event)
    player_event_handler._respawn_handler.handle_player_delirium_respawned.assert_awaited_once_with(event)


@pytest.mark.asyncio
async def test_handle_player_entered_error_handling(player_event_handler):
    """Test handle_player_entered() propagates errors from room handler."""
    event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    send_occupants_update = MagicMock()
    player_event_handler._room_handler.handle_player_entered = AsyncMock(side_effect=Exception("Error"))
    # Errors are propagated (not caught in the main handler)
    with pytest.raises(Exception, match="Error"):
        await player_event_handler.handle_player_entered(event, send_occupants_update)


@pytest.mark.asyncio
async def test_handle_player_left_error_handling(player_event_handler):
    """Test handle_player_left() propagates errors from room handler."""
    event = PlayerLeftRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    send_occupants_update = MagicMock()
    player_event_handler._room_handler.handle_player_left = AsyncMock(side_effect=Exception("Error"))
    # Errors are propagated (not caught in the main handler)
    with pytest.raises(Exception, match="Error"):
        await player_event_handler.handle_player_left(event, send_occupants_update)


@pytest.mark.asyncio
async def test_handle_player_xp_awarded_error_handling(player_event_handler):
    """Test handle_player_xp_awarded() propagates errors from state handler."""
    event = PlayerXPAwardEvent(player_id=uuid.uuid4(), xp_amount=100, new_level=5)
    player_event_handler._state_handler.handle_player_xp_awarded = AsyncMock(side_effect=Exception("Error"))
    # Errors are propagated (not caught in the main handler)
    with pytest.raises(Exception, match="Error"):
        await player_event_handler.handle_player_xp_awarded(event)


@pytest.mark.asyncio
async def test_handle_player_dp_updated_error_handling(player_event_handler):
    """Test handle_player_dp_updated() propagates errors from state handler."""
    event = PlayerDPUpdated(player_id=uuid.uuid4(), old_dp=60, new_dp=50, max_dp=100)
    player_event_handler._state_handler.handle_player_dp_updated = AsyncMock(side_effect=Exception("Error"))
    # Errors are propagated (not caught in the main handler)
    with pytest.raises(Exception, match="Error"):
        await player_event_handler.handle_player_dp_updated(event)
