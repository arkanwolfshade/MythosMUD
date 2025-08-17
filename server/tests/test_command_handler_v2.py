"""
Tests for Command Handler v2 - Integrated Pydantic + Click validation system.

This test suite validates the new command handling system that integrates our
robust Pydantic + Click validation with the existing MythosMUD infrastructure.

As the ancient texts suggest: "Testing is the foundation upon which all
knowledge must be built, lest we build upon shifting sands."
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ..command_handler_v2 import (
    CommandRequest,
    clean_command_input,
    handle_command,
    normalize_command,
    process_command_with_validation,
)
from ..utils.command_processor import CommandProcessor, get_command_processor


class TestCommandHandlerV2:
    """Test the new command handler v2 functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.command_processor = get_command_processor()

    def test_normalize_command(self):
        """Test command normalization."""
        # Test with slash prefix
        assert normalize_command("/look north") == "look north"
        assert normalize_command("/say hello") == "say hello"

        # Test without slash prefix
        assert normalize_command("look north") == "look north"
        assert normalize_command("say hello") == "say hello"

        # Test edge cases
        assert normalize_command("") == ""
        assert normalize_command("/") == ""
        assert normalize_command("   /look   ") == "look"

    def test_clean_command_input(self):
        """Test command input cleaning."""
        # Test multiple spaces
        assert clean_command_input("look    north") == "look north"
        assert clean_command_input("say   hello   world") == "say hello world"

        # Test leading/trailing whitespace
        assert clean_command_input("  look north  ") == "look north"

        # Test edge cases
        assert clean_command_input("") == ""
        assert clean_command_input("   ") == ""

    @pytest.mark.asyncio
    async def test_handle_command_authentication_required(self):
        """Test that authentication is required."""
        from fastapi import HTTPException

        request = CommandRequest(command="look")

        with pytest.raises(HTTPException) as exc_info:
            await handle_command(request, current_user=None, request=None)

        assert exc_info.value.status_code == 401
        assert exc_info.value.detail == "Authentication required"

    @pytest.mark.asyncio
    async def test_handle_command_too_long(self):
        """Test command length validation."""
        from fastapi import HTTPException

        # Create a command that exceeds the limit
        long_command = "say " + "a" * 1001
        request = CommandRequest(command=long_command)
        current_user = {"username": "testuser"}

        with pytest.raises(HTTPException) as exc_info:
            await handle_command(request, current_user=current_user, request=None)

        assert exc_info.value.status_code == 400
        assert "Command too long" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_handle_command_empty_after_cleaning(self):
        """Test handling of empty commands after cleaning."""
        request = CommandRequest(command="   ")
        current_user = {"username": "testuser"}

        result = await handle_command(request, current_user=current_user, request=None)
        assert result == {"result": ""}

    @pytest.mark.asyncio
    async def test_handle_command_empty_after_normalization(self):
        """Test handling of empty commands after normalization."""
        request = CommandRequest(command="/")
        current_user = {"username": "testuser"}

        result = await handle_command(request, current_user=current_user, request=None)
        assert result == {"result": ""}

    @pytest.mark.asyncio
    @patch("server.command_handler_v2.AliasStorage")
    async def test_handle_command_with_alias_expansion(self, mock_alias_storage):
        """Test command handling with alias expansion."""
        # Mock alias storage
        mock_storage = MagicMock()
        mock_alias = MagicMock()
        mock_alias.name = "test_alias"
        mock_alias.get_expanded_command.return_value = "look north"
        mock_storage.get_alias.return_value = mock_alias
        mock_alias_storage.return_value = mock_storage

        request = CommandRequest(command="test_alias")
        current_user = {"username": "testuser"}

        # Mock the validation system to return a valid look command
        with patch.object(self.command_processor, "process_command_string") as mock_process:
            mock_process.return_value = (MagicMock(), None, "look")

            with patch("server.command_handler_v2.handle_look_command") as mock_look:
                mock_look.return_value = {"result": "You see a room to the north."}

                await handle_command(request, current_user=current_user, request=None)

                # Verify alias was expanded
                mock_storage.get_alias.assert_called_once_with("testuser", "test_alias")
                mock_alias.get_expanded_command.assert_called_once_with([])

                # Verify the expanded command was processed
                mock_process.assert_called()
                mock_look.assert_called()

    @pytest.mark.asyncio
    @patch("server.command_handler_v2.AliasStorage")
    async def test_handle_command_validation_failure(self, mock_alias_storage):
        """Test command handling when validation fails."""
        # Mock alias storage
        mock_storage = MagicMock()
        mock_storage.get_alias.return_value = None
        mock_alias_storage.return_value = mock_storage

        request = CommandRequest(command="invalid command")
        current_user = {"username": "testuser"}

        # Mock the validation system to return an error
        with patch.object(self.command_processor, "process_command_string") as mock_process:
            mock_process.return_value = (None, "Invalid command format", None)

            result = await handle_command(request, current_user=current_user, request=None)

            assert result == {"result": "Invalid command format"}

    @pytest.mark.asyncio
    async def test_process_command_with_validation_success(self):
        """Test successful command processing with validation."""
        current_user = {"username": "testuser"}
        request = MagicMock()
        alias_storage = MagicMock()
        player_name = "testuser"
        command_line = "look north"

        # Mock the command processor
        mock_command = MagicMock()
        mock_command.command_type.value = "look"

        with patch.object(self.command_processor, "process_command_string") as mock_process:
            with patch.object(self.command_processor, "extract_command_data") as mock_extract:
                mock_process.return_value = (mock_command, None, "look")
                mock_extract.return_value = {"command_type": "look", "direction": "north"}

                with patch("server.command_handler_v2.handle_look_command") as mock_look:
                    mock_look.return_value = {"result": "You see a room to the north."}

                    result = await process_command_with_validation(
                        command_line, current_user, request, alias_storage, player_name
                    )

                    assert result == {"result": "You see a room to the north."}
                    mock_process.assert_called_once_with(command_line, player_name)
                    mock_extract.assert_called_once_with(mock_command)
                    mock_look.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_command_with_validation_error(self):
        """Test command processing when validation returns an error."""
        current_user = {"username": "testuser"}
        request = MagicMock()
        alias_storage = MagicMock()
        player_name = "testuser"
        command_line = "invalid command"

        # Mock the command processor to return an error
        with patch.object(self.command_processor, "process_command_string") as mock_process:
            mock_process.return_value = (None, "Invalid command format", None)

            result = await process_command_with_validation(
                command_line, current_user, request, alias_storage, player_name
            )

            assert result == {"result": "Invalid command format"}

    @pytest.mark.asyncio
    async def test_process_command_with_validation_no_command(self):
        """Test command processing when no validated command is returned."""
        current_user = {"username": "testuser"}
        request = MagicMock()
        alias_storage = MagicMock()
        player_name = "testuser"
        command_line = "unknown command"

        # Mock the command processor to return no command
        with patch.object(self.command_processor, "process_command_string") as mock_process:
            mock_process.return_value = (None, None, None)

            result = await process_command_with_validation(
                command_line, current_user, request, alias_storage, player_name
            )

            assert result == {"result": "Invalid command format"}

    @pytest.mark.asyncio
    async def test_process_command_with_validation_exception(self):
        """Test command processing when an exception occurs."""
        current_user = {"username": "testuser"}
        request = MagicMock()
        alias_storage = MagicMock()
        player_name = "testuser"
        command_line = "look north"

        # Mock the command processor to raise an exception
        with patch.object(self.command_processor, "process_command_string") as mock_process:
            mock_process.side_effect = Exception("Unexpected error")

            result = await process_command_with_validation(
                command_line, current_user, request, alias_storage, player_name
            )

            assert result == {"result": "An error occurred while processing your command."}

    @pytest.mark.asyncio
    async def test_handle_look_command_success(self):
        """Test successful look command handling."""
        from server.command_handler_v2 import handle_look_command

        validated_command = MagicMock()
        command_data = {"direction": "north"}
        current_user = {"username": "testuser"}

        # Mock persistence and player data
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.current_room_id = "room_1"
        mock_room = MagicMock()
        mock_room.exits = {"north": "room_2"}
        mock_target_room = MagicMock()
        mock_target_room.name = "Northern Room"
        mock_target_room.description = "A room to the north."

        mock_persistence.get_player_by_name.return_value = mock_player
        mock_persistence.get_room.side_effect = [mock_room, mock_target_room]

        result = await handle_look_command(validated_command, command_data, current_user, mock_persistence, "testuser")

        assert result == {"result": "Northern Room\nA room to the north."}

    @pytest.mark.asyncio
    async def test_handle_go_command_success(self):
        """Test successful go command handling."""
        from server.command_handler_v2 import handle_go_command

        validated_command = MagicMock()
        command_data = {"direction": "north"}
        current_user = {"username": "testuser"}
        request = MagicMock()

        # Mock persistence and player data
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = "player_1"
        mock_player.current_room_id = "room_1"
        mock_room = MagicMock()
        mock_room.exits = {"north": "room_2"}
        mock_target_room = MagicMock()
        mock_target_room.name = "Northern Room"
        mock_target_room.description = "A room to the north."
        mock_target_room.exits = {"south": "room_1"}

        mock_persistence.get_player_by_name.return_value = mock_player
        mock_persistence.get_room.side_effect = [mock_room, mock_target_room]

        # Mock movement service
        with patch("server.command_handler_v2.MovementService") as mock_movement_service:
            mock_service = MagicMock()
            mock_service.move_player.return_value = True
            mock_movement_service.return_value = mock_service

            result = await handle_go_command(
                validated_command, command_data, current_user, request, mock_persistence, "testuser"
            )

            expected_result = "Northern Room\nA room to the north.\n\nExits: south"
            assert result == {"result": expected_result}

    @pytest.mark.asyncio
    async def test_handle_say_command_success(self):
        """Test successful say command handling."""
        from server.command_handler_v2 import handle_say_command

        validated_command = MagicMock()
        command_data = {"message": "Hello, world!"}
        current_user = {"username": "testuser"}

        # Mock persistence and player data
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = "player_1"
        mock_player.name = "TestUser"

        mock_persistence.get_player_by_name.return_value = mock_player

        # Mock chat service
        with patch("server.command_handler_v2.ChatService") as mock_chat_service:
            mock_service = MagicMock()
            mock_service.send_say_message = AsyncMock(return_value={"success": True})
            mock_chat_service.return_value = mock_service

            result = await handle_say_command(
                validated_command, command_data, current_user, mock_persistence, "testuser"
            )

            assert result == {"result": "TestUser says: Hello, world!"}

    @pytest.mark.asyncio
    async def test_handle_help_command(self):
        """Test help command handling."""
        from server.command_handler_v2 import handle_help_command

        validated_command = MagicMock()
        command_data = {}
        player_name = "testuser"

        # Mock the command processor's help function
        with patch.object(self.command_processor, "get_command_help") as mock_help:
            mock_help.return_value = "Available commands: look, go, say, etc."

            result = await handle_help_command(validated_command, command_data, player_name)

            assert result == {"result": "Available commands: look, go, say, etc."}
            mock_help.assert_called_once()


class TestCommandProcessorIntegration:
    """Test the CommandProcessor integration functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.processor = CommandProcessor()

    def test_process_command_string_success(self):
        """Test successful command string processing."""
        command_line = "look north"
        player_name = "testuser"

        validated_command, error_message, command_type = self.processor.process_command_string(
            command_line, player_name
        )

        assert error_message is None
        assert validated_command is not None
        assert command_type == "look"

    def test_process_command_string_validation_error(self):
        """Test command string processing with validation error."""
        command_line = "say <script>alert('xss')</script>"
        player_name = "testuser"

        validated_command, error_message, command_type = self.processor.process_command_string(
            command_line, player_name
        )

        assert error_message is not None
        assert "Invalid command" in error_message
        assert validated_command is None
        assert command_type is None

    def test_extract_command_data(self):
        """Test command data extraction."""
        # Create a mock validated command
        mock_command = MagicMock()
        mock_command.command_type.value = "look"
        mock_command.direction.value = "north"

        command_data = self.processor.extract_command_data(mock_command)

        assert command_data["command_type"] == "look"
        assert command_data["direction"] == "north"
        assert command_data["player_name"] is None  # Will be set by calling code

    def test_validate_command_safety_success(self):
        """Test command safety validation success."""
        command_line = "look north"

        is_safe, error_message = self.processor.validate_command_safety(command_line)

        assert is_safe is True
        assert error_message is None

    def test_validate_command_safety_failure(self):
        """Test command safety validation failure."""
        command_line = "look; rm -rf /"

        is_safe, error_message = self.processor.validate_command_safety(command_line)

        assert is_safe is False
        assert error_message is not None

    def test_get_command_help(self):
        """Test command help retrieval."""
        help_content = self.processor.get_command_help()

        assert help_content is not None
        assert isinstance(help_content, str)
        assert len(help_content) > 0
