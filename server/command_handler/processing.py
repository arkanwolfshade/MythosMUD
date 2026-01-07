"""
Command Processing Logic for MythosMUD.

This module contains the core command validation and processing logic,
including the main validation pipeline and error handling.
"""

import traceback
from typing import TYPE_CHECKING, Any

from ..commands.command_service import CommandService
from ..exceptions import ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import audit_logger
from ..utils.command_processor import get_command_processor
from ..validators.command_validator import CommandValidator
from ..validators.security_validator import strip_ansi_codes

if TYPE_CHECKING:
    from fastapi import Request

    from ..alias_storage import AliasStorage

logger = get_logger(__name__)

# Global instances
command_service = CommandService()
command_processor = get_command_processor()


async def process_command_with_validation(
    command_line: str,
    current_user: dict,
    request: "Request",
    alias_storage: "AliasStorage | None",
    player_name: str,
) -> dict[str, Any]:
    """
    Process a command using the Pydantic + Click validation system.

    This function validates the command through the new validation pipeline,
    extracts command data, and routes to the appropriate handler.

    Args:
        command_line: The command line to process
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Optional alias storage instance
        player_name: The player's name

    Returns:
        dict: Command result with 'result' key and optional metadata
    """
    logger.debug(
        "=== UNIFIED COMMAND HANDLER: Processing with validation ===",
        player=player_name,
        command=command_line,
    )

    try:
        # Use our command processor for validation
        validated_command, error_message, command_type = command_processor.process_command_string(
            command_line, player_name
        )

        if error_message:
            logger.warning("Command validation failed", player=player_name, error=error_message)
            return {"result": error_message}

        if not validated_command:
            logger.warning("No validated command returned")
            return {"result": "Invalid command format"}

        # Extract command data for processing
        command_data = command_processor.extract_command_data(validated_command)
        command_data["player_name"] = player_name

        logger.debug(
            "Command validated successfully",
            player=player_name,
            command_type=command_type,
            data=command_data,
        )

        # Use the command service for processing with validated data
        result = await command_service.process_validated_command(
            command_data, current_user, request, alias_storage, player_name
        )

        logger.debug(
            "Command processed successfully",
            player=player_name,
            command_type=command_type,
        )

        # Audit logging for security-sensitive commands (CRITICAL-3)
        # Log admin/privileged commands for security auditing and compliance
        if CommandValidator.is_security_sensitive(command_line):
            _log_security_sensitive_command(player_name, command_line, command_type, result, request)

        return result

    except ValidationError as e:
        return _handle_validation_error(e, command_line, player_name)
    except Exception as e:  # pylint: disable=broad-except  # Reason: Command processing must catch all exceptions to ensure proper error logging and user-friendly error responses. Security-sensitive command errors are logged with full context for auditing. Test compatibility requires catching generic Exception from mocks. All exceptions are sanitized before user exposure per security requirements.
        return _handle_processing_error(e, command_line, player_name)


def _log_security_sensitive_command(
    player_name: str,
    command_line: str,
    command_type: str | None,
    result: dict[str, Any],
    request: "Request",
) -> None:
    """Log a security-sensitive command for auditing."""
    # Extract session if available
    session_id = getattr(request.state, "session_id", None) if hasattr(request, "state") else None

    audit_logger.log_command(
        player_name=player_name,
        command=command_line,
        success=True,  # If we got here, command was successful
        result=str(result.get("result", ""))[:500],  # Truncate result
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
) -> dict[str, Any]:
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
) -> dict[str, Any]:
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
