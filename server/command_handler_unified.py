"""
Unified Command Handler for MythosMUD.

This module provides a single, unified command processing system that
works for both HTTP API and WebSocket connections. It replaces the
previous command_handler_v2.py and provides a clean, maintainable
architecture for all command processing.

As the Necronomicon states: "In unity there is strength, and in
consistency there is power."
"""

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel

from .alias_storage import AliasStorage
from .auth.users import get_current_user
from .command_handler import (
    MAX_COMMAND_LENGTH,
    check_alias_safety,
    check_catatonia_block,
    clean_command_input,
    handle_expanded_command,
    normalize_command,
    process_command_with_validation,
    should_treat_as_emote,
    validate_expanded_command,
)
from .commands.command_service import CommandService
from .config import get_config
from .help.help_content import get_help_content as get_help_content_new
from .middleware.command_rate_limiter import command_rate_limiter
from .structured_logging.enhanced_logging_config import get_logger
from .utils.audit_logger import audit_logger
from .utils.command_parser import get_username_from_user
from .validators.command_validator import CommandValidator

logger = get_logger(__name__)

router = APIRouter(prefix="/command", tags=["command"])

# Global instances
command_service = CommandService()


class CommandRequest(BaseModel):
    """Request model for command processing."""

    command: str


async def process_command_unified(
    command_line: str,
    current_user: dict,
    request: Request,
    alias_storage: AliasStorage | None = None,
    player_name: str | None = None,
) -> dict[str, Any]:
    """
    Unified command processing function for both HTTP and WebSocket.

    This is the single source of truth for all command processing in MythosMUD.
    It handles command validation, alias expansion, and routing to appropriate handlers.

    Args:
        command_line: The raw command string
        current_user: Current user information
        request: FastAPI request object (or WebSocket request context)
        alias_storage: Optional alias storage instance
        player_name: Optional player name (will be extracted from current_user if not provided)

    Returns:
        dict: Command result with 'result' key and optional metadata
    """
    # Extract player name if not provided
    if not player_name:
        player_name = get_username_from_user(current_user)

    logger.debug(
        "=== UNIFIED COMMAND HANDLER: Processing command ===",
        player=player_name,
        command=command_line,
    )

    # Step 1: Command Rate Limiting (CRITICAL-3)
    # Prevent command flooding and DoS attacks
    rate_limit_result = _check_rate_limit(player_name)
    if rate_limit_result:
        return rate_limit_result

    # Step 2: Basic validation
    validation_result = _validate_command_basics(command_line, player_name)
    if validation_result:
        return validation_result

    # Step 3: Clean and normalize command
    command_line = clean_command_input(command_line)
    if not command_line:
        logger.debug("Empty command after cleaning")
        return {"result": ""}

    command_line = normalize_command(command_line)
    if not command_line:
        logger.debug("Empty command after normalization")
        return {"result": ""}

    # Step 4: Initialize alias storage if not provided
    alias_storage = _ensure_alias_storage(alias_storage)

    # Step 5: Parse command and arguments
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    logger.debug(
        "Command parsed",
        player=player_name,
        command=cmd,
        args=args,
        original_command=command_line,
    )

    # Step 6: Check catatonia
    logger.debug("Checking catatonia before command processing", player=player_name, command=cmd)
    block_catatonia, catatonia_message = await check_catatonia_block(player_name, cmd, request)
    logger.debug(
        "Catatonia check result",
        player=player_name,
        command=cmd,
        block=block_catatonia,
        message=catatonia_message,
    )
    if block_catatonia:
        logger.info(
            "Command blocked due to catatonia",
            player=player_name,
            command=cmd,
            message=catatonia_message,
        )
        return {"result": catatonia_message}

    # Step 7: Check if player is casting
    casting_result = await _check_casting_state(cmd, player_name, request)
    if casting_result:
        return casting_result

    # Step 8: Handle alias management commands first (don't expand these)
    if cmd in ["alias", "aliases", "unalias"]:
        logger.debug("Processing alias management command", player=player_name, command=cmd)
        if alias_storage is None:
            return {"result": "Alias system not available"}
        return await command_service.process_command(command_line, current_user, request, alias_storage, player_name)

    # Step 9: Check for alias expansion with cycle detection
    alias_result = await _process_alias_expansion(cmd, args, alias_storage, player_name, current_user, request)
    if alias_result:
        return alias_result

    # Step 10: Check if single word command is an emote
    if not args and should_treat_as_emote(cmd):
        logger.debug(
            "Single word emote detected, converting to emote command",
            player=player_name,
            emote=cmd,
        )
        emote_command = f"emote {cmd}"
        return await command_service.process_command(emote_command, current_user, request, alias_storage, player_name)

    # Step 11: Process command with validation system
    logger.debug("Processing command with validation system", player=player_name, command=cmd)
    return await process_command_with_validation(command_line, current_user, request, alias_storage, player_name)


def _check_rate_limit(player_name: str) -> dict[str, Any] | None:
    """Check if player is rate limited. Returns result dict if blocked, None if allowed."""
    if not command_rate_limiter.is_allowed(player_name):
        wait_time = command_rate_limiter.get_wait_time(player_name)
        logger.warning("Command rate limit exceeded", player=player_name, wait_time=wait_time)
        # Log security event
        audit_logger.log_security_event(
            event_type="rate_limit_violation",
            player_name=player_name,
            description=f"Command rate limit exceeded, wait {wait_time:.1f}s",
            severity="medium",
            metadata={"wait_time": wait_time},
        )
        return {"result": f"Too many commands. Please wait {wait_time:.1f} seconds."}
    return None


def _validate_command_basics(command_line: str, player_name: str) -> dict[str, Any] | None:
    """Validate basic command requirements. Returns result dict if invalid, None if valid."""
    if not command_line:
        logger.debug("Empty command received")
        return {"result": ""}

    if len(command_line) > MAX_COMMAND_LENGTH:
        logger.warning(
            "Command too long rejected",
            player=player_name,
            length=len(command_line),
            max_length=MAX_COMMAND_LENGTH,
        )
        return {"result": f"Command too long (max {MAX_COMMAND_LENGTH} characters)"}

    # Command Content Validation (CRITICAL-3)
    # Prevent command injection and malicious input
    is_valid, validation_error = CommandValidator.validate_command_content(command_line)
    if not is_valid:
        logger.warning(
            "Command validation failed",
            player=player_name,
            error=validation_error,
            command=CommandValidator.sanitize_for_logging(command_line),
        )
        # Log security event
        audit_logger.log_security_event(
            event_type="command_injection_attempt",
            player_name=player_name,
            description=validation_error or "Invalid command format",
            severity="high",
            metadata={"command_sample": command_line[:100]},
        )
        return {"result": "Invalid command format"}

    return None


def _ensure_alias_storage(alias_storage: AliasStorage | None) -> AliasStorage | None:
    """Ensure alias storage is initialized."""
    if alias_storage:
        return alias_storage

    try:
        config = get_config()
        aliases_dir = config.game.aliases_dir
        storage = AliasStorage(storage_dir=aliases_dir) if aliases_dir else AliasStorage()
        logger.debug("AliasStorage initialized")
        return storage
    except (OSError, ValueError, TypeError) as e:
        logger.error(
            "Failed to initialize AliasStorage",
            error=str(e),
            error_type=type(e).__name__,
        )
        return None


async def _check_casting_state(cmd: str, player_name: str, request: Request) -> dict[str, Any] | None:
    """Check if player is casting and should be blocked. Returns result if blocked."""
    # Allow: stop, interrupt, status
    allowed_during_casting = ["stop", "interrupt", "status"]
    if cmd in allowed_during_casting:
        return None

    try:
        # Get magic service from app state
        magic_service = getattr(request.app.state, "magic_service", None)
        if magic_service and magic_service.casting_state_manager:
            # Get player ID
            player_service = getattr(request.app.state, "player_service", None)
            if player_service:
                player = await player_service.get_player_by_name(player_name)
                if player and magic_service.casting_state_manager.is_casting(player.player_id):
                    casting_state = magic_service.casting_state_manager.get_casting_state(player.player_id)
                    if casting_state:
                        return {"result": f"You are casting {casting_state.spell_name}. Use 'stop' to interrupt."}
    except (AttributeError, OSError, TypeError, RuntimeError) as e:
        # If we can't check casting state, allow command to proceed
        logger.debug("Could not check casting state", player=player_name, error=str(e))

    return None


async def _process_alias_expansion(
    cmd: str,
    args: list[str],
    alias_storage: AliasStorage | None,
    player_name: str,
    current_user: dict,
    request: Request,
) -> dict[str, Any] | None:
    """Process alias expansion if applicable. Returns result if alias processed."""
    if not alias_storage:
        return None

    alias = alias_storage.get_alias(player_name, cmd)
    if not alias:
        return None

    logger.debug(
        "Alias found, checking safety",
        player=player_name,
        alias_name=alias.name,
        original_command=cmd,
    )

    # Check alias safety (cycles, depth)
    is_safe, error_msg, expansion_depth = await check_alias_safety(alias_storage, player_name, alias.name)
    if not is_safe:
        return {"result": error_msg}

    # Expand the alias
    expanded_command = alias.get_expanded_command(args)

    # Validate expanded command
    is_valid, validation_error = validate_expanded_command(expanded_command, player_name, alias.name, expansion_depth)
    if not is_valid:
        return {"result": validation_error}

    # Log successful alias expansion
    audit_logger.log_alias_expansion(
        player_name=player_name,
        alias_name=alias.name,
        expanded_command=expanded_command,
        cycle_detected=False,
        expansion_depth=expansion_depth,
    )

    logger.debug(
        "Alias safe to expand",
        player=player_name,
        alias_name=alias.name,
        depth=expansion_depth,
    )

    # Recursively process the expanded command
    result = await handle_expanded_command(
        expanded_command,
        current_user,
        request,
        alias_storage,
        player_name,
        depth=0,
        alias_chain=[],
    )
    # Add alias chain information to the result
    if "alias_chain" not in result:
        result["alias_chain"] = [{"original": cmd, "expanded": expanded_command, "alias_name": alias.name}]
    return result


# HTTP API endpoint
@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def handle_command(
    req: CommandRequest,
    request: Request,
    current_user: dict = Depends(get_current_user),
) -> dict[str, Any]:
    """Handle incoming HTTP command requests."""
    command_line = req.command

    # Check if user is authenticated
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")

    player_name = get_username_from_user(current_user)
    logger.info(
        "HTTP command received",
        player=player_name,
        command=command_line,
        length=len(command_line),
    )

    # Process command using unified handler
    result = await process_command_unified(command_line, current_user, request, player_name=player_name)

    logger.debug("HTTP command processed successfully", player=player_name, result=result)
    return result


# Legacy compatibility function
async def process_command(
    cmd: str,
    args: list[str],
    current_user: dict,
    request: Request,
    alias_storage: AliasStorage,
    player_name: str,
) -> dict[str, Any]:
    """
    Legacy command processing function for backward compatibility.

    This function maintains compatibility with existing code that expects
    the old command signature while delegating to the new unified system.
    """
    logger.debug("Using legacy command processing", player=player_name, command=cmd, args=args)

    # Reconstruct the command line
    command_line = f"{cmd} {' '.join(args)}".strip()

    # Use the new unified system
    return await process_command_unified(command_line, current_user, request, alias_storage, player_name)


def get_help_content(command_name: str | None = None) -> str:
    """
    Get help content for commands.

    This is a compatibility function that delegates to the new help system.
    """
    return get_help_content_new(command_name)
