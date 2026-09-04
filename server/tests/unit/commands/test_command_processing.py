"""Unit tests for command_handler.processing module."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.command_handler import processing
from server.exceptions import ValidationError


def test_parse_command_line_or_client_error_with_message() -> None:
    with patch(
        "server.command_handler.processing.command_processor.process_command_string",
        return_value=(None, "Bad command", "look"),
    ):
        validated, cmd_type, err = processing._parse_command_line_or_client_error("bad", "player1")

    assert validated is None
    assert cmd_type == "look"
    assert err == {"result": "Bad command"}


def test_parse_command_line_or_client_error_no_validated() -> None:
    with patch(
        "server.command_handler.processing.command_processor.process_command_string",
        return_value=(None, None, None),
    ):
        validated, cmd_type, err = processing._parse_command_line_or_client_error("x", "player1")

    assert validated is None
    assert err == {"result": "Invalid command format"}


def test_parse_command_line_or_client_error_success() -> None:
    mock_cmd = MagicMock()
    with patch(
        "server.command_handler.processing.command_processor.process_command_string",
        return_value=(mock_cmd, None, "look"),
    ):
        validated, cmd_type, err = processing._parse_command_line_or_client_error("look", "player1")

    assert validated is mock_cmd
    assert cmd_type == "look"
    assert err is None


@pytest.mark.asyncio
async def test_dispatch_parsed_command_client_error() -> None:
    with patch(
        "server.command_handler.processing._parse_command_line_or_client_error",
        return_value=(None, None, {"result": "nope"}),
    ):
        result = await processing._dispatch_parsed_command("x", {}, MagicMock(), None, "player1")

    assert result == {"result": "nope"}


@pytest.mark.asyncio
async def test_dispatch_parsed_command_success() -> None:
    mock_cmd = MagicMock()
    with (
        patch(
            "server.command_handler.processing._parse_command_line_or_client_error",
            return_value=(mock_cmd, "look", None),
        ),
        patch(
            "server.command_handler.processing._run_command_service_for_validated",
            new_callable=AsyncMock,
            return_value={"result": "You look around."},
        ) as mock_run,
    ):
        result = await processing._dispatch_parsed_command("look", {}, MagicMock(), None, "player1")

    assert result == {"result": "You look around."}
    mock_run.assert_awaited_once()


@pytest.mark.asyncio
async def test_run_command_service_security_sensitive_audit() -> None:
    mock_cmd = MagicMock()
    mock_request = MagicMock()
    mock_request.state = MagicMock(session_id="sess-1")

    with (
        patch(
            "server.command_handler.processing.command_processor.extract_command_data",
            return_value={"command": "admin"},
        ),
        patch(
            "server.command_handler.processing.command_service.process_validated_command",
            new_callable=AsyncMock,
            return_value={"result": "done"},
        ),
        patch("server.command_handler.processing.CommandValidator.is_security_sensitive", return_value=True),
        patch("server.command_handler.processing.audit_logger") as audit,
    ):
        result = await processing._run_command_service_for_validated(
            mock_cmd, "admin", "admin kick player1", {}, mock_request, None, "admin1"
        )

    assert result == {"result": "done"}
    audit.log_command.assert_called_once()


def test_log_security_sensitive_command_no_session() -> None:
    mock_request = MagicMock()
    del mock_request.state

    with (
        patch("server.command_handler.processing.audit_logger") as audit,
        patch("server.command_handler.processing.logger"),
        patch(
            "server.command_handler.processing.CommandValidator.sanitize_for_logging",
            return_value="admin kick",
        ),
    ):
        processing._log_security_sensitive_command("admin1", "admin kick x", "admin", {"result": "ok"}, mock_request)

    audit.log_command.assert_called_once()
    assert audit.log_command.call_args.kwargs["session_id"] is None


def test_handle_validation_error_security_sensitive() -> None:
    err = ValidationError("invalid command")
    with (
        patch("server.command_handler.processing.CommandValidator.is_security_sensitive", return_value=True),
        patch("server.command_handler.processing.audit_logger") as audit,
    ):
        result = processing._handle_validation_error(err, "admin x", "player1")

    assert result == {"result": "Invalid command format"}
    audit.log_command.assert_called_once()


def test_handle_processing_error() -> None:
    with (
        patch("server.command_handler.processing.CommandValidator.is_security_sensitive", return_value=False),
        patch("server.command_handler.processing.traceback.format_exc", return_value="trace"),
        patch("server.command_handler.processing.strip_ansi_codes", return_value="trace"),
        patch("server.command_handler.processing.logger") as log_mock,
    ):
        result = processing._handle_processing_error(RuntimeError("boom"), "look", "player1")

    assert result == {"result": "An error occurred while processing your command."}
    log_mock.error.assert_called_once()


@pytest.mark.asyncio
async def test_process_command_with_validation_validation_error() -> None:
    with patch(
        "server.command_handler.processing._dispatch_parsed_command",
        new_callable=AsyncMock,
        side_effect=ValidationError("bad command"),
    ):
        result = await processing.process_command_with_validation("bad", {}, MagicMock(), None, "player1")

    assert result == {"result": "Invalid command format"}


@pytest.mark.asyncio
async def test_process_command_with_validation_generic_error() -> None:
    with patch(
        "server.command_handler.processing._dispatch_parsed_command",
        new_callable=AsyncMock,
        side_effect=RuntimeError("fail"),
    ):
        result = await processing.process_command_with_validation("look", {}, MagicMock(), None, "player1")

    assert result == {"result": "An error occurred while processing your command."}
