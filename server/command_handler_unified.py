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
from .config_loader import get_config
from .logging_config import get_logger
from .utils.command_processor import get_command_processor

logger = get_logger(__name__)

router = APIRouter(prefix="/command", tags=["command"])

# Global instances
command_service = CommandService()
command_processor = get_command_processor()

# Configuration
MAX_COMMAND_LENGTH = get_config().get("max_command_length", 1000)


def get_username_from_user(user_obj) -> str:
    """Safely extract username from user object or dictionary."""
    if hasattr(user_obj, "username"):
        return user_obj.username
    elif isinstance(user_obj, dict) and "username" in user_obj:
        return user_obj["username"]
    else:
        raise ValueError("User object must have username attribute or key")


class CommandRequest(BaseModel):
    """Request model for command processing."""

    command: str


def clean_command_input(command: str) -> str:
    """Clean and normalize command input by collapsing multiple spaces and stripping whitespace."""
    cleaned = re.sub(r"\s+", " ", command).strip()
    if cleaned != command:
        logger.debug("Command input cleaned", original=command, cleaned=cleaned)
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
        logger.debug("Slash prefix removed from command", original=command, normalized=normalized)
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
        logger.warning(f"Error checking predefined emote: {e}")
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

    logger.debug("=== UNIFIED COMMAND HANDLER: Processing command ===", command=command_line)

    # Step 1: Basic validation
    if not command_line:
        logger.debug("Empty command received")
        return {"result": ""}

    if len(command_line) > MAX_COMMAND_LENGTH:
        logger.warning(
            "Command too long rejected", player=player_name, length=len(command_line), max_length=MAX_COMMAND_LENGTH
        )
        return {"result": f"Command too long (max {MAX_COMMAND_LENGTH} characters)"}

    # Step 2: Clean and normalize command
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
            alias_storage = AliasStorage()
            logger.debug("AliasStorage initialized")
        except Exception as e:
            logger.error("Failed to initialize AliasStorage", error=str(e))
            alias_storage = None

    # Step 4: Parse command and arguments
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    logger.debug("Command parsed", command=cmd, args=args, original_command=command_line)

    # Step 5: Handle alias management commands first (don't expand these)
    if cmd in ["alias", "aliases", "unalias"]:
        logger.debug("Processing alias management command", command=cmd)
        return await command_service.process_command(command_line, current_user, request, alias_storage, player_name)

    # Step 6: Check for alias expansion
    if alias_storage:
        alias = alias_storage.get_alias(player_name, cmd)
        if alias:
            logger.debug("Alias found, expanding", alias_name=alias.name, original_command=cmd)
            # Expand the alias
            expanded_command = alias.get_expanded_command(args)
            # Recursively process the expanded command (with depth limit to prevent loops)
            result = await handle_expanded_command(
                expanded_command, current_user, request, alias_storage, player_name, depth=0, alias_chain=[]
            )
            # Add alias chain information to the result
            if "alias_chain" not in result:
                result["alias_chain"] = [{"original": cmd, "expanded": expanded_command, "alias_name": alias.name}]
            return result

    # Step 6.5: Check if single word command is an emote
    if not args and _is_predefined_emote(cmd):
        logger.debug("Single word emote detected, converting to emote command", emote=cmd)
        emote_command = f"emote {cmd}"
        # Use the command service directly to avoid recursion
        return await command_service.process_command(emote_command, current_user, request, alias_storage, player_name)

    # Step 7: Process command with new validation system
    logger.debug("Processing command with validation system", command=cmd)
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
            logger.warning("Command validation failed", error=error_message)
            return {"result": error_message}

        if not validated_command:
            logger.warning("No validated command returned")
            return {"result": "Invalid command format"}

        # Extract command data for processing
        command_data = command_processor.extract_command_data(validated_command)
        command_data["player_name"] = player_name

        logger.debug("Command validated successfully", command_type=command_type, data=command_data)

        # Use the command service for processing with validated data
        result = await command_service.process_validated_command(
            command_data, current_user, request, alias_storage, player_name
        )

        logger.debug("Command processed successfully", command_type=command_type)
        return result

    except Exception as e:
        logger.error(f"Error processing command for {player_name}: {str(e)}", exc_info=True)
        logger.error(f"Exception type: {type(e).__name__}")
        logger.error(f"Exception args: {e.args}")
        return {"result": "An error occurred while processing your command."}


async def handle_expanded_command(
    command_line: str,
    current_user: dict,
    request: Request,
    alias_storage: AliasStorage,
    player_name: str,
    depth: int = 0,
    alias_chain: list[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Handle command processing with alias expansion and loop detection."""
    logger.debug("Handling expanded command", command_line=command_line, depth=depth)

    # Prevent infinite loops
    if depth > 10:
        logger.warning("Alias expansion depth limit exceeded", depth=depth)
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
    logger.info("HTTP command received", command=command_line, length=len(command_line))

    # Process command using unified handler
    result = await process_command_unified(command_line, current_user, request, player_name=player_name)

    logger.debug("HTTP command processed successfully", result=result)
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
    logger.debug("Using legacy command processing", command=cmd, args=args)

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
