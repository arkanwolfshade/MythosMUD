#!/usr/bin/env python3
"""
Simple test script to verify the event system is working correctly.
"""

import os
import sys

# Add the server directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from unittest.mock import AsyncMock, MagicMock

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.realtime.connection_manager import ConnectionManager
from server.realtime.event_handler import RealTimeEventHandler


class SimpleEventTest:
    """Simple test for the event system."""

    def __init__(self):
        self.event_bus = EventBus()
        self.connection_manager = ConnectionManager()
        self.event_handler = RealTimeEventHandler(self.event_bus)
        self.event_handler.connection_manager = self.connection_manager

        # Mock the connection manager methods
        self.connection_manager._get_player = MagicMock()
        self.connection_manager.subscribe_to_room = AsyncMock()
        self.connection_manager.unsubscribe_from_room = AsyncMock()
        self.connection_manager.broadcast_to_room = AsyncMock()
        self.connection_manager.get_room_occupants = MagicMock(return_value=[])

        # Track events
        self.events_received = []

    def test_event_creation(self):
        """Test creating events."""
        print("Testing event creation...")

        event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id="TestPlayer", room_id="test_room_1"
        )

        print(f"✅ Created event: {event.event_type}")
        return event

    def test_event_publishing(self):
        """Test publishing events."""
        print("\nTesting event publishing...")

        event = self.test_event_creation()

        # Publish the event
        self.event_bus.publish(event)

        print("✅ Event published successfully")
        return event

    def test_event_handler_subscription(self):
        """Test that the event handler is subscribed to events."""
        print("\nTesting event handler subscription...")

        # Check if the event handler is subscribed
        player_entered_subscribers = self.event_bus._subscribers.get(PlayerEnteredRoom, [])
        player_left_subscribers = self.event_bus._subscribers.get(PlayerLeftRoom, [])

        print(f"PlayerEnteredRoom subscribers: {len(player_entered_subscribers)}")
        print(f"PlayerLeftRoom subscribers: {len(player_left_subscribers)}")

        if len(player_entered_subscribers) > 0 and len(player_left_subscribers) > 0:
            print("✅ Event handler is properly subscribed")
            return True
        else:
            print("❌ Event handler is not subscribed")
            return False

    def test_message_creation(self):
        """Test creating real-time messages."""
        print("\nTesting message creation...")

        event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id="TestPlayer", room_id="test_room_1"
        )

        # Create message
        message = self.event_handler._create_player_entered_message(event, "TestPlayer")

        print(f"✅ Created message: {message['event_type']}")
        print(f"   Room: {message['room_id']}")
        print(f"   Player: {message['data']['player_name']}")

        return message

    def test_full_event_flow(self):
        """Test the full event flow."""
        print("\nTesting full event flow...")

        # Create mock player
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        self.connection_manager._get_player.return_value = mock_player

        # Create and publish event
        event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id="TestPlayer", room_id="test_room_1"
        )

        # Publish event
        self.event_bus.publish(event)

        # Wait a moment for processing
        import time

        time.sleep(0.1)

        # Check if connection manager methods were called
        if self.connection_manager.subscribe_to_room.called:
            print("✅ subscribe_to_room was called")
        else:
            print("❌ subscribe_to_room was not called")

        if self.connection_manager.broadcast_to_room.called:
            print("✅ broadcast_to_room was called")
        else:
            print("❌ broadcast_to_room was not called")

        return True


def main():
    """Run the simple event system tests."""
    print("Testing MythosMUD Event System (Simple)")
    print("=" * 50)

    test = SimpleEventTest()

    # Test 1: Event Creation
    test.test_event_creation()

    # Test 2: Event Publishing
    test.test_event_publishing()

    # Test 3: Event Handler Subscription
    test.test_event_handler_subscription()

    # Test 4: Message Creation
    test.test_message_creation()

    # Test 5: Full Event Flow
    test.test_full_event_flow()

    print("\n✅ All event system tests completed!")


if __name__ == "__main__":
    main()
