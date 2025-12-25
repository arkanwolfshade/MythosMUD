"""
Tests for event handlers.

This module tests the EventHandler class and its methods for handling
NATS event messages and broadcasting them to WebSocket clients.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.realtime.event_handlers import EventHandler
from server.services.nats_exceptions import NATSError


class TestEventHandlerInit:
    """Test EventHandler initialization."""

    def test_event_handler_init(self) -> None:
        """Test EventHandler initialization."""
        mock_connection_manager = MagicMock()

        handler = EventHandler(mock_connection_manager)

        assert handler.connection_manager == mock_connection_manager


class TestGetEventHandlerMap:
    """Test get_event_handler_map method."""

    def test_get_event_handler_map(self) -> None:
        """Test getting event handler map."""
        mock_connection_manager = MagicMock()
        handler = EventHandler(mock_connection_manager)

        handler_map = handler.get_event_handler_map()

        assert isinstance(handler_map, dict)
        assert "player_entered" in handler_map
        assert "player_left" in handler_map
        assert "game_tick" in handler_map
        assert "combat_started" in handler_map
        assert "combat_ended" in handler_map
        assert "player_attacked" in handler_map
        assert "npc_attacked" in handler_map
        assert "npc_took_damage" in handler_map
        assert "npc_died" in handler_map


class TestValidateEventMessage:
    """Test validate_event_message method."""

    def test_validate_event_message_valid(self) -> None:
        """Test validation with valid message."""
        mock_connection_manager = MagicMock()
        handler = EventHandler(mock_connection_manager)

        result = handler.validate_event_message("player_entered", {"room_id": "room-123"})

        assert result is True

    def test_validate_event_message_no_event_type(self) -> None:
        """Test validation with missing event_type."""
        mock_connection_manager = MagicMock()
        handler = EventHandler(mock_connection_manager)

        with patch("server.realtime.event_handlers.logger"):
            result = handler.validate_event_message(None, {"room_id": "room-123"})

            assert result is False

    def test_validate_event_message_no_data(self) -> None:
        """Test validation with missing data."""
        mock_connection_manager = MagicMock()
        handler = EventHandler(mock_connection_manager)

        with patch("server.realtime.event_handlers.logger"):
            result = handler.validate_event_message("player_entered", {})

            assert result is False


class TestHandleEventMessage:
    """Test handle_event_message method."""

    @pytest.mark.asyncio
    async def test_handle_event_message_success(self) -> None:
        """Test successfully handling an event message."""
        mock_connection_manager = MagicMock()
        handler = EventHandler(mock_connection_manager)

        message_data = {
            "event_type": "player_entered",
            "event_data": {"room_id": "room-123", "player_id": "player-123"},
        }

        with patch.object(handler, "handle_player_entered_event", new_callable=AsyncMock) as mock_handler:
            with patch("server.realtime.event_handlers.logger"):
                await handler.handle_event_message(message_data)

                mock_handler.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_event_message_invalid(self) -> None:
        """Test handling invalid event message."""
        mock_connection_manager = MagicMock()
        handler = EventHandler(mock_connection_manager)

        message_data: dict[str, Any] = {"event_type": None, "event_data": {}}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_event_message(message_data)

            # Should return early without calling handlers

    @pytest.mark.asyncio
    async def test_handle_event_message_unknown_type(self) -> None:
        """Test handling unknown event type."""
        mock_connection_manager = MagicMock()
        handler = EventHandler(mock_connection_manager)

        message_data = {"event_type": "unknown_event", "event_data": {}}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_event_message(message_data)

            # Should log unknown event type

    @pytest.mark.asyncio
    async def test_handle_event_message_npc_attacked_special_handling(self) -> None:
        """Test special handling for npc_attacked event."""
        mock_connection_manager = MagicMock()
        handler = EventHandler(mock_connection_manager)

        message_data = {"event_type": "npc_attacked", "event_data": {"room_id": "room-123"}}

        with patch.object(handler, "handle_npc_attacked_event", new_callable=AsyncMock) as mock_handler:
            with patch("server.realtime.event_handlers.logger"):
                await handler.handle_event_message(message_data)

                mock_handler.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_event_message_nats_error(self) -> None:
        """Test handling NATS error."""
        mock_connection_manager = MagicMock()
        handler = EventHandler(mock_connection_manager)

        message_data = {"event_type": "player_entered", "event_data": {}}

        with patch.object(handler, "handle_player_entered_event", new_callable=AsyncMock) as mock_handler:
            mock_handler.side_effect = NATSError("NATS connection error")
            with patch("server.realtime.event_handlers.logger"):
                await handler.handle_event_message(message_data)

                # Should catch and log error


class TestHandlePlayerEnteredEvent:
    """Test handle_player_entered_event method."""

    @pytest.mark.asyncio
    async def test_handle_player_entered_event_success(self) -> None:
        """Test successfully handling player entered event."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"room_id": "room-123", "player_id": "player-123"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_player_entered_event(data)

            mock_connection_manager.broadcast_room_event.assert_called_once_with("player_entered", "room-123", data)

    @pytest.mark.asyncio
    async def test_handle_player_entered_event_no_room_id(self) -> None:
        """Test handling player entered event without room_id."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"player_id": "player-123"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_player_entered_event(data)

            mock_connection_manager.broadcast_room_event.assert_not_called()


class TestHandlePlayerLeftEvent:
    """Test handle_player_left_event method."""

    @pytest.mark.asyncio
    async def test_handle_player_left_event_success(self) -> None:
        """Test successfully handling player left event."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"room_id": "room-123", "player_id": "player-123"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_player_left_event(data)

            mock_connection_manager.broadcast_room_event.assert_called_once_with("player_left", "room-123", data)

    @pytest.mark.asyncio
    async def test_handle_player_left_event_no_room_id(self) -> None:
        """Test handling player left event without room_id."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"player_id": "player-123"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_player_left_event(data)

            mock_connection_manager.broadcast_room_event.assert_not_called()


class TestHandleGameTickEvent:
    """Test handle_game_tick_event method."""

    @pytest.mark.asyncio
    async def test_handle_game_tick_event_success(self) -> None:
        """Test successfully handling game tick event."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"tick_number": 100}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_game_tick_event(data)

            mock_connection_manager.broadcast_global_event.assert_called_once_with("game_tick", data)


class TestHandleCombatStartedEvent:
    """Test handle_combat_started_event method."""

    @pytest.mark.asyncio
    async def test_handle_combat_started_event_success(self) -> None:
        """Test successfully handling combat started event."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.broadcast_room_event = AsyncMock()
        mock_connection_manager.get_player = AsyncMock(return_value=MagicMock())
        mock_connection_manager.send_personal_message = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        player_id = uuid4()
        data = {"room_id": "room-123", "participants": {str(player_id): {}}}

        with patch("server.realtime.event_handlers.build_event", return_value={"type": "player_update"}):
            with patch("server.realtime.event_handlers.logger"):
                await handler.handle_combat_started_event(data)

                mock_connection_manager.broadcast_room_event.assert_called_once()
                mock_connection_manager.send_personal_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_combat_started_event_no_room_id(self) -> None:
        """Test handling combat started event without room_id."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data: dict[str, Any] = {"participants": {}}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_combat_started_event(data)

            mock_connection_manager.broadcast_room_event.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_combat_started_event_no_participants(self) -> None:
        """Test handling combat started event without participants."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"room_id": "room-123"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_combat_started_event(data)

            mock_connection_manager.broadcast_room_event.assert_called_once()
            mock_connection_manager.send_personal_message.assert_not_called()


class TestHandleCombatEndedEvent:
    """Test handle_combat_ended_event method."""

    @pytest.mark.asyncio
    async def test_handle_combat_ended_event_success(self) -> None:
        """Test successfully handling combat ended event."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.broadcast_room_event = AsyncMock()
        mock_connection_manager.get_player = AsyncMock(return_value=MagicMock())
        mock_connection_manager.send_personal_message = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        player_id = uuid4()
        data = {"room_id": "room-123", "participants": {str(player_id): {}}}

        with patch("server.realtime.event_handlers.build_event", return_value={"type": "player_update"}):
            with patch("server.realtime.event_handlers.logger"):
                await handler.handle_combat_ended_event(data)

                mock_connection_manager.broadcast_room_event.assert_called_once()
                mock_connection_manager.send_personal_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_combat_ended_event_no_room_id(self) -> None:
        """Test handling combat ended event without room_id."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data: dict[str, Any] = {"participants": {}}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_combat_ended_event(data)

            mock_connection_manager.broadcast_room_event.assert_not_called()


class TestHandlePlayerAttackedEvent:
    """Test handle_player_attacked_event method."""

    @pytest.mark.asyncio
    async def test_handle_player_attacked_event_success(self) -> None:
        """Test successfully handling player attacked event."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"room_id": "room-123", "attacker_id": "player-1", "target_id": "player-2"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_player_attacked_event(data)

            mock_connection_manager.broadcast_room_event.assert_called_once_with("player_attacked", "room-123", data)

    @pytest.mark.asyncio
    async def test_handle_player_attacked_event_no_room_id(self) -> None:
        """Test handling player attacked event without room_id."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"attacker_id": "player-1"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_player_attacked_event(data)

            mock_connection_manager.broadcast_room_event.assert_not_called()


class TestHandleNpcAttackedEvent:
    """Test handle_npc_attacked_event method."""

    @pytest.mark.asyncio
    async def test_handle_npc_attacked_event_success(self) -> None:
        """Test successfully handling NPC attacked event."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"room_id": "room-123", "npc_id": "npc-1", "attacker_id": "player-1"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_npc_attacked_event(data)

            mock_connection_manager.broadcast_room_event.assert_called_once_with("npc_attacked", "room-123", data)

    @pytest.mark.asyncio
    async def test_handle_npc_attacked_event_no_room_id(self) -> None:
        """Test handling NPC attacked event without room_id."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"npc_id": "npc-1"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_npc_attacked_event(data)

            mock_connection_manager.broadcast_room_event.assert_not_called()


class TestHandleNpcTookDamageEvent:
    """Test handle_npc_took_damage_event method."""

    @pytest.mark.asyncio
    async def test_handle_npc_took_damage_event_success(self) -> None:
        """Test successfully handling NPC took damage event."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"room_id": "room-123", "npc_id": "npc-1", "damage": 10}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_npc_took_damage_event(data)

            mock_connection_manager.broadcast_room_event.assert_called_once_with("npc_took_damage", "room-123", data)

    @pytest.mark.asyncio
    async def test_handle_npc_took_damage_event_no_room_id(self) -> None:
        """Test handling NPC took damage event without room_id."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"npc_id": "npc-1", "damage": 10}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_npc_took_damage_event(data)

            mock_connection_manager.broadcast_room_event.assert_not_called()


class TestHandleNpcDiedEvent:
    """Test handle_npc_died_event method."""

    @pytest.mark.asyncio
    async def test_handle_npc_died_event_success(self) -> None:
        """Test successfully handling NPC died event."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.broadcast_room_event = AsyncMock()
        mock_event_bus = MagicMock()
        mock_connection_manager.event_bus = mock_event_bus
        handler = EventHandler(mock_connection_manager)

        data = {"room_id": "room-123", "npc_id": "npc-1", "npc_name": "TestNPC"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_npc_died_event(data)

            mock_connection_manager.broadcast_room_event.assert_called_once_with("npc_died", "room-123", data)
            mock_event_bus.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_npc_died_event_no_room_id(self) -> None:
        """Test handling NPC died event without room_id."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"npc_id": "npc-1", "npc_name": "TestNPC"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_npc_died_event(data)

            mock_connection_manager.broadcast_room_event.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_npc_died_event_no_npc_id(self) -> None:
        """Test handling NPC died event without npc_id."""
        mock_connection_manager = AsyncMock()
        handler = EventHandler(mock_connection_manager)

        data = {"room_id": "room-123", "npc_name": "TestNPC"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_npc_died_event(data)

            mock_connection_manager.broadcast_room_event.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_npc_died_event_no_event_bus(self) -> None:
        """Test handling NPC died event when event_bus is not available."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.broadcast_room_event = AsyncMock()
        mock_connection_manager.event_bus = None
        handler = EventHandler(mock_connection_manager)

        data = {"room_id": "room-123", "npc_id": "npc-1", "npc_name": "TestNPC"}

        with patch("server.realtime.event_handlers.logger"):
            await handler.handle_npc_died_event(data)

            mock_connection_manager.broadcast_room_event.assert_called_once()
