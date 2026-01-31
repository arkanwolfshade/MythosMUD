"""
Unit tests for player room event handlers (player left / unsubscribe / broadcast left).

Tests unsubscribe_player_from_room, broadcast_player_left_message, handle_player_left,
and _log_occupants_info. Fixtures from conftest.py.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.events.event_types import PlayerLeftRoom

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names


@pytest.mark.asyncio
async def test_unsubscribe_player_from_room_success(player_room_event_handler, mock_connection_manager):
    """Test unsubscribe_player_from_room() successfully unsubscribes player."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_connection_manager.unsubscribe_from_room = AsyncMock()
    await player_room_event_handler.unsubscribe_player_from_room(player_id, room_id)
    mock_connection_manager.unsubscribe_from_room.assert_awaited_once_with(player_id, room_id)


@pytest.mark.asyncio
async def test_unsubscribe_player_from_room_string_id(player_room_event_handler, mock_connection_manager):
    """Test unsubscribe_player_from_room() handles string player_id."""
    player_id_str = str(uuid.uuid4())
    room_id = "room_001"
    mock_connection_manager.unsubscribe_from_room = AsyncMock()
    await player_room_event_handler.unsubscribe_player_from_room(player_id_str, room_id)
    mock_connection_manager.unsubscribe_from_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_unsubscribe_player_from_room_invalid_id(player_room_event_handler, mock_logger):
    """Test unsubscribe_player_from_room() handles invalid player_id."""
    await player_room_event_handler.unsubscribe_player_from_room("invalid_uuid", "room_001")
    mock_logger.warning.assert_called_once()


@pytest.mark.asyncio
async def test_broadcast_player_left_message_not_disconnecting(player_room_event_handler, mock_connection_manager):
    """Test broadcast_player_left_message() broadcasts when not disconnecting."""
    message = {"type": "player_left"}
    room_id_str = "room_001"
    exclude_player_id = "player_001"
    mock_connection_manager.broadcast_to_room = AsyncMock()
    await player_room_event_handler.broadcast_player_left_message(
        message, room_id_str, exclude_player_id, is_disconnecting=False
    )
    mock_connection_manager.broadcast_to_room.assert_awaited_once_with(
        room_id_str, message, exclude_player=exclude_player_id
    )


@pytest.mark.asyncio
async def test_broadcast_player_left_message_disconnecting(player_room_event_handler, mock_connection_manager):
    """Test broadcast_player_left_message() skips when player is disconnecting."""
    message = {"type": "player_left"}
    room_id_str = "room_001"
    exclude_player_id = "player_001"
    mock_connection_manager.broadcast_to_room = AsyncMock()
    await player_room_event_handler.broadcast_player_left_message(
        message, room_id_str, exclude_player_id, is_disconnecting=True
    )
    mock_connection_manager.broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_broadcast_player_left_message_no_room_id(player_room_event_handler, mock_connection_manager):
    """Test broadcast_player_left_message() skips when room_id is None."""
    message = {"type": "player_left"}
    mock_connection_manager.broadcast_to_room = AsyncMock()
    await player_room_event_handler.broadcast_player_left_message(message, None, "player_001", is_disconnecting=False)
    mock_connection_manager.broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_handle_player_left_success(player_room_event_handler, mock_room_sync_service):
    """Test handle_player_left() successfully handles event."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    event = PlayerLeftRoom(player_id=str(player_id), room_id=room_id)
    processed_event = PlayerLeftRoom(player_id=str(player_id), room_id=room_id)
    mock_room_sync_service.process_event_with_ordering.return_value = processed_event
    mock_player = MagicMock()
    player_room_event_handler.log_player_movement = AsyncMock()
    player_room_event_handler.message_builder.create_player_left_message = MagicMock(
        return_value={"type": "player_left"}
    )
    player_room_event_handler.broadcast_player_left_message = AsyncMock()
    player_room_event_handler.unsubscribe_player_from_room = AsyncMock()
    send_occupants_update = AsyncMock()
    with patch.object(
        player_room_event_handler.utils,
        "get_player_info",
        new_callable=AsyncMock,
        return_value=(mock_player, "TestPlayer"),
    ):
        with patch.object(player_room_event_handler.utils, "is_player_disconnecting", return_value=False):
            await player_room_event_handler.handle_player_left(event, send_occupants_update)
            player_room_event_handler.broadcast_player_left_message.assert_awaited_once()
            player_room_event_handler.unsubscribe_player_from_room.assert_awaited_once()
            send_occupants_update.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_left_no_connection_manager(player_room_event_handler, mock_logger):
    """Test handle_player_left() skips when connection manager not available."""
    player_room_event_handler.connection_manager = None
    event = PlayerLeftRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    send_occupants_update = AsyncMock()
    await player_room_event_handler.handle_player_left(event, send_occupants_update)
    mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_left_no_player_info(player_room_event_handler, mock_room_sync_service):
    """Test handle_player_left() handles player not found."""
    event = PlayerLeftRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    processed_event = PlayerLeftRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    mock_room_sync_service.process_event_with_ordering.return_value = processed_event
    player_room_event_handler.broadcast_player_left_message = AsyncMock()
    send_occupants_update = AsyncMock()
    with patch.object(player_room_event_handler.utils, "get_player_info", new_callable=AsyncMock, return_value=None):
        await player_room_event_handler.handle_player_left(event, send_occupants_update)
        player_room_event_handler.broadcast_player_left_message.assert_not_called()


@pytest.mark.asyncio
async def test_handle_player_left_disconnecting(player_room_event_handler, mock_room_sync_service):
    """Test handle_player_left() skips broadcast when player is disconnecting."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    event = PlayerLeftRoom(player_id=str(player_id), room_id=room_id)
    processed_event = PlayerLeftRoom(player_id=str(player_id), room_id=room_id)
    mock_room_sync_service.process_event_with_ordering.return_value = processed_event
    mock_player = MagicMock()
    player_room_event_handler.log_player_movement = AsyncMock()
    player_room_event_handler.message_builder.create_player_left_message = MagicMock(
        return_value={"type": "player_left"}
    )
    player_room_event_handler.broadcast_player_left_message = AsyncMock()
    player_room_event_handler.unsubscribe_player_from_room = AsyncMock()
    send_occupants_update = AsyncMock()
    with patch.object(
        player_room_event_handler.utils,
        "get_player_info",
        new_callable=AsyncMock,
        return_value=(mock_player, "TestPlayer"),
    ):
        with patch.object(player_room_event_handler.utils, "is_player_disconnecting", return_value=True):
            await player_room_event_handler.handle_player_left(event, send_occupants_update)
            # Should still call broadcast_player_left_message, but with is_disconnecting=True
            call_args = player_room_event_handler.broadcast_player_left_message.call_args
            assert call_args[0][3] is True  # is_disconnecting parameter


@pytest.mark.asyncio
async def test_handle_player_left_error_handling(player_room_event_handler, mock_room_sync_service, mock_logger):
    """Test handle_player_left() handles errors."""
    event = PlayerLeftRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    mock_room_sync_service.process_event_with_ordering.side_effect = SQLAlchemyError("Database error")
    send_occupants_update = AsyncMock()
    await player_room_event_handler.handle_player_left(event, send_occupants_update)
    mock_logger.error.assert_called_once()


def test_log_occupants_info(player_room_event_handler, mock_logger):
    """Test _log_occupants_info() logs occupant information."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    occupants_snapshot = [{"player_name": "Player1"}, {"npc_name": "NPC1"}]
    occupants_data = {"players": ["Player1"], "npcs": ["NPC1"], "occupants": ["Player1", "NPC1"], "count": 2}
    with patch.object(player_room_event_handler.utils, "count_occupants_by_type", return_value=(1, 1)):
        player_room_event_handler._log_occupants_info(player_id, room_id, occupants_snapshot, occupants_data)
        mock_logger.info.assert_called_once()
