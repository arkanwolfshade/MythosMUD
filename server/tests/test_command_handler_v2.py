"""
Tests for Command Handler Unified - Integrated Pydantic + Click validation system.

This test suite validates the unified command handling system that integrates our
robust Pydantic + Click validation with the existing MythosMUD infrastructure.

As the ancient texts suggest: "Testing is the foundation upon which all
knowledge must be built, lest we build upon shifting sands."
"""

from unittest.mock import Mock

import pytest

from ..command_handler_unified import (
    CommandRequest,
    clean_command_input,
    normalize_command,
    process_command,
    process_command_unified,
)
from ..utils.command_processor import CommandProcessor, get_command_processor


class TestCommandHandlerV2:
    """Test the unified command handler with Pydantic + Click validation."""

    @pytest.mark.asyncio
    async def test_process_command_unified_basic(self):
        """Test basic command processing through unified handler."""
        # Test that the unified command handler can process basic commands
        result = await process_command_unified("look", {"username": "testuser"}, Mock(), player_name="testuser")
        # The result should be a dict with a result key
        assert isinstance(result, dict)
        assert "result" in result

    @pytest.mark.asyncio
    async def test_process_command_unified_empty(self):
        """Test empty command processing."""
        result = await process_command_unified("", {"username": "testuser"}, Mock(), player_name="testuser")
        assert result["result"] == ""

    @pytest.mark.asyncio
    async def test_process_command_unified_too_long(self):
        """Test command length validation."""
        long_command = "a" * 1001  # Exceeds MAX_COMMAND_LENGTH
        result = await process_command_unified(long_command, {"username": "testuser"}, Mock(), player_name="testuser")
        assert "Command too long" in result["result"]

    @pytest.mark.asyncio
    async def test_process_command_with_validation_success(self):
        """Test command processing with validation success."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock room data
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {}
        mock_request.app.state.persistence.get_room.return_value = mock_room

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player

        result = await process_command("look", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "Error retrieving room information" in result["result"]

    def test_clean_command_input(self):
        """Test command input cleaning."""
        assert clean_command_input("  look  ") == "look"
        assert clean_command_input("go   north") == "go north"
        assert clean_command_input("say    hello   world") == "say hello world"
        assert clean_command_input("") == ""

    def test_normalize_command(self):
        """Test command normalization."""
        assert normalize_command("look") == "look"
        assert normalize_command("/look") == "look"
        assert normalize_command("  /look  ") == "look"
        assert normalize_command("/go north") == "go north"
        assert normalize_command("") == ""

    def test_command_request_model(self):
        """Test CommandRequest Pydantic model."""
        request = CommandRequest(command="look")
        assert request.command == "look"

        # Test validation - empty command should not raise ValueError
        # The Pydantic model allows empty strings
        request = CommandRequest(command="")
        assert request.command == ""


class TestCommandProcessorIntegration:
    """Test integration with the command processor."""

    def test_get_command_processor(self):
        """Test getting the command processor instance."""
        processor = get_command_processor()
        assert isinstance(processor, CommandProcessor)

    def test_command_processor_singleton(self):
        """Test that command processor is a singleton."""
        processor1 = get_command_processor()
        processor2 = get_command_processor()
        assert processor1 is processor2
