"""
Unit tests for player state event handlers.

Tests the PlayerStateEventHandler class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.events.event_types import PlayerDPUpdated
from server.realtime.player_event_handlers_state import PlayerStateEventHandler
from server.realtime.player_event_handlers_utils import PlayerEventHandlerUtils
from server.services.player_combat_service import PlayerXPAwardEvent


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
def player_state_event_handler(mock_connection_manager, mock_utils, mock_logger):
    """Create a PlayerStateEventHandler instance."""
    return PlayerStateEventHandler(mock_connection_manager, mock_utils, mock_logger)


def test_player_state_event_handler_init(player_state_event_handler, mock_connection_manager, mock_utils, mock_logger):
    """Test PlayerStateEventHandler initialization."""
    assert player_state_event_handler.connection_manager == mock_connection_manager
    assert player_state_event_handler.utils == mock_utils
    assert player_state_event_handler._logger == mock_logger


@pytest.mark.asyncio
async def test_handle_player_xp_awarded_success(player_state_event_handler, mock_connection_manager):
    """Test handle_player_xp_awarded() successfully sends XP update."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_player.experience_points = 1000
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_connection_manager.send_personal_message = AsyncMock()
    event = PlayerXPAwardEvent(player_id=player_id, xp_amount=100, new_level=5)
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_xp_updated"}
        await player_state_event_handler.handle_player_xp_awarded(event)
        mock_connection_manager.get_player.assert_awaited_once_with(player_id)
        mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_xp_awarded_no_connection_manager(player_state_event_handler, mock_logger):
    """Test handle_player_xp_awarded() skips when connection manager not available."""
    player_state_event_handler.connection_manager = None
    event = PlayerXPAwardEvent(player_id=uuid.uuid4(), xp_amount=100, new_level=5)
    await player_state_event_handler.handle_player_xp_awarded(event)
    mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_xp_awarded_player_not_found(player_state_event_handler, mock_connection_manager, mock_logger):
    """Test handle_player_xp_awarded() handles player not found."""
    player_id = uuid.uuid4()
    mock_connection_manager.get_player = AsyncMock(return_value=None)
    event = PlayerXPAwardEvent(player_id=player_id, xp_amount=100, new_level=5)
    await player_state_event_handler.handle_player_xp_awarded(event)
    mock_logger.warning.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_xp_awarded_error_handling(player_state_event_handler, mock_connection_manager, mock_logger):
    """Test handle_player_xp_awarded() handles errors."""
    player_id = uuid.uuid4()
    mock_connection_manager.get_player = AsyncMock(side_effect=ValueError("Database error"))
    event = PlayerXPAwardEvent(player_id=player_id, xp_amount=100, new_level=5)
    await player_state_event_handler.handle_player_xp_awarded(event)
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_xp_awarded_player_no_current_room_id(player_state_event_handler, mock_connection_manager):
    """Test handle_player_xp_awarded() handles player without current_room_id."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_player.experience_points = 1000
    del mock_player.current_room_id  # Remove attribute
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_connection_manager.send_personal_message = AsyncMock()
    event = PlayerXPAwardEvent(player_id=player_id, xp_amount=100, new_level=5)
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_xp_updated"}
        await player_state_event_handler.handle_player_xp_awarded(event)
        mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_dp_updated_success(player_state_event_handler, mock_connection_manager):
    """Test handle_player_dp_updated() successfully sends DP update."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.get_stats.return_value = {"current_dp": 50, "position": "standing"}
    mock_player.current_room_id = "room_001"
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_connection_manager.send_personal_message = AsyncMock()
    event = PlayerDPUpdated(player_id=player_id, old_dp=60, new_dp=50, max_dp=100)
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_dp_updated"}
        await player_state_event_handler.handle_player_dp_updated(event)
        mock_connection_manager.get_player.assert_awaited_once_with(player_id)
        mock_connection_manager.send_personal_message.assert_awaited_once_with(player_id, mock_build_event.return_value)


@pytest.mark.asyncio
async def test_handle_player_dp_updated_no_connection_manager(player_state_event_handler, mock_logger):
    """Test handle_player_dp_updated() skips when connection manager not available."""
    player_state_event_handler.connection_manager = None
    event = PlayerDPUpdated(player_id=uuid.uuid4(), old_dp=60, new_dp=50, max_dp=100)
    await player_state_event_handler.handle_player_dp_updated(event)
    mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_dp_updated_player_not_found(player_state_event_handler, mock_connection_manager):
    """Test handle_player_dp_updated() handles player not found."""
    player_id = uuid.uuid4()
    mock_connection_manager.get_player = AsyncMock(return_value=None)
    mock_connection_manager.send_personal_message = AsyncMock()
    event = PlayerDPUpdated(player_id=player_id, old_dp=60, new_dp=50, max_dp=100)
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_dp_updated"}
        await player_state_event_handler.handle_player_dp_updated(event)
        # Should still send message with event data
        mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_dp_updated_player_no_get_stats(player_state_event_handler, mock_connection_manager):
    """Test handle_player_dp_updated() handles player without get_stats method."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    del mock_player.get_stats  # Remove get_stats method
    mock_player.current_room_id = "room_001"
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_connection_manager.send_personal_message = AsyncMock()
    event = PlayerDPUpdated(player_id=player_id, old_dp=60, new_dp=50, max_dp=100)
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_dp_updated"}
        await player_state_event_handler.handle_player_dp_updated(event)
        mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_dp_updated_error_handling(player_state_event_handler, mock_connection_manager, mock_logger):
    """Test handle_player_dp_updated() handles errors."""
    player_id = uuid.uuid4()
    mock_connection_manager.get_player = AsyncMock(side_effect=SQLAlchemyError("Database error"))
    event = PlayerDPUpdated(player_id=player_id, old_dp=60, new_dp=50, max_dp=100)
    await player_state_event_handler.handle_player_dp_updated(event)
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_died_success(player_state_event_handler, mock_connection_manager):
    """Test handle_player_died() successfully sends death notification."""
    player_id = uuid.uuid4()
    mock_connection_manager.send_personal_message = AsyncMock(return_value=True)
    event = MagicMock()
    event.player_id = player_id
    event.player_name = "TestPlayer"
    event.death_location = "room_001"
    event.room_id = "room_001"
    event.killer_id = None
    event.killer_name = None
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_died"}
        await player_state_event_handler.handle_player_died(event)
        mock_connection_manager.send_personal_message.assert_awaited_once()
        mock_logger = player_state_event_handler._logger
        mock_logger.info.assert_called()


@pytest.mark.asyncio
async def test_handle_player_died_no_connection_manager(player_state_event_handler, mock_logger):
    """Test handle_player_died() skips when connection manager not available."""
    player_state_event_handler.connection_manager = None
    event = MagicMock()
    event.player_id = uuid.uuid4()
    await player_state_event_handler.handle_player_died(event)
    mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_died_no_death_location(player_state_event_handler, mock_connection_manager):
    """Test handle_player_died() uses room_id when death_location not available."""
    player_id = uuid.uuid4()
    mock_connection_manager.send_personal_message = AsyncMock(return_value=True)
    event = MagicMock()
    event.player_id = player_id
    event.player_name = "TestPlayer"
    event.death_location = None
    event.room_id = "room_001"
    event.killer_id = None
    event.killer_name = None
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_died"}
        await player_state_event_handler.handle_player_died(event)
        # Should use room_id as fallback
        call_args = mock_build_event.call_args
        assert call_args[0][1]["death_location"] == "room_001"


@pytest.mark.asyncio
async def test_handle_player_died_invalid_player_id(player_state_event_handler, mock_connection_manager, mock_logger):
    """Test handle_player_died() handles invalid player_id format."""
    mock_connection_manager.send_personal_message = AsyncMock(side_effect=ValueError("Invalid UUID"))
    event = MagicMock()
    event.player_id = "invalid_uuid"
    event.player_name = "TestPlayer"
    event.death_location = "room_001"
    event.room_id = "room_001"
    event.killer_id = None
    event.killer_name = None
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_died"}
        await player_state_event_handler.handle_player_died(event)
        mock_logger.error.assert_called()


@pytest.mark.asyncio
async def test_handle_player_died_error_handling(player_state_event_handler, mock_connection_manager, mock_logger):
    """Test handle_player_died() handles errors."""
    event = MagicMock()
    event.player_id = uuid.uuid4()
    del event.player_name  # Cause AttributeError
    await player_state_event_handler.handle_player_died(event)
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_dp_decay_success(player_state_event_handler, mock_connection_manager):
    """Test handle_player_dp_decay() successfully sends decay notification."""
    player_id = uuid.uuid4()
    mock_connection_manager.send_personal_message = AsyncMock()
    event = MagicMock()
    event.player_id = player_id
    event.old_dp = 60
    event.new_dp = 50
    event.decay_amount = 10
    event.room_id = "room_001"
    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "player_dp_decay"}
        await player_state_event_handler.handle_player_dp_decay(event)
        mock_connection_manager.send_personal_message.assert_awaited_once_with(
            str(player_id), mock_build_event.return_value
        )


@pytest.mark.asyncio
async def test_handle_player_dp_decay_no_connection_manager(player_state_event_handler, mock_logger):
    """Test handle_player_dp_decay() skips when connection manager not available."""
    player_state_event_handler.connection_manager = None
    event = MagicMock()
    event.player_id = uuid.uuid4()
    await player_state_event_handler.handle_player_dp_decay(event)
    mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_dp_decay_error_handling(player_state_event_handler, mock_connection_manager, mock_logger):
    """Test handle_player_dp_decay() handles errors."""
    event = MagicMock()
    event.player_id = uuid.uuid4()
    del event.old_dp  # Cause AttributeError
    await player_state_event_handler.handle_player_dp_decay(event)
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_dp_decay_no_player_id_attr(player_state_event_handler, mock_connection_manager, mock_logger):
    """Test handle_player_dp_decay() handles missing player_id attribute."""
    event = MagicMock()
    del event.player_id  # Remove player_id attribute
    await player_state_event_handler.handle_player_dp_decay(event)
    mock_logger.error.assert_called_once()
