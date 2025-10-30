"""
Unified Command Handler for MythosMUD.

This module provides a single, unified command processing system that
works for both HTTP API and WebSocket connections. It replaces the
previous command_handler_v2.py and provides a clean, maintainable
architecture for all command processing.

As the Necronomicon states: "In unity there is strength, and in
consistency there is power."
"""

import re
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel

from .alias_storage import AliasStorage
from .auth.users import get_current_user
from .commands.command_service import CommandService
from .config import get_config
from .exceptions import ValidationError
from .logging.enhanced_logging_config import get_logger
from .middleware.command_rate_limiter import command_rate_limiter
from .utils.alias_graph import AliasGraph
from .utils.audit_logger import audit_logger
from .utils.command_parser import get_username_from_user
from .utils.command_processor import get_command_processor
from .validators.command_validator import CommandValidator

logger = get_logger(__name__)

router = APIRouter(prefix="/command", tags=["command"])

# Global instances
command_service = CommandService()
command_processor = get_command_processor()

# Configuration
MAX_COMMAND_LENGTH = get_config().game.max_command_length
MAX_EXPANDED_COMMAND_LENGTH = CommandValidator.MAX_EXPANDED_COMMAND_LENGTH


class CommandRequest(BaseModel):
    """Request model for command processing."""

    command: str


def clean_command_input(command: str) -> str:
    """Clean and normalize command input by collapsing multiple spaces and stripping whitespace."""
    cleaned = re.sub(r"\s+", " ", command).strip()
    if cleaned != command:
        logger.debug("Command input cleaned")
    return cleaned


def normalize_command(command: str) -> str:
    """
    Normalize command input by removing optional slash prefix.

    Supports both traditional MUD commands (go north) and modern slash commands (/go north).
    This allows for flexible command input while maintaining backward compatibility.

    Args:
        command: The raw command string from user input

    Returns:
        Normalized command string with slash prefix removed if present
    """
    if not command:
        return command

    # Strip whitespace first
    command = command.strip()

    # Remove leading slash if present
    if command.startswith("/"):
        normalized = command[1:].strip()
        logger.debug("Slash prefix removed from command")
        return normalized

    return command


def _is_predefined_emote(command: str) -> bool:
    """
    Check if a command is a predefined emote alias.

    Args:
        command: The command to check

    Returns:
        True if the command is a predefined emote, False otherwise
    """
    try:
        from .game.emote_service import EmoteService

        emote_service = EmoteService()
        return emote_service.is_emote_alias(command)
    except Exception as e:
        logger.warning("Error checking predefined emote", error=str(e))
        return False


def _should_treat_as_emote(command: str) -> bool:
    """
    Check if a single word command should be treated as an emote.

    This function determines if a single word command is likely an emote
    rather than a system command. It excludes known system commands.

    Args:
        command: The command to check

    Returns:
        True if the command should be treated as an emote, False otherwise
    """
    # List of known system commands that should NOT be treated as emotes
    system_commands = {
        "look",
        "say",
        "go",
        "move",
        "quit",
        "logout",
        "help",
        "who",
        "emote",
        "alias",
        "aliases",
        "unalias",
        "mute",
        "mutes",
        "unmute",
        "admin",
        "pose",
        "tell",
        "whisper",
        "shout",
        "yell",
        "chat",
        "ooc",
        "ic",
        "afk",
        "back",
        "inventory",
        "inv",
        "i",
        "examine",
        "ex",
        "get",
        "take",
        "drop",
        "put",
        "give",
        "wear",
        "remove",
        "wield",
        "unwield",
        "kill",
        "attack",
        "flee",
        "rest",
        "sleep",
        "wake",
        "sit",
        "stand",
        "north",
        "south",
        "east",
        "west",
        "up",
        "down",
        "n",
        "s",
        "e",
        "w",
        "u",
        "d",
        "ne",
        "nw",
        "se",
        "sw",
        "northeast",
        "northwest",
        "southeast",
        "southwest",
        "unknown_command",
    }

    # If it's a known system command, don't treat as emote
    if command.lower() in system_commands:
        return False

    # If it's a predefined emote, treat as emote
    if _is_predefined_emote(command):
        return True

    # Only treat as emote if it's a predefined emote
    # Unknown words should go through proper command validation
    return False


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

    logger.debug("=== UNIFIED COMMAND HANDLER: Processing command ===", player=player_name, command=command_line)

    # Step 1: Command Rate Limiting (NEW - CRITICAL-3)
    # AI: Prevent command flooding and DoS attacks
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

    # Step 2: Basic validation
    if not command_line:
        logger.debug("Empty command received")
        return {"result": ""}

    if len(command_line) > MAX_COMMAND_LENGTH:
        logger.warning(
            "Command too long rejected", player=player_name, length=len(command_line), max_length=MAX_COMMAND_LENGTH
        )
        return {"result": f"Command too long (max {MAX_COMMAND_LENGTH} characters)"}

    # Step 3: Command Content Validation (NEW - CRITICAL-3)
    # AI: Prevent command injection and malicious input
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

    # Step 4: Clean and normalize command
    command_line = clean_command_input(command_line)
    if not command_line:
        logger.debug("Empty command after cleaning")
        return {"result": ""}

    command_line = normalize_command(command_line)
    if not command_line:
        logger.debug("Empty command after normalization")
        return {"result": ""}

    # Step 3: Initialize alias storage if not provided
    if not alias_storage:
        try:
            config = get_config()
            aliases_dir = config.game.aliases_dir
            alias_storage = AliasStorage(storage_dir=aliases_dir) if aliases_dir else AliasStorage()
            logger.debug("AliasStorage initialized")
        except (OSError, ValueError, TypeError) as e:
            logger.error("Failed to initialize AliasStorage", error=str(e), error_type=type(e).__name__)
            alias_storage = None

    # Step 4: Parse command and arguments
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

    # Step 5: Handle alias management commands first (don't expand these)
    if cmd in ["alias", "aliases", "unalias"]:
        logger.debug("Processing alias management command", player=player_name, command=cmd)
        if alias_storage is None:
            return {"result": "Alias system not available"}
        return await command_service.process_command(command_line, current_user, request, alias_storage, player_name)

    # Step 6: Check for alias expansion with cycle detection (ENHANCED - CRITICAL-3)
    if alias_storage:
        alias = alias_storage.get_alias(player_name, cmd)
        if alias:
            logger.debug(
                "Alias found, checking safety", player=player_name, alias_name=alias.name, original_command=cmd
            )

            # NEW: Build alias dependency graph and check for cycles
            # AI: This prevents "alias bombs" - recursive aliases that create infinite loops
            alias_graph = AliasGraph(alias_storage)
            alias_graph.build_graph(player_name)

            if not alias_graph.is_safe_to_expand(alias.name):
                cycle = alias_graph.detect_cycle(alias.name)
                cycle_path = " → ".join(cycle) if cycle else "unknown"

                logger.warning(
                    "Circular alias dependency detected - expansion blocked",
                    player=player_name,
                    alias=alias.name,
                    cycle=cycle,
                )

                # Log security event
                audit_logger.log_alias_expansion(
                    player_name=player_name,
                    alias_name=alias.name,
                    expanded_command="[BLOCKED - Circular dependency]",
                    cycle_detected=True,
                    expansion_depth=0,
                )

                return {
                    "result": f"Alias '{alias.name}' contains circular dependency: {cycle_path}\n"
                    f"Please remove the circular reference using 'unalias {alias.name}'"
                }

            # NEW: Check expansion depth as additional safety measure
            expansion_depth = alias_graph.get_expansion_depth(alias.name)
            if expansion_depth > 10:  # Reasonable depth limit
                logger.warning(
                    "Alias expansion depth too deep", player=player_name, alias=alias.name, depth=expansion_depth
                )
                return {
                    "result": f"Alias '{alias.name}' has excessive expansion depth ({expansion_depth} levels). "
                    f"Maximum allowed is 10."
                }

            # Expand the alias
            expanded_command = alias.get_expanded_command(args)

            # NEW: Validate expanded command length
            # AI: Prevent expansion attacks where small aliases expand to huge commands
            if len(expanded_command) > MAX_EXPANDED_COMMAND_LENGTH:
                logger.warning(
                    "Expanded command exceeds length limit",
                    player=player_name,
                    alias=alias.name,
                    length=len(expanded_command),
                    max_length=MAX_EXPANDED_COMMAND_LENGTH,
                )
                # Log security event
                audit_logger.log_alias_expansion(
                    player_name=player_name,
                    alias_name=alias.name,
                    expanded_command="[BLOCKED - Too long]",
                    cycle_detected=False,
                    expansion_depth=expansion_depth,
                )
                return {
                    "result": f"Expanded command too long ({len(expanded_command)} chars, max {MAX_EXPANDED_COMMAND_LENGTH})"
                }

            # NEW: Validate expanded command content
            is_valid_expanded, expanded_error = CommandValidator.validate_expanded_command(expanded_command)
            if not is_valid_expanded:
                logger.warning(
                    "Expanded command validation failed", player=player_name, alias=alias.name, error=expanded_error
                )
                # Log security event
                audit_logger.log_security_event(
                    event_type="malicious_alias_detected",
                    player_name=player_name,
                    description=f"Alias expands to dangerous content: {expanded_error}",
                    severity="high",
                    metadata={"alias": alias.name},
                )
                return {"result": f"Alias expansion blocked: {expanded_error}"}

            # Log successful alias expansion
            audit_logger.log_alias_expansion(
                player_name=player_name,
                alias_name=alias.name,
                expanded_command=expanded_command,
                cycle_detected=False,
                expansion_depth=expansion_depth,
            )

            logger.debug("Alias safe to expand", player=player_name, alias_name=alias.name, depth=expansion_depth)

            # Recursively process the expanded command (with depth limit to prevent loops)
            result = await handle_expanded_command(
                expanded_command, current_user, request, alias_storage, player_name, depth=0, alias_chain=[]
            )
            # Add alias chain information to the result
            if "alias_chain" not in result:
                result["alias_chain"] = [{"original": cmd, "expanded": expanded_command, "alias_name": alias.name}]
            return result

    # Step 6.5: Check if single word command is an emote
    # Only treat single word commands as emotes if they are not known system commands
    if not args and _should_treat_as_emote(cmd):
        logger.debug("Single word emote detected, converting to emote command", player=player_name, emote=cmd)
        emote_command = f"emote {cmd}"
        # Use the command service directly to avoid recursion
        return await command_service.process_command(emote_command, current_user, request, alias_storage, player_name)

    # Step 7: Process command with new validation system
    logger.debug("Processing command with validation system", player=player_name, command=cmd)
    return await process_command_with_validation(command_line, current_user, request, alias_storage, player_name)


async def process_command_with_validation(
    command_line: str, current_user: dict, request: Request, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, Any]:
    """Process a command using the new Pydantic + Click validation system."""
    logger.debug(
        "=== UNIFIED COMMAND HANDLER: Processing with validation ===", player=player_name, command=command_line
    )

    try:
        # Use our new command processor for validation
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

        logger.debug("Command validated successfully", player=player_name, command_type=command_type, data=command_data)

        # Use the command service for processing with validated data
        result = await command_service.process_validated_command(
            command_data, current_user, request, alias_storage, player_name
        )

        logger.debug("Command processed successfully", player=player_name, command_type=command_type)

        # NEW: Audit logging for security-sensitive commands (CRITICAL-3)
        # AI: Log admin/privileged commands for security auditing and compliance
        if CommandValidator.is_security_sensitive(command_line):
            # Extract session and IP if available
            session_id = getattr(request.state, "session_id", None) if hasattr(request, "state") else None
            ip_address = getattr(request.client, "host", None) if hasattr(request, "client") else None

            audit_logger.log_command(
                player_name=player_name,
                command=command_line,
                success=True,  # If we got here, command was successful
                result=str(result.get("result", ""))[:500],  # Truncate result
                ip_address=ip_address,
                session_id=session_id,
                metadata={"command_type": command_type},
            )

            logger.info(
                "Security-sensitive command executed",
                player=player_name,
                command=CommandValidator.sanitize_for_logging(command_line),
            )

        return result

    except ValidationError as e:
        logger.warning("Command validation error")

        # NEW: Audit log validation failures for security-sensitive commands (CRITICAL-3)
        if CommandValidator.is_security_sensitive(command_line):
            audit_logger.log_command(
                player_name=player_name,
                command=command_line,
                success=False,
                result=f"Validation error: {str(e)}",
                metadata={"error_type": "ValidationError"},
            )

        return {"result": str(e)}
    except Exception as e:
        logger.error("Error processing command", player=player_name, error=str(e), exc_info=True)
        return {"result": "An error occurred while processing your command."}


async def handle_expanded_command(
    command_line: str,
    current_user: dict,
    request: Request,
    alias_storage: AliasStorage,
    player_name: str,
    depth: int = 0,
    alias_chain: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Handle command processing with alias expansion and loop detection."""
    logger.debug("Handling expanded command", player=player_name, command_line=command_line, depth=depth)

    # Prevent infinite loops
    if depth > 10:
        logger.warning("Alias expansion depth limit exceeded", player=player_name, depth=depth)
        return {"result": "Alias expansion too deep - possible loop detected"}

    # Initialize alias chain if not provided
    if alias_chain is None:
        alias_chain = []

    # Process the expanded command
    return await process_command_with_validation(command_line, current_user, request, alias_storage, player_name)


# HTTP API endpoint
@router.post("", status_code=status.HTTP_200_OK)
async def handle_command(
    req: CommandRequest,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Handle incoming HTTP command requests."""
    command_line = req.command

    # Check if user is authenticated
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")

    player_name = get_username_from_user(current_user)
    logger.info("HTTP command received", player=player_name, command=command_line, length=len(command_line))

    # Process command using unified handler
    result = await process_command_unified(command_line, current_user, request, player_name=player_name)

    logger.debug("HTTP command processed successfully", player=player_name, result=result)
    return result


# Legacy compatibility function
async def process_command(
    cmd: str, args: list[str], current_user: dict, request: Request, alias_storage: AliasStorage, player_name: str
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
    from .help.help_content import get_help_content as get_help_content_new

    return get_help_content_new(command_name)
