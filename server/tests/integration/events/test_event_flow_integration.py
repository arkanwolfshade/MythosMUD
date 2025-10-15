"""
Integration tests for complete event flow.

This test suite verifies the complete event flow from WebSocket connection
through event publishing, processing, and broadcasting to other clients.
"""

import asyncio
import json
from unittest.mock import AsyncMock, Mock

import pytest

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom
from server.models.room import Room
from server.realtime.event_handler import RealTimeEventHandler


class TestCompleteEventFlowIntegration:
    """Test complete event flow integration."""

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager with realistic behavior."""
        cm = AsyncMock()
        cm._get_player = Mock()
        cm.persistence = Mock()
        cm.broadcast_to_room = AsyncMock()
        cm.subscribe_to_room = AsyncMock()
        cm.unsubscribe_from_room = AsyncMock()
        cm.send_personal_message = AsyncMock()
        return cm

    @pytest.mark.asyncio
    async def test_websocket_connection_to_event_broadcasting_flow(self, mock_connection_manager):
        """Test the complete flow from WebSocket connection to event broadcasting."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager
        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_player.id = "test_player_123"
        mock_connection_manager._get_player.return_value = mock_player

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Simulate the WebSocket connection flow
        # 1. Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, event_bus)

        # 2. Simulate WebSocket connection handler calling room.player_entered
        room.player_entered("test_player_123")

        # 3. Wait for event processing
        await asyncio.sleep(0.3)

        # 4. Verify the complete flow worked:
        # - Room published PlayerEnteredRoom event
        # - EventBus processed the event
        # - RealTimeEventHandler received and processed the event
        # - ConnectionManager was called to broadcast

        # Verify broadcast_to_room was called with player_entered message
        assert mock_connection_manager.broadcast_to_room.call_count >= 1

        # Find the player_entered message
        player_entered_calls = [
            call
            for call in mock_connection_manager.broadcast_to_room.call_args_list
            if call[0][1]["event_type"] == "player_entered"
        ]
        assert len(player_entered_calls) == 1

        # Verify the message structure
        player_entered_message = player_entered_calls[0][0][1]
        assert player_entered_message["event_type"] == "player_entered"
        assert player_entered_message["room_id"] == "test_room_001"
        assert player_entered_message["data"]["player_id"] == "test_player_123"
        assert player_entered_message["data"]["player_name"] == "TestPlayer"
        assert player_entered_message["data"]["message"] == "TestPlayer enters the room."

        # Verify exclude_player parameter
        exclude_player = player_entered_calls[0][1].get("exclude_player")
        assert exclude_player == "test_player_123"

    @pytest.mark.asyncio
    async def test_websocket_disconnection_to_event_broadcasting_flow(self, mock_connection_manager):
        """Test the complete flow from WebSocket disconnection to event broadcasting."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_player.id = "test_player_123"
        mock_connection_manager._get_player.return_value = mock_player

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Simulate the WebSocket disconnection flow
        # 1. Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, event_bus)

        # 2. First add player to room
        room.player_entered("test_player_123")
        await asyncio.sleep(0.1)  # Brief wait
        mock_connection_manager.broadcast_to_room.reset_mock()  # Clear enter events

        # 3. Simulate WebSocket disconnection handler calling room.player_left
        room.player_left("test_player_123")

        # 4. Wait for event processing
        await asyncio.sleep(0.3)

        # 5. Verify the complete disconnection flow worked
        assert mock_connection_manager.broadcast_to_room.call_count >= 1

        # Find the player_left message
        player_left_calls = [
            call
            for call in mock_connection_manager.broadcast_to_room.call_args_list
            if call[0][1]["event_type"] == "player_left"
        ]
        assert len(player_left_calls) == 1

        # Verify the message structure
        player_left_message = player_left_calls[0][0][1]
        assert player_left_message["event_type"] == "player_left"
        assert player_left_message["room_id"] == "test_room_001"
        assert player_left_message["data"]["player_id"] == "test_player_123"
        assert player_left_message["data"]["player_name"] == "TestPlayer"
        assert player_left_message["data"]["message"] == "TestPlayer leaves the room."

    @pytest.mark.asyncio
    async def test_multiple_players_simultaneous_events(self, mock_connection_manager):
        """Test multiple players entering/leaving simultaneously."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Setup mock players
        mock_player1 = Mock()
        mock_player1.name = "Player1"
        mock_player1.id = "player_001"

        mock_player2 = Mock()
        mock_player2.name = "Player2"
        mock_player2.id = "player_002"

        def mock_get_player(player_id):
            if player_id == "player_001":
                return mock_player1
            elif player_id == "player_002":
                return mock_player2
            return None

        mock_connection_manager._get_player.side_effect = mock_get_player

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, event_bus)

        # Simulate multiple players entering simultaneously
        room.player_entered("player_001")
        room.player_entered("player_002")

        # Wait for event processing
        await asyncio.sleep(0.5)

        # Verify both player_entered events were broadcast
        player_entered_calls = [
            call
            for call in mock_connection_manager.broadcast_to_room.call_args_list
            if call[0][1]["event_type"] == "player_entered"
        ]
        assert len(player_entered_calls) == 2

        # Verify both messages are correct
        player_names = [call[0][1]["data"]["player_name"] for call in player_entered_calls]
        assert "Player1" in player_names
        assert "Player2" in player_names

    @pytest.mark.asyncio
    async def test_event_data_structure_matches_client_expectations(self, mock_connection_manager):
        """Test that event data structure matches what the client expects."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Create and publish event
        event = PlayerEnteredRoom(timestamp=None, event_type="", player_id="test_player_123", room_id="test_room_001")

        event_bus.publish(event)
        await asyncio.sleep(0.3)

        # Get the broadcast message
        player_entered_calls = [
            call
            for call in mock_connection_manager.broadcast_to_room.call_args_list
            if call[0][1]["event_type"] == "player_entered"
        ]
        assert len(player_entered_calls) == 1

        message = player_entered_calls[0][0][1]

        # Verify the message structure matches client expectations
        required_fields = ["event_type", "timestamp", "sequence_number", "room_id", "data"]
        for field in required_fields:
            assert field in message, f"Missing required field: {field}"

        # Verify data structure
        data = message["data"]
        required_data_fields = ["player_id", "player_name", "message"]
        for field in required_data_fields:
            assert field in data, f"Missing required data field: {field}"

        # Verify field types
        assert isinstance(message["event_type"], str)
        assert isinstance(message["timestamp"], str)
        assert isinstance(message["sequence_number"], int)
        assert isinstance(message["room_id"], str)
        assert isinstance(data["player_id"], str)
        assert isinstance(data["player_name"], str)
        assert isinstance(data["message"], str)

        # Verify the message is JSON serializable (important for WebSocket transmission)
        json_str = json.dumps(message)
        parsed_message = json.loads(json_str)
        assert parsed_message == message

    @pytest.mark.asyncio
    async def test_error_handling_in_event_flow(self, mock_connection_manager):
        """Test error handling in the event flow."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Setup mock to simulate errors
        mock_connection_manager._get_player.side_effect = Exception("Database error")

        # Create and publish event
        event = PlayerEnteredRoom(timestamp=None, event_type="", player_id="test_player_123", room_id="test_room_001")

        # This should not crash the system
        event_bus.publish(event)
        await asyncio.sleep(0.3)

        # Verify that broadcast was not called due to error
        player_entered_calls = [
            call
            for call in mock_connection_manager.broadcast_to_room.call_args_list
            if call[0][1]["event_type"] == "player_entered"
        ]
        assert len(player_entered_calls) == 0

        # Verify the system is still functional by testing a successful event
        mock_connection_manager._get_player.side_effect = None
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        # Reset mocks
        mock_connection_manager.broadcast_to_room.reset_mock()

        # Publish another event
        event_bus.publish(event)
        await asyncio.sleep(0.3)

        # Verify this event was processed successfully
        player_entered_calls = [
            call
            for call in mock_connection_manager.broadcast_to_room.call_args_list
            if call[0][1]["event_type"] == "player_entered"
        ]
        assert len(player_entered_calls) == 1


# ============================================================================
# Tests merged from test_real_event_flow_legacy.py
# ============================================================================


"""
Test the real event flow with proper event loop setup.

This test simulates the actual application environment where the EventBus
has access to the main event loop and can properly execute async handlers.
"""


class TestRealEventFlow:
    """Test the real event flow with proper async handling."""

    @pytest.fixture
    def event_bus(self):
        """Create an EventBus for testing."""
        from server.events import EventBus

        return EventBus()

    @pytest.fixture
    def event_loop_setup(self, isolated_event_loop, event_bus):
        """Set up a proper event loop that EventBus can use."""
        # Use standardized fixtures instead of manual loop creation
        loop = isolated_event_loop
        event_bus = event_bus

        return loop, event_bus

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager."""
        cm = AsyncMock()
        cm._get_player = Mock()
        cm.persistence = Mock()
        cm.broadcast_to_room = AsyncMock()
        cm.subscribe_to_room = AsyncMock()
        cm.unsubscribe_from_room = AsyncMock()
        cm.send_personal_message = AsyncMock()
        return cm

    @pytest.mark.asyncio
    async def test_real_event_flow_with_proper_loop(self, event_loop_setup, mock_connection_manager):
        """Test that events are properly processed with a real event loop."""
        loop, event_bus = event_loop_setup

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Set the main loop for async event handling
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Setup mock player and room
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []  # Return empty list to avoid iteration errors
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Create event
        event = PlayerEnteredRoom(timestamp=None, event_type="", player_id="test_player_123", room_id="test_room_001")

        # Publish event
        event_bus.publish(event)

        # Wait for background processing
        await asyncio.sleep(0.3)

        # Verify that the event handler was called (enhanced synchronization sends 2 events)
        assert mock_connection_manager.broadcast_to_room.call_count == 2

        # Verify the message content (check the first call which should be player_entered)
        calls = mock_connection_manager.broadcast_to_room.call_args_list
        player_entered_call = calls[0]  # First call should be player_entered
        message = player_entered_call[0][1]
        assert message["event_type"] == "player_entered"
        assert message["data"]["player_name"] == "TestPlayer"

    @pytest.mark.asyncio
    async def test_websocket_connection_flow_simulation(self, event_loop_setup, mock_connection_manager):
        """Simulate the actual WebSocket connection flow."""
        loop, event_bus = event_loop_setup

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Set the main loop for async event handling
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Setup mock room data
        mock_room_data = {"id": "test_room_001", "name": "Test Room"}
        from server.models.room import Room

        room = Room(mock_room_data, event_bus)

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player
        mock_connection_manager.persistence.get_room.return_value = room

        # Simulate player entering room (this should trigger event)
        room.player_entered("test_player_123")

        # Wait for event processing
        await asyncio.sleep(0.3)

        # Verify that broadcast was called (enhanced synchronization sends 2 events)
        assert mock_connection_manager.broadcast_to_room.call_count == 2

        # Reset for next test
        mock_connection_manager.broadcast_to_room.reset_mock()

        # Simulate player leaving room
        room.player_left("test_player_123")

        # Wait for event processing
        await asyncio.sleep(0.3)

        # Verify that broadcast was called for leave event (enhanced synchronization sends 2 events)
        assert mock_connection_manager.broadcast_to_room.call_count == 2

        # Verify it was a player_left message (check the first call)
        calls = mock_connection_manager.broadcast_to_room.call_args_list
        player_left_call = calls[0]  # First call should be player_left
        message = player_left_call[0][1]
        assert message["event_type"] == "player_left"

    @pytest.mark.asyncio
    async def test_event_bus_loop_detection(self):
        """Test that EventBus properly detects running event loops."""
        # Test with no running loop
        bus1 = EventBus()
        assert bus1._main_loop is None

        # Test with running loop (in the async test function):
        # First test basic setting
        async def _test_with_running_loop():
            bus3 = EventBus()
            bus3.set_main_loop(asyncio.get_running_loop())
            assert bus3._main_loop.is_running() is True
            return bus3

        bus3 = await _test_with_running_loop()
        # Note: The loop is closed after asyncio.run() completes, so we can't check is_running()
        # Instead, just verify the loop was set correctly
        assert bus3._main_loop is not None
