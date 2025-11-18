"""
Tests for the EventBus system.

This module tests the EventBus class and event types to ensure proper
functionality of the pub/sub system for room state changes and player
movements.

As noted in the Pnakotic Manuscripts, proper testing of dimensional
event systems is essential for maintaining the integrity of our eldritch
architecture.

Updated to use pure asyncio patterns as per the architectural transformation
documented in the asyncio remediation tasks. The EventBus now operates
within async event loops, requiring proper async test coordination.
"""

import asyncio
from datetime import datetime

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import (
    BaseEvent,
    NPCEnteredRoom,
    NPCLeftRoom,
    ObjectAddedToRoom,
    ObjectRemovedFromRoom,
    PlayerEnteredRoom,
    PlayerLeftRoom,
)
from server.tests.conftest import TestingAsyncMixin


class TestEventTypes:
    """Test the event type classes."""

    def test_base_event_creation(self):
        """Test that BaseEvent can be created with proper defaults."""
        event = BaseEvent()
        event.event_type = "TestEvent"

        assert event.timestamp is not None
        assert isinstance(event.timestamp, datetime)
        assert event.event_type == "TestEvent"

    def test_player_entered_room_event(self):
        """Test PlayerEnteredRoom event creation."""
        event = PlayerEnteredRoom(player_id="player123", room_id="room456", from_room_id="room789")

        assert event.player_id == "player123"
        assert event.room_id == "room456"
        assert event.from_room_id == "room789"
        assert event.event_type == "PlayerEnteredRoom"

    def test_player_left_room_event(self):
        """Test PlayerLeftRoom event creation."""
        event = PlayerLeftRoom(player_id="player123", room_id="room456", to_room_id="room789")

        assert event.player_id == "player123"
        assert event.room_id == "room456"
        assert event.to_room_id == "room789"
        assert event.event_type == "PlayerLeftRoom"

    def test_object_added_to_room_event(self):
        """Test ObjectAddedToRoom event creation."""
        event = ObjectAddedToRoom(object_id="object123", room_id="room456", player_id="player789")

        assert event.object_id == "object123"
        assert event.room_id == "room456"
        assert event.player_id == "player789"
        assert event.event_type == "ObjectAddedToRoom"

    def test_object_removed_from_room_event(self):
        """Test ObjectRemovedFromRoom event creation."""
        event = ObjectRemovedFromRoom(object_id="object123", room_id="room456", player_id="player789")

        assert event.object_id == "object123"
        assert event.room_id == "room456"
        assert event.player_id == "player789"
        assert event.event_type == "ObjectRemovedFromRoom"

    def test_npc_entered_room_event(self):
        """Test NPCEnteredRoom event creation."""
        event = NPCEnteredRoom(npc_id="npc123", room_id="room456", from_room_id="room789")

        assert event.npc_id == "npc123"
        assert event.room_id == "room456"
        assert event.from_room_id == "room789"
        assert event.event_type == "NPCEnteredRoom"

    def test_npc_left_room_event(self):
        """Test NPCLeftRoom event creation."""
        event = NPCLeftRoom(npc_id="npc123", room_id="room456", to_room_id="room789")

        assert event.npc_id == "npc123"
        assert event.room_id == "room456"
        assert event.to_room_id == "room789"
        assert event.event_type == "NPCLeftRoom"


class TestEventBus(TestingAsyncMixin):
    """Test the EventBus class with async coordination."""

    @pytest.mark.asyncio
    async def test_event_bus_creation(self):
        """Test that EventBus can be created successfully."""
        event_bus = EventBus()

        assert event_bus is not None
        assert hasattr(event_bus, "_subscribers")
        assert hasattr(event_bus, "_event_queue")

        # Clean up the EventBus properly
        await event_bus.shutdown()
        assert hasattr(event_bus, "_running")

    @pytest.mark.asyncio
    async def test_event_bus_shutdown(self):
        """Test that EventBus can be shut down properly."""
        event_bus = EventBus()

        # Give the async processing time to start
        await asyncio.sleep(0.1)

        # Shutdown should not raise exceptions
        await event_bus.shutdown()

        # Verify shutdown
        assert not event_bus._running

    @pytest.mark.asyncio
    async def test_publish_invalid_event(self):
        """Test that publishing invalid events raises ValueError."""
        event_bus = EventBus()

        with pytest.raises(ValueError, match="Event must inherit from BaseEvent"):
            event_bus.publish("not an event")

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_subscribe_invalid_event_type(self):
        """Test that subscribing to invalid event types raises ValueError."""
        event_bus = EventBus()

        with pytest.raises(ValueError, match="Event type must inherit from BaseEvent"):
            event_bus.subscribe(str, lambda x: None)

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_subscribe_invalid_handler(self):
        """Test that subscribing with invalid handler raises ValueError."""
        event_bus = EventBus()

        with pytest.raises(ValueError, match="Handler must be callable"):
            event_bus.subscribe(PlayerEnteredRoom, "not callable")

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_subscribe_and_publish(self):
        """Test basic subscribe and publish functionality."""
        event_bus = EventBus()
        received_events = []

        def handler(event):
            received_events.append(event)

        # Subscribe to PlayerEnteredRoom events
        event_bus.subscribe(PlayerEnteredRoom, handler)

        # Create and publish an event
        event = PlayerEnteredRoom(player_id="player123", room_id="room456")
        event_bus.publish(event)

        # Give the async processing time to process
        await asyncio.sleep(0.1)

        assert len(received_events) == 1
        assert received_events[0] == event

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_multiple_subscribers(self):
        """Test that multiple subscribers receive the same event."""
        event_bus = EventBus()
        received_events_1 = []
        received_events_2 = []

        def handler1(event):
            received_events_1.append(event)

        def handler2(event):
            received_events_2.append(event)

        # Subscribe two handlers to the same event type
        event_bus.subscribe(PlayerEnteredRoom, handler1)
        event_bus.subscribe(PlayerEnteredRoom, handler2)

        # Create and publish an event
        event = PlayerEnteredRoom(player_id="player123", room_id="room456")
        event_bus.publish(event)

        # Give the async processing time to process
        await asyncio.sleep(0.1)

        assert len(received_events_1) == 1
        assert len(received_events_2) == 1
        assert received_events_1[0] == event
        assert received_events_2[0] == event

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_unsubscribe(self):
        """Test that unsubscribing removes the handler."""
        event_bus = EventBus()
        received_events = []

        def handler(event):
            received_events.append(event)

        # Subscribe and then unsubscribe
        event_bus.subscribe(PlayerEnteredRoom, handler)
        success = event_bus.unsubscribe(PlayerEnteredRoom, handler)

        assert success is True

        # Publish an event - should not be received
        event = PlayerEnteredRoom(player_id="player123", room_id="room456")
        event_bus.publish(event)

        # Give the async processing time to process
        await asyncio.sleep(0.1)

        assert len(received_events) == 0

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_unsubscribe_nonexistent_handler(self):
        """Test that unsubscribing non-existent handler returns False."""
        event_bus = EventBus()

        def handler(event):
            pass

        # Try to unsubscribe without subscribing first
        success = event_bus.unsubscribe(PlayerEnteredRoom, handler)

        assert success is False

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_get_subscriber_count(self):
        """Test getting subscriber count for specific event type."""
        event_bus = EventBus()

        def handler1(event):
            pass

        def handler2(event):
            pass

        # Initially no subscribers
        assert event_bus.get_subscriber_count(PlayerEnteredRoom) == 0

        # Add subscribers
        event_bus.subscribe(PlayerEnteredRoom, handler1)
        assert event_bus.get_subscriber_count(PlayerEnteredRoom) == 1

        event_bus.subscribe(PlayerEnteredRoom, handler2)
        assert event_bus.get_subscriber_count(PlayerEnteredRoom) == 2

        # Remove one subscriber
        event_bus.unsubscribe(PlayerEnteredRoom, handler1)
        assert event_bus.get_subscriber_count(PlayerEnteredRoom) == 1

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_get_all_subscriber_counts(self):
        """Test getting subscriber counts for all event types."""
        event_bus = EventBus()

        def handler(event):
            pass

        # Subscribe to multiple event types
        event_bus.subscribe(PlayerEnteredRoom, handler)
        event_bus.subscribe(PlayerLeftRoom, handler)
        event_bus.subscribe(ObjectAddedToRoom, handler)

        counts = event_bus.get_all_subscriber_counts()

        assert counts["PlayerEnteredRoom"] == 1
        assert counts["PlayerLeftRoom"] == 1
        assert counts["ObjectAddedToRoom"] == 1
        assert "NPCEnteredRoom" not in counts  # No subscribers

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_event_processing_error_handling(self):
        """Test that errors in event handlers don't crash the system."""
        event_bus = EventBus()
        received_events = []

        def error_handler(event):
            raise ValueError("Test error")

        def good_handler(event):
            received_events.append(event)

        # Subscribe both handlers
        event_bus.subscribe(PlayerEnteredRoom, error_handler)
        event_bus.subscribe(PlayerEnteredRoom, good_handler)

        # Publish an event
        event = PlayerEnteredRoom(player_id="player123", room_id="room456")
        event_bus.publish(event)

        # Give the async processing time to process
        await asyncio.sleep(0.1)

        # The good handler should still receive the event
        assert len(received_events) == 1
        assert received_events[0] == event

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_concurrent_operations(self):
        """Test that EventBus handles concurrent operations correctly."""
        event_bus = EventBus()
        received_events = []

        def handler(event):
            received_events.append(event)

        event_bus.subscribe(PlayerEnteredRoom, handler)

        # Create multiple async tasks that publish events
        async def publish_events():
            for i in range(10):
                event = PlayerEnteredRoom(player_id=f"player{i}", room_id=f"room{i}")
                event_bus.publish(event)
                await asyncio.sleep(0.01)

        # Create 5 concurrent tasks
        tasks = []
        for _ in range(5):
            task = asyncio.create_task(publish_events())
            tasks.append(task)

        # Wait for all tasks to complete
        await asyncio.gather(*tasks)

        # Give the async processing time to process all events
        await asyncio.sleep(0.5)

        # Should have received 50 events (5 tasks * 10 events each)
        assert len(received_events) == 50

        # Clean up the EventBus properly
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_cleanup_on_destruction(self):
        """Test that EventBus cleans up properly when destroyed."""
        event_bus = EventBus()

        # Publish an event to start the processing
        event = PlayerEnteredRoom(player_id="player123", room_id="room456")
        event_bus.publish(event)

        # Give the async processing time to start
        await asyncio.sleep(0.1)

        # Verify the processing is running
        assert event_bus._running
        assert event_bus._processing_task is not None

        # Clean up the EventBus properly before deletion
        await event_bus.shutdown()

        # Verify it's shut down
        assert not event_bus._running

        # Destroy the event bus
        del event_bus

        # Give time for cleanup
        await asyncio.sleep(0.1)

    @pytest.mark.asyncio
    async def test_structured_concurrency_multiple_async_subscribers(self):
        """
        Test that EventBus uses structured concurrency for multiple async subscribers.

        AnyIO Pattern: All async subscribers should run concurrently and complete
        even if some fail, using asyncio.gather with return_exceptions=True.
        """
        event_bus = EventBus()
        results = []
        errors = []

        async def subscriber1(event):
            await asyncio.sleep(0.01)
            results.append("subscriber1")
            return "result1"

        async def subscriber2(event):
            await asyncio.sleep(0.01)
            results.append("subscriber2")
            return "result2"

        async def failing_subscriber(event):
            await asyncio.sleep(0.01)
            errors.append("failing_subscriber")
            raise ValueError("Test error")

        # Subscribe all handlers
        event_bus.subscribe(PlayerEnteredRoom, subscriber1)
        event_bus.subscribe(PlayerEnteredRoom, subscriber2)
        event_bus.subscribe(PlayerEnteredRoom, failing_subscriber)

        # Publish an event
        event = PlayerEnteredRoom(player_id="player123", room_id="room456")
        event_bus.publish(event)

        # Give time for all subscribers to complete
        await asyncio.sleep(0.2)

        # All subscribers should have run (structured concurrency ensures all complete)
        assert len(results) == 2
        assert "subscriber1" in results
        assert "subscriber2" in results
        assert len(errors) == 1  # Failing subscriber should have run and failed

        # Verify tasks are cleaned up
        await asyncio.sleep(0.1)
        # Active tasks should be empty or contain only completed tasks
        for task in event_bus._active_tasks:
            assert task.done()

        # Clean up
        await event_bus.shutdown()

    @pytest.mark.asyncio
    async def test_structured_concurrency_task_cleanup(self):
        """
        Test that EventBus properly cleans up tasks after structured concurrency execution.

        AnyIO Pattern: Tasks created for async subscribers should be properly tracked
        and cleaned up after completion.
        """
        event_bus = EventBus()

        async def subscriber(event):
            await asyncio.sleep(0.05)
            return "done"

        event_bus.subscribe(PlayerEnteredRoom, subscriber)

        # Publish an event
        event = PlayerEnteredRoom(player_id="player123", room_id="room456")
        event_bus.publish(event)

        # Wait for processing
        await asyncio.sleep(0.1)

        # Tasks should be created and then cleaned up
        # After completion, active tasks should be empty or only contain done tasks
        await asyncio.sleep(0.1)
        for task in event_bus._active_tasks:
            assert task.done()

        # Clean up
        await event_bus.shutdown()
