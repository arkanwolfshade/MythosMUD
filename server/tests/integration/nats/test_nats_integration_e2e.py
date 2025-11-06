"""
End-to-end integration tests for complete NATS event flow.
"""

import asyncio
from datetime import UTC, datetime
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.realtime.connection_manager import ConnectionManager
from server.realtime.event_publisher import EventPublisher
from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.game_tick_service import GameTickService


class TestNATSIntegrationE2E:
    """End-to-end integration tests for NATS event flow."""

    def setup_method(self):
        """Set up test fixtures."""
        # Mock NATS service
        self.mock_nats_service = Mock()
        self.mock_nats_service.publish = AsyncMock(return_value=True)
        self.mock_nats_service.subscribe = AsyncMock(return_value=True)
        self.mock_nats_service.unsubscribe = AsyncMock(return_value=True)
        self.mock_nats_service.is_connected = Mock(return_value=True)

        # Create EventPublisher
        self.event_publisher = EventPublisher(self.mock_nats_service)

        # Create ConnectionManager with EventPublisher
        self.connection_manager = ConnectionManager(event_publisher=self.event_publisher)

        # AI Agent: Create NATSMessageHandler with injected connection_manager (no longer a global)
        #           Post-migration: connection_manager must be passed via constructor
        self.nats_handler = NATSMessageHandler(self.mock_nats_service, None, self.connection_manager)

        # Create GameTickService
        self.game_tick_service = GameTickService(
            event_publisher=self.event_publisher,
            tick_interval=0.1,  # Fast interval for testing
        )

        # Mock room manager for ConnectionManager
        self.connection_manager.room_manager = Mock()
        self.connection_manager.room_manager.get_room_occupants.return_value = [
            {"player_name": "player1"},
            {"player_name": "player2"},
        ]
        self.connection_manager.online_players = {"player1": {"name": "player1"}, "player2": {"name": "player2"}}

        # Mock broadcast methods
        self.connection_manager.broadcast_to_room = AsyncMock()
        self.connection_manager.broadcast_global = AsyncMock()

    @pytest.mark.asyncio
    async def test_complete_player_entered_event_flow(self):
        """Test complete flow: ConnectionManager -> NATS -> NATSMessageHandler -> broadcast."""
        # Start NATS handler
        await self.nats_handler.start()

        # Simulate player entering room
        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        # This should publish to NATS and broadcast room_occupants
        await self.connection_manager._handle_player_entered_room(event_data)

        # Verify NATS publish was called
        self.mock_nats_service.publish.assert_called()

        # Get the published message
        publish_calls = self.mock_nats_service.publish.call_args_list
        player_entered_call = None
        for call in publish_calls:
            subject = call[0][0]
            if subject == "events.player_entered.test_room_1":
                player_entered_call = call
                break

        assert player_entered_call is not None, "Player entered event should be published to NATS"

        # Verify message content
        message_data = player_entered_call[0][1]
        assert message_data["event_type"] == "player_entered"
        assert message_data["data"]["player_id"] == "player1"
        assert message_data["data"]["room_id"] == "test_room_1"

        # Verify room_occupants was still broadcast
        self.connection_manager.broadcast_to_room.assert_called()

        await self.nats_handler.stop()

    @pytest.mark.asyncio
    async def test_complete_player_left_event_flow(self):
        """Test complete flow: ConnectionManager -> NATS -> NATSMessageHandler -> broadcast."""
        # Start NATS handler
        await self.nats_handler.start()

        # Simulate player leaving room
        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        # This should publish to NATS and broadcast room_occupants
        await self.connection_manager._handle_player_left_room(event_data)

        # Verify NATS publish was called
        self.mock_nats_service.publish.assert_called()

        # Get the published message
        publish_calls = self.mock_nats_service.publish.call_args_list
        player_left_call = None
        for call in publish_calls:
            subject = call[0][0]
            if subject == "events.player_left.test_room_1":
                player_left_call = call
                break

        assert player_left_call is not None, "Player left event should be published to NATS"

        # Verify message content
        message_data = player_left_call[0][1]
        assert message_data["event_type"] == "player_left"
        assert message_data["data"]["player_id"] == "player1"
        assert message_data["data"]["room_id"] == "test_room_1"

        # Verify room_occupants was still broadcast
        self.connection_manager.broadcast_to_room.assert_called()

        await self.nats_handler.stop()

    @pytest.mark.asyncio
    async def test_complete_game_tick_event_flow(self):
        """Test complete flow: GameTickService -> NATS -> NATSMessageHandler -> broadcast."""
        # Start NATS handler
        await self.nats_handler.start()

        # Start game tick service
        await self.game_tick_service.start()

        # Wait for at least one tick
        await asyncio.sleep(0.15)

        # Verify NATS publish was called
        self.mock_nats_service.publish.assert_called()

        # Get the published message
        publish_calls = self.mock_nats_service.publish.call_args_list
        game_tick_call = None
        for call in publish_calls:
            subject = call[0][0]
            if subject == "events.game_tick":
                game_tick_call = call
                break

        assert game_tick_call is not None, "Game tick event should be published to NATS"

        # Verify message content
        message_data = game_tick_call[0][1]
        assert message_data["event_type"] == "game_tick"
        assert "tick_number" in message_data["data"]
        assert message_data["data"]["tick_number"] > 0

        # Stop services
        await self.game_tick_service.stop()
        await self.nats_handler.stop()

    @pytest.mark.asyncio
    async def test_nats_message_handler_routes_events_to_connection_manager(self):
        """Test that NATSMessageHandler properly routes events to ConnectionManager."""
        # Start NATS handler
        await self.nats_handler.start()

        # Simulate NATS message for player_entered event
        player_entered_message = {
            "event_type": "player_entered",
            "data": {"player_id": "player1", "room_id": "test_room_1"},
            "timestamp": datetime.now(UTC).isoformat(),
        }

        # AI Agent: Patch the method on the handler's injected connection_manager instance
        #           Post-migration: connection_manager is no longer a module-level global
        with patch.object(
            self.nats_handler._connection_manager, "broadcast_room_event", new_callable=AsyncMock
        ) as mock_broadcast:
            # Simulate receiving the message
            await self.nats_handler._handle_nats_message(player_entered_message)

            # Verify broadcast_room_event was called
            mock_broadcast.assert_called_once()
            call_args = mock_broadcast.call_args
            assert call_args[0][0] == "player_entered"  # event_type
            assert call_args[0][1] == "test_room_1"  # room_id
            assert call_args[0][2]["player_id"] == "player1"  # data

        await self.nats_handler.stop()

    @pytest.mark.asyncio
    async def test_nats_message_handler_routes_game_tick_to_global_broadcast(self):
        """Test that NATSMessageHandler routes game_tick events to global broadcast."""
        # Start NATS handler
        await self.nats_handler.start()

        # Simulate NATS message for game_tick event
        game_tick_message = {
            "event_type": "game_tick",
            "data": {"tick_number": 1, "tick_interval": 10.0},
            "timestamp": datetime.now(UTC).isoformat(),
        }

        # AI Agent: Patch the method on the handler's injected connection_manager instance
        #           Post-migration: connection_manager is no longer a module-level global
        with patch.object(
            self.nats_handler._connection_manager, "broadcast_global_event", new_callable=AsyncMock
        ) as mock_broadcast:
            # Simulate receiving the message
            await self.nats_handler._handle_nats_message(game_tick_message)

            # Verify broadcast_global_event was called
            mock_broadcast.assert_called_once()
            call_args = mock_broadcast.call_args
            assert call_args[0][0] == "game_tick"  # event_type
            assert call_args[0][1]["tick_number"] == 1  # data

        await self.nats_handler.stop()

    @pytest.mark.asyncio
    async def test_multiple_concurrent_players_entering_leaving(self):
        """Test multiple concurrent players entering and leaving rooms."""
        # Start NATS handler
        await self.nats_handler.start()

        # Simulate multiple players entering different rooms
        tasks = []
        for i in range(5):
            event_data = {"room_id": f"test_room_{i}", "player_id": f"player_{i}"}
            task = self.connection_manager._handle_player_entered_room(event_data)
            tasks.append(task)

        # Wait for all events to complete
        await asyncio.gather(*tasks)

        # Verify all events were published to NATS
        publish_calls = self.mock_nats_service.publish.call_args_list
        player_entered_calls = [call for call in publish_calls if "events.player_entered" in call[0][0]]
        assert len(player_entered_calls) == 5, "Should have 5 player entered events"

        # Simulate players leaving
        tasks = []
        for i in range(5):
            event_data = {"room_id": f"test_room_{i}", "player_id": f"player_{i}"}
            task = self.connection_manager._handle_player_left_room(event_data)
            tasks.append(task)

        # Wait for all events to complete
        await asyncio.gather(*tasks)

        # Verify all leave events were published
        publish_calls = self.mock_nats_service.publish.call_args_list
        player_left_calls = [call for call in publish_calls if "events.player_left" in call[0][0]]
        assert len(player_left_calls) == 5, "Should have 5 player left events"

        await self.nats_handler.stop()

    @pytest.mark.asyncio
    async def test_game_tick_with_multiple_ticks(self):
        """Test game tick service with multiple ticks."""
        # Start NATS handler
        await self.nats_handler.start()

        # Start game tick service
        await self.game_tick_service.start()

        # Wait for multiple ticks
        await asyncio.sleep(0.35)  # Should get at least 3 ticks

        # Stop services
        await self.game_tick_service.stop()
        await self.nats_handler.stop()

        # Verify multiple game tick events were published
        publish_calls = self.mock_nats_service.publish.call_args_list
        game_tick_calls = [call for call in publish_calls if call[0][0] == "events.game_tick"]
        assert len(game_tick_calls) >= 3, f"Should have at least 3 game tick events, got {len(game_tick_calls)}"

        # Verify tick numbers are sequential
        tick_numbers = []
        for call in game_tick_calls:
            message_data = call[0][1]
            tick_numbers.append(message_data["data"]["tick_number"])

        tick_numbers.sort()
        for i in range(1, len(tick_numbers)):
            assert tick_numbers[i] == tick_numbers[i - 1] + 1, "Tick numbers should be sequential"

    @pytest.mark.asyncio
    async def test_error_handling_in_event_flow(self):
        """Test error handling throughout the event flow."""
        # Make NATS service fail
        self.mock_nats_service.publish.side_effect = Exception("NATS error")

        # Start NATS handler
        await self.nats_handler.start()

        # Simulate player entering room - should not raise exception
        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        # Should not raise exception despite NATS failure
        await self.connection_manager._handle_player_entered_room(event_data)

        # Verify room_occupants was still broadcast despite NATS failure
        self.connection_manager.broadcast_to_room.assert_called()

        await self.nats_handler.stop()

    @pytest.mark.asyncio
    async def test_event_publisher_without_nats_service(self):
        """Test EventPublisher behavior when NATS service is not connected."""
        # Create EventPublisher without NATS service
        event_publisher_no_nats = EventPublisher(None)

        # Should not raise exception
        result = await event_publisher_no_nats.publish_player_entered_event(player_id="player1", room_id="test_room_1")

        assert result is False, "Should return False when NATS service is not available"

    @pytest.mark.asyncio
    async def test_connection_manager_without_event_publisher(self):
        """Test ConnectionManager behavior when EventPublisher is not available."""
        # Create ConnectionManager without EventPublisher
        connection_manager_no_publisher = ConnectionManager()

        # Mock room manager
        connection_manager_no_publisher.room_manager = Mock()
        connection_manager_no_publisher.room_manager.get_room_occupants.return_value = []
        connection_manager_no_publisher.online_players = {}
        connection_manager_no_publisher.broadcast_to_room = AsyncMock()

        # Should not raise exception
        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        await connection_manager_no_publisher._handle_player_entered_room(event_data)

        # Verify room_occupants was still broadcast
        connection_manager_no_publisher.broadcast_to_room.assert_called()
