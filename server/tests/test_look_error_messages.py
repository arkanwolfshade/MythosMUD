"""
Test error message consistency for the look command.

This test verifies that error messages are consistent across different scenarios.
"""

from unittest.mock import Mock, patch

import pytest

from server.commands.exploration_commands import handle_look_command
from server.utils.command_parser import parse_command

# Skip database setup for these tests
pytestmark = pytest.mark.skip_db_setup


class TestLookCommandErrorMessages:
    """Test error message consistency for look command."""

    @pytest.mark.asyncio
    async def test_no_matches_error_message(self):
        """Test that 'no matches' error message is consistent."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        current_user = Mock()
        current_user.name = "testuser"
        mock_alias_storage = Mock()

        # Mock player
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        # Mock room with NPCs that don't match
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.description = "A test room."
        mock_room.exits = {}
        mock_room.get_npcs.return_value = ["npc_001"]
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC that doesn't match
        mock_npc = Mock()
        mock_npc.name = "Merchant"
        mock_npc.description = "A friendly merchant."

        # Mock NPC service
        mock_npc_service = Mock()
        mock_npc_service.get_npc_by_id.return_value = mock_npc

        # Test various search terms that don't match
        test_cases = ["guard", "warrior", "knight", "wizard", "dragon"]

        for search_term in test_cases:
            with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
                parsed_cmd = parse_command(f"look {search_term}")
                command_data = {"target": parsed_cmd.target, "direction": parsed_cmd.direction}

                result = await handle_look_command(
                    command_data, current_user, mock_request, mock_alias_storage, "testuser"
                )

                # Verify consistent error message
                assert "result" in result
                assert result["result"] == "You don't see anyone like that here."

    @pytest.mark.asyncio
    async def test_no_valid_exit_error_message(self):
        """Test that 'no valid exit' error message is consistent."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        current_user = Mock()
        current_user.name = "testuser"
        mock_alias_storage = Mock()

        # Mock player
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        # Mock room with limited exits
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.description = "A test room."
        mock_room.exits = {"north": "room2"}  # Only north exit
        mock_room.get_npcs.return_value = []
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC service
        mock_npc_service = Mock()

        # Test various invalid directions
        invalid_directions = ["south", "east", "west", "up", "down", "northeast", "northwest", "southeast", "southwest"]

        for direction in invalid_directions:
            with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
                parsed_cmd = parse_command(f"look {direction}")
                command_data = {"target": parsed_cmd.target, "direction": parsed_cmd.direction}

                result = await handle_look_command(
                    command_data, current_user, mock_request, mock_alias_storage, "testuser"
                )

                # Verify consistent error message
                assert "result" in result
                assert result["result"] == "You see nothing special that way."

    @pytest.mark.asyncio
    async def test_no_persistence_error_message(self):
        """Test error message when persistence layer is not available."""
        # Setup mocks without persistence
        mock_request = Mock()
        mock_request.app.state.persistence = None  # No persistence

        current_user = Mock()
        current_user.name = "testuser"
        mock_alias_storage = Mock()

        # Test look command
        parsed_cmd = parse_command("look")
        command_data = {"target": parsed_cmd.target, "direction": parsed_cmd.direction}

        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

        # Verify error message
        assert "result" in result
        assert result["result"] == "You see nothing special."

    @pytest.mark.asyncio
    async def test_player_not_found_error_message(self):
        """Test error message when player is not found."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        current_user = Mock()
        current_user.name = "testuser"
        mock_alias_storage = Mock()

        # Mock persistence to return no player
        mock_persistence.get_player_by_name.return_value = None

        # Test look command
        parsed_cmd = parse_command("look")
        command_data = {"target": parsed_cmd.target, "direction": parsed_cmd.direction}

        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

        # Verify error message
        assert "result" in result
        assert result["result"] == "You see nothing special."

    @pytest.mark.asyncio
    async def test_room_not_found_error_message(self):
        """Test error message when room is not found."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        current_user = Mock()
        current_user.name = "testuser"
        mock_alias_storage = Mock()

        # Mock player
        mock_player = Mock()
        mock_player.current_room_id = "invalid_room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        # Mock persistence to return no room
        mock_persistence.get_room.return_value = None

        # Test look command
        parsed_cmd = parse_command("look")
        command_data = {"target": parsed_cmd.target, "direction": parsed_cmd.direction}

        result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

        # Verify error message
        assert "result" in result
        assert result["result"] == "You see nothing special."

    @pytest.mark.asyncio
    async def test_multiple_npc_matches_message_format(self):
        """Test that multiple NPC matches message format is consistent."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        current_user = Mock()
        current_user.name = "testuser"
        mock_alias_storage = Mock()

        # Mock player
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        # Mock room with multiple NPCs
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.description = "A test room."
        mock_room.exits = {}
        mock_room.get_npcs.return_value = ["npc_001", "npc_002", "npc_003"]
        mock_persistence.get_room.return_value = mock_room

        # Mock multiple NPCs
        mock_npc1 = Mock()
        mock_npc1.name = "City Guard"
        mock_npc1.description = "A stern guard."

        mock_npc2 = Mock()
        mock_npc2.name = "Guard Captain"
        mock_npc2.description = "A senior guard."

        mock_npc3 = Mock()
        mock_npc3.name = "Guard Dog"
        mock_npc3.description = "A loyal companion."

        # Mock NPC service
        mock_npc_service = Mock()

        def mock_get_npc_by_id(npc_id):
            if npc_id == "npc_001":
                return mock_npc1
            elif npc_id == "npc_002":
                return mock_npc2
            elif npc_id == "npc_003":
                return mock_npc3
            return None

        mock_npc_service.get_npc_by_id.side_effect = mock_get_npc_by_id

        # Test look command
        with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
            parsed_cmd = parse_command("look guard")
            command_data = {"target": parsed_cmd.target, "direction": parsed_cmd.direction}

            result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

            # Verify consistent message format
            assert "result" in result
            assert "You see several people here:" in result["result"]
            assert "City Guard" in result["result"]
            assert "Guard Captain" in result["result"]
            assert "Guard Dog" in result["result"]
            # Check that names are listed with dashes
            assert "- City Guard" in result["result"]
            assert "- Guard Captain" in result["result"]
            assert "- Guard Dog" in result["result"]

    @pytest.mark.asyncio
    async def test_single_npc_message_format(self):
        """Test that single NPC message format is consistent."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        current_user = Mock()
        current_user.name = "testuser"
        mock_alias_storage = Mock()

        # Mock player
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        # Mock room with single NPC
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.description = "A test room."
        mock_room.exits = {}
        mock_room.get_npcs.return_value = ["npc_001"]
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC
        mock_npc = Mock()
        mock_npc.name = "City Guard"
        mock_npc.description = "A stern-looking man in a weathered uniform."

        # Mock NPC service
        mock_npc_service = Mock()
        mock_npc_service.get_npc_by_id.return_value = mock_npc

        # Test look command
        with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
            parsed_cmd = parse_command("look guard")
            command_data = {"target": parsed_cmd.target, "direction": parsed_cmd.direction}

            result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

            # Verify consistent message format
            assert "result" in result
            assert result["result"] == "City Guard\nA stern-looking man in a weathered uniform."

    @pytest.mark.asyncio
    async def test_room_look_message_format(self):
        """Test that room look message format is consistent."""
        # Setup mocks
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        current_user = Mock()
        current_user.name = "testuser"
        mock_alias_storage = Mock()

        # Mock player
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.name = "Town Square"
        mock_room.description = "A bustling town square with people going about their business."
        mock_room.exits = {"north": "room2", "south": "room3"}
        mock_room.get_npcs.return_value = []
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC service
        mock_npc_service = Mock()

        # Test look command
        with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
            parsed_cmd = parse_command("look")
            command_data = {"target": parsed_cmd.target, "direction": parsed_cmd.direction}

            result = await handle_look_command(command_data, current_user, mock_request, mock_alias_storage, "testuser")

            # Verify consistent message format
            assert "result" in result
            assert "Town Square" in result["result"]
            assert "A bustling town square" in result["result"]
            assert "Exits: north, south" in result["result"]
