"""
Tests for command_handler_unified.py - Command handling system.

This module tests the unified command handler which processes player commands
including security validation, alias expansion, and command execution.
"""

import importlib.util
import os
from unittest.mock import Mock

import pytest

from server.command_handler_unified import (
    clean_command_input,
    get_help_content,
    get_username_from_user,
    normalize_command,
    process_command,
)
from server.exceptions import ValidationError

from ..models.room import Room

# Import models.py directly to avoid package conflicts
spec = importlib.util.spec_from_file_location(
    "models_module", os.path.join(os.path.dirname(__file__), "..", "models.py")
)
models_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(models_module)

# Test data
test_room_data = {
    "room_id": "test_room_001",
    "name": "Test Room",
    "description": "A test room for testing purposes.",
    "exits": {"north": "test_room_002"},
    "zone": "test_zone",
}

test_player_data = {
    "player_id": "test_player_001",
    "username": "testuser",
    "current_room_id": "test_room_001",
    "is_admin": False,
    "is_muted": False,
    "mute_expires_at": None,
    "pose": None,
}


class TestCommandInputCleaning:
    """Test command input cleaning and normalization."""

    def test_clean_command_input_basic(self):
        """Test basic command cleaning."""
        assert clean_command_input("look") == "look"
        assert clean_command_input("  look  ") == "look"
        assert clean_command_input("go   north") == "go north"
        assert clean_command_input("say    hello    world") == "say hello world"

    def test_clean_command_input_edge_cases(self):
        """Test command cleaning with edge cases."""
        test_cases = [
            ("", ""),
            ("   ", ""),
            ("\t\n\r", ""),
            ("  look  ", "look"),
            ("go\t\tnorth", "go north"),
        ]

        for input_cmd, expected in test_cases:
            result = clean_command_input(input_cmd)
            assert result == expected, f"Expected '{expected}', got '{result}'"

    def test_normalize_command_basic(self):
        """Test basic command normalization."""
        assert normalize_command("look") == "look"
        assert normalize_command("/look") == "look"
        assert normalize_command("  /look  ") == "look"
        assert normalize_command("/go north") == "go north"

    def test_normalize_command_edge_cases(self):
        """Test command normalization with edge cases."""
        test_cases = [
            ("", ""),
            ("   ", ""),
            ("/", ""),
            ("/   ", ""),
            ("look", "look"),
            ("/look", "look"),
        ]

        for input_cmd, expected in test_cases:
            result = normalize_command(input_cmd)
            assert result == expected, f"Expected '{expected}', got '{result}'"


class TestHelpSystem:
    """Test help system functionality."""

    def test_get_help_content_no_command(self):
        """Test getting general help content."""
        result = get_help_content()
        assert "MythosMUD Help System" in result
        assert "Exploration Commands" in result
        assert "Movement Commands" in result
        assert "Communication Commands" in result
        assert "System Commands" in result

    def test_get_help_content_unknown_command(self):
        """Test getting help for unknown command."""
        result = get_help_content("unknown_command")
        assert "Command Not Found" in result
        assert "unknown_command" in result

    def test_get_help_content_specific_command(self):
        """Test getting help for specific command."""
        result = get_help_content("look")
        assert "look" in result.lower()
        assert "examine" in result.lower()

    def test_commands_structure(self):
        """Test that help content has proper structure."""
        result = get_help_content()
        assert "Exploration Commands" in result
        assert "Movement Commands" in result
        assert "Communication Commands" in result
        assert "System Commands" in result


class TestCommandProcessing:
    """Test command processing functionality."""

    @pytest.mark.asyncio
    async def test_process_command_look(self):
        """Test processing look command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock room data
        mock_room = Mock(spec=Room)
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"north": "room2"}
        mock_request.app.state.persistence.get_room.return_value = mock_room

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player

        result = await process_command("look", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "Test Room" in result["result"]
        assert "A test room" in result["result"]
        assert "Exits: north" in result["result"]

    @pytest.mark.asyncio
    async def test_process_command_go(self):
        """Test processing go command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock room data
        mock_room = Mock(spec=Room)
        mock_room.name = "North Room"
        mock_room.description = "A room to the north"
        mock_room.exits = {}
        mock_request.app.state.persistence.get_room.return_value = mock_room

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player

        result = await process_command("go", ["north"], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result

    @pytest.mark.asyncio
    async def test_process_command_help(self):
        """Test processing help command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        result = await process_command("help", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        # New command validation expects different format
        assert "help" in result["result"].lower() or "usage" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_unknown(self):
        """Test processing unknown command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        result = await process_command(
            "unknown_command", [], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result
        assert "Unknown command" in result["result"]

    @pytest.mark.asyncio
    async def test_process_command_alias(self):
        """Test processing alias command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock alias storage
        mock_alias_storage.get_alias_count.return_value = 5
        mock_alias_storage.validate_alias_name.return_value = True
        mock_alias_storage.validate_alias_command.return_value = True

        result = await process_command(
            "alias", ["n", "go", "north"], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result


class TestCommandValidation:
    """Test command validation edge cases."""

    def test_command_length_validation(self):
        """Test command length validation."""
        # Test various command lengths
        short_cmd = "look"
        assert normalize_command(short_cmd) == "look"

    def test_command_cleaning_edge_cases(self):
        """Test command cleaning with edge cases."""
        test_cases = [
            ("", ""),
            ("   ", ""),
            ("\t\n\r", ""),
            ("  look  ", "look"),
            ("go\t\tnorth", "go north"),
        ]

        for input_cmd, expected in test_cases:
            result = clean_command_input(input_cmd)
            assert result == expected, f"Expected '{expected}', got '{result}'"


class TestUtilityFunctions:
    """Test utility functions."""

    def test_get_username_from_user_dict(self):
        """Test extracting username from dictionary."""
        user_dict = {"username": "testuser"}
        assert get_username_from_user(user_dict) == "testuser"

    def test_get_username_from_user_object(self):
        """Test extracting username from object."""
        user_obj = Mock()
        user_obj.username = "testuser"
        assert get_username_from_user(user_obj) == "testuser"

    def test_get_username_from_user_name_key(self):
        """Test extracting username using name key."""
        user_dict = {"name": "testuser"}
        assert get_username_from_user(user_dict) == "testuser"

    def test_get_username_from_user_name_attr(self):
        """Test extracting username using name attribute."""
        user_obj = Mock()
        # Set name attribute directly to ensure it's a string
        user_obj.name = "testuser"
        # Remove username attribute to ensure it uses name
        del user_obj.username
        assert get_username_from_user(user_obj) == "testuser"

    def test_get_username_from_user_invalid(self):
        """Test extracting username from invalid object."""
        user_obj = Mock()
        # Remove username and name attributes
        del user_obj.username
        del user_obj.name

        with pytest.raises(ValidationError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_obj)
