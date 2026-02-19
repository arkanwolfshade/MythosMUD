"""
Helper functions for command parsing and validation.

This module contains utility functions that were previously in command_parser.py,
including command safety validation, help text generation, and username extraction.
"""

import re
from typing import Any

from ..exceptions import ValidationError as MythosValidationError
from ..models.command import CommandType
from ..structured_logging.enhanced_logging_config import get_logger
from .enhanced_error_logging import log_and_raise_enhanced

logger = get_logger(__name__)


def validate_command_safety(command_string: str) -> bool:
    """
    Perform additional safety validation on command string.

    Args:
        command_string: Raw command string

    Returns:
        True if command is safe, False otherwise
    """
    # Check for obvious injection attempts
    dangerous_patterns = [
        r"[;|&`$()]",  # Shell metacharacters
        r"\b(and|or)\s*=\s*",  # SQL injection
        r"__import__|eval|exec|system|os\.",  # Python injection
        r"%[a-zA-Z]",  # Format string injection
        r"<script|javascript:",  # XSS attempts
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, command_string, re.IGNORECASE):
            logger.warning("Dangerous pattern detected in command", pattern=pattern, command=command_string)
            return False

    return True


def get_command_help(command_type: str | None = None) -> str:
    """
    Get help text for commands.

    Args:
        command_type: Specific command to get help for, or None for general help

    Returns:
        Help text string
    """
    if command_type:
        command_type = command_type.lower()
        if command_type not in [cmd.value for cmd in CommandType]:
            return f"Unknown command: {command_type}"

        # Return specific help for command
        help_texts = {
            CommandType.LOOK.value: "look [direction] - Look around or in a specific direction",
            CommandType.GO.value: "go <direction> - Move in a specific direction",
            CommandType.SAY.value: "say <message> - Say something to other players",
            CommandType.LOCAL.value: "local <message> - Send message to local channel (sub-zone)",
            CommandType.WHISPER.value: "whisper <player> <message> - Send private message to player",
            CommandType.REPLY.value: "reply <message> - Reply to last whisper received",
            CommandType.EMOTE.value: "emote <action> - Perform an action",
            CommandType.ME.value: "me <action> - Describe an action",
            CommandType.POSE.value: "pose [description] - Set or display your pose",
            CommandType.ALIAS.value: "alias <name> [command] - Create or view an alias",
            CommandType.ALIASES.value: "aliases - List all your aliases",
            CommandType.UNALIAS.value: "unalias <name> - Remove an alias",
            CommandType.HELP.value: "help [command] - Get help on commands",
            CommandType.MUTE.value: "mute <player> [duration] [reason] - Mute a player",
            CommandType.UNMUTE.value: "unmute <player> - Unmute a player",
            CommandType.MUTE_GLOBAL.value: "mute_global <player> [duration] [reason] - Globally mute a player",
            CommandType.UNMUTE_GLOBAL.value: "unmute_global <player> - Globally unmute a player",
            CommandType.ADD_ADMIN.value: "add_admin <player> - Make a player an admin",
            CommandType.MUTES.value: "mutes - Show your mute status",
            CommandType.SUMMON.value: "summon <prototype_id> [quantity] [item|npc] - Admin: conjure items or NPCs",
            CommandType.WHO.value: "who [player] - List online players with optional filtering",
            CommandType.STATUS.value: "status - Show your character status",
            CommandType.SKILLS.value: "skills - Show your character's skills",
            CommandType.TIME.value: "time - Show the current Mythos time",
            CommandType.WHOAMI.value: "whoami - Show your personal status (alias of status)",
            CommandType.INVENTORY.value: "inventory - Show your inventory",
            CommandType.PICKUP.value: "pickup <item-number> [quantity] - Pick up a room item",
            CommandType.DROP.value: "drop <inventory-number> [quantity] - Drop an inventory item",
            CommandType.EQUIP.value: "equip <inventory-number> [slot] - Equip an item",
            CommandType.UNEQUIP.value: "unequip <slot> - Unequip an item",
            CommandType.QUIT.value: "quit - Quit the game",
            CommandType.SIT.value: "sit - Sit down and adopt a seated posture",
            CommandType.STAND.value: "stand - Return to a standing posture",
            CommandType.LIE.value: "lie [down] - Lie down on the ground",
        }

        return help_texts.get(command_type, f"No help available for: {command_type}")

    # Return general help
    return """
Available Commands:
- look [direction] - Look around or in a specific direction
- go <direction> - Move in a specific direction
- say <message> - Say something to other players
- local <message> - Send message to local channel (sub-zone)
- whisper <player> <message> - Send private message to player
- reply <message> - Reply to last whisper received
- emote <action> - Perform an action
- me <action> - Describe an action
- pose [description] - Set or display your pose
- alias <name> [command] - Create or view an alias
- aliases - List all your aliases
- unalias <name> - Remove an alias
- help [command] - Get help on commands
- mute <player> [duration] [reason] - Mute a player
- unmute <player> - Unmute a player
- mute_global <player> [duration] [reason] - Globally mute a player
- unmute_global <player> - Globally unmute a player
- add_admin <player> - Make a player an admin
- mutes - Show your mute status
- summon <prototype_id> [quantity] [item|npc] - Admin: conjure items or NPCs
- who [player] - List online players with optional filtering
- status - Show your character status
- time - Show the current Mythos time
- whoami - Show your personal status (alias of status)
- inventory - Show your inventory
- quit - Quit the game
- sit - Sit down and adopt a seated posture
- stand - Return to a standing posture
- lie [down] - Lie down on the ground

Directions: north, south, east, west
Use 'help <command>' for detailed information about a specific command.
"""


def get_username_from_user(user_obj: Any) -> str:
    """
    Safely extract username from user object or dictionary.

    This utility function eliminates code duplication across command handlers
    by providing a centralized way to extract usernames from various user object formats.
    As noted in the restricted archives, this pattern reduces maintenance burden
    and ensures consistent behavior across all command implementations.

    Args:
        user_obj: User object that may be a dict, object with attributes, or other format

    Returns:
        str: The username/name from the user object

    Raises:
        ValueError: If no username or name can be extracted from the user object
    """
    # User object attribute extraction factory - maps common attribute patterns
    # This eliminates the need for repetitive if/elif chains across command files

    # Handle Player objects (which have 'name' attribute)
    if hasattr(user_obj, "name") and hasattr(user_obj, "player_id"):
        return str(user_obj.name)
    if hasattr(user_obj, "username"):
        return str(user_obj.username)
    if hasattr(user_obj, "name"):
        return str(user_obj.name)
    if isinstance(user_obj, dict) and "username" in user_obj:
        return str(user_obj["username"])
    if isinstance(user_obj, dict) and "name" in user_obj:
        return str(user_obj["name"])
    log_and_raise_enhanced(
        MythosValidationError,
        "User object must have username or name attribute or key",
        user_obj_type=type(user_obj).__name__,
        user_obj=str(user_obj),
        logger_name=__name__,
    )
