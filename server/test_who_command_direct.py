#!/usr/bin/env python3
"""
Direct test of handle_who_command function from within the server directory.
"""

import asyncio
import os
import time
from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

# Set up environment variables
os.environ["ENVIRONMENT"] = "unit_test"
os.environ["DATABASE_PATH"] = "data/unit_test/players.db"
os.environ["NPC_DATABASE_PATH"] = "data/unit_test/npcs.db"
os.environ["DEFAULT_PLAYER_ROOM"] = "earth_arkhamcity_northside_intersection_derby_high"
os.environ["ALIASES_DIRECTORY"] = "data/unit_test/aliases"
os.environ["LOG_LEVEL"] = "DEBUG"
os.environ["PORT"] = "54731"
os.environ["HOST"] = "localhost"
os.environ["SECRET_KEY"] = "test-secret-key"


async def test_who_command():
    try:
        from commands.utility_commands import handle_who_command

        # Create mock objects
        mock_request = MagicMock()
        mock_alias_storage = MagicMock()
        mock_persistence = MagicMock()

        # Create a large list of players (2000 players)
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        players = []

        print("Creating 2000 mock players...")
        for i in range(2000):
            player = MagicMock()
            player.name = f"player_{i:04d}"
            player.level = (i % 50) + 1
            player.current_room_id = f"earth_arkhamcity_room_{i:04d}"
            player.is_admin = i % 50 == 0
            player.last_active = recent_time
            players.append(player)

        mock_persistence.list_players.return_value = players
        mock_request.app.state.persistence = mock_persistence

        # Test the command
        print("Executing handle_who_command with 2000 players...")
        start_time = time.time()

        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        end_time = time.time()
        print(f"Command completed in {end_time - start_time:.2f} seconds")
        print(f"Result length: {len(result['result'])} characters")
        print(f"Result preview: {result['result'][:100]}...")

        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        return False


async def test_who_command_multiple_iterations():
    """Test the command multiple times like in the original test."""
    try:
        from commands.utility_commands import handle_who_command

        # Create mock objects
        mock_request = MagicMock()
        mock_alias_storage = MagicMock()
        mock_persistence = MagicMock()

        # Create a large list of players (2000 players)
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        players = []

        print("Creating 2000 mock players...")
        for i in range(2000):
            player = MagicMock()
            player.name = f"player_{i:04d}"
            player.level = (i % 50) + 1
            player.current_room_id = f"earth_arkhamcity_room_{i:04d}"
            player.is_admin = i % 50 == 0
            player.last_active = recent_time
            players.append(player)

        mock_persistence.list_players.return_value = players
        mock_request.app.state.persistence = mock_persistence

        # Execute who command multiple times (like in the original test)
        print("Executing who command 10 times...")
        for iteration in range(10):
            print(f"  Iteration {iteration + 1}/10...")

            result = await handle_who_command(
                {"target_player": ""},
                {"username": "testuser"},
                mock_request,
                mock_alias_storage,
                "testuser",
            )

            if "Online Players (2000):" not in result["result"]:
                print(f"ERROR: Unexpected result in iteration {iteration + 1}: {result['result'][:100]}...")
                return False

        print("All 10 iterations completed successfully!")
        return True

    except Exception as e:
        print(f"Error in multiple iterations test: {e}")
        import traceback

        traceback.print_exc()
        return False


async def main():
    print("Starting direct who command testing...")

    # Test 1: Single execution
    print("\n=== Test 1: Single execution ===")
    if not await test_who_command():
        print("Single execution test failed")
        return

    # Test 2: Multiple iterations
    print("\n=== Test 2: Multiple iterations ===")
    if not await test_who_command_multiple_iterations():
        print("Multiple iterations test failed")
        return

    print("\nAll tests completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
