#!/usr/bin/env python3
"""
Test script to verify occupant tracking functionality.
"""

import os
import sys

# Add server directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from server.persistence import get_persistence


def test_occupant_tracking():
    """Test the occupant tracking functionality."""
    print("Testing occupant tracking...")

    # Get persistence layer
    persistence = get_persistence()

    # Test room ID
    room_id = "earth_arkham_city_northside_Derby_High"

    # Get players in room
    players = persistence.get_players_in_room(room_id)

    print(f"Players in room {room_id}:")
    for player in players:
        print(f"  - {player.name} (ID: {player.player_id})")

    print(f"Total players in room: {len(players)}")

    return len(players) > 0


if __name__ == "__main__":
    success = test_occupant_tracking()
    if success:
        print("✅ Occupant tracking test passed!")
    else:
        print("❌ Occupant tracking test failed!")
