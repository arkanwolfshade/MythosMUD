"""
Command Processing Logic for MythosMUD.

This module contains the core command validation and processing logic,
including the main validation pipeline and error handling.
"""

import traceback
from typing import TYPE_CHECKING, cast

from structlog.stdlib import BoundLogger

from ..commands.command_service import CommandService
from ..exceptions import ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import audit_logger
from ..utils.command_processor import get_command_processor
from ..validators.command_validator import CommandValidator
from ..validators.security_validator import strip_ansi_codes
from .command_execution_request import CommandExecutionRequest

if TYPE_CHECKING:
    from ..alias_storage import AliasStorage

logger: BoundLogger = get_logger(__name__)

# Global instances
command_service = CommandService()
command_processor = get_command_processor()


def _parse_command_line_or_client_error(
    command_line: str, player_name: str
) -> tuple[object | None, str | None, dict[str, object] | None]:
    """
    Validate the raw command string via CommandProcessor.

    Returns:
        (validated_command, command_type, client_error_response).
        When client_error_response is not None, return it to the caller and skip execution.
    """
    validated_command, error_message, command_type = command_processor.process_command_string(command_line, player_name)
    if error_message:
        return None, command_type, {"result": error_message}
    if not validated_command:
        logger.warning("No validated command returned")
        return None, command_type, {"result": "Invalid command format"}
    return validated_command, command_type, None


async def _run_command_service_for_validated(
    validated_command: object,
    command_type: str | None,
    command_line: str,
    current_user: dict[str, object],
    request: CommandExecutionRequest,
    alias_storage: "AliasStorage | None",
    player_name: str,
) -> dict[str, object]:
    """Extract structured command data, dispatch to CommandService, audit if needed."""
    command_data: dict[str, object] = cast(dict[str, object], command_processor.extract_command_data(validated_command))
    command_data["player_name"] = player_name

    logger.debug(
        "Command validated successfully",
        player=player_name,
        command_type=command_type,
        data=command_data,
    )

    result = await command_service.process_validated_command(
        command_data, current_user, request, alias_storage, player_name
    )

    logger.debug(
        "Command processed successfully",
        player=player_name,
        command_type=command_type,
    )

    if CommandValidator.is_security_sensitive(command_line):
        _log_security_sensitive_command(player_name, command_line, command_type, result, request)

    return result


async def _dispatch_parsed_command(
    command_line: str,
    current_user: dict[str, object],
    request: CommandExecutionRequest,
    alias_storage: "AliasStorage | None",
    player_name: str,
) -> dict[str, object]:
    """Parse the command line; on success run CommandService (see ``_parse_command_line_or_client_error``)."""
    validated_command, command_type, client_error = _parse_command_line_or_client_error(command_line, player_name)
    if client_error is not None:
        return client_error
    if validated_command is None:
        logger.warning("Validated command missing after successful parse branch")
        return {"result": "Invalid command format"}
    return await _run_command_service_for_validated(
        validated_command,
        command_type,
        command_line,
        current_user,
        request,
        alias_storage,
        player_name,
    )


async def process_command_with_validation(
    command_line: str,
    current_user: dict[str, object],
    request: CommandExecutionRequest,
    alias_storage: "AliasStorage | None",
    player_name: str,
) -> dict[str, object]:
    """Validate ``command_line`` via Click/Pydantic, dispatch to handlers; result dict includes ``result``."""
    logger.debug(
        "=== UNIFIED COMMAND HANDLER: Processing with validation ===",
        player=player_name,
        command=command_line,
    )

    try:
        return await _dispatch_parsed_command(command_line, current_user, request, alias_storage, player_name)

    except ValidationError as e:
        return _handle_validation_error(e, command_line, player_name)
    except Exception as e:  # pylint: disable=broad-except  # Reason: Command processing must catch all exceptions to ensure proper error logging and user-friendly error responses. Security-sensitive command errors are logged with full context for auditing. Test compatibility requires catching generic Exception from mocks. All exceptions are sanitized before user exposure per security requirements.
        return _handle_processing_error(e, command_line, player_name)


def _log_security_sensitive_command(
    player_name: str,
    command_line: str,
    command_type: str | None,
    result: dict[str, object],
    request: CommandExecutionRequest,
) -> None:
    """Log a security-sensitive command for auditing."""
    # Extract session if available (HTTP Request has .state; WebSocketRequestContext does not)
    req_obj: CommandExecutionRequest = request
    req_state: object | None = getattr(req_obj, "state", None)
    session_raw: object | None = getattr(req_state, "session_id", None) if req_state is not None else None
    session_id: str | None
    if session_raw is None:
        session_id = None
    elif isinstance(session_raw, str):
        session_id = session_raw
    else:
        session_id = str(session_raw)

    raw_result = result.get("result", "")
    result_preview = str(raw_result) if raw_result is not None else ""

    audit_logger.log_command(
        player_name=player_name,
        command=command_line,
        success=True,  # If we got here, command was successful
        result=result_preview[:500],  # Truncate result
        session_id=session_id,
        metadata={"command_type": command_type},
    )

    logger.info(
        "Security-sensitive command executed",
        player=player_name,
        command=CommandValidator.sanitize_for_logging(command_line),
    )


def _handle_validation_error(
    e: ValidationError,
    command_line: str,
    player_name: str,
) -> dict[str, object]:
    """Handle a validation error during command processing."""
    logger.warning("Command validation error", error_type=type(e).__name__)

    # Audit log validation failures for security-sensitive commands (CRITICAL-3)
    if CommandValidator.is_security_sensitive(command_line):
        audit_logger.log_command(
            player_name=player_name,
            command=command_line,
            success=False,
            result="Validation error occurred",
            metadata={"error_type": "ValidationError"},
        )

    # Human reader: do not expose exception details to users.
    # AI reader: CodeQL requires no exception information exposure to external users.
    return {"result": "Invalid command format"}


def _handle_processing_error(
    e: Exception,
    command_line: str,
    player_name: str,
) -> dict[str, object]:
    """Handle a general exception during command processing."""
    # Audit log processing failures for security-sensitive commands (CRITICAL-3)
    if CommandValidator.is_security_sensitive(command_line):
        audit_logger.log_command(
            player_name=player_name,
            command=command_line,
            success=False,
            result="Processing error occurred",
            metadata={"error_type": type(e).__name__},
        )

    # Format exception traceback and sanitize ANSI codes for Windows compatibility
    try:
        exc_traceback = traceback.format_exc()
        # Strip ANSI codes to prevent UnicodeEncodeError on Windows console
        sanitized_traceback = strip_ansi_codes(exc_traceback)
        logger.error(
            "Error processing command",
            player=player_name,
            error=str(e),
            error_type=type(e).__name__,
            traceback=sanitized_traceback,
        )
    except (ImportError, AttributeError, TypeError, RuntimeError) as log_error:
        # If logging itself fails, use a minimal safe log
        try:
            logger.error(
                "Error processing command (logging error occurred)",
                player=player_name,
                error=str(e)[:200],  # Truncate to avoid encoding issues
                log_error=str(log_error)[:200],
            )
        except (ImportError, AttributeError, TypeError, RuntimeError):
            # Last resort: silent failure to prevent test crashes
            pass

    return {"result": "An error occurred while processing your command."}
