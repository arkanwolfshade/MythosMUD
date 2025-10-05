"""
Simple tests for NPC look command functionality without database dependencies.

This module tests the extended look command that allows players to examine NPCs
in their current room by name, using mocks to avoid database setup issues.
"""

from unittest.mock import Mock

import pytest

from server.commands.exploration_commands import handle_look_command

# Skip database setup for these tests
pytestmark = pytest.mark.skip_db_setup


class TestLookNPCCommandSimple:
    """Test NPC look command functionality with simple mocks."""

    @pytest.mark.asyncio
    async def test_look_npc_single_match(self):
        """Test looking at a single NPC that matches the search term."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence
        mock_alias_storage = Mock()
        current_user = {"username": "testuser"}

        # Mock player and room
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = Mock()
        mock_room.get_npcs.return_value = ["npc_001"]
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC instance
        mock_npc = Mock()
        mock_npc.name = "City Guard"
        mock_npc.description = "A stern-looking man in a weathered uniform."
        mock_npc.npc_type = "guard"
        mock_persistence.get_npc_by_id.return_value = mock_npc

        # Test command
        command_data = {"target": "guard"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

        # Verify result
        assert "result" in result
        assert "City Guard" in result["result"]
        assert "A stern-looking man in a weathered uniform." in result["result"]
        mock_persistence.get_npc_by_id.assert_called_once_with("npc_001")

    @pytest.mark.asyncio
    async def test_look_npc_case_insensitive_matching(self):
        """Test that NPC matching is case-insensitive."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence
        mock_alias_storage = Mock()
        current_user = {"username": "testuser"}

        # Mock player and room
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = Mock()
        mock_room.get_npcs.return_value = ["npc_001"]
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC instance
        mock_npc = Mock()
        mock_npc.name = "City Guard"
        mock_npc.description = "A stern-looking man in a weathered uniform."
        mock_npc.npc_type = "guard"
        mock_persistence.get_npc_by_id.return_value = mock_npc

        # Test command with different case
        command_data = {"target": "GUARD"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

        # Verify result
        assert "result" in result
        assert "City Guard" in result["result"]

    @pytest.mark.asyncio
    async def test_look_npc_no_matches(self):
        """Test looking at NPCs when no matches are found."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence
        mock_alias_storage = Mock()
        current_user = {"username": "testuser"}

        # Mock player and room
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = Mock()
        mock_room.get_npcs.return_value = ["npc_001"]
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC instance that doesn't match
        mock_npc = Mock()
        mock_npc.name = "Merchant"
        mock_npc.description = "A friendly trader."
        mock_npc.npc_type = "merchant"
        mock_persistence.get_npc_by_id.return_value = mock_npc

        # Test command
        command_data = {"target": "guard"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

        # Verify error message
        assert "result" in result
        assert result["result"] == "You don't see anyone like that here."

    @pytest.mark.asyncio
    async def test_look_npc_no_npcs_in_room(self):
        """Test looking at NPCs when there are no NPCs in the room."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence
        mock_alias_storage = Mock()
        current_user = {"username": "testuser"}

        # Mock player and room
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = Mock()
        mock_room.get_npcs.return_value = []  # No NPCs
        mock_persistence.get_room.return_value = mock_room

        # Test command
        command_data = {"target": "guard"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

        # Verify error message
        assert "result" in result
        assert result["result"] == "You don't see anyone like that here."

    @pytest.mark.asyncio
    async def test_look_npc_fallback_to_direction(self):
        """Test that NPC look falls back to direction look when no NPCs match."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence
        mock_alias_storage = Mock()
        current_user = {"username": "testuser"}

        # Mock player and room
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = Mock()
        mock_room.get_npcs.return_value = ["npc_001"]
        mock_room.exits = {"north": "room2"}
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC instance that doesn't match
        mock_npc = Mock()
        mock_npc.name = "Merchant"
        mock_npc.description = "A friendly trader."
        mock_npc.npc_type = "merchant"
        mock_persistence.get_npc_by_id.return_value = mock_npc

        # Mock target room for direction look
        mock_target_room = Mock()
        mock_target_room.name = "Northern Room"
        mock_target_room.description = "A room to the north."
        mock_persistence.get_room.side_effect = (
            lambda room_id: mock_room if room_id == "test_room_001" else mock_target_room
        )

        # Test command with direction that also matches NPC search
        command_data = {"target": "north"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

        # Verify it falls back to direction look
        assert "result" in result
        assert "Northern Room" in result["result"]
        assert "A room to the north." in result["result"]

    @pytest.mark.asyncio
    async def test_look_npc_priority_over_direction(self):
        """Test that NPC look takes priority over direction look when both match."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence
        mock_alias_storage = Mock()
        current_user = {"username": "testuser"}

        # Mock player and room
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = Mock()
        mock_room.get_npcs.return_value = ["npc_001"]
        mock_room.exits = {"north": "room2"}
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC instance that matches
        mock_npc = Mock()
        mock_npc.name = "North"
        mock_npc.description = "A person named North."
        mock_npc.npc_type = "civilian"
        mock_persistence.get_npc_by_id.return_value = mock_npc

        # Test command
        command_data = {"target": "north"}
        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

        # Verify NPC look takes priority
        assert "result" in result
        assert "North" in result["result"]
        assert "A person named North." in result["result"]
        # Should not show direction look result
        assert "Northern Room" not in result["result"]
