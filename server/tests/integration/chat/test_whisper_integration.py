"""
Integration tests for whisper command functionality.

This module tests the complete whisper command integration including
command parsing, validation, and execution.
"""

import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import CommandType, ReplyCommand, WhisperCommand
from server.utils.command_parser import parse_command


class TestWhisperCommandIntegration:
    """Test whisper command integration."""

    def test_whisper_command_parsing(self):
        """Test that whisper commands are parsed correctly."""
        # Test basic whisper command
        command = parse_command("whisper TestPlayer Hello there!")
        assert isinstance(command, WhisperCommand)
        assert command.command_type == CommandType.WHISPER
        assert command.target == "TestPlayer"
        assert command.message == "Hello there!"

        # Test whisper command with slash prefix
        command = parse_command("/whisper TestPlayer Hello there!")
        assert isinstance(command, WhisperCommand)
        assert command.command_type == CommandType.WHISPER
        assert command.target == "TestPlayer"
        assert command.message == "Hello there!"

        # Test whisper command with different message formats
        command = parse_command("whisper TestPlayer This is a longer message with multiple words!")
        assert isinstance(command, WhisperCommand)
        assert command.command_type == CommandType.WHISPER
        assert command.target == "TestPlayer"
        assert command.message == "This is a longer message with multiple words!"

    def test_reply_command_parsing(self):
        """Test that reply commands are parsed correctly."""
        # Test basic reply command
        command = parse_command("reply Hello back!")
        assert isinstance(command, ReplyCommand)
        assert command.command_type == CommandType.REPLY
        assert command.message == "Hello back!"

        # Test reply command with slash prefix
        command = parse_command("/reply Hello back!")
        assert isinstance(command, ReplyCommand)
        assert command.command_type == CommandType.REPLY
        assert command.message == "Hello back!"

    def test_whisper_command_validation(self):
        """Test whisper command validation."""
        # Test valid whisper command
        command = WhisperCommand(target="TestPlayer", message="Hello!")
        assert command.target == "TestPlayer"
        assert command.message == "Hello!"

        # Test invalid target name
        with pytest.raises(ValueError, match="Target player name must start with a letter"):
            WhisperCommand(target="123Player", message="Hello!")

        # Test empty message
        with pytest.raises(Exception, match="String should have at least 1 character"):
            WhisperCommand(target="TestPlayer", message="")

        # Test message too long
        long_message = "x" * 2001
        with pytest.raises(Exception, match="String should have at most 2000 characters"):
            WhisperCommand(target="TestPlayer", message=long_message)

    def test_reply_command_validation(self):
        """Test reply command validation."""
        # Test valid reply command
        command = ReplyCommand(message="Hello back!")
        assert command.message == "Hello back!"

        # Test empty message
        with pytest.raises(Exception, match="String should have at least 1 character"):
            ReplyCommand(message="")

        # Test message too long
        long_message = "x" * 2001
        with pytest.raises(Exception, match="String should have at most 2000 characters"):
            ReplyCommand(message=long_message)

    def test_whisper_command_injection_prevention(self):
        """Test that whisper commands prevent injection attempts."""
        # Test dangerous characters
        with pytest.raises(ValueError, match="Message contains dangerous characters"):
            WhisperCommand(target="TestPlayer", message="Hello<script>alert('xss')</script>")

        # Test command injection (dangerous characters are caught first)
        # Semicolons are still blocked - pattern changed
        with pytest.raises(Exception, match="potentially dangerous pattern"):
            WhisperCommand(target="TestPlayer", message="Hello; say something")

    def test_reply_command_injection_prevention(self):
        """Test that reply commands prevent injection attempts."""
        # Test dangerous characters
        with pytest.raises(ValueError, match="Message contains dangerous characters"):
            ReplyCommand(message="Hello<script>alert('xss')</script>")

        # Test command injection (dangerous characters are caught first)
        # Semicolons are still blocked - pattern changed
        with pytest.raises(Exception, match="potentially dangerous pattern"):
            ReplyCommand(message="Hello; say something")

    def test_whisper_command_error_handling(self):
        """Test whisper command error handling."""
        # Test missing target
        # Error messages no longer wrapped with "Failed to create command:"
        with pytest.raises(MythosValidationError, match="Usage: whisper"):
            parse_command("whisper")

        # Test missing message
        # Error messages no longer wrapped with "Failed to create command:"
        with pytest.raises(MythosValidationError, match="You must provide a message to whisper"):
            parse_command("whisper TestPlayer")

        # Test empty message (now returns specific error)
        with pytest.raises(MythosValidationError, match="You must provide a message to whisper"):
            parse_command("whisper TestPlayer    ")

    def test_reply_command_error_handling(self):
        """Test reply command error handling."""
        # Test missing message
        # Error messages no longer wrapped with "Failed to create command:"
        with pytest.raises(MythosValidationError, match="Usage: reply"):
            parse_command("reply")

        # Test empty message
        # Error messages no longer wrapped with "Failed to create command:"
        with pytest.raises(MythosValidationError, match="Usage: reply"):
            parse_command("reply    ")


class TestWhisperCommandHelp:
    """Test whisper command help integration."""

    def test_whisper_command_help_included(self):
        """Test that whisper command help is included in general help."""
        from server.utils.command_parser import get_command_help

        help_text = get_command_help()
        assert "whisper <player> <message> - Send private message to player" in help_text
        assert "reply <message> - Reply to last whisper received" in help_text

    def test_whisper_command_specific_help(self):
        """Test specific help for whisper command."""
        from server.utils.command_parser import get_command_help

        help_text = get_command_help("whisper")
        assert "whisper <player> <message> - Send private message to player" in help_text

    def test_reply_command_specific_help(self):
        """Test specific help for reply command."""
        from server.utils.command_parser import get_command_help

        help_text = get_command_help("reply")
        assert "reply <message> - Reply to last whisper received" in help_text
