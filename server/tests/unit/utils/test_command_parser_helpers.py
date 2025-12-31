"""
Unit tests for command_parser helper methods.

Tests the helper methods in CommandParser class.
"""

from unittest.mock import MagicMock, patch

import pytest
from pydantic import ValidationError as PydanticValidationError

from server.exceptions import ValidationError as MythosValidationError
from server.utils.command_parser import CommandParser


@pytest.fixture
def command_parser():
    """Create a CommandParser instance."""
    return CommandParser()


def test_normalize_command_removes_slash_prefix(command_parser):
    """Test _normalize_command() removes leading slash."""
    result = command_parser._normalize_command("/look north")
    assert result == "look north"


def test_normalize_command_cleans_whitespace(command_parser):
    """Test _normalize_command() cleans multiple whitespace."""
    result = command_parser._normalize_command("look   north   east")
    assert result == "look north east"


def test_normalize_command_strips_whitespace(command_parser):
    """Test _normalize_command() strips leading/trailing whitespace."""
    result = command_parser._normalize_command("  look north  ")
    assert result == "look north"


def test_normalize_command_no_slash(command_parser):
    """Test _normalize_command() handles command without slash."""
    result = command_parser._normalize_command("look north")
    assert result == "look north"


def test_parse_command_parts_simple(command_parser):
    """Test _parse_command_parts() parses simple command."""
    command, args = command_parser._parse_command_parts("look")
    assert command == "look"
    assert args == []


def test_parse_command_parts_with_args(command_parser):
    """Test _parse_command_parts() parses command with arguments."""
    command, args = command_parser._parse_command_parts("say hello world")
    assert command == "say"
    assert args == ["hello", "world"]


def test_parse_command_parts_lowercases_command(command_parser):
    """Test _parse_command_parts() lowercases command."""
    command, args = command_parser._parse_command_parts("LOOK north")
    assert command == "look"
    assert args == ["north"]


def test_parse_command_parts_empty_raises(command_parser):
    """Test _parse_command_parts() raises error for empty command."""
    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._parse_command_parts("")
    assert "Empty command" in str(exc_info.value)


def test_parse_command_parts_whitespace_only_raises(command_parser):
    """Test _parse_command_parts() raises error for whitespace-only."""
    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._parse_command_parts("   ")
    assert "Empty command" in str(exc_info.value)


def test_get_command_help_specific_command(command_parser):
    """Test get_command_help() returns help for specific command."""
    result = command_parser.get_command_help("look")
    assert "look" in result.lower()
    assert "direction" in result.lower()


def test_get_command_help_unknown_command(command_parser):
    """Test get_command_help() returns error for unknown command."""
    result = command_parser.get_command_help("unknown_command")
    assert "unknown" in result.lower() or "not found" in result.lower()


def test_get_command_help_none(command_parser):
    """Test get_command_help() returns general help when None."""
    result = command_parser.get_command_help(None)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Available commands" in result or "commands" in result.lower()


def test_create_command_object_with_alias_l(command_parser):
    """Test _create_command_object() handles 'l' alias."""
    with patch.object(command_parser, "_command_factory", {"local": MagicMock(return_value=MagicMock())}):
        result = command_parser._create_command_object("l", ["hello"])
        assert result is not None


def test_create_command_object_with_alias_g(command_parser):
    """Test _create_command_object() handles 'g' alias."""
    with patch.object(command_parser, "_command_factory", {"global": MagicMock(return_value=MagicMock())}):
        result = command_parser._create_command_object("g", ["hello"])
        assert result is not None


def test_create_command_object_with_alias_w(command_parser):
    """Test _create_command_object() handles 'w' alias."""
    with patch.object(command_parser, "_command_factory", {"whisper": MagicMock(return_value=MagicMock())}):
        result = command_parser._create_command_object("w", ["player", "hello"])
        assert result is not None


def test_create_command_object_unsupported_command(command_parser):
    """Test _create_command_object() raises error for unsupported command."""
    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._create_command_object("unsupported", [])
    assert "Unsupported" in str(exc_info.value) or "not found" in str(exc_info.value).lower()


def test_create_command_object_pydantic_validation_error(command_parser):
    """Test _create_command_object() handles PydanticValidationError."""
    mock_factory = MagicMock()
    mock_factory.side_effect = PydanticValidationError.from_exception_data("TestModel", [])
    command_parser._command_factory = {"test": mock_factory}

    with pytest.raises(MythosValidationError):
        command_parser._create_command_object("test", [])


def test_create_command_object_value_error(command_parser):
    """Test _create_command_object() handles ValueError."""
    mock_factory = MagicMock()
    mock_factory.side_effect = ValueError("Test error")
    command_parser._command_factory = {"test": mock_factory}

    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._create_command_object("test", [])
    assert "Failed to create command" in str(exc_info.value)
