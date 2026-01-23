"""
Unit tests for player room event handlers.

Tests the PlayerRoomEventHandler class.
"""

import uuid
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.realtime.player_event_handlers_room import PlayerRoomEventHandler
from server.realtime.player_event_handlers_utils import PlayerEventHandlerUtils


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
def mock_utils(mock_connection_manager):
    """Create a mock PlayerEventHandlerUtils."""
    return PlayerEventHandlerUtils(mock_connection_manager, MagicMock(), MagicMock())


@pytest.fixture
def mock_logger():
    """Create a mock logger."""
    return MagicMock()


@pytest.fixture
def player_room_event_handler(
    mock_connection_manager,
    mock_room_sync_service,
    mock_chat_logger,
    mock_message_builder,
    mock_name_extractor,
    mock_occupant_manager,
    mock_utils,
    mock_logger,
):
    """Create a PlayerRoomEventHandler instance."""
    return PlayerRoomEventHandler(
        connection_manager=mock_connection_manager,
        room_sync_service=mock_room_sync_service,
        chat_logger=mock_chat_logger,
        message_builder=mock_message_builder,
        name_extractor=mock_name_extractor,
        occupant_manager=mock_occupant_manager,
        utils=mock_utils,
        logger=mock_logger,
    )


def test_player_room_event_handler_init(player_room_event_handler, mock_connection_manager):
    """Test PlayerRoomEventHandler initialization."""
    assert player_room_event_handler.connection_manager == mock_connection_manager
    assert player_room_event_handler.room_sync_service is not None
    assert player_room_event_handler.chat_logger is not None
    assert player_room_event_handler.message_builder is not None
    assert player_room_event_handler.name_extractor is not None
    assert player_room_event_handler.occupant_manager is not None
    assert player_room_event_handler.utils is not None


@pytest.mark.asyncio
async def test_log_player_movement_joined(player_room_event_handler, mock_connection_manager, mock_chat_logger):
    """Test log_player_movement() logs player joined."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    room_id = "room_001"
    mock_room = MagicMock()
    mock_room.name = "Test Room"
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    await player_room_event_handler.log_player_movement(player_id, player_name, room_id, "joined")
    mock_chat_logger.log_player_joined_room.assert_called_once()


@pytest.mark.asyncio
async def test_log_player_movement_left(player_room_event_handler, mock_connection_manager, mock_chat_logger):
    """Test log_player_movement() logs player left."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    room_id = "room_001"
    mock_room = MagicMock()
    mock_room.name = "Test Room"
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    await player_room_event_handler.log_player_movement(player_id, player_name, room_id, "left")
    mock_chat_logger.log_player_left_room.assert_called_once()


@pytest.mark.asyncio
async def test_log_player_movement_no_connection_manager(player_room_event_handler, mock_chat_logger):
    """Test log_player_movement() skips when connection manager not available."""
    player_room_event_handler.connection_manager = None
    await player_room_event_handler.log_player_movement(uuid.uuid4(), "TestPlayer", "room_001", "joined")
    mock_chat_logger.log_player_joined_room.assert_not_called()


@pytest.mark.asyncio
async def test_log_player_movement_no_room(player_room_event_handler, mock_connection_manager, mock_chat_logger):
    """Test log_player_movement() handles room not found."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    room_id = "room_001"
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=None)
    await player_room_event_handler.log_player_movement(player_id, player_name, room_id, "joined")
    # Should use room_id as fallback for room_name
    mock_chat_logger.log_player_joined_room.assert_called_once()


@pytest.mark.asyncio
async def test_log_player_movement_error_handling(player_room_event_handler, mock_connection_manager, mock_logger):
    """Test log_player_movement() handles errors."""
    # Set async_persistence to None to trigger error path
    mock_connection_manager.async_persistence = None
    # The error handling catches exceptions, so we need to trigger one
    # by making get_room_by_id raise an error
    await player_room_event_handler.log_player_movement(uuid.uuid4(), "TestPlayer", "room_001", "joined")
    # Error is caught and logged, but since async_persistence is None, it returns early
    # So we just verify it doesn't raise


@pytest.mark.asyncio
async def test_broadcast_player_entered_message(player_room_event_handler, mock_connection_manager):
    """Test broadcast_player_entered_message() broadcasts to room."""
    message = {"type": "player_entered"}
    room_id_str = "room_001"
    exclude_player_id = "player_001"
    mock_connection_manager.broadcast_to_room = AsyncMock()
    await player_room_event_handler.broadcast_player_entered_message(message, room_id_str, exclude_player_id)
    mock_connection_manager.broadcast_to_room.assert_awaited_once_with(
        room_id_str, message, exclude_player=exclude_player_id
    )


@pytest.mark.asyncio
async def test_broadcast_player_entered_message_no_room_id(player_room_event_handler, mock_connection_manager):
    """Test broadcast_player_entered_message() skips when room_id is None."""
    message = {"type": "player_entered"}
    mock_connection_manager.broadcast_to_room = AsyncMock()
    await player_room_event_handler.broadcast_player_entered_message(message, None, "player_001")
    mock_connection_manager.broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_subscribe_player_to_room_success(player_room_event_handler, mock_connection_manager):
    """Test subscribe_player_to_room() successfully subscribes player."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_connection_manager.subscribe_to_room = AsyncMock()
    with patch.object(player_room_event_handler.utils, "normalize_player_id", return_value=player_id):
        await player_room_event_handler.subscribe_player_to_room(player_id, room_id)
        mock_connection_manager.subscribe_to_room.assert_awaited_once_with(player_id, room_id)


@pytest.mark.asyncio
async def test_subscribe_player_to_room_invalid_id(player_room_event_handler, mock_logger):
    """Test subscribe_player_to_room() handles invalid player_id."""
    with patch.object(player_room_event_handler.utils, "normalize_player_id", return_value=None):
        await player_room_event_handler.subscribe_player_to_room("invalid_uuid", "room_001")
        mock_logger.warning.assert_called_once()


@pytest.mark.asyncio
async def test_subscribe_player_to_room_error(player_room_event_handler, mock_connection_manager, mock_logger):
    """Test subscribe_player_to_room() handles subscription errors."""
    player_id = uuid.uuid4()
    mock_connection_manager.subscribe_to_room = AsyncMock(side_effect=ValueError("Subscription error"))
    with patch.object(player_room_event_handler.utils, "normalize_player_id", return_value=player_id):
        await player_room_event_handler.subscribe_player_to_room(player_id, "room_001")
        mock_logger.warning.assert_called_once()


@pytest.mark.asyncio
async def test_send_room_name_message(player_room_event_handler, mock_connection_manager):
    """Test _send_room_name_message() sends room name."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    room_name = "Test Room"
    mock_connection_manager.send_personal_message = AsyncMock()
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "command_response"}
        await player_room_event_handler._send_room_name_message(player_id, room_id, room_name)
        mock_connection_manager.send_personal_message.assert_awaited_once_with(player_id, mock_build_event.return_value)


@pytest.mark.asyncio
async def test_prepare_room_data_with_to_dict(player_room_event_handler, mock_connection_manager):
    """Test _prepare_room_data() prepares room data with to_dict."""
    mock_room = MagicMock()
    mock_room.to_dict.return_value = {"id": "room_001", "name": "Test Room", "players": ["player1"]}
    mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(
        return_value={"id": "room_001", "name": "Test Room"}
    )
    result = await player_room_event_handler._prepare_room_data(mock_room, "room_001")
    assert "players" not in result
    assert "npcs" not in result
    assert "occupants" not in result


@pytest.mark.asyncio
async def test_prepare_room_data_without_to_dict(player_room_event_handler, mock_connection_manager):
    """Test _prepare_room_data() handles room without to_dict method."""
    mock_room = {"id": "room_001", "name": "Test Room", "players": ["player1"]}
    mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(
        return_value={"id": "room_001", "name": "Test Room"}
    )
    result = await player_room_event_handler._prepare_room_data(mock_room, "room_001")
    assert "players" not in result


@pytest.mark.asyncio
async def test_send_room_update_to_player_success(
    player_room_event_handler, mock_connection_manager, mock_occupant_manager
):
    """Test send_room_update_to_player() successfully sends room update."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_room = MagicMock()
    mock_room.name = "Test Room"
    mock_room.to_dict.return_value = {"id": room_id, "name": "Test Room"}
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(
        return_value={"id": room_id, "name": "Test Room"}
    )
    mock_connection_manager.send_personal_message = AsyncMock()
    mock_occupant_manager.get_room_occupants = AsyncMock(return_value=[])
    with patch.object(player_room_event_handler.utils, "extract_occupant_names", return_value=[]):
        player_room_event_handler.message_builder.build_room_update_message = MagicMock(
            return_value={"type": "room_update"}
        )
        await player_room_event_handler.send_room_update_to_player(player_id, room_id)
        mock_connection_manager.send_personal_message.assert_awaited()


@pytest.mark.asyncio
async def test_send_room_update_to_player_no_connection_manager(player_room_event_handler, mock_logger):
    """Test send_room_update_to_player() skips when connection manager not available."""
    player_room_event_handler.connection_manager = None
    await player_room_event_handler.send_room_update_to_player(uuid.uuid4(), "room_001")
    mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_send_room_update_to_player_room_not_found(player_room_event_handler, mock_connection_manager):
    """Test send_room_update_to_player() handles room not found."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=None)
    mock_connection_manager.send_personal_message = AsyncMock()
    await player_room_event_handler.send_room_update_to_player(player_id, room_id)
    mock_connection_manager.send_personal_message.assert_not_called()


@pytest.mark.asyncio
async def test_send_room_update_to_player_error_handling(
    player_room_event_handler, mock_connection_manager, mock_logger
):
    """Test send_room_update_to_player() handles errors."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(side_effect=SQLAlchemyError("Database error"))
    await player_room_event_handler.send_room_update_to_player(player_id, room_id)
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_build_room_occupants_message(player_room_event_handler, mock_message_builder):
    """Test build_room_occupants_message() builds correct message."""
    mock_message_builder.get_next_sequence.return_value = 1
    room_id = "room_001"
    occupants_data = {"players": ["Player1"], "npcs": ["NPC1"], "occupants": ["Player1", "NPC1"], "count": 2}
    result = player_room_event_handler.build_room_occupants_message(room_id, occupants_data)
    assert result["event_type"] == "room_occupants"
    assert result["room_id"] == room_id
    assert result["data"] == occupants_data
    assert "timestamp" in result
    assert "sequence_number" in result


@pytest.mark.asyncio
async def test_query_room_occupants_snapshot(player_room_event_handler, mock_occupant_manager):
    """Test query_room_occupants_snapshot() queries occupants."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_occupants: list[dict[str, Any]] = [{"player_name": "Player1"}, {"npc_name": "NPC1"}]
    mock_occupant_manager.get_room_occupants = AsyncMock(return_value=mock_occupants)
    result = await player_room_event_handler.query_room_occupants_snapshot(player_id, room_id)
    assert result == mock_occupants
    mock_occupant_manager.get_room_occupants.assert_awaited_once_with(room_id, ensure_player_included=player_id)


@pytest.mark.asyncio
async def test_send_occupants_snapshot_to_player_success(
    player_room_event_handler, mock_connection_manager, mock_occupant_manager
):
    """Test send_occupants_snapshot_to_player() successfully sends snapshot."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_occupants = [{"player_name": "Player1"}]
    mock_occupant_manager.get_room_occupants = AsyncMock(return_value=mock_occupants)
    mock_connection_manager.send_personal_message = AsyncMock()
    with patch.object(
        player_room_event_handler.utils,
        "build_occupants_snapshot_data",
        return_value={"players": ["Player1"], "npcs": [], "occupants": ["Player1"], "count": 1},
    ):
        await player_room_event_handler.send_occupants_snapshot_to_player(player_id, room_id)
        mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_occupants_snapshot_to_player_string_id(
    player_room_event_handler, mock_connection_manager, mock_occupant_manager
):
    """Test send_occupants_snapshot_to_player() handles string player_id."""
    player_id_str = str(uuid.uuid4())
    room_id = "room_001"
    mock_occupants: list[dict[str, Any]] = []
    mock_occupant_manager.get_room_occupants = AsyncMock(return_value=mock_occupants)
    mock_connection_manager.send_personal_message = AsyncMock()
    with patch.object(
        player_room_event_handler.utils,
        "build_occupants_snapshot_data",
        return_value={"players": [], "npcs": [], "occupants": [], "count": 0},
    ):
        await player_room_event_handler.send_occupants_snapshot_to_player(player_id_str, room_id)
        mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_occupants_snapshot_to_player_no_connection_manager(player_room_event_handler, mock_logger):
    """Test send_occupants_snapshot_to_player() skips when connection manager not available."""
    player_room_event_handler.connection_manager = None
    await player_room_event_handler.send_occupants_snapshot_to_player(uuid.uuid4(), "room_001")
    mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_send_occupants_snapshot_to_player_error_handling(
    player_room_event_handler, mock_connection_manager, mock_occupant_manager, mock_logger
):
    """Test send_occupants_snapshot_to_player() handles errors."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_occupant_manager.get_room_occupants = AsyncMock(side_effect=ValueError("Error"))
    await player_room_event_handler.send_occupants_snapshot_to_player(player_id, room_id)
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_send_room_updates_to_entering_player_success(player_room_event_handler):
    """Test send_room_updates_to_entering_player() sends updates."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    room_id = "room_001"
    player_room_event_handler.send_room_update_to_player = AsyncMock()
    player_room_event_handler.send_occupants_snapshot_to_player = AsyncMock()
    with patch.object(player_room_event_handler.utils, "normalize_player_id", return_value=player_id):
        await player_room_event_handler.send_room_updates_to_entering_player(player_id, player_name, room_id)
        player_room_event_handler.send_room_update_to_player.assert_awaited_once_with(player_id, room_id)
        player_room_event_handler.send_occupants_snapshot_to_player.assert_awaited_once_with(player_id, room_id)


@pytest.mark.asyncio
async def test_send_room_updates_to_entering_player_invalid_id(player_room_event_handler, mock_logger):
    """Test send_room_updates_to_entering_player() handles invalid player_id."""
    player_id = "invalid_uuid"
    player_name = "TestPlayer"
    room_id = "room_001"
    player_room_event_handler.send_room_update_to_player = AsyncMock()
    player_room_event_handler.send_occupants_snapshot_to_player = AsyncMock()
    with patch.object(player_room_event_handler.utils, "normalize_player_id", return_value=None):
        await player_room_event_handler.send_room_updates_to_entering_player(player_id, player_name, room_id)
        # Should use string fallback
        player_room_event_handler.send_room_update_to_player.assert_awaited_once_with(player_id, room_id)
        player_room_event_handler.send_occupants_snapshot_to_player.assert_awaited_once_with(player_id, room_id)


@pytest.mark.asyncio
async def test_send_room_updates_to_entering_player_error_handling(player_room_event_handler, mock_logger):
    """Test send_room_updates_to_entering_player() handles errors."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    room_id = "room_001"
    player_room_event_handler.send_occupants_snapshot_to_player = AsyncMock(side_effect=ValueError("Error"))
    player_room_event_handler.send_room_update_to_player = AsyncMock()
    with patch.object(player_room_event_handler.utils, "normalize_player_id", return_value=player_id):
        await player_room_event_handler.send_room_updates_to_entering_player(player_id, player_name, room_id)
        mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_process_player_entered_event_success(player_room_event_handler):
    """Test _process_player_entered_event() successfully processes event."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    event = PlayerEnteredRoom(player_id=str(player_id), room_id=room_id)
    mock_player = MagicMock()
    with patch.object(
        player_room_event_handler.utils,
        "get_player_info",
        new_callable=AsyncMock,
        return_value=(mock_player, "TestPlayer"),
    ):
        with patch.object(
            player_room_event_handler.utils, "normalize_event_ids", return_value=(str(player_id), room_id)
        ):
            result = await player_room_event_handler._process_player_entered_event(event)
            assert result is not None
            player_name, exclude_player_id, room_id_str = result
            assert player_name == "TestPlayer"
            assert exclude_player_id == str(player_id)
            assert room_id_str == room_id


@pytest.mark.asyncio
async def test_process_player_entered_event_no_player_info(player_room_event_handler):
    """Test _process_player_entered_event() returns None when player not found."""
    event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    with patch.object(player_room_event_handler.utils, "get_player_info", new_callable=AsyncMock, return_value=None):
        result = await player_room_event_handler._process_player_entered_event(event)
        assert result is None


@pytest.mark.asyncio
async def test_process_player_entered_event_no_room_id(player_room_event_handler, mock_logger):
    """Test _process_player_entered_event() returns None when room_id is None."""
    player_id = uuid.uuid4()
    event = PlayerEnteredRoom(player_id=str(player_id), room_id="room_001")
    mock_player = MagicMock()
    with patch.object(
        player_room_event_handler.utils,
        "get_player_info",
        new_callable=AsyncMock,
        return_value=(mock_player, "TestPlayer"),
    ):
        with patch.object(player_room_event_handler.utils, "normalize_event_ids", return_value=(str(player_id), None)):
            result = await player_room_event_handler._process_player_entered_event(event)
            assert result is None
            mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_entered_success(
    player_room_event_handler, mock_connection_manager, mock_room_sync_service
):
    """Test handle_player_entered() successfully handles event."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    event = PlayerEnteredRoom(player_id=str(player_id), room_id=room_id)
    processed_event = PlayerEnteredRoom(player_id=str(player_id), room_id=room_id)
    mock_room_sync_service.process_event_with_ordering.return_value = processed_event
    mock_player = MagicMock()
    player_room_event_handler.log_player_movement = AsyncMock()
    player_room_event_handler.message_builder.create_player_entered_message = MagicMock(
        return_value={"type": "player_entered"}
    )
    player_room_event_handler.broadcast_player_entered_message = AsyncMock()
    player_room_event_handler.subscribe_player_to_room = AsyncMock()
    player_room_event_handler.send_room_updates_to_entering_player = AsyncMock()
    send_occupants_update = AsyncMock()
    with patch.object(
        player_room_event_handler.utils,
        "get_player_info",
        new_callable=AsyncMock,
        return_value=(mock_player, "TestPlayer"),
    ):
        with patch.object(
            player_room_event_handler.utils, "normalize_event_ids", return_value=(str(player_id), room_id)
        ):
            await player_room_event_handler.handle_player_entered(event, send_occupants_update)
            player_room_event_handler.broadcast_player_entered_message.assert_awaited_once()
            player_room_event_handler.subscribe_player_to_room.assert_awaited_once()
            player_room_event_handler.send_room_updates_to_entering_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_entered_no_connection_manager(player_room_event_handler, mock_logger):
    """Test handle_player_entered() skips when connection manager not available."""
    player_room_event_handler.connection_manager = None
    event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    await player_room_event_handler.handle_player_entered(event, None)
    mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_entered_no_player_info(
    player_room_event_handler, mock_connection_manager, mock_room_sync_service
):
    """Test handle_player_entered() handles player not found."""
    event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    processed_event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    mock_room_sync_service.process_event_with_ordering.return_value = processed_event
    player_room_event_handler.broadcast_player_entered_message = AsyncMock()
    with patch.object(player_room_event_handler.utils, "get_player_info", new_callable=AsyncMock, return_value=None):
        await player_room_event_handler.handle_player_entered(event, None)
        player_room_event_handler.broadcast_player_entered_message.assert_not_called()


@pytest.mark.asyncio
async def test_handle_player_entered_error_handling(
    player_room_event_handler, mock_connection_manager, mock_room_sync_service, mock_logger
):
    """Test handle_player_entered() handles errors."""
    event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room_001")
    mock_room_sync_service.process_event_with_ordering.side_effect = ValueError("Error")
    await player_room_event_handler.handle_player_entered(event, None)
    mock_logger.error.assert_called_once()


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
async def test_handle_player_left_success(player_room_event_handler, mock_connection_manager, mock_room_sync_service):
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
async def test_handle_player_left_no_player_info(
    player_room_event_handler, mock_connection_manager, mock_room_sync_service
):
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
async def test_handle_player_left_disconnecting(
    player_room_event_handler, mock_connection_manager, mock_room_sync_service
):
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
async def test_handle_player_left_error_handling(
    player_room_event_handler, mock_connection_manager, mock_room_sync_service, mock_logger
):
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


def test_log_occupants_info_no_npcs(player_room_event_handler, mock_logger):
    """Test _log_occupants_info() logs warning when no NPCs."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    occupants_snapshot = [{"player_name": "Player1"}]
    occupants_data = {"players": ["Player1"], "npcs": [], "occupants": ["Player1"], "count": 1}
    with patch.object(player_room_event_handler.utils, "count_occupants_by_type", return_value=(0, 1)):
        player_room_event_handler._log_occupants_info(player_id, room_id, occupants_snapshot, occupants_data)
        mock_logger.warning.assert_called_once()
