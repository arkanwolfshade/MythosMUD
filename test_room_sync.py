#!/usr/bin/env python3
"""
Test script to verify Room object synchronization.
"""

import os
import sys

# Add the server directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from server.persistence import get_persistence


def test_room_sync():
    """Test if Room objects are properly synchronized with the database."""

    # Get the persistence layer
    persistence = get_persistence()

    # Get a specific room
    room_id = "earth_arkham_city_northside_intersection_Derby_High"
    room = persistence.get_room(room_id)

    if not room:
        print(f"Room {room_id} not found!")
        return

    print(f"Room: {room.name} ({room.id})")
    print(f"Players in room: {room.get_players()}")
    print(f"Room object ID: {id(room)}")

    # Check if a specific player is in the room
    player_id = "7be08702-6557-4926-925f-ab2c033245e7"
    has_player = room.has_player(player_id)
    print(f"Player {player_id} in room: {has_player}")

    # Get the same room again to see if it's the same object
    room2 = persistence.get_room(room_id)
    print(f"Second room object ID: {id(room2)}")
    print(f"Same object: {room is room2}")

    # Check if the player is in the second room object
    has_player2 = room2.has_player(player_id)
    print(f"Player {player_id} in second room object: {has_player2}")

    # Check the _players set directly
    print(f"Room 1 _players set: {room._players}")
    print(f"Room 2 _players set: {room2._players}")
    print(f"Same _players set: {room._players is room2._players}")


if __name__ == "__main__":
    test_room_sync()
