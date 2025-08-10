#!/usr/bin/env python3
"""
Simple test script to debug room loader issues.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "room_validator"))

from core.room_loader import RoomLoader


def main():
    """Test the room loader."""
    print("Testing room loader...")

    loader = RoomLoader("./data/rooms")

    try:
        print("Building room database...")
        room_database = loader.build_room_database(show_progress=False)
        print(f"Found {len(room_database)} rooms")

        print("Getting zones...")
        zones = loader.get_zones()
        print(f"Zones: {zones}")

        if zones:
            print(f"Testing get_rooms_by_zone for {zones[0]}...")
            zone_rooms = loader.get_rooms_by_zone(zones[0])
            print(f"Type: {type(zone_rooms)}")
            print(f"Content: {zone_rooms}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
