#!/usr/bin/env python3
"""
Test script to verify the movement fix is working.
"""

import os
import sys

# Add the server directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from server.game.movement_service import MovementService
from server.persistence import get_persistence
from server.realtime.event_handler import get_real_time_event_handler


def test_movement():
    """Test that movement works for player Ithaqua."""

    # Initialize the persistence and event handler
    event_handler = get_real_time_event_handler()
    persistence = get_persistence(event_bus=event_handler.event_bus)

    # Create movement service
    movement_service = MovementService(event_bus=event_handler.event_bus)

    # Get the player
    player = persistence.get_player_by_name("Ithaqua")
    if not player:
        print("ERROR: Player Ithaqua not found!")
        return False

    print(f"Found player: {player.name} (ID: {player.player_id})")
    print(f"Current room: {player.current_room_id}")

    # Get the current room
    current_room = persistence.get_room(player.current_room_id)
    if not current_room:
        print(f"ERROR: Current room {player.current_room_id} not found!")
        return False

    print(f"Current room: {current_room.name}")
    print(f"Available exits: {current_room.exits}")

    # Test moving north
    north_room_id = current_room.exits.get("north")
    if not north_room_id:
        print("ERROR: No north exit available!")
        return False

    print(f"Attempting to move north to: {north_room_id}")

    # Try the movement
    success = movement_service.move_player(player.player_id, player.current_room_id, north_room_id)

    if success:
        print("SUCCESS: Movement worked!")

        # Check if player is now in the new room
        updated_player = persistence.get_player_by_name("Ithaqua")
        print(f"Player is now in room: {updated_player.current_room_id}")

        # Check if the room has the player
        new_room = persistence.get_room(north_room_id)
        if new_room.has_player(player.player_id):
            print("SUCCESS: Player is properly in the new room!")
        else:
            print("WARNING: Player is not in the new room's in-memory state")

        return True
    else:
        print("ERROR: Movement failed!")
        return False


if __name__ == "__main__":
    print("Testing movement fix...")
    success = test_movement()
    if success:
        print("\n✅ Movement fix is working!")
    else:
        print("\n❌ Movement fix failed!")
        sys.exit(1)
