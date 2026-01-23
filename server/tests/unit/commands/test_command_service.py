"""
Unit tests for command service.

Tests the CommandService class which handles command routing, validation, and execution.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.command_service import CommandService
from server.exceptions import ValidationError as MythosValidationError


@pytest.fixture
def command_service():
    """Create a CommandService instance."""
    return CommandService()


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.fixture
def mock_user():
    """Create a mock user object."""
    return {"username": "testuser", "id": "user-id"}


@pytest.mark.asyncio
async def test_process_validated_command_success(command_service, mock_request, mock_user):
    """Test process_validated_command successfully routes to handler."""
    mock_handler = AsyncMock(return_value={"result": "Command executed"})
    command_service.command_handlers["test_command"] = mock_handler

    command_data = {"command_type": "test_command", "args": []}
    result = await command_service.process_validated_command(command_data, mock_user, mock_request, None, "TestPlayer")

    assert result == {"result": "Command executed"}
    mock_handler.assert_awaited_once_with(command_data, mock_user, mock_request, None, "TestPlayer")


@pytest.mark.asyncio
async def test_process_validated_command_no_command_type(command_service, mock_request, mock_user):
    """Test process_validated_command handles missing command_type."""
    command_data: dict[str, Any] = {}
    result = await command_service.process_validated_command(command_data, mock_user, mock_request, None, "TestPlayer")

    assert result == {"result": "Invalid command format"}


@pytest.mark.asyncio
async def test_process_validated_command_unknown_command(command_service, mock_request, mock_user):
    """Test process_validated_command handles unknown command type."""
    command_data: dict[str, Any] = {"command_type": "unknown_command"}
    result = await command_service.process_validated_command(command_data, mock_user, mock_request, None, "TestPlayer")

    assert result == {"result": "Unknown command: unknown_command"}


@pytest.mark.asyncio
async def test_process_validated_command_handler_error(command_service, mock_request, mock_user):
    """Test process_validated_command handles handler errors."""
    mock_handler = AsyncMock(side_effect=ValueError("Handler error"))
    command_service.command_handlers["test_command"] = mock_handler

    command_data = {"command_type": "test_command"}
    result = await command_service.process_validated_command(command_data, mock_user, mock_request, None, "TestPlayer")

    assert "Error processing test_command command" in result["result"]


@pytest.mark.asyncio
async def test_process_validated_command_validation_error(command_service, mock_request, mock_user):
    """Test process_validated_command handles ValidationError."""
    mock_handler = AsyncMock(side_effect=MythosValidationError("Validation failed"))
    command_service.command_handlers["test_command"] = mock_handler

    command_data = {"command_type": "test_command"}
    result = await command_service.process_validated_command(command_data, mock_user, mock_request, None, "TestPlayer")

    assert "Error processing test_command command" in result["result"]


@pytest.mark.asyncio
async def test_process_validated_command_logging_error(command_service, mock_request, mock_user):
    """Test process_validated_command handles logging errors gracefully."""
    mock_handler = AsyncMock(side_effect=RuntimeError("Handler error"))
    command_service.command_handlers["test_command"] = mock_handler

    # Mock traceback.format_exc to raise an error
    with patch("server.commands.command_service.traceback.format_exc", side_effect=ValueError("Logging error")):
        command_data: dict[str, Any] = {"command_type": "test_command"}
        result = await command_service.process_validated_command(
            command_data, mock_user, mock_request, None, "TestPlayer"
        )

        # Should still return error message even if logging fails
        assert "Error processing test_command command" in result["result"]


def test_parse_command_string_success(command_service):
    """Test _parse_command_string successfully parses command."""
    with patch("server.commands.command_service.parse_command") as mock_parse:
        mock_parsed = MagicMock()
        mock_parsed.command_type.value = "look"
        mock_parsed.args = ["at", "item"]
        mock_parsed.subcommand = None  # Explicitly set to None to avoid subcommand prepending
        mock_parse.return_value = mock_parsed

        result = command_service._parse_command_string("look at item", "TestPlayer")

        assert isinstance(result, tuple)
        assert result[0] == mock_parsed
        assert result[1] == "look"
        assert result[2] == ["at", "item"]


def test_parse_command_string_with_subcommand(command_service):
    """Test _parse_command_string handles subcommands."""
    with patch("server.commands.command_service.parse_command") as mock_parse:
        mock_parsed = MagicMock()
        mock_parsed.command_type.value = "admin"
        mock_parsed.args = ["arg1", "arg2"]
        mock_parsed.subcommand = "teleport"
        mock_parse.return_value = mock_parsed

        result = command_service._parse_command_string("admin teleport arg1 arg2", "TestPlayer")

        assert isinstance(result, tuple)
        assert result[2] == ["teleport", "arg1", "arg2"]  # Subcommand prepended


def test_parse_command_string_validation_error(command_service):
    """Test _parse_command_string handles ValidationError."""
    with patch("server.commands.command_service.parse_command", side_effect=MythosValidationError("Invalid command")):
        result = command_service._parse_command_string("invalid command", "TestPlayer")

        assert isinstance(result, dict)
        assert "result" in result
        assert "Invalid command" in result["result"]


def test_parse_command_string_unexpected_error(command_service):
    """Test _parse_command_string handles unexpected errors."""
    with patch("server.commands.command_service.parse_command", side_effect=RuntimeError("Unexpected error")):
        result = command_service._parse_command_string("command", "TestPlayer")

        assert isinstance(result, dict)
        assert "Error processing command" in result["result"]


def test_prepare_command_data_basic(command_service):
    """Test _prepare_command_data creates basic command_data dict."""
    mock_parsed = MagicMock()
    mock_parsed.model_dump = MagicMock(return_value={"field1": "value1", "args": ["arg1", "arg2"]})

    result = command_service._prepare_command_data(mock_parsed, "look", ["arg1", "arg2"], "TestPlayer")

    assert result["command_type"] == "look"
    assert result["args"] == ["arg1", "arg2"]
    assert result["field1"] == "value1"


def test_prepare_command_data_with_pipe_target(command_service):
    """Test _prepare_command_data includes pipe_target if present."""
    mock_parsed = MagicMock()
    mock_parsed.model_dump = MagicMock(return_value={"pipe_target": "inventory", "args": ["arg1"]})

    result = command_service._prepare_command_data(mock_parsed, "look", ["arg1"], "TestPlayer")

    assert result["pipe_target"] == "inventory"


def test_extract_parsed_fields_basic(command_service):
    """Test _extract_parsed_fields extracts basic fields."""
    mock_parsed = MagicMock()
    mock_parsed.model_dump = MagicMock(return_value={"args": ["arg1"], "pipe_target": None})
    command_data: dict[str, Any] = {}

    result = command_service._extract_parsed_fields(mock_parsed, "look", "TestPlayer", command_data)

    assert "args" in result
    assert result["args"] == ["arg1"]


def test_extract_parsed_fields_with_pipe_target(command_service):
    """Test _extract_parsed_fields includes pipe_target."""
    mock_parsed = MagicMock()
    mock_parsed.model_dump = MagicMock(return_value={"args": [], "pipe_target": "inventory"})
    command_data: dict[str, Any] = {}

    result = command_service._extract_parsed_fields(mock_parsed, "look", "TestPlayer", command_data)

    assert result["pipe_target"] == "inventory"


def test_extract_parsed_fields_handles_missing_attributes(command_service):
    """Test _extract_parsed_fields handles missing attributes gracefully."""
    mock_parsed = MagicMock()
    mock_parsed.model_dump = MagicMock(side_effect=AttributeError("No model_dump"))
    # Mock dir() to return some attributes
    mock_parsed.field1 = "value1"
    command_data: dict[str, Any] = {}

    with patch("builtins.dir", return_value=["field1", "__class__", "__init__"]):
        result = command_service._extract_parsed_fields(mock_parsed, "look", "TestPlayer", command_data)

    # Should not raise, returns dict with available fields
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_execute_command_handler_success(command_service, mock_request, mock_user):
    """Test _execute_command_handler successfully executes handler."""
    mock_handler = AsyncMock(return_value={"result": "Success"})
    mock_parsed = MagicMock()

    command_data: dict[str, Any] = {"command_type": "test", "args": []}
    result = await command_service._execute_command_handler(
        mock_handler, command_data, mock_parsed, mock_user, mock_request, None, "TestPlayer", "test"
    )

    assert result == {"result": "Success"}
    mock_handler.assert_awaited_once_with(command_data, mock_user, mock_request, None, "TestPlayer")


@pytest.mark.asyncio
async def test_execute_command_handler_error(command_service, mock_request, mock_user):
    """Test _execute_command_handler handles handler errors."""
    mock_handler = AsyncMock(side_effect=ValueError("Handler error"))
    mock_parsed = MagicMock()

    command_data: dict[str, Any] = {"command_type": "test"}
    result = await command_service._execute_command_handler(
        mock_handler, command_data, mock_parsed, mock_user, mock_request, None, "TestPlayer", "test"
    )

    assert "Error processing command" in result["result"]


@pytest.mark.asyncio
async def test_process_command_success(command_service, mock_request, mock_user):
    """Test process_command successfully processes command string."""
    mock_handler = AsyncMock(return_value={"result": "Success"})
    command_service.command_handlers["look"] = mock_handler

    mock_parsed = MagicMock()
    mock_parsed.model_dump = MagicMock(return_value={"args": ["at", "item"]})

    with patch.object(command_service, "_parse_command_string", return_value=(mock_parsed, "look", ["at", "item"])):
        result = await command_service.process_command("look at item", mock_user, mock_request, None, "TestPlayer")

        assert result == {"result": "Success"}


@pytest.mark.asyncio
async def test_process_command_parse_error(command_service, mock_request, mock_user):
    """Test process_command handles parse errors."""
    with patch.object(command_service, "_parse_command_string", return_value={"result": "Parse error"}):
        result = await command_service.process_command("invalid command", mock_user, mock_request, None, "TestPlayer")

        assert result == {"result": "Parse error"}


@pytest.mark.asyncio
async def test_process_command_no_handler(command_service, mock_request, mock_user):
    """Test process_command handles missing handler."""
    mock_parsed = MagicMock()
    with patch.object(command_service, "_parse_command_string", return_value=(mock_parsed, "unknown", [])):
        result = await command_service.process_command("unknown command", mock_user, mock_request, None, "TestPlayer")

        assert "Unknown command" in result["result"]


def test_get_available_commands(command_service):
    """Test get_available_commands returns list of registered commands."""
    commands = command_service.get_available_commands()

    assert isinstance(commands, list)
    assert "look" in commands
    assert "say" in commands
    assert "who" in commands
    assert len(commands) > 0


def test_register_command_handler(command_service):
    """Test register_command_handler adds new handler."""
    mock_handler = AsyncMock()

    command_service.register_command_handler("custom_command", mock_handler)

    assert "custom_command" in command_service.command_handlers
    assert command_service.command_handlers["custom_command"] == mock_handler


def test_register_command_handler_overwrites_existing(command_service):
    """Test register_command_handler overwrites existing handler."""
    original_handler = command_service.command_handlers["look"]
    new_handler = AsyncMock()

    command_service.register_command_handler("look", new_handler)

    assert command_service.command_handlers["look"] == new_handler
    assert command_service.command_handlers["look"] != original_handler


def test_unregister_command_handler(command_service):
    """Test unregister_command_handler removes handler."""
    assert "look" in command_service.command_handlers

    command_service.unregister_command_handler("look")

    assert "look" not in command_service.command_handlers


def test_unregister_command_handler_nonexistent(command_service):
    """Test unregister_command_handler handles nonexistent command."""
    # Should not raise
    command_service.unregister_command_handler("nonexistent_command")


def test_log_parsed_command_inspection(command_service):
    """Test _log_parsed_command_inspection logs command inspection."""
    mock_parsed = MagicMock()

    # Should not raise
    command_service._log_parsed_command_inspection(mock_parsed, "look", "TestPlayer")


def test_log_model_dump_result(command_service):
    """Test _log_model_dump_result logs model dump."""
    parsed_fields = {"field1": "value1", "field2": "value2"}

    # Should not raise
    command_service._log_model_dump_result(parsed_fields, "look", "TestPlayer")


@pytest.mark.asyncio
async def test_execute_command_handler_returns_non_dict(command_service, mock_request, mock_user):
    """Test _execute_command_handler handles handler returning non-dict."""
    # This shouldn't happen in practice, but test defensive code
    mock_handler = AsyncMock(return_value="string result")
    mock_parsed = MagicMock()

    command_data: dict[str, Any] = {"command_type": "test"}

    # The code catches TypeError and returns an error dict instead of raising
    result = await command_service._execute_command_handler(
        mock_handler, command_data, mock_parsed, mock_user, mock_request, None, "TestPlayer", "test"
    )

    assert "Error processing command" in result["result"]
    assert "Command handler must return a dict" in result["result"]
