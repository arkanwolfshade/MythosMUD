"""
Tests for real-time event timestamp normalization.

As noted in Prof. Armitage's marginalia, consistent chronology prevents madness
when correlating events across realms. These tests ensure all outbound
real-time messages use a single ISO 8601 UTC format with 'Z'.
"""

import asyncio
import re
from datetime import UTC, datetime
from unittest.mock import AsyncMock, Mock
from uuid import uuid4

import pytest

from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.realtime.event_handler import RealTimeEventHandler

TIMESTAMP_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


class TestEventHandlerTimestamps:
    """Verify that real-time messages carry normalized UTC timestamps."""

    def test_player_entered_message_timestamp(self) -> None:
        handler = RealTimeEventHandler()

        # Create event with a deterministic timestamp input; handler doesn't use it directly
        event = PlayerEnteredRoom(player_id="p1", room_id="r1")
        event.timestamp = datetime.now(UTC)

        message = handler._create_player_entered_message(event, "Alice")
        assert isinstance(message["timestamp"], str)
        assert TIMESTAMP_REGEX.match(message["timestamp"]) is not None

    def test_player_left_message_timestamp(self) -> None:
        handler = RealTimeEventHandler()

        event = PlayerLeftRoom(player_id="p1", room_id="r1")
        event.timestamp = datetime.now(UTC)

        message = handler._create_player_left_message(event, "Alice")
        assert isinstance(message["timestamp"], str)
        assert TIMESTAMP_REGEX.match(message["timestamp"]) is not None

    def test_timestamp_format_consistency(self) -> None:
        """Test that all timestamp formats are consistent across different message types."""
        handler = RealTimeEventHandler()

        # Test multiple events to ensure consistent formatting
        event1 = PlayerEnteredRoom(player_id="p1", room_id="r1")
        event1.timestamp = datetime.now(UTC)
        event2 = PlayerLeftRoom(player_id="p2", room_id="r1")
        event2.timestamp = datetime.now(UTC)

        message1 = handler._create_player_entered_message(event1, "Alice")
        message2 = handler._create_player_left_message(event2, "Bob")

        # Both should have the same timestamp format
        assert TIMESTAMP_REGEX.match(message1["timestamp"]) is not None
        assert TIMESTAMP_REGEX.match(message2["timestamp"]) is not None

        # Verify both follow the exact same format pattern
        assert len(message1["timestamp"]) == len(message2["timestamp"])
        assert message1["timestamp"].endswith("Z")
        assert message2["timestamp"].endswith("Z")

        # Verify the format structure is consistent
        assert message1["timestamp"][-1] == "Z"  # Both end with Z
        assert message2["timestamp"][-1] == "Z"  # Both end with Z

        # Verify the timestamp format structure (YYYY-MM-DDTHH:MM:SSZ)
        assert len(message1["timestamp"]) == 20  # 19 chars + Z
        assert message1["timestamp"][4] == "-"  # Year-month separator
        assert message1["timestamp"][7] == "-"  # Month-day separator
        assert message1["timestamp"][10] == "T"  # Date-time separator
        assert message1["timestamp"][13] == ":"  # Hour-minute separator
        assert message1["timestamp"][16] == ":"  # Minute-second separator


# ============================================================================
# Tests merged from test_event_handler_broadcasting_legacy.py
# ============================================================================


"""
Test RealTimeEventHandler broadcasting functionality.

This test suite verifies that the RealTimeEventHandler properly broadcasts
player_entered and player_left messages to room occupants.
"""


class TestEventHandlerBroadcasting:
    """Test RealTimeEventHandler broadcasting functionality."""

    @pytest.fixture
    def event_bus(self):
        """Create an EventBus with proper event loop setup."""
        from server.events import EventBus

        return EventBus()

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager."""
        cm = AsyncMock()
        cm.get_player = AsyncMock()
        cm._get_player = AsyncMock()  # Keep for backward compatibility
        cm.persistence = Mock()
        # Mock async_persistence with get_room_by_id (sync method)
        cm.async_persistence = Mock()
        cm.async_persistence.get_room_by_id = Mock()
        cm.broadcast_to_room = AsyncMock()
        cm.subscribe_to_room = AsyncMock()
        cm.unsubscribe_from_room = AsyncMock()
        cm.send_personal_message = AsyncMock()
        return cm

    @pytest.fixture
    def event_handler(self, event_bus, mock_connection_manager):
        """Create a RealTimeEventHandler with mocked dependencies."""
        handler = RealTimeEventHandler(event_bus, connection_manager=mock_connection_manager)
        # Also update player_handler's connection_manager
        handler.player_handler.connection_manager = mock_connection_manager
        return handler

    @pytest.mark.asyncio
    async def test_player_entered_event_broadcasting(self, event_bus, event_handler, mock_connection_manager):
        """Test that PlayerEnteredRoom events are properly broadcast."""
        # Set the main loop for async event handling
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

        # Setup mock room - use get_room_by_id (sync method)
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []  # Return empty list to avoid iteration errors
        mock_connection_manager.async_persistence.get_room_by_id.return_value = mock_room

        # Mock room sync service to pass through the event with the correct player_id
        def mock_process_event(evt):
            evt.sequence_number = 1
            return evt

        event_handler.room_sync_service.process_event_with_ordering = Mock(side_effect=mock_process_event)

        # Mock chat logger
        event_handler.chat_logger.log_player_joined_room = Mock()

        # Mock NPC instance service to avoid initialization errors
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = Mock()
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)

            # Create and publish event (use UUID for player_id)
            test_player_id = str(uuid4())
            event = PlayerEnteredRoom(player_id=test_player_id, room_id="test_room_001")

            # Publish the event
            event_bus.publish(event)

            # Wait for async processing
            await asyncio.sleep(0.2)

            # Verify that broadcast_to_room was called
            assert mock_connection_manager.broadcast_to_room.call_count >= 1

            # Get the call arguments
            calls = mock_connection_manager.broadcast_to_room.call_args_list
            player_entered_call = calls[0]  # First call should be player_entered

            # Verify the first call (player_entered)
            _room_id, message, exclude_player = (
                player_entered_call[0][0],
                player_entered_call[0][1],
                player_entered_call[1].get("exclude_player"),
            )
            assert message["event_type"] == "player_entered"
            assert message["data"]["player_name"] == "TestPlayer"
            assert message["data"]["message"] == "TestPlayer enters the room."
            assert exclude_player == test_player_id

    @pytest.mark.asyncio
    async def test_player_left_event_broadcasting(self, event_bus, event_handler, mock_connection_manager):
        """Test that PlayerLeftRoom events are properly broadcast."""
        # Set the main loop for async event handling
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

        # Setup mock room - use get_room_by_id (sync method)
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []  # Return empty list to avoid iteration errors
        mock_connection_manager.async_persistence.get_room_by_id.return_value = mock_room

        # Mock room sync service to pass through the event with the correct player_id
        def mock_process_event(evt):
            evt.sequence_number = 1
            return evt

        event_handler.room_sync_service.process_event_with_ordering = Mock(side_effect=mock_process_event)

        # Mock chat logger
        event_handler.chat_logger.log_player_left_room = Mock()

        # Mock NPC instance service to avoid initialization errors
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = Mock()
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)

            # Create and publish event (use UUID for player_id)
            test_player_id = str(uuid4())
            event = PlayerLeftRoom(player_id=test_player_id, room_id="test_room_001")

            # Publish the event
            event_bus.publish(event)

            # Wait for async processing
            await asyncio.sleep(0.2)

            # Verify that broadcast_to_room was called
            assert mock_connection_manager.broadcast_to_room.call_count >= 1

            # Get the call arguments
            calls = mock_connection_manager.broadcast_to_room.call_args_list
            player_left_call = calls[0]  # First call should be player_left

            # Verify the first call (player_left)
            _room_id, message, exclude_player = (
                player_left_call[0][0],
                player_left_call[0][1],
                player_left_call[1].get("exclude_player"),
            )
            assert message["event_type"] == "player_left"
            assert message["data"]["player_name"] == "TestPlayer"
            assert message["data"]["message"] == "TestPlayer leaves the room."
            assert exclude_player == test_player_id

    @pytest.mark.asyncio
    async def test_event_handler_handles_missing_player_gracefully(
        self,
        event_bus,
        event_handler,
        mock_connection_manager,  # pylint: disable=unused-argument
    ):
        """Test that RealTimeEventHandler handles missing players gracefully."""
        # Setup mock to return None for player lookup
        mock_connection_manager.get_player = AsyncMock(return_value=None)

        # Create and publish event
        event = PlayerEnteredRoom(player_id="nonexistent_player", room_id="test_room_001")

        # Publish the event
        event_bus.publish(event)

        # Wait for async processing
        await asyncio.sleep(0.2)

        # Verify that broadcast_to_room was NOT called (since player not found)
        mock_connection_manager.broadcast_to_room.assert_not_called()

    @pytest.mark.asyncio
    async def test_event_handler_handles_missing_room_gracefully(
        self,
        event_bus,
        event_handler,
        mock_connection_manager,  # pylint: disable=unused-argument
    ):
        """Test that RealTimeEventHandler handles missing rooms gracefully."""
        # Set the main loop for async event handling
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

        # Setup mock to return None for room lookup
        mock_connection_manager.async_persistence.get_room_by_id.return_value = None

        # Mock NPC instance service to avoid initialization errors
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = Mock()
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)

            # Create and publish event (use UUID for player_id)
            test_player_id = str(uuid4())
            event = PlayerEnteredRoom(player_id=test_player_id, room_id="nonexistent_room")

            # Publish the event
            event_bus.publish(event)

            # Wait for async processing
            await asyncio.sleep(0.2)

            # Verify that broadcast_to_room was still called (with room_id as string)
            assert mock_connection_manager.broadcast_to_room.call_count >= 1

    def test_message_creation_formats(self, event_handler):
        """Test that message creation methods return properly formatted messages."""
        # Test player entered message (use UUID string for player_id)
        test_player_id = str(uuid4())
        entered_event = PlayerEnteredRoom(player_id=test_player_id, room_id="test_room")
        entered_message = event_handler._create_player_entered_message(entered_event, "TestPlayer")

        assert entered_message["event_type"] == "player_entered"
        assert entered_message["data"]["player_id"] == test_player_id
        assert entered_message["data"]["player_name"] == "TestPlayer"
        assert entered_message["data"]["message"] == "TestPlayer enters the room."
        assert "timestamp" in entered_message
        assert "sequence_number" in entered_message

        # Test player left message (use UUID string for player_id)
        test_player_id = str(uuid4())
        left_event = PlayerLeftRoom(player_id=test_player_id, room_id="test_room")
        left_message = event_handler._create_player_left_message(left_event, "TestPlayer")

        assert left_message["event_type"] == "player_left"
        assert left_message["data"]["player_id"] == test_player_id
        assert left_message["data"]["player_name"] == "TestPlayer"
        assert left_message["data"]["message"] == "TestPlayer leaves the room."
        assert "timestamp" in left_message
        assert "sequence_number" in left_message
