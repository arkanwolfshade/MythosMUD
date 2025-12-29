"""
Unit tests for command processor.

Tests the CommandProcessor class which integrates Pydantic validation with command infrastructure.
"""

from unittest.mock import MagicMock, patch

import pytest
from pydantic import ValidationError as PydanticValidationError

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import CommandType
from server.utils.command_processor import CommandProcessor, get_command_processor


@pytest.fixture
def command_processor():
    """Create a CommandProcessor instance."""
    return CommandProcessor()


def test_command_processor_initialization(command_processor):
    """Test CommandProcessor initializes correctly."""
    assert command_processor.parser is not None


def test_process_command_string_success(command_processor):
    """Test process_command_string successfully processes valid command."""
    with patch("server.utils.command_processor.parse_command") as mock_parse:
        mock_command = MagicMock()
        mock_command.command_type.value = "look"
        mock_parse.return_value = mock_command

        result, error, cmd_type = command_processor.process_command_string("look at item", "TestPlayer")

        assert result == mock_command
        assert error is None
        assert cmd_type == "look"


def test_process_command_string_pydantic_validation_error(command_processor):
    """Test process_command_string handles Pydantic validation errors."""
    # Create a Pydantic validation error by actually triggering validation
    from pydantic import BaseModel

    class TestModel(BaseModel):
        field: int

    try:
        TestModel(field="not_an_int")  # This will raise ValidationError
    except PydanticValidationError as validation_error:
        with patch("server.utils.command_processor.parse_command", side_effect=validation_error):
            result, error, cmd_type = command_processor.process_command_string("invalid command", "TestPlayer")

            assert result is None
            assert error is not None
            assert "Invalid command" in error
            assert cmd_type is None


def test_process_command_string_mythos_validation_error(command_processor):
    """Test process_command_string handles MythosMUD validation errors."""
    with patch("server.utils.command_processor.parse_command", side_effect=MythosValidationError("Invalid input")):
        result, error, cmd_type = command_processor.process_command_string("bad command", "TestPlayer")

        assert result is None
        assert error == "Invalid input"
        assert cmd_type is None


def test_process_command_string_value_error(command_processor):
    """Test process_command_string handles ValueError."""
    with patch("server.utils.command_processor.parse_command", side_effect=ValueError("Unknown command")):
        result, error, cmd_type = command_processor.process_command_string("unknown", "TestPlayer")

        assert result is None
        assert error == "Unknown command"
        assert cmd_type is None


def test_process_command_string_type_error(command_processor):
    """Test process_command_string handles TypeError."""
    with patch("server.utils.command_processor.parse_command", side_effect=TypeError("Type error")):
        result, error, cmd_type = command_processor.process_command_string("command", "TestPlayer")

        assert result is None
        assert "Unexpected error processing command" in error
        assert cmd_type is None


def test_process_command_string_attribute_error(command_processor):
    """Test process_command_string handles AttributeError."""
    with patch("server.utils.command_processor.parse_command", side_effect=AttributeError("Missing attribute")):
        result, error, cmd_type = command_processor.process_command_string("command", "TestPlayer")

        assert result is None
        assert "Unexpected error processing command" in error
        assert cmd_type is None


def test_process_command_string_key_error(command_processor):
    """Test process_command_string handles KeyError."""
    with patch("server.utils.command_processor.parse_command", side_effect=KeyError("Missing key")):
        result, error, cmd_type = command_processor.process_command_string("command", "TestPlayer")

        assert result is None
        assert "Unexpected error processing command" in error
        assert cmd_type is None


def test_process_command_string_runtime_error(command_processor):
    """Test process_command_string handles RuntimeError."""
    with patch("server.utils.command_processor.parse_command", side_effect=RuntimeError("Runtime error")):
        result, error, cmd_type = command_processor.process_command_string("command", "TestPlayer")

        assert result is None
        assert "Unexpected error processing command" in error
        assert cmd_type is None


def test_extract_attributes_basic(command_processor):
    """Test _extract_attributes extracts attributes correctly."""
    mock_command = MagicMock()
    mock_command.direction = "north"
    mock_command.message = "Hello"

    attribute_map = {"direction": "direction", "message": "message"}
    result = command_processor._extract_attributes(mock_command, attribute_map)

    assert result["direction"] == "north"
    assert result["message"] == "Hello"


def test_extract_attributes_missing_attribute(command_processor):
    """Test _extract_attributes handles missing attributes."""

    # Use a simple object instead of MagicMock to avoid auto-attribute creation
    class MockCommand:
        direction = "north"
        # message attribute not set

    mock_command = MockCommand()
    attribute_map = {"direction": "direction", "message": "message"}
    result = command_processor._extract_attributes(mock_command, attribute_map)

    assert "direction" in result
    assert "message" not in result


def test_is_combat_command_attack(command_processor):
    """Test _is_combat_command returns True for attack command."""
    assert command_processor._is_combat_command(CommandType.ATTACK) is True


def test_is_combat_command_punch(command_processor):
    """Test _is_combat_command returns True for punch command."""
    assert command_processor._is_combat_command(CommandType.PUNCH) is True


def test_is_combat_command_kick(command_processor):
    """Test _is_combat_command returns True for kick command."""
    assert command_processor._is_combat_command(CommandType.KICK) is True


def test_is_combat_command_strike(command_processor):
    """Test _is_combat_command returns True for strike command."""
    assert command_processor._is_combat_command(CommandType.STRIKE) is True


def test_is_combat_command_non_combat(command_processor):
    """Test _is_combat_command returns False for non-combat command."""
    assert command_processor._is_combat_command(CommandType.LOOK) is False
    assert command_processor._is_combat_command(CommandType.SAY) is False


def test_extract_command_data_basic(command_processor):
    """Test extract_command_data extracts basic command data."""
    mock_command = MagicMock()
    mock_command.command_type = "look"
    mock_command.direction = "north"
    mock_command.message = None

    result = command_processor.extract_command_data(mock_command)

    assert result["command_type"] == "look"
    assert result["direction"] == "north"
    assert result["player_name"] is None


def test_extract_command_data_with_target(command_processor):
    """Test extract_command_data handles target attribute."""
    mock_command = MagicMock()
    mock_command.command_type = "say"
    mock_command.target = "player1"

    result = command_processor.extract_command_data(mock_command)

    assert result["target"] == "player1"


def test_extract_command_data_combat_target(command_processor):
    """Test extract_command_data sets target_player for combat commands."""

    # Create a simple object instead of MagicMock to avoid auto-attributes
    class MockCombatCommand:
        # command_type needs to be the enum itself, not the value, for _is_combat_command to work
        command_type = CommandType.ATTACK
        target = "enemy"

    mock_command = MockCombatCommand()

    result = command_processor.extract_command_data(mock_command)

    assert result["target"] == "enemy"
    # The code checks if command_type is a combat command
    # Since we're passing CommandType.ATTACK enum, _is_combat_command should return True
    assert result["target_player"] == "enemy"


def test_extract_command_data_player_name(command_processor):
    """Test extract_command_data handles player_name attribute."""
    mock_command = MagicMock()
    mock_command.command_type = "whisper"
    mock_command.player_name = "target_player"

    result = command_processor.extract_command_data(mock_command)

    assert result["target_player"] == "target_player"


def test_extract_command_data_multiple_attributes(command_processor):
    """Test extract_command_data extracts multiple attributes."""
    mock_command = MagicMock()
    mock_command.command_type = "get"
    mock_command.item = "sword"
    mock_command.container = "bag"
    mock_command.quantity = 1

    result = command_processor.extract_command_data(mock_command)

    assert result["item"] == "sword"
    assert result["container"] == "bag"
    assert result["quantity"] == 1


def test_validate_command_safety_safe(command_processor):
    """Test validate_command_safety returns True for safe command."""
    # The function imports validate_command_safety from command_parser inside the method
    with patch("server.utils.command_parser.validate_command_safety", return_value=True):
        is_safe, error = command_processor.validate_command_safety("look")

        assert is_safe is True
        assert error is None


def test_validate_command_safety_unsafe(command_processor):
    """Test validate_command_safety returns False for unsafe command."""
    # The function imports validate_command_safety from command_parser inside the method
    with patch("server.utils.command_parser.validate_command_safety", return_value=False):
        is_safe, error = command_processor.validate_command_safety("dangerous command")

        assert is_safe is False
        assert error == "Command contains dangerous patterns"


def test_get_command_help_success(command_processor):
    """Test get_command_help returns help text."""
    with patch.object(command_processor.parser, "get_command_help", return_value="Help text"):
        result = command_processor.get_command_help("look")

        assert result == "Help text"


def test_get_command_help_none(command_processor):
    """Test get_command_help returns general help when command_name is None."""
    with patch.object(command_processor.parser, "get_command_help", return_value="General help"):
        result = command_processor.get_command_help(None)

        assert result == "General help"


def test_get_command_help_value_error(command_processor):
    """Test get_command_help handles ValueError."""
    with patch.object(command_processor.parser, "get_command_help", side_effect=ValueError("Invalid command")):
        result = command_processor.get_command_help("invalid")

        assert result == "Help system temporarily unavailable."


def test_get_command_help_type_error(command_processor):
    """Test get_command_help handles TypeError."""
    with patch.object(command_processor.parser, "get_command_help", side_effect=TypeError("Type error")):
        result = command_processor.get_command_help("command")

        assert result == "Help system temporarily unavailable."


def test_get_command_help_attribute_error(command_processor):
    """Test get_command_help handles AttributeError."""
    with patch.object(command_processor.parser, "get_command_help", side_effect=AttributeError("Missing attr")):
        result = command_processor.get_command_help("command")

        assert result == "Help system temporarily unavailable."


def test_get_command_help_key_error(command_processor):
    """Test get_command_help handles KeyError."""
    with patch.object(command_processor.parser, "get_command_help", side_effect=KeyError("Missing key")):
        result = command_processor.get_command_help("command")

        assert result == "Help system temporarily unavailable."


def test_get_command_help_runtime_error(command_processor):
    """Test get_command_help handles RuntimeError."""
    with patch.object(command_processor.parser, "get_command_help", side_effect=RuntimeError("Runtime error")):
        result = command_processor.get_command_help("command")

        assert result == "Help system temporarily unavailable."


def test_get_command_processor():
    """Test get_command_processor returns global instance."""
    processor = get_command_processor()

    assert isinstance(processor, CommandProcessor)
    # Should return the same instance
    assert get_command_processor() is processor
