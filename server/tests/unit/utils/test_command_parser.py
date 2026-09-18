"""
Unit tests for command parser.

Tests the CommandParser class which provides secure command parsing and validation.
"""
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pyright: reportUnknownParameterType=false, reportMissingParameterType=false
# pyright: reportUnknownVariableType=false, reportUnknownMemberType=false
# TEST_MOCK: the `command_parser` fixture parameter is untyped throughout this file (207 findings
# already baselined for the identical pattern); new tests using it inherit the same shape.

from unittest.mock import MagicMock, patch

import pytest
from pydantic import ValidationError as PydanticValidationError

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import Command, CommandType
from server.utils.command_parser import CommandParser, parse_command


@pytest.fixture
def command_parser():
    """Create a CommandParser instance."""
    return CommandParser()


def test_command_parser_initialization(command_parser):
    """Test CommandParser initializes correctly."""
    assert command_parser.max_command_length == 1000
    assert len(command_parser.valid_commands) > 0
    assert command_parser.factory is not None


def test_parse_command_empty_string(command_parser):
    """Test parse_command raises error for empty string."""
    with pytest.raises(MythosValidationError) as exc_info:
        command_parser.parse_command("")

    assert "Empty command" in str(exc_info.value)


def test_parse_command_whitespace_only(command_parser):
    """Test parse_command raises error for whitespace-only string."""
    with pytest.raises(MythosValidationError) as exc_info:
        command_parser.parse_command("   ")

    assert "Empty command" in str(exc_info.value)


def test_parse_command_too_long(command_parser):
    """Test parse_command raises error for command exceeding max length."""
    long_command = "a" * 1001
    with pytest.raises(MythosValidationError) as exc_info:
        command_parser.parse_command(long_command)

    assert "too long" in str(exc_info.value).lower()


def test_parse_command_unknown_command(command_parser):
    """Test parse_command raises error for unknown command."""
    with pytest.raises(MythosValidationError) as exc_info:
        command_parser.parse_command("unknown_command")

    assert "Unknown command" in str(exc_info.value)


def test_parse_command_valid_look(command_parser):
    """Test parse_command successfully parses look command."""
    result = command_parser.parse_command("look")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.LOOK


def test_parse_command_valid_cleanse(command_parser):
    """#804: parse_command must recognize 'cleanse' -- this is the exact gate a new command's
    (CommandType, CommandFactory registration, factory dict entry) can silently miss, leaving
    the handler registered in command_service.py but unreachable through real command input."""
    result = command_parser.parse_command("cleanse")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.CLEANSE


def test_parse_command_valid_go(command_parser):
    """Test parse_command successfully parses go command."""
    result = command_parser.parse_command("go north")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.GO


def test_parse_command_valid_read(command_parser):
    """#813: parse_command must recognize 'read' -- registered in _COMMAND_HANDLERS but
    missing from CommandType, so it was unreachable through real command input."""
    result = command_parser.parse_command("read spellbook")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.READ


def test_parse_command_valid_stop(command_parser):
    """#813: parse_command must recognize 'stop' -- registered in _COMMAND_HANDLERS but
    missing from CommandType, so it was unreachable through real command input."""
    result = command_parser.parse_command("stop")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.STOP


def test_parse_command_valid_teach(command_parser):
    """#813: parse_command must recognize 'teach' -- registered in _COMMAND_HANDLERS but
    missing from CommandType, so it was unreachable through real command input."""
    result = command_parser.parse_command("teach professor cantrip")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.TEACH


def test_parse_command_valid_global(command_parser):
    """#813: 'global' was in CommandType but had no factory entry, so it cleared the
    valid_commands gate and then died with 'Unsupported command: global'."""
    result = command_parser.parse_command("global hello everyone")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.GLOBAL
    assert result.message == "hello everyone"


def test_parse_command_valid_global_alias_g(command_parser):
    """#813: '/g' resolves to 'global' via _resolve_command_alias and hit the same
    'Unsupported command' dead end as bare 'global' before create_global_command existed."""
    result = command_parser.parse_command("g hello everyone")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.GLOBAL
    assert result.message == "hello everyone"


def test_parse_command_with_slash_prefix(command_parser):
    """Test parse_command handles slash prefix."""
    result = command_parser.parse_command("/look")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.LOOK


def test_parse_command_spawn_alias(command_parser):
    """Test /spawn parses as alias for npc spawn."""
    result = command_parser.parse_command("/spawn 1 room_123")

    assert result.command_type == CommandType.NPC
    assert result.subcommand == "spawn"
    assert result.args == ["1", "room_123"]


def test_parse_command_catalog(command_parser):
    """Regression: /catalog must be a known CommandType (e2e Unknown command)."""
    result = command_parser.parse_command("/catalog")

    assert result.command_type == CommandType.CATALOG
    assert result.args == []


def test_parse_command_catalog_with_filters(command_parser):
    """Regression: /catalog filter args must survive parsing into CatalogCommand.args."""
    result = command_parser.parse_command("/catalog type=weapon page=2")

    assert result.command_type == CommandType.CATALOG
    assert result.args == ["type=weapon", "page=2"]


def test_parse_command_alias_l(command_parser):
    """Test parse_command handles 'l' alias for local."""
    result = command_parser.parse_command("l hello")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.LOCAL


def test_parse_command_alias_g(command_parser):
    """Test parse_command handles 'g' alias for 'global'.

    #813: 'global' was in CommandType but had no factory entry, so both 'global' and
    its 'g' alias used to fail with 'Unsupported command: global' once
    create_global_command was added. See test_parse_command_valid_global_alias_g for
    the dedicated regression test.
    """
    result = command_parser.parse_command("g hello")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.GLOBAL
    assert result.message == "hello"


def test_normalize_command_removes_slash(command_parser):
    """Test _normalize_command removes leading slash."""
    result = command_parser._normalize_command("/go north")
    assert result == "go north"


def test_normalize_command_cleans_whitespace(command_parser):
    """Test _normalize_command cleans whitespace."""
    result = command_parser._normalize_command("go    north")
    assert result == "go north"


def test_normalize_command_no_slash(command_parser):
    """Test _normalize_command handles command without slash."""
    result = command_parser._normalize_command("go north")
    assert result == "go north"


def test_parse_command_parts_basic(command_parser):
    """Test _parse_command_parts parses basic command."""
    command, args = command_parser._parse_command_parts("go north")

    assert command == "go"
    assert args == ["north"]


def test_parse_command_parts_no_args(command_parser):
    """Test _parse_command_parts handles command without args."""
    command, args = command_parser._parse_command_parts("look")

    assert command == "look"
    assert args == []


def test_parse_command_parts_multiple_args(command_parser):
    """Test _parse_command_parts handles multiple arguments."""
    command, args = command_parser._parse_command_parts("say hello world")

    assert command == "say"
    assert args == ["hello", "world"]


def test_parse_command_parts_empty_string(command_parser):
    """Test _parse_command_parts raises error for empty string."""
    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._parse_command_parts("")

    assert "Empty command after parsing" in str(exc_info.value)


def test_parse_command_parts_mock_object_detection(command_parser):
    """Test _parse_command_parts detects mock objects."""
    mock_string = MagicMock()
    mock_string._mock_name = "test"

    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._parse_command_parts(mock_string)

    assert "Mock object" in str(exc_info.value)


def test_create_command_object_success(command_parser):
    """Test _create_command_object successfully creates command."""
    with patch.object(command_parser.factory, "create_look_command", return_value=MagicMock(spec=Command)):
        result = command_parser._create_command_object("look", [])

        assert result is not None


def test_create_command_object_handles_alias_w(command_parser):
    """Test _create_command_object handles 'w' alias."""
    # 'w' should be converted to 'whisper' before factory lookup
    # The factory method is actually called, so we need to patch it in the factory dict
    mock_command = MagicMock(spec=Command)
    original_method = command_parser._command_factory.get("whisper")

    def mock_create_whisper(_args):
        return mock_command

    command_parser._command_factory["whisper"] = mock_create_whisper
    result = command_parser._create_command_object("w", ["player", "message"])

    assert result == mock_command

    # Restore original (only if we successfully retrieved it)
    if original_method is not None:
        command_parser._command_factory["whisper"] = original_method


def test_create_command_object_handles_alias_l(command_parser):
    """Test _create_command_object handles 'l' alias."""
    # 'l' is converted to 'local'; 'local' has special handling and calls
    # factory.create_local_command directly (bypasses _command_factory lookup)
    mock_command = MagicMock(spec=Command)
    with patch.object(
        command_parser.factory,
        "create_local_command",
        return_value=mock_command,
    ):
        result = command_parser._create_command_object("l", ["message"])

    assert result == mock_command


def test_create_command_object_handles_alias_g(command_parser):
    """Test _create_command_object handles 'g' alias.

    #813: 'g' is converted to 'global' before the _command_factory dict lookup, then
    routed to whatever create_global_command is registered under CommandType.GLOBAL.
    The dict entry is a bound-method reference captured at CommandParser.__init__, so
    (unlike the 'local' special case in _invoke_create_method) patching the factory
    instance's method afterward would not affect it -- patch the dict entry directly.
    """
    mock_command = MagicMock(spec=Command)
    mock_create = MagicMock(return_value=mock_command)
    original = command_parser._command_factory["global"]
    command_parser._command_factory["global"] = mock_create
    try:
        result = command_parser._create_command_object("g", ["message"])
    finally:
        command_parser._command_factory["global"] = original

    assert result == mock_command
    mock_create.assert_called_once_with(["message"])


def test_create_command_object_unsupported_command(command_parser):
    """Test _create_command_object raises error for unsupported command."""
    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._create_command_object("unsupported", [])

    assert "Unsupported command" in str(exc_info.value)


def test_create_command_object_pydantic_validation_error(command_parser: CommandParser) -> None:
    """Test _create_command_object handles Pydantic validation errors."""
    from pydantic import BaseModel

    class TestModel(BaseModel):
        """Test model for triggering Pydantic validation errors."""

        field: int

    # Create a validation error
    try:
        TestModel(field="not_an_int")
    except PydanticValidationError:
        pass

    # Create a function that raises PydanticValidationError
    def raise_pydantic_error(args):
        raise PydanticValidationError.from_exception_data(
            "TestError",
            [
                {
                    "type": "int_parsing",
                    "loc": ("field",),
                    "msg": "Input should be a valid integer",  # type: ignore[typeddict-unknown-key]  # Pydantic's from_exception_data uses "msg" key, not "message"
                    "input": "not_an_int",
                }
            ],
        )

    # Replace the factory method in the mapping
    original_method = command_parser._command_factory.get("look")
    command_parser._command_factory["look"] = raise_pydantic_error

    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._create_command_object("look", [])

    assert "Invalid command format" in str(exc_info.value)

    # Restore original (only if we successfully retrieved it)
    if original_method is not None:
        command_parser._command_factory["look"] = original_method


def test_create_command_object_value_error(command_parser):
    """Test _create_command_object handles ValueError."""
    # Replace the factory method in the mapping
    original_method = command_parser._command_factory.get("look")

    def raise_value_error(args):
        raise ValueError("Value error")

    command_parser._command_factory["look"] = raise_value_error

    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._create_command_object("look", [])

    assert "Failed to create command" in str(exc_info.value)

    # Restore original (only if we successfully retrieved it)
    if original_method is not None:
        command_parser._command_factory["look"] = original_method


def test_create_command_object_type_error(command_parser):
    """Test _create_command_object handles TypeError."""
    # Replace the factory method in the mapping
    original_method = command_parser._command_factory.get("look")

    def raise_type_error(args):
        raise TypeError("Type error")

    command_parser._command_factory["look"] = raise_type_error

    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._create_command_object("look", [])

    assert "Failed to create command" in str(exc_info.value)

    # Restore original (only if we successfully retrieved it)
    if original_method is not None:
        command_parser._command_factory["look"] = original_method


def test_create_command_object_attribute_error(command_parser):
    """Test _create_command_object handles AttributeError."""
    # Replace the factory method in the mapping
    original_method = command_parser._command_factory.get("look")

    def raise_attribute_error(args):
        raise AttributeError("Attr error")

    command_parser._command_factory["look"] = raise_attribute_error

    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._create_command_object("look", [])

    assert "Failed to create command" in str(exc_info.value)

    # Restore original (only if we successfully retrieved it)
    if original_method is not None:
        command_parser._command_factory["look"] = original_method


def test_create_command_object_key_error(command_parser):
    """Test _create_command_object handles KeyError."""
    # Replace the factory method in the mapping
    original_method = command_parser._command_factory.get("look")

    def raise_key_error(args):
        raise KeyError("Key error")

    command_parser._command_factory["look"] = raise_key_error

    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._create_command_object("look", [])

    assert "Failed to create command" in str(exc_info.value)

    # Restore original (only if we successfully retrieved it)
    if original_method is not None:
        command_parser._command_factory["look"] = original_method


def test_create_command_object_runtime_error(command_parser):
    """Test _create_command_object handles RuntimeError."""
    # Replace the factory method in the mapping
    original_method = command_parser._command_factory.get("look")

    def raise_runtime_error(args):
        raise RuntimeError("Runtime error")

    command_parser._command_factory["look"] = raise_runtime_error

    with pytest.raises(MythosValidationError) as exc_info:
        command_parser._create_command_object("look", [])

    assert "Failed to create command" in str(exc_info.value)

    # Restore original (only if we successfully retrieved it)
    if original_method is not None:
        command_parser._command_factory["look"] = original_method


def test_create_command_object_re_raises_mythos_validation_error(command_parser):
    """Test _create_command_object re-raises MythosValidationError without wrapping."""
    original_error = MythosValidationError("Original error")

    # Replace the factory method in the mapping
    original_method = command_parser._command_factory.get("look")

    def raise_mythos_error(args):
        raise original_error

    command_parser._command_factory["look"] = raise_mythos_error

    # The code should re-raise MythosValidationError without wrapping
    # The except block just does `raise` which re-raises the same exception
    with pytest.raises(MythosValidationError):
        command_parser._create_command_object("look", [])

    # Restore original (only if we successfully retrieved it)
    if original_method is not None:
        command_parser._command_factory["look"] = original_method


def test_get_command_help_specific(command_parser):
    """Test get_command_help returns help for specific command."""
    result = command_parser.get_command_help("look")

    assert "Examine your surroundings" in result


def test_get_command_help_none(command_parser):
    """Test get_command_help returns general help when command_name is None."""
    result = command_parser.get_command_help(None)

    assert "Available commands" in result
    assert "look:" in result


def test_get_command_help_unknown_command(command_parser):
    """Test get_command_help returns error message for unknown command."""
    result = command_parser.get_command_help("unknown_command")

    assert "No help available" in result


def test_get_command_help_case_insensitive(command_parser):
    """Test get_command_help is case-insensitive."""
    result_lower = command_parser.get_command_help("look")
    result_upper = command_parser.get_command_help("LOOK")

    assert result_lower == result_upper


def test_parse_command_global_function():
    """Test parse_command global function uses global parser."""
    result = parse_command("look")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.LOOK


def test_parse_command_global_function_with_args():
    """Test parse_command global function handles arguments."""
    result = parse_command("go north")

    assert isinstance(result, Command)
    assert result.command_type == CommandType.GO
