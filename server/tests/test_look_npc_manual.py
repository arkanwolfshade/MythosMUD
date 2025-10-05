"""
Manual test for NPC look command functionality.

This is a simple script to manually test the NPC look command without pytest.
"""

import asyncio
from unittest.mock import Mock, patch

from server.commands.exploration_commands import handle_look_command


async def test_npc_look_manual():
    """Manual test of NPC look command functionality."""
    print("Testing NPC look command...")

    # Setup mocks
    mock_request = Mock()
    mock_persistence = Mock()
    mock_request.app.state.persistence = mock_persistence
    mock_alias_storage = Mock()
    current_user = Mock()
    current_user.name = "testuser"

    # Mock player and room
    mock_player = Mock()
    mock_player.current_room_id = "test_room_001"
    mock_persistence.get_player_by_name.return_value = mock_player

    mock_room = Mock()
    mock_room.get_npcs.return_value = ["npc_001"]
    mock_room.exits = {}  # Add exits attribute
    mock_room.name = "Test Room"
    mock_room.description = "A test room for testing."
    mock_persistence.get_room.return_value = mock_room

    # Mock NPC instance
    mock_npc = Mock()
    mock_npc.name = "City Guard"
    mock_npc.description = "A stern-looking man in a weathered uniform."
    mock_npc.npc_type = "guard"

    # Mock NPC service
    mock_npc_service = Mock()
    mock_npc_service.get_npc_by_id.return_value = mock_npc

    # Test 1: Single NPC match
    print("\n1. Testing single NPC match...")
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
        command_data = {"target": "guard"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")
    print(f"Result: {result}")
    assert "City Guard" in result["result"]
    assert "A stern-looking man in a weathered uniform." in result["result"]
    print("✓ Single NPC match test passed")

    # Test 2: Case insensitive matching
    print("\n2. Testing case insensitive matching...")
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
        command_data = {"target": "GUARD"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")
    print(f"Result: {result}")
    assert "City Guard" in result["result"]
    print("✓ Case insensitive matching test passed")

    # Test 3: No matches
    print("\n3. Testing no matches...")
    mock_npc.name = "Merchant"  # Change NPC name to not match
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
        command_data = {"target": "guard"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")
    print(f"Result: {result}")
    assert result["result"] == "You don't see anyone like that here."
    print("✓ No matches test passed")

    # Test 4: No NPCs in room
    print("\n4. Testing no NPCs in room...")
    mock_room.get_npcs.return_value = []  # No NPCs
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
        command_data = {"target": "guard"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")
    print(f"Result: {result}")
    assert result["result"] == "You don't see anyone like that here."
    print("✓ No NPCs in room test passed")

    # Test 5: Fallback to direction
    print("\n5. Testing fallback to direction...")
    mock_room.get_npcs.return_value = ["npc_001"]
    mock_room.exits = {"north": "room2"}
    mock_npc.name = "Merchant"  # NPC doesn't match

    # Mock target room for direction look
    mock_target_room = Mock()
    mock_target_room.name = "Northern Room"
    mock_target_room.description = "A room to the north."
    mock_persistence.get_room.side_effect = (
        lambda room_id: mock_room if room_id == "test_room_001" else mock_target_room
    )

    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
        command_data = {"target": "north"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")
    print(f"Result: {result}")
    assert "Northern Room" in result["result"]
    assert "A room to the north." in result["result"]
    print("✓ Fallback to direction test passed")

    # Test 6: NPC priority over direction
    print("\n6. Testing NPC priority over direction...")
    mock_npc.name = "North"  # NPC matches direction
    mock_npc.description = "A person named North."

    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
        command_data = {"target": "north"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")
    print(f"Result: {result}")
    assert "North" in result["result"]
    assert "A person named North." in result["result"]
    assert "Northern Room" not in result["result"]  # Should not show direction result
    print("✓ NPC priority over direction test passed")

    print("\n🎉 All manual tests passed!")


if __name__ == "__main__":
    asyncio.run(test_npc_look_manual())
