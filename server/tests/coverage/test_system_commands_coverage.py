"""
Tests for system commands to improve coverage.

This module provides targeted tests for system_commands.py
to cover the remaining uncovered lines.

As noted in the Pnakotic Manuscripts, even simple incantations
require proper testing to ensure they function correctly.
"""

from unittest.mock import Mock, patch

import pytest

from server.commands.system_commands import handle_help_command


class TestHelpCommand:
    """Test help command functionality."""

    @pytest.mark.asyncio
    async def test_help_command_no_args(self):
        """Test help command with no arguments.

        AI: Tests help command to get general help content.
        """
        current_user = {"username": "testuser"}
        request = Mock()
        alias_storage = Mock()
        player_name = "testuser"

        with patch("server.commands.system_commands.get_help_content") as mock_help:
            mock_help.return_value = "General help content"

            result = await handle_help_command({"args": []}, current_user, request, alias_storage, player_name)

            assert result["result"] == "General help content"
            mock_help.assert_called_once_with(None)

    @pytest.mark.asyncio
    async def test_help_command_with_specific_command(self):
        """Test help command with specific command argument.

        AI: Tests help command to get help for a specific command.
        """
        current_user = {"username": "testuser"}
        request = Mock()
        alias_storage = Mock()
        player_name = "testuser"

        with patch("server.commands.system_commands.get_help_content") as mock_help:
            mock_help.return_value = "Help for 'say' command"

            result = await handle_help_command({"args": ["say"]}, current_user, request, alias_storage, player_name)

            assert result["result"] == "Help for 'say' command"
            mock_help.assert_called_once_with("say")

    @pytest.mark.asyncio
    async def test_help_command_too_many_arguments(self):
        """Test help command with too many arguments.

        AI: Tests error handling when help command has too many arguments.
        This covers lines 34-36.
        """
        current_user = {"username": "testuser"}
        request = Mock()
        alias_storage = Mock()
        player_name = "testuser"

        result = await handle_help_command(
            {"args": ["say", "extra"]}, current_user, request, alias_storage, player_name
        )

        assert "Usage: help [command]" in result["result"]

    @pytest.mark.asyncio
    async def test_help_command_with_various_commands(self):
        """Test help command with various command names.

        AI: Tests help command with different command names.
        """
        current_user = {"username": "testuser"}
        request = Mock()
        alias_storage = Mock()
        player_name = "testuser"

        test_commands = ["look", "go", "emote", "whisper"]

        for command in test_commands:
            with patch("server.commands.system_commands.get_help_content") as mock_help:
                mock_help.return_value = f"Help for {command}"

                result = await handle_help_command(
                    {"args": [command]}, current_user, request, alias_storage, player_name
                )

                assert result["result"] == f"Help for {command}"
                mock_help.assert_called_once_with(command)
