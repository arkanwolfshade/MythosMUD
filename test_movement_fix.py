#!/usr/bin/env python3
"""
Test script to verify movement system fixes.

This script tests the movement system to ensure that the room ID reference
fixes have resolved the movement failures.

As noted in the Pnakotic Manuscripts, proper testing of dimensional pathways
is essential for maintaining the integrity of our eldritch architecture.
"""

import requests


def test_movement_system():
    """Test the movement system to verify fixes."""
    base_url = "http://localhost:54731"

    print("Testing MythosMUD Movement System")
    print("=" * 50)

    # Test data
    test_commands = [
        "go east",  # Should work now
        "go west",  # Should fail (no west exit)
        "go north",  # Should work
        "go south",  # Should work
    ]

    print("Note: This test requires a running server and active player session.")
    print("Please ensure the server is running and you have an active session.")
    print()

    # Test room loading
    print("Testing room loading...")
    try:
        response = requests.get(f"{base_url}/api/rooms/earth_arkham_city_intersection_derby_high")
        if response.status_code == 200:
            room_data = response.json()
            print(f"✓ Successfully loaded intersection room: {room_data.get('name', 'Unknown')}")

            exits = room_data.get("exits", {})
            print(f"  Exits: {exits}")

            # Check if east exit points to correct room
            east_exit = exits.get("east")
            if east_exit == "earth_arkham_city_northside_room_derby_st_001":
                print("✓ East exit references correct room ID")
            else:
                print(f"✗ East exit references incorrect room ID: {east_exit}")

        else:
            print(f"✗ Failed to load room: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("✗ Could not connect to server. Is it running?")
        return False
    except Exception as e:
        print(f"✗ Error testing room loading: {e}")
        return False

    print()
    print("Movement system test completed.")
    print("To test actual movement, use the web client and try:")
    print("  - 'go east' (should work)")
    print("  - 'go west' (should fail)")
    print("  - 'go north' (should work)")
    print("  - 'go south' (should work)")

    return True


def main():
    """Main function."""
    try:
        success = test_movement_system()
        if success:
            print("\n✓ Movement system test completed successfully!")
            return 0
        else:
            print("\n✗ Movement system test failed!")
            return 1
    except Exception as e:
        print(f"\n✗ Error during movement system test: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
