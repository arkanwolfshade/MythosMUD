"""
Tests for player state event handlers.

This module tests the PlayerStateEventHandler class which handles
player state updates (XP, DP, death, decay).
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.events.event_types import PlayerDiedEvent, PlayerDPDecayEvent, PlayerDPUpdated
from server.realtime.player_event_handlers_state import PlayerStateEventHandler
from server.services.player_combat_service import PlayerXPAwardEvent


class TestPlayerStateEventHandler:
    """Test PlayerStateEventHandler class."""

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock ConnectionManager."""
        manager = MagicMock()
        manager.get_player = AsyncMock()
        manager.send_personal_message = AsyncMock(return_value=True)
        return manager

    @pytest.fixture
    def mock_utils(self):
        """Create a mock PlayerEventHandlerUtils."""
        return MagicMock()

    @pytest.fixture
    def mock_logger(self):
        """Create a mock logger."""
        return MagicMock()

    @pytest.fixture
    def handler(self, mock_connection_manager, mock_utils, mock_logger):
        """Create a PlayerStateEventHandler instance."""
        return PlayerStateEventHandler(mock_connection_manager, mock_utils, mock_logger)

    @pytest.fixture
    def mock_player(self):
        """Create a mock player."""
        player = MagicMock()
        player.player_id = uuid4()
        player.name = "TestPlayer"
        player.level = 5
        player.experience_points = 1000
        player.current_room_id = "room_123"
        player.get_stats = MagicMock(return_value={"position": "standing", "dp": 50, "max_dp": 100})
        return player

    @pytest.mark.asyncio
    async def test_init(self, mock_connection_manager, mock_utils, mock_logger):
        """Test PlayerStateEventHandler initialization."""
        handler = PlayerStateEventHandler(mock_connection_manager, mock_utils, mock_logger)
        assert handler.connection_manager == mock_connection_manager
        assert handler.utils == mock_utils
        assert handler._logger == mock_logger

    @pytest.mark.asyncio
    async def test_handle_player_xp_awarded_success(self, handler, mock_connection_manager, mock_player):
        """Test handling player XP award event successfully."""
        player_id = uuid4()
        event = PlayerXPAwardEvent(player_id=player_id, xp_amount=100, new_level=6)
        mock_connection_manager.get_player.return_value = mock_player
        mock_player.player_id = player_id

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"type": "player_xp_updated", "data": {}}

            await handler.handle_player_xp_awarded(event)

            mock_connection_manager.get_player.assert_called_once_with(player_id)
            mock_connection_manager.send_personal_message.assert_called_once()
            handler._logger.info.assert_called()

    @pytest.mark.asyncio
    async def test_handle_player_xp_awarded_no_connection_manager(self, mock_utils, mock_logger):
        """Test handling player XP award when connection manager is None."""
        handler = PlayerStateEventHandler(None, mock_utils, mock_logger)
        player_id = uuid4()
        event = PlayerXPAwardEvent(player_id=player_id, xp_amount=100, new_level=6)

        await handler.handle_player_xp_awarded(event)

        handler._logger.debug.assert_called_once()
        mock_utils.get_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_player_xp_awarded_player_not_found(self, handler, mock_connection_manager):
        """Test handling player XP award when player is not found."""
        player_id = uuid4()
        event = PlayerXPAwardEvent(player_id=player_id, xp_amount=100, new_level=6)
        mock_connection_manager.get_player.return_value = None

        await handler.handle_player_xp_awarded(event)

        handler._logger.warning.assert_called_once()
        mock_connection_manager.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_player_xp_awarded_exception(self, handler, mock_connection_manager):
        """Test handling player XP award when exception occurs."""
        player_id = uuid4()
        event = PlayerXPAwardEvent(player_id=player_id, xp_amount=100, new_level=6)
        mock_connection_manager.get_player.side_effect = ValueError("Test error")

        await handler.handle_player_xp_awarded(event)

        handler._logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_dp_updated_success(self, handler, mock_connection_manager, mock_player):
        """Test handling player DP update event successfully."""
        player_id = uuid4()
        event = PlayerDPUpdated(
            player_id=player_id, old_dp=100, new_dp=80, max_dp=100, damage_taken=20, room_id="room_123"
        )
        mock_connection_manager.get_player.return_value = mock_player
        mock_player.player_id = player_id

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"type": "player_dp_updated", "data": {}}

            await handler.handle_player_dp_updated(event)

            mock_connection_manager.get_player.assert_called_once_with(player_id)
            mock_connection_manager.send_personal_message.assert_called_once()
            handler._logger.info.assert_called()

    @pytest.mark.asyncio
    async def test_handle_player_dp_updated_no_connection_manager(self, mock_utils, mock_logger):
        """Test handling player DP update when connection manager is None."""
        handler = PlayerStateEventHandler(None, mock_utils, mock_logger)
        player_id = uuid4()
        event = PlayerDPUpdated(player_id=player_id, old_dp=100, new_dp=80, max_dp=100)

        await handler.handle_player_dp_updated(event)

        handler._logger.debug.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_dp_updated_player_not_found(self, handler, mock_connection_manager):
        """Test handling player DP update when player is not found."""
        player_id = uuid4()
        event = PlayerDPUpdated(player_id=player_id, old_dp=100, new_dp=80, max_dp=100)
        mock_connection_manager.get_player.return_value = None

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"type": "player_dp_updated", "data": {}}

            await handler.handle_player_dp_updated(event)

            handler._logger.debug.assert_called()
            mock_connection_manager.send_personal_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_dp_updated_player_no_get_stats(self, handler, mock_connection_manager, mock_player):
        """Test handling player DP update when player has no get_stats method."""
        player_id = uuid4()
        event = PlayerDPUpdated(player_id=player_id, old_dp=100, new_dp=80, max_dp=100)
        mock_connection_manager.get_player.return_value = mock_player
        del mock_player.get_stats

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"type": "player_dp_updated", "data": {}}

            await handler.handle_player_dp_updated(event)

            mock_connection_manager.send_personal_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_dp_updated_exception(self, handler, mock_connection_manager):
        """Test handling player DP update when exception occurs."""
        player_id = uuid4()
        event = PlayerDPUpdated(player_id=player_id, old_dp=100, new_dp=80, max_dp=100)
        mock_connection_manager.get_player.side_effect = SQLAlchemyError("Test error")

        await handler.handle_player_dp_updated(event)

        handler._logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_died_success(self, handler, mock_connection_manager):
        """Test handling player death event successfully."""
        player_id = uuid4()
        event = PlayerDiedEvent(
            player_id=player_id,
            player_name="TestPlayer",
            room_id="room_123",
            killer_id="killer_123",
            killer_name="Killer",
            death_location="room_123",
        )

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"type": "player_died", "data": {}}

            await handler.handle_player_died(event)

            mock_connection_manager.send_personal_message.assert_called_once()
            handler._logger.info.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_died_no_death_location(self, handler, mock_connection_manager):
        """Test handling player death event without death_location (uses room_id)."""
        player_id = uuid4()
        event = PlayerDiedEvent(player_id=player_id, player_name="TestPlayer", room_id="room_123", death_location=None)

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"type": "player_died", "data": {}}

            await handler.handle_player_died(event)

            # Verify build_event was called with room_id as death_location
            call_args = mock_build_event.call_args
            # build_event is called with (event_type, data_dict, player_id=...)
            # call_args[0] is positional args tuple, call_args[1] is keyword args dict
            data_dict = call_args[0][1]
            assert data_dict["death_location"] == "room_123"
            mock_connection_manager.send_personal_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_died_no_connection_manager(self, mock_utils, mock_logger):
        """Test handling player death when connection manager is None."""
        handler = PlayerStateEventHandler(None, mock_utils, mock_logger)
        player_id = uuid4()
        event = PlayerDiedEvent(player_id=player_id, player_name="TestPlayer", room_id="room_123")

        await handler.handle_player_died(event)

        handler._logger.debug.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_died_invalid_uuid(self, handler, mock_connection_manager):
        """Test handling player death with invalid UUID conversion."""
        player_id = uuid4()
        event = PlayerDiedEvent(player_id=player_id, player_name="TestPlayer", room_id="room_123")

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"type": "player_died", "data": {}}
            mock_connection_manager.send_personal_message.side_effect = ValueError("Invalid UUID")

            await handler.handle_player_died(event)

            handler._logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_died_exception(self, handler, mock_connection_manager):
        """Test handling player death when exception occurs."""
        player_id = uuid4()
        event = PlayerDiedEvent(player_id=player_id, player_name="TestPlayer", room_id="room_123")
        # Simulate exception in build_event
        with patch("server.realtime.envelope.build_event", side_effect=ImportError("Test error")):
            await handler.handle_player_died(event)

            handler._logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_dp_decay_success(self, handler, mock_connection_manager):
        """Test handling player DP decay event successfully."""
        player_id = uuid4()
        event = PlayerDPDecayEvent(player_id=player_id, old_dp=0, new_dp=-1, decay_amount=1, room_id="room_123")

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"type": "player_dp_decay", "data": {}}

            await handler.handle_player_dp_decay(event)

            mock_connection_manager.send_personal_message.assert_called_once()
            handler._logger.debug.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_dp_decay_no_connection_manager(self, mock_utils, mock_logger):
        """Test handling player DP decay when connection manager is None."""
        handler = PlayerStateEventHandler(None, mock_utils, mock_logger)
        player_id = uuid4()
        event = PlayerDPDecayEvent(player_id=player_id, old_dp=0, new_dp=-1, decay_amount=1)

        await handler.handle_player_dp_decay(event)

        handler._logger.debug.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_dp_decay_exception(self, handler, mock_connection_manager):
        """Test handling player DP decay when exception occurs."""
        player_id = uuid4()
        event = PlayerDPDecayEvent(player_id=player_id, old_dp=0, new_dp=-1, decay_amount=1)
        # Simulate exception in build_event
        with patch("server.realtime.envelope.build_event", side_effect=TypeError("Test error")):
            await handler.handle_player_dp_decay(event)

            handler._logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_xp_awarded_no_current_room_id(self, handler, mock_connection_manager, mock_player):
        """Test handling player XP award when player has no current_room_id."""
        player_id = uuid4()
        event = PlayerXPAwardEvent(player_id=player_id, xp_amount=100, new_level=6)
        mock_connection_manager.get_player.return_value = mock_player
        mock_player.player_id = player_id
        del mock_player.current_room_id

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"type": "player_xp_updated", "data": {}}

            await handler.handle_player_xp_awarded(event)

            # Verify build_event was called with None for current_room_id
            call_args = mock_build_event.call_args
            # build_event is called with (event_type, data_dict, player_id=...)
            # call_args[0] is positional args tuple, call_args[1] is keyword args dict
            data_dict = call_args[0][1]
            assert data_dict["player"]["current_room_id"] is None
            mock_connection_manager.send_personal_message.assert_called_once()
