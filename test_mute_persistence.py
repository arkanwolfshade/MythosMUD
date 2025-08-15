#!/usr/bin/env python3
"""
Test script for UserManager JSON persistence functionality.
"""

import json
import os
import sys

# Add the server directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from server.services.user_manager import UserManager


def test_mute_persistence():
    """Test the mute persistence functionality."""
    print("🧪 Testing UserManager JSON Persistence")
    print("=" * 50)

    # Create a test UserManager instance
    user_manager = UserManager()

    # Test player IDs
    player1_id = "test_player_1"
    player2_id = "test_player_2"

    print(f"📁 Data directory: {user_manager.data_dir}")

    # Test 1: Add some mutes
    print("\n1️⃣ Adding test mutes...")

    # Player 1 mutes Player 2
    success = user_manager.mute_player(
        muter_id=player1_id,
        muter_name="TestPlayer1",
        target_id=player2_id,
        target_name="TestPlayer2",
        duration_minutes=30,
        reason="Testing mute persistence",
    )
    print(f"   Player mute: {'✅' if success else '❌'}")

    # Player 1 mutes the "say" channel
    success = user_manager.mute_channel(
        player_id=player1_id,
        player_name="TestPlayer1",
        channel="say",
        duration_minutes=60,
        reason="Testing channel mute",
    )
    print(f"   Channel mute: {'✅' if success else '❌'}")

    # Player 1 globally mutes Player 2
    success = user_manager.mute_global(
        muter_id=player1_id,
        muter_name="TestPlayer1",
        target_id=player2_id,
        target_name="TestPlayer2",
        duration_minutes=120,
        reason="Testing global mute",
    )
    print(f"   Global mute: {'✅' if success else '❌'}")

    # Add Player 1 as admin
    user_manager.add_admin(player1_id, "TestPlayer1")
    print("   Admin status: ✅")

    # Test 2: Save mute data
    print("\n2️⃣ Saving mute data...")
    success1 = user_manager.save_player_mutes(player1_id)
    success2 = user_manager.save_player_mutes(player2_id)
    print(f"   Player 1 save: {'✅' if success1 else '❌'}")
    print(f"   Player 2 save: {'✅' if success2 else '❌'}")

    # Test 3: Check if files were created
    print("\n3️⃣ Checking file creation...")
    file1 = user_manager._get_player_mute_file(player1_id)
    file2 = user_manager._get_player_mute_file(player2_id)

    print(f"   Player 1 file: {file1}")
    print(f"   File exists: {'✅' if file1.exists() else '❌'}")
    print(f"   Player 2 file: {file2}")
    print(f"   File exists: {'✅' if file2.exists() else '❌'}")

    # Test 4: Read and display file contents
    print("\n4️⃣ File contents:")
    if file1.exists():
        with open(file1, encoding="utf-8") as f:
            data = json.load(f)
            print(f"   Player 1 data: {json.dumps(data, indent=2)}")

    # Test 5: Create new UserManager and load data
    print("\n5️⃣ Testing data loading...")
    new_user_manager = UserManager()

    # Load Player 1's data
    success = new_user_manager.load_player_mutes(player1_id)
    print(f"   Load Player 1: {'✅' if success else '❌'}")

    # Check if data was loaded correctly
    is_muted = new_user_manager.is_player_muted(player1_id, player2_id)
    is_channel_muted = new_user_manager.is_channel_muted(player1_id, "say")
    is_globally_muted = new_user_manager.is_globally_muted(player2_id)
    is_admin = new_user_manager.is_admin(player1_id)

    print(f"   Player mute loaded: {'✅' if is_muted else '❌'}")
    print(f"   Channel mute loaded: {'✅' if is_channel_muted else '❌'}")
    print(f"   Global mute loaded: {'✅' if is_globally_muted else '❌'}")
    print(f"   Admin status loaded: {'✅' if is_admin else '❌'}")

    # Test 6: Cleanup
    print("\n6️⃣ Testing cleanup...")
    success = new_user_manager.cleanup_player_mutes(player1_id)
    print(f"   Cleanup Player 1: {'✅' if success else '❌'}")
    print(f"   File deleted: {'✅' if not file1.exists() else '❌'}")

    print("\n🎉 Test completed!")


if __name__ == "__main__":
    test_mute_persistence()
