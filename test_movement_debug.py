#!/usr/bin/env python3
"""
Debug script to test the movement system.
"""

import os
import sys

# Add the server directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from server.models.room import Room


def test_movement():
    """Test the movement system with a simple scenario."""

    # Load the room data
    room_data = {
        "id": "earth_arkham_city_northside_intersection_derby_high",
        "name": "W. Derby and High Lane Intersection",
        "description": "The intersection where W. Derby Street meets High Lane.",
        "plane": "earth",
        "zone": "arkham_city",
        "sub_zone": "northside",
        "environment": "outdoors",
        "exits": {
            "north": "earth_arkham_city_northside_room_high_ln_002",
            "south": "earth_arkham_city_northside_room_high_ln_003",
            "east": "earth_arkham_city_northside_room_derby_st_001",
            "west": None,
            "up": None,
            "down": None,
        },
    }

    # Create a room
    room = Room(room_data)

    # Add a test player to the room
    test_player_id = "test-player-123"
    room.player_entered(test_player_id)

    print(f"Room ID: {room.id}")
    print(f"Room players: {room.get_players()}")
    print(f"Has player {test_player_id}: {room.has_player(test_player_id)}")
    print(f"Room exits: {room.exits}")

    # Test movement validation
    target_room_id = room.exits["north"]
    print(f"Target room ID: {target_room_id}")

    # Test the validation
    from_room = room
    to_room_id = target_room_id

    # Check if player is in the from_room
    print(f"Player {test_player_id} in room {from_room.id}: {from_room.has_player(test_player_id)}")

    # Test the exit validation
    exits = from_room.exits
    target_room_id_from_exits = exits.get("north")
    print(f"Target room from exits: {target_room_id_from_exits}")
    print(f"Target room matches: {target_room_id_from_exits == to_room_id}")


if __name__ == "__main__":
    test_movement()
