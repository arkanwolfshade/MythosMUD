#!/usr/bin/env python3
"""
Simple test to verify the movement validation fix.
"""

import os
import sys

# Add the server directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from unittest.mock import Mock

from server.game.movement_service import MovementService
from server.models.room import Room


def test_movement_validation_fix():
    """Test that the movement validation fix works correctly."""

    # Create mock event bus
    mock_event_bus = Mock()

    # Create movement service
    movement_service = MovementService(event_bus=mock_event_bus)

    # Create test rooms
    room_data_1 = {
        "id": "room_1",
        "name": "Test Room 1",
        "description": "A test room",
        "exits": {"north": "room_2", "south": None, "east": None, "west": None},
    }

    room_data_2 = {
        "id": "room_2",
        "name": "Test Room 2",
        "description": "Another test room",
        "exits": {"north": None, "south": "room_1", "east": None, "west": None},
    }

    room_1 = Room(room_data_1, event_bus=mock_event_bus)
    room_2 = Room(room_data_2, event_bus=mock_event_bus)

    # Create mock persistence
    mock_persistence = Mock()
    mock_persistence.get_room.side_effect = lambda room_id: {"room_1": room_1, "room_2": room_2}.get(room_id)

    # Create mock player
    mock_player = Mock()
    mock_player.player_id = "test_player_123"
    mock_player.current_room_id = "room_1"

    mock_persistence.get_player.return_value = mock_player

    # Replace the persistence in the movement service
    movement_service._persistence = mock_persistence

    print("Testing movement validation fix...")
    print(f"Room 1 exits: {room_1.exits}")
    print(f"Room 2 exits: {room_2.exits}")

    # Test 1: Player not in room's in-memory state but current_room_id matches
    print("\nTest 1: Player not in room's in-memory state but current_room_id matches")
    print(f"Player in room_1 before: {room_1.has_player('test_player_123')}")

    # The validation should add the player to the room and allow movement
    success = movement_service._validate_movement("test_player_123", "room_1", "room_2")

    print(f"Validation result: {success}")
    print(f"Player in room_1 after: {room_1.has_player('test_player_123')}")

    if success and room_1.has_player("test_player_123"):
        print("✅ Test 1 PASSED: Player was added to room and movement validated")
        return True
    else:
        print("❌ Test 1 FAILED: Player was not added to room or movement failed")
        return False


if __name__ == "__main__":
    success = test_movement_validation_fix()
    if success:
        print("\n🎉 Movement validation fix is working!")
    else:
        print("\n💥 Movement validation fix failed!")
        sys.exit(1)
