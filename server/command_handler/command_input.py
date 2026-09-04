"""
Command Input Utilities for MythosMUD.

This module provides utilities for cleaning, normalizing, and validating
command input. It handles the initial processing of raw command strings
before they are parsed and executed.
"""

import re

from ..config import get_config
from ..structured_logging.enhanced_logging_config import get_logger
from ..validators.command_validator import CommandValidator
from .command_execution_request import CommandExecutionRequest, command_request_app_state

logger = get_logger(__name__)

# Configuration
MAX_COMMAND_LENGTH = get_config().game.max_command_length
MAX_EXPANDED_COMMAND_LENGTH = CommandValidator.MAX_EXPANDED_COMMAND_LENGTH
CATATONIA_ALLOWED_COMMANDS = {"help", "who", "status", "time"}


# List of known system commands that should NOT be treated as emotes
_SYSTEM_COMMANDS = {
    "look",
    "say",
    "go",
    "move",
    "quit",
    "logout",
    "help",
    "who",
    "time",
    "emote",
    "alias",
    "aliases",
    "unalias",
    "mute",
    "mutes",
    "unmute",
    "admin",
    "spawn",
    "summon",
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
    "skills",
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
    "follow",
    "unfollow",
    "following",
    "party",
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


def _is_predefined_emote(command: str, request: CommandExecutionRequest | None = None) -> bool:
    """
    Check if a command is a predefined emote alias.

    Args:
        command: The command to check
        request: Current request, used to reach the container-loaded EmoteService via
                 app.state. Falls back to False (not an emote) when unavailable, matching
                 the previous behavior for tests/environments without a wired service.

    Returns:
        True if the command is a predefined emote, False otherwise
    """
    try:
        state = command_request_app_state(request) if request is not None else None
        emote_service = getattr(state, "emote_service", None)
        if emote_service is None:
            return False
        return bool(emote_service.is_emote_alias(command))
    except (AttributeError, TypeError, RuntimeError) as e:
        logger.warning("Error checking predefined emote", error=str(e))
        return False


def should_treat_as_emote(command: str, request: CommandExecutionRequest | None = None) -> bool:
    """
    Check if a single word command should be treated as an emote.

    This function determines if a single word command is likely an emote
    rather than a system command. It excludes known system commands.

    Args:
        command: The command to check
        request: Current request, passed through to _is_predefined_emote to reach the
                 container-loaded EmoteService.

    Returns:
        True if the command should be treated as an emote, False otherwise
    """
    # If it's a known system command, don't treat as emote
    if command.lower() in _SYSTEM_COMMANDS:
        return False

    # If it's a predefined emote, treat as emote
    if _is_predefined_emote(command, request):
        return True

    # Only treat as emote if it's a predefined emote
    # Unknown words should go through proper command validation
    return False
