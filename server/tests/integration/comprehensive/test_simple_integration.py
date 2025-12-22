"""
Simple integration tests for the complete event flow.

This test suite verifies the complete event flow from WebSocket connection
through event publishing, processing, and broadcasting.
"""

import asyncio
import json
from unittest.mock import AsyncMock, MagicMock, Mock
from uuid import uuid4

import pytest

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.models.room import Room
from server.realtime.event_handler import RealTimeEventHandler


class TestSimpleIntegration:
    """Test simple integration scenarios."""

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager with realistic behavior."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        cm = MagicMock()
        cm._get_player = AsyncMock()
        cm.get_player = AsyncMock()
        cm.persistence = Mock()
        cm.persistence.get_room = AsyncMock()
        # async_persistence.get_room_by_id is a sync method (uses cache)
        cm.async_persistence = Mock()
        cm.async_persistence.get_room_by_id = Mock()
        cm.broadcast_to_room = AsyncMock()
        cm.subscribe_to_room = AsyncMock()
        cm.unsubscribe_from_room = AsyncMock()
        cm.send_personal_message = AsyncMock()
        # convert_room_players_uuids_to_names is async and returns a dict (not AsyncMock)
        cm.convert_room_players_uuids_to_names = AsyncMock(return_value={})
        return cm

    @pytest.mark.asyncio
    async def test_complete_connection_flow(self, mock_connection_manager):
        """Test the complete flow from WebSocket connection to event broadcasting."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create event handler with connection manager
        event_handler = RealTimeEventHandler(event_bus, connection_manager=mock_connection_manager)
        # Also update player_handler's connection_manager in case it was already initialized
        event_handler.player_handler.connection_manager = mock_connection_manager
        event_handler.player_handler._room_handler.connection_manager = mock_connection_manager

        # Use UUID for player_id
        player_id = uuid4()

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        # Mock both _get_player (legacy) and get_player (current)
        mock_connection_manager._get_player = AsyncMock(return_value=mock_player)
        mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []
        # Mock both persistence methods
        mock_connection_manager.persistence.get_room.return_value = mock_room
        # async_persistence.get_room_by_id is a sync method (uses cache)
        mock_connection_manager.async_persistence.get_room_by_id.return_value = mock_room

        # Simulate the WebSocket connection flow
        # 1. Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, event_bus)

        # 2. Simulate WebSocket connection handler calling room.player_entered
        room.player_entered(str(player_id))

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
        assert player_entered_message["data"]["player_id"] == str(player_id)
        assert player_entered_message["data"]["player_name"] == "TestPlayer"
        assert player_entered_message["data"]["message"] == "TestPlayer enters the room."

        # Verify exclude_player parameter
        exclude_player = player_entered_calls[0][1].get("exclude_player")
        assert exclude_player == str(player_id)

    @pytest.mark.asyncio
    async def test_complete_disconnection_flow(self, mock_connection_manager):
        """Test the complete flow from WebSocket disconnection to event broadcasting."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create event handler with connection manager
        event_handler = RealTimeEventHandler(event_bus, connection_manager=mock_connection_manager)
        # Also update player_handler's connection_manager in case it was already initialized
        event_handler.player_handler.connection_manager = mock_connection_manager
        event_handler.player_handler._room_handler.connection_manager = mock_connection_manager

        # Use UUID for player_id
        player_id = uuid4()

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        # Mock both _get_player (legacy) and get_player (current)
        mock_connection_manager._get_player = AsyncMock(return_value=mock_player)
        mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []
        # Mock both persistence methods
        mock_connection_manager.persistence.get_room.return_value = mock_room
        # async_persistence.get_room_by_id is a sync method (uses cache)
        mock_connection_manager.async_persistence.get_room_by_id.return_value = mock_room

        # Simulate the WebSocket disconnection flow
        # 1. Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, event_bus)

        # 2. First add player to room
        room.player_entered(str(player_id))
        await asyncio.sleep(0.1)  # Brief wait
        mock_connection_manager.broadcast_to_room.reset_mock()  # Clear enter events

        # 3. Simulate WebSocket disconnection handler calling room.player_left
        room.player_left(str(player_id))

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
        assert player_left_message["data"]["player_id"] == str(player_id)
        assert player_left_message["data"]["player_name"] == "TestPlayer"
        assert player_left_message["data"]["message"] == "TestPlayer leaves the room."

    @pytest.mark.asyncio
    async def test_event_data_structure_matches_client_expectations(self, mock_connection_manager):
        """Test that event data structure matches what the client expects."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create event handler with connection manager
        event_handler = RealTimeEventHandler(event_bus, connection_manager=mock_connection_manager)
        # Also update player_handler's connection_manager in case it was already initialized
        event_handler.player_handler.connection_manager = mock_connection_manager
        event_handler.player_handler._room_handler.connection_manager = mock_connection_manager

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        # Mock both _get_player (legacy) and get_player (current)
        mock_connection_manager._get_player = AsyncMock(return_value=mock_player)
        mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []
        # Mock both persistence methods
        mock_connection_manager.persistence.get_room.return_value = mock_room
        # async_persistence.get_room_by_id is a sync method (uses cache)
        mock_connection_manager.async_persistence.get_room_by_id.return_value = mock_room

        # Use UUID for player_id
        player_id = uuid4()

        # Create and publish event
        event = PlayerEnteredRoom(player_id=str(player_id), room_id="test_room_001")

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
    async def test_multiple_players_simultaneous_events(self, mock_connection_manager):
        """Test multiple players entering simultaneously."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create event handler with connection manager
        event_handler = RealTimeEventHandler(event_bus, connection_manager=mock_connection_manager)
        # Also update player_handler's connection_manager in case it was already initialized
        event_handler.player_handler.connection_manager = mock_connection_manager
        event_handler.player_handler._room_handler.connection_manager = mock_connection_manager

        # Use UUIDs for player_ids
        player_id1 = uuid4()
        player_id2 = uuid4()

        # Setup mock players
        mock_player1 = Mock()
        mock_player1.name = "Player1"
        mock_player1.id = player_id1

        mock_player2 = Mock()
        mock_player2.name = "Player2"
        mock_player2.id = player_id2

        def mock_get_player(player_id_uuid):
            if player_id_uuid == player_id1:
                return mock_player1
            elif player_id_uuid == player_id2:
                return mock_player2
            return None

        mock_connection_manager._get_player = AsyncMock(side_effect=mock_get_player)
        mock_connection_manager.get_player = AsyncMock(side_effect=mock_get_player)

        # Mock _get_players_batch to return a dictionary of players when awaited
        async def mock_get_players_batch(player_ids):
            """Return a dictionary of player_id -> player for the batch request."""
            result = {}
            for player_id in player_ids:
                if player_id == player_id1:
                    result[player_id] = mock_player1
                elif player_id == player_id2:
                    result[player_id] = mock_player2
            return result

        mock_connection_manager._get_players_batch = AsyncMock(side_effect=mock_get_players_batch)

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []
        mock_room.get_npcs.return_value = []  # Return empty list for NPCs
        # Mock both persistence.get_room and async_persistence.get_room_by_id
        mock_connection_manager.persistence.get_room.return_value = mock_room
        # async_persistence.get_room_by_id is a sync method that uses cache (not async)
        if (
            not hasattr(mock_connection_manager, "async_persistence")
            or mock_connection_manager.async_persistence is None
        ):
            mock_connection_manager.async_persistence = Mock()
        mock_connection_manager.async_persistence.get_room_by_id = Mock(return_value=mock_room)
        # Mock _canonical_room_id to return the room_id directly (not a coroutine)
        mock_connection_manager._canonical_room_id = Mock(return_value="test_room_001")
        # convert_room_players_uuids_to_names is async and returns a dict (not AsyncMock)
        mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(
            return_value={"id": "test_room_001", "name": "Test Room"}
        )

        # Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, event_bus)

        # Simulate multiple players entering simultaneously
        room.player_entered(str(player_id1))
        room.player_entered(str(player_id2))

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


# ============================================================================
# Tests merged from test_simple_connection_events_legacy.py
# ============================================================================


"""
Simple tests to investigate WebSocket connection event firing issues.

This test suite focuses on the core event publishing mechanism without complex async mocking.
"""


class TestSimpleConnectionEvents:
    """Simple tests for connection event firing."""

    def test_room_player_entered_publishes_event(self) -> None:
        """Test that Room.player_entered publishes PlayerEnteredRoom event."""
        # Create mock event bus
        mock_event_bus = Mock()
        mock_event_bus.publish = Mock()

        # Use UUID for player_id
        player_id = uuid4()

        # Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, mock_event_bus)

        # Call player_entered
        room.player_entered(str(player_id))

        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        published_event = mock_event_bus.publish.call_args[0][0]
        assert isinstance(published_event, PlayerEnteredRoom)
        assert published_event.player_id == str(player_id)
        assert published_event.room_id == "test_room_001"

    def test_room_player_left_publishes_event(self) -> None:
        """Test that Room.player_left publishes PlayerLeftRoom event."""
        # Create mock event bus
        mock_event_bus = Mock()
        mock_event_bus.publish = Mock()

        # Use UUID for player_id
        player_id = uuid4()

        # Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, mock_event_bus)

        # First add player to room
        room.player_entered(str(player_id))
        mock_event_bus.publish.reset_mock()  # Clear the enter event

        # Then remove player from room
        room.player_left(str(player_id))

        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        published_event = mock_event_bus.publish.call_args[0][0]
        assert isinstance(published_event, PlayerLeftRoom)
        assert published_event.player_id == str(player_id)
        assert published_event.room_id == "test_room_001"

    def test_room_without_event_bus_handles_gracefully(self) -> None:
        """Test that Room works without event bus (should not crash)."""
        # Use UUID for player_id
        player_id = uuid4()

        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data)  # No event bus

        # Should not crash
        room.player_entered(str(player_id))
        room.player_left(str(player_id))

        # Verify player was added and removed
        assert not room.has_player(str(player_id))

    def test_event_types_have_correct_attributes(self) -> None:
        """Test that event types have the correct attributes."""
        # Use UUID for player_id
        player_id = uuid4()

        # Test PlayerEnteredRoom
        entered_event = PlayerEnteredRoom(player_id=str(player_id), room_id="test_room")
        assert entered_event.player_id == str(player_id)
        assert entered_event.room_id == "test_room"
        assert entered_event.event_type == "PlayerEnteredRoom"

        # Test PlayerLeftRoom
        left_event = PlayerLeftRoom(player_id=str(player_id), room_id="test_room")
        assert left_event.player_id == str(player_id)
        assert left_event.room_id == "test_room"
        assert left_event.event_type == "PlayerLeftRoom"
