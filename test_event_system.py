#!/usr/bin/env python3
"""
Test script to verify the event system is working correctly.
"""

import os
import sys

# Set test environment variables
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///server/tests/data/players/test_players.db"
os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key-for-testing-only"
os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-for-testing-only"
os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-testing-only"
os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-testing-only"
os.environ["MYTHOSMUD_ADMIN_PASSWORD"] = "testpass123"
os.environ["ALIASES_DIR"] = "server/tests/data/players/aliases"
os.environ["DEBUG"] = "true"

# Add the server directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

# Import after path setup
from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom
from server.game.movement_service import MovementService
from server.models import Player
from server.models.room import Room
from server.persistence import get_persistence
from server.realtime.connection_manager import ConnectionManager
from server.realtime.event_handler import RealTimeEventHandler


class TestEventSystem:
    """Test the event system directly."""

    def __init__(self):
        self.event_bus = EventBus()
        self.connection_manager = ConnectionManager()
        self.event_handler = RealTimeEventHandler(self.event_bus)
        self.event_handler.connection_manager = self.connection_manager
        self.persistence = get_persistence()

        # Track events received
        self.events_received = []

    def setup_test_data(self):
        """Setup test data."""
        # Create test rooms
        room1 = Room(
            {
                "id": "test_room_1",
                "name": "Test Room 1",
                "description": "A test room",
                "exits": {"north": "test_room_2"},
            }
        )

        room2 = Room(
            {
                "id": "test_room_2",
                "name": "Test Room 2",
                "description": "Another test room",
                "exits": {"south": "test_room_1"},
            }
        )

        # Create test player
        player = Player(player_id="TestPlayer", name="TestPlayer", current_room_id="test_room_1")

        # Add to persistence
        self.persistence.save_player(player)
        self.persistence._room_cache["test_room_1"] = room1
        self.persistence._room_cache["test_room_2"] = room2

        return player, room1, room2

    def test_movement_service(self):
        """Test the movement service directly."""
        print("Testing MovementService...")

        player, room1, room2 = self.setup_test_data()

        # Create movement service
        movement_service = MovementService(self.event_bus)

        # Test moving player
        print(f"Player starts in room: {player.current_room_id}")

        success = movement_service.move_player("TestPlayer", "test_room_1", "test_room_2")

        print(f"Movement successful: {success}")
        print(f"Player now in room: {player.current_room_id}")

        return success

    def test_event_handler(self):
        """Test the event handler directly."""
        print("\nTesting EventHandler...")

        # Create test event
        event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id="TestPlayer", room_id="test_room_2"
        )

        # Publish event
        print("Publishing PlayerEnteredRoom event...")
        self.event_bus.publish(event)

        # Wait a moment for processing
        import time

        time.sleep(0.1)

        print("Event published successfully")

    def test_full_flow(self):
        """Test the full flow from movement to events."""
        print("\nTesting full flow...")

        player, room1, room2 = self.setup_test_data()

        # Create movement service with event bus
        movement_service = MovementService(self.event_bus)

        # Move player (this should trigger events)
        print("Moving player from room1 to room2...")
        success = movement_service.move_player("TestPlayer", "test_room_1", "test_room_2")

        if success:
            print("✅ Movement successful - events should have been triggered")
        else:
            print("❌ Movement failed")

        return success


def main():
    """Run the event system tests."""
    print("Testing MythosMUD Event System")
    print("=" * 40)

    test = TestEventSystem()

    # Test 1: Movement Service
    test.test_movement_service()

    # Test 2: Event Handler
    test.test_event_handler()

    # Test 3: Full Flow
    test.test_full_flow()

    print("\nEvent system tests completed!")


if __name__ == "__main__":
    main()
