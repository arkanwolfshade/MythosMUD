"""
Unit tests for player respawn event handlers.

Tests the PlayerRespawnEventHandler class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.realtime.player_event_handlers_respawn import PlayerRespawnEventHandler
from server.realtime.player_event_handlers_utils import PlayerEventHandlerUtils


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
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
def player_respawn_event_handler(mock_connection_manager, mock_utils, mock_logger):
    """Create a PlayerRespawnEventHandler instance."""
    return PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)


def test_player_respawn_event_handler_init(
    player_respawn_event_handler, mock_connection_manager, mock_utils, mock_logger
):
    """Test PlayerRespawnEventHandler initialization."""
    assert player_respawn_event_handler.connection_manager == mock_connection_manager
    assert player_respawn_event_handler.utils == mock_utils
    assert player_respawn_event_handler._logger == mock_logger


def test_update_connection_manager_position_success(player_respawn_event_handler, mock_connection_manager, mock_logger):
    """Test update_connection_manager_position() updates position."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    mock_connection_manager.online_players = {player_id: {"position": "lying"}}
    player_respawn_event_handler.update_connection_manager_position(player_id_str, "standing")
    assert mock_connection_manager.online_players[player_id]["position"] == "standing"
    mock_logger.debug.assert_called_once()


def test_update_connection_manager_position_player_not_online(player_respawn_event_handler, mock_connection_manager):
    """Test update_connection_manager_position() handles player not in online_players."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    mock_connection_manager.online_players = {}
    # Should not raise
    player_respawn_event_handler.update_connection_manager_position(player_id_str, "standing")


def test_update_connection_manager_position_no_online_players_attr(
    player_respawn_event_handler, mock_connection_manager
):
    """Test update_connection_manager_position() handles missing online_players attribute."""
    player_id_str = str(uuid.uuid4())
    del mock_connection_manager.online_players
    # Should not raise
    player_respawn_event_handler.update_connection_manager_position(player_id_str, "standing")


@pytest.mark.asyncio
async def test_get_player_data_for_respawn_success(player_respawn_event_handler, mock_connection_manager):
    """Test get_player_data_for_respawn() successfully retrieves player data."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_player.experience_points = 1000
    mock_player.get_stats.return_value = {"current_dp": 100, "position": "standing", "strength": 12}
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_connection_manager.online_players = {player_id: {}}
    result, position = await player_respawn_event_handler.get_player_data_for_respawn(player_id_str)
    assert result is not None
    assert result["name"] == "TestPlayer"
    assert result["position"] == "standing"
    assert position == "standing"
    assert mock_connection_manager.online_players[player_id]["position"] == "standing"


@pytest.mark.asyncio
async def test_get_player_data_for_respawn_no_connection_manager(player_respawn_event_handler):
    """Test get_player_data_for_respawn() returns None when connection manager not available."""
    player_respawn_event_handler.connection_manager = None
    result, position = await player_respawn_event_handler.get_player_data_for_respawn(str(uuid.uuid4()))
    assert result is None
    assert position == "standing"


@pytest.mark.asyncio
async def test_get_player_data_for_respawn_no_persistence(player_respawn_event_handler, mock_connection_manager):
    """Test get_player_data_for_respawn() returns None when persistence not available."""
    mock_connection_manager.async_persistence = None
    result, position = await player_respawn_event_handler.get_player_data_for_respawn(str(uuid.uuid4()))
    assert result is None
    assert position == "standing"


@pytest.mark.asyncio
async def test_get_player_data_for_respawn_player_not_found(player_respawn_event_handler, mock_connection_manager):
    """Test get_player_data_for_respawn() returns None when player not found."""
    player_id_str = str(uuid.uuid4())
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_player_by_id = AsyncMock(return_value=None)
    result, position = await player_respawn_event_handler.get_player_data_for_respawn(player_id_str)
    assert result is None
    assert position == "standing"


@pytest.mark.asyncio
async def test_get_player_data_for_respawn_error_handling(
    player_respawn_event_handler, mock_connection_manager, mock_logger
):
    """Test get_player_data_for_respawn() handles errors."""
    player_id_str = str(uuid.uuid4())
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_player_by_id = AsyncMock(
        side_effect=SQLAlchemyError("Database error")
    )
    result, position = await player_respawn_event_handler.get_player_data_for_respawn(player_id_str)
    assert result is None
    assert position == "standing"
    mock_logger.warning.assert_called_once()


@pytest.mark.asyncio
async def test_send_respawn_event_with_retry_success(player_respawn_event_handler, mock_connection_manager):
    """Test send_respawn_event_with_retry() successfully sends event."""
    player_id = uuid.uuid4()
    respawn_event = {"type": "player_respawned"}
    mock_connection_manager.player_websockets = {player_id: MagicMock()}
    mock_connection_manager.send_personal_message = AsyncMock(
        return_value={"websocket_delivered": 1, "active_connections": 1}
    )
    await player_respawn_event_handler.send_respawn_event_with_retry(player_id, respawn_event)
    mock_connection_manager.send_personal_message.assert_awaited_once_with(player_id, respawn_event)


@pytest.mark.asyncio
async def test_send_respawn_event_with_retry_waits_for_connection(
    player_respawn_event_handler, mock_connection_manager
):
    """Test send_respawn_event_with_retry() waits for connection to become available."""
    player_id = uuid.uuid4()
    respawn_event = {"type": "player_respawned"}
    # Start with no connection, then add it
    mock_connection_manager.player_websockets = {}
    mock_connection_manager.send_personal_message = AsyncMock(
        return_value={"websocket_delivered": 1, "active_connections": 1}
    )

    async def add_connection_after_delay():
        await asyncio.sleep(0.1)
        mock_connection_manager.player_websockets[player_id] = MagicMock()

    import asyncio

    asyncio.create_task(add_connection_after_delay())
    await player_respawn_event_handler.send_respawn_event_with_retry(player_id, respawn_event, max_wait_time=1.0)
    mock_connection_manager.send_personal_message.assert_awaited()


@pytest.mark.asyncio
async def test_send_respawn_event_with_retry_timeout(player_respawn_event_handler, mock_connection_manager):
    """Test send_respawn_event_with_retry() times out when connection never available."""
    player_id = uuid.uuid4()
    respawn_event = {"type": "player_respawned"}
    mock_connection_manager.player_websockets = {}
    mock_connection_manager.send_personal_message = AsyncMock()
    await player_respawn_event_handler.send_respawn_event_with_retry(player_id, respawn_event, max_wait_time=0.1)
    # Should not send message if connection never available
    mock_connection_manager.send_personal_message.assert_not_called()


@pytest.mark.asyncio
async def test_handle_player_respawned_success(player_respawn_event_handler, mock_connection_manager):
    """Test handle_player_respawned() successfully handles event."""
    player_id = uuid.uuid4()
    event = MagicMock()
    event.player_id = player_id
    event.player_name = "TestPlayer"
    event.respawn_room_id = "room_001"
    event.old_dp = 0
    event.new_dp = 100
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_player.experience_points = 1000
    mock_player.get_stats.return_value = {"current_dp": 100, "position": "standing"}
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_connection_manager.online_players = {player_id: {}}
    mock_connection_manager.player_websockets = {player_id: MagicMock()}
    mock_connection_manager.send_personal_message = AsyncMock(
        return_value={"websocket_delivered": 1, "active_connections": 1}
    )
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_respawned"}
        await player_respawn_event_handler.handle_player_respawned(event)
        mock_connection_manager.send_personal_message.assert_awaited()


@pytest.mark.asyncio
async def test_handle_player_respawned_error_handling(
    player_respawn_event_handler, mock_connection_manager, mock_logger
):
    """Test handle_player_respawned() handles errors."""
    event = MagicMock()
    event.player_id = uuid.uuid4()
    del event.player_name  # Cause AttributeError
    await player_respawn_event_handler.handle_player_respawned(event)
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_get_current_lucidity_found(player_respawn_event_handler):
    """Test get_current_lucidity() returns lucidity from database."""
    player_id = uuid.uuid4()
    mock_lucidity_record = MagicMock()
    mock_lucidity_record.current_lcd = 75
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=mock_lucidity_record)

    async def async_gen():
        yield mock_session

    with patch("server.database.get_async_session", return_value=async_gen()):
        result = await player_respawn_event_handler.get_current_lucidity(player_id, 100)
        assert result == 75


@pytest.mark.asyncio
async def test_get_current_lucidity_not_found(player_respawn_event_handler):
    """Test get_current_lucidity() returns default when record not found."""
    player_id = uuid.uuid4()
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=None)

    async def async_gen():
        yield mock_session

    with patch("server.database.get_async_session", return_value=async_gen()):
        result = await player_respawn_event_handler.get_current_lucidity(player_id, 100)
        assert result == 100


@pytest.mark.asyncio
async def test_get_player_data_for_delirium_respawn_success(player_respawn_event_handler, mock_connection_manager):
    """Test get_player_data_for_delirium_respawn() successfully retrieves player data."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_player.experience_points = 1000
    mock_player.get_stats.return_value = {"current_dp": 100, "position": "standing"}
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_connection_manager.online_players = {player_id: {}}
    mock_session = MagicMock()
    mock_lucidity_record = MagicMock()
    mock_lucidity_record.current_lcd = 80
    mock_session.get = AsyncMock(return_value=mock_lucidity_record)

    async def async_gen():
        yield mock_session

    with patch("server.database.get_async_session", return_value=async_gen()):
        result, position = await player_respawn_event_handler.get_player_data_for_delirium_respawn(player_id_str, 75)
        assert result is not None
        assert result["stats"]["lucidity"] == 80  # Should use value from database, not default
        assert position == "standing"


@pytest.mark.asyncio
async def test_get_player_data_for_delirium_respawn_no_connection_manager(player_respawn_event_handler):
    """Test get_player_data_for_delirium_respawn() returns None when connection manager not available."""
    player_respawn_event_handler.connection_manager = None
    result, position = await player_respawn_event_handler.get_player_data_for_delirium_respawn(str(uuid.uuid4()), 100)
    assert result is None
    assert position == "standing"


@pytest.mark.asyncio
async def test_get_player_data_for_delirium_respawn_player_not_found(
    player_respawn_event_handler, mock_connection_manager
):
    """Test get_player_data_for_delirium_respawn() returns None when player not found."""
    player_id_str = str(uuid.uuid4())
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_player_by_id = AsyncMock(return_value=None)
    result, position = await player_respawn_event_handler.get_player_data_for_delirium_respawn(player_id_str, 100)
    assert result is None
    assert position == "standing"


@pytest.mark.asyncio
async def test_get_player_data_for_delirium_respawn_error_handling(
    player_respawn_event_handler, mock_connection_manager, mock_logger
):
    """Test get_player_data_for_delirium_respawn() handles errors."""
    player_id_str = str(uuid.uuid4())
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_player_by_id = AsyncMock(side_effect=ValueError("Error"))
    result, position = await player_respawn_event_handler.get_player_data_for_delirium_respawn(player_id_str, 100)
    assert result is None
    assert position == "standing"
    mock_logger.warning.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_delirium_respawned_success(player_respawn_event_handler, mock_connection_manager):
    """Test handle_player_delirium_respawned() successfully handles event."""
    player_id = uuid.uuid4()
    event = MagicMock()
    event.player_id = player_id
    event.player_name = "TestPlayer"
    event.respawn_room_id = "room_001"
    event.old_lucidity = 0
    event.new_lucidity = 100
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_player.experience_points = 1000
    mock_player.get_stats.return_value = {"current_dp": 100, "position": "standing"}
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_connection_manager.online_players = {player_id: {}}
    mock_connection_manager.player_websockets = {player_id: MagicMock()}
    mock_connection_manager.send_personal_message = AsyncMock(
        return_value={"websocket_delivered": 1, "active_connections": 1}
    )
    mock_session = MagicMock()
    mock_lucidity_record = MagicMock()
    mock_lucidity_record.current_lcd = 100
    mock_session.get = AsyncMock(return_value=mock_lucidity_record)

    async def async_gen():
        yield mock_session

    with patch("server.realtime.envelope.build_event") as mock_build_event:
        with patch("server.database.get_async_session", return_value=async_gen()):
            mock_build_event.return_value = {"type": "player_delirium_respawned"}
            await player_respawn_event_handler.handle_player_delirium_respawned(event)
            mock_connection_manager.send_personal_message.assert_awaited()


@pytest.mark.asyncio
async def test_handle_player_delirium_respawned_error_handling(
    player_respawn_event_handler, mock_connection_manager, mock_logger
):
    """Test handle_player_delirium_respawned() handles errors."""
    event = MagicMock()
    event.player_id = uuid.uuid4()
    del event.player_name  # Cause AttributeError
    await player_respawn_event_handler.handle_player_delirium_respawned(event)
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_get_player_data_for_respawn_no_get_stats(
    player_respawn_event_handler, mock_connection_manager, mock_logger
):
    """Test get_player_data_for_respawn() handles player without get_stats method."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_player.experience_points = 1000
    del mock_player.get_stats  # Remove get_stats method
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_connection_manager.online_players = {player_id: {}}
    # Should handle gracefully - AttributeError is caught and returns None
    result, position = await player_respawn_event_handler.get_player_data_for_respawn(player_id_str)
    assert result is None
    assert position == "standing"
    mock_logger.warning.assert_called_once()
