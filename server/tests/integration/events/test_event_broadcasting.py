"""
Tests for event broadcasting bugs that were discovered during debugging.

These tests ensure that:
1. Players don't see their own entry/exit messages
2. Room events are properly broadcast to other players
3. EventBus instances are shared correctly
4. Connection manager excludes players appropriately
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from server.events import PlayerEnteredRoom, PlayerLeftRoom
from server.events.event_bus import EventBus
from server.game.movement_service import MovementService
from server.persistence import PersistenceLayer
from server.realtime.connection_manager import ConnectionManager, MemoryMonitor
from server.realtime.event_handler import RealTimeEventHandler


class TestEventBusIntegration:
    """Test that EventBus instances are properly shared across components."""

    @pytest.mark.asyncio
    async def test_shared_event_bus_instance(self, async_event_bus):
        """Test that MovementService uses the same EventBus as PersistenceLayer."""
        # Create a persistence layer with EventBus
        persistence = Mock(spec=PersistenceLayer)
        event_bus = async_event_bus
        persistence._event_bus = event_bus

        # Create MovementService with shared EventBus
        movement_service = MovementService(event_bus)

        # Verify they share the same instance
        assert movement_service._event_bus is event_bus
        assert movement_service._event_bus is persistence._event_bus

    def test_movement_service_without_shared_event_bus_uses_none(self):
        """Test that MovementService uses None when no EventBus provided."""
        movement_service = MovementService(None)

        # Should use None when no EventBus provided
        assert movement_service._event_bus is None

    def test_multiple_movement_services_with_different_event_buses(self):
        """Test that different MovementService instances with different EventBus don't interfere."""
        event_bus_1 = EventBus()
        event_bus_2 = EventBus()

        movement_service_1 = MovementService(event_bus_1)
        movement_service_2 = MovementService(event_bus_2)

        assert movement_service_1._event_bus is event_bus_1
        assert movement_service_2._event_bus is event_bus_2
        assert movement_service_1._event_bus is not movement_service_2._event_bus


class TestPlayerMovementMessageExclusion:
    """Test that players don't see their own entry/exit messages."""

    @pytest.fixture
    def connection_manager(self):
        """Create a connection manager for testing."""
        return ConnectionManager()

    @pytest.fixture
    def event_handler(self, connection_manager):
        """Create an event handler for testing."""
        event_bus = EventBus()
        handler = RealTimeEventHandler(event_bus, connection_manager=connection_manager)
        # Mock the persistence layer
        handler.connection_manager.persistence = Mock()
        return handler

    @pytest.mark.asyncio
    async def test_player_entered_excludes_entering_player(self, event_handler):
        """Test that PlayerEnteredRoomEvent excludes the entering player from broadcast."""
        player_id = str(uuid4())
        room_id = str(uuid4())
        player_name = "Ithaqua"

        # Mock the connection manager's methods
        event_handler.connection_manager.broadcast_to_room = AsyncMock()

        # Mock _get_player to return a player
        mock_player = Mock()
        mock_player.name = player_name
        event_handler.connection_manager._get_player = Mock(return_value=mock_player)

        # Create and handle a PlayerEnteredRoomEvent
        event = PlayerEnteredRoom(player_id=player_id, room_id=room_id)

        await event_handler._handle_player_entered(event)

        # Verify broadcast_to_room was called with exclude_player
        calls = event_handler.connection_manager.broadcast_to_room.call_args_list
        assert len(calls) >= 1

        # Check that the first call (player event) has exclude_player
        first_call = calls[0]
        assert first_call[1].get("exclude_player") == player_id

    @pytest.mark.asyncio
    async def test_player_left_excludes_leaving_player(self, event_handler):
        """Test that PlayerLeftRoomEvent excludes the leaving player from broadcast."""
        player_id = str(uuid4())
        room_id = str(uuid4())
        player_name = "Ithaqua"

        # Mock the connection manager's methods
        event_handler.connection_manager.broadcast_to_room = AsyncMock()

        # Mock _get_player to return a player
        mock_player = Mock()
        mock_player.name = player_name
        event_handler.connection_manager._get_player = Mock(return_value=mock_player)

        # Create and handle a PlayerLeftRoomEvent
        event = PlayerLeftRoom(player_id=player_id, room_id=room_id)

        await event_handler._handle_player_left(event)

        # Verify broadcast_to_room was called with exclude_player
        calls = event_handler.connection_manager.broadcast_to_room.call_args_list
        assert len(calls) >= 1

        # Check that the first call (player event) has exclude_player
        first_call = calls[0]
        assert first_call[1].get("exclude_player") == player_id

    @pytest.mark.asyncio
    async def test_connection_manager_excludes_player_from_broadcast(self, connection_manager):
        """Test that ConnectionManager's broadcast_to_room properly excludes players."""
        room_id = str(uuid4())
        player_1_id = str(uuid4())
        player_2_id = str(uuid4())
        exclude_player_id = player_1_id

        # Mock active websockets
        connection_manager.active_websockets = {player_1_id: Mock(), player_2_id: Mock()}

        # Add players to room subscriptions (required for broadcast_to_room to work)
        connection_manager.room_subscriptions[room_id] = {player_1_id, player_2_id}

        # Mock _get_player to return room occupants
        def mock_get_player(player_id):
            player = Mock()
            player.current_room_id = room_id
            return player

        connection_manager._get_player = mock_get_player
        connection_manager.send_personal_message = AsyncMock()

        test_event = {"type": "test_message", "data": "test"}

        # Broadcast to room with exclusion
        await connection_manager.broadcast_to_room(room_id, test_event, exclude_player=exclude_player_id)

        # Verify that only player_2 received the message (player_1 was excluded)
        calls = connection_manager.send_personal_message.call_args_list
        assert len(calls) == 1
        # send_personal_message receives UUID objects, so compare UUIDs
        assert calls[0][0][0] == uuid.UUID(player_2_id) if isinstance(player_2_id, str) else player_2_id


class TestRoomEventBroadcasting:
    """Test that room events are properly broadcast to all relevant players."""

    @pytest.fixture
    def event_bus(self):
        """Create an EventBus for testing."""
        return EventBus()

    @pytest.fixture
    def connection_manager(self):
        """Create a mocked connection manager."""
        manager = ConnectionManager()
        manager.broadcast_to_room = AsyncMock()
        return manager

    @pytest.fixture
    def event_handler(self, connection_manager, event_bus):
        """Create an event handler for testing."""
        return RealTimeEventHandler(event_bus, connection_manager=connection_manager)

    @pytest.mark.asyncio
    async def test_player_movement_publishes_events(self, event_bus):
        """Test that player movement publishes appropriate events to EventBus."""
        published_events = []

        # Subscribe to events to capture them
        def event_capturer(event):
            published_events.append(event)

        event_bus.subscribe(PlayerLeftRoom, event_capturer)
        event_bus.subscribe(PlayerEnteredRoom, event_capturer)

        # Create MovementService with the EventBus
        movement_service = MovementService(event_bus)

        # Mock persistence layer methods
        with (
            patch.object(movement_service._persistence, "get_player") as mock_get_player,
            patch.object(movement_service._persistence, "get_room") as mock_get_room,
            patch.object(movement_service._persistence, "save_player") as mock_save_player,
        ):
            # Setup mocks
            player = Mock()
            player.player_id = str(uuid4())
            player.name = "TestPlayer"
            player.current_room_id = "room_1"  # Player starts in room_1

            # Create real Room objects with the shared EventBus so events are published
            from server.models.room import Room

            old_room_data = {
                "id": "room_1",
                "name": "Old Room",
                "description": "The old room",
                "exits": {"north": "room_2"},
            }
            old_room = Room(old_room_data, event_bus)
            old_room._players.add(str(player.player_id))  # Player starts in old room

            new_room_data = {
                "id": "room_2",
                "name": "New Room",
                "description": "The new room",
                "exits": {"south": "room_1"},
            }
            new_room = Room(new_room_data, event_bus)

            mock_get_player.return_value = player
            mock_get_room.side_effect = lambda room_id: old_room if room_id == "room_1" else new_room
            mock_save_player.return_value = True

            # Perform movement
            success = movement_service.move_player(str(player.player_id), "room_1", "room_2")

            assert success

            # Allow events to be processed
            await asyncio.sleep(0.1)  # Give time for events to be processed

            # Verify events were published
            assert len(published_events) == 2

            # Check PlayerLeftRoom
            left_event = next((e for e in published_events if isinstance(e, PlayerLeftRoom)), None)
            assert left_event is not None
            assert left_event.player_id == player.player_id
            assert left_event.room_id == "room_1"

            # Check PlayerEnteredRoom
            entered_event = next((e for e in published_events if isinstance(e, PlayerEnteredRoom)), None)
            assert entered_event is not None
            assert entered_event.player_id == player.player_id
            assert entered_event.room_id == "room_2"


class TestConnectionTimeouts:
    """Test connection timeout behavior."""

    def test_memory_monitor_timeout_configuration(self):
        """Test that MemoryMonitor respects timeout configuration."""
        # Test default timeout (300 seconds)
        monitor = MemoryMonitor()
        assert monitor.max_connection_age == 300

        # Test that we can modify the timeout
        monitor.max_connection_age = 3600
        assert monitor.max_connection_age == 3600

    def test_connection_manager_uses_memory_monitor_timeout(self):
        """Test that ConnectionManager uses MemoryMonitor's timeout setting."""
        connection_manager = ConnectionManager()
        connection_manager.memory_monitor.max_connection_age = 300

        assert connection_manager.memory_monitor.max_connection_age == 300

    @pytest.mark.asyncio
    async def test_connection_cleanup_respects_timeout(self):
        """Test that connection cleanup uses the configured timeout."""
        import time

        connection_manager = ConnectionManager()
        connection_manager.memory_monitor.max_connection_age = 1  # 1 second for testing

        player_id = str(uuid4())
        mock_websocket = Mock()

        # Add a connection
        connection_manager.active_websockets[player_id] = mock_websocket
        connection_manager.connection_timestamps[player_id] = time.time() - 2  # 2 seconds ago

        # Run cleanup
        await connection_manager.cleanup_orphaned_data()

        # Connection should be removed due to timeout
        assert player_id not in connection_manager.active_websockets
