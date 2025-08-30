"""
Command models for MythosMUD using Pydantic for validation.

This module provides type-safe command models with comprehensive validation
to prevent command injection and ensure data integrity.
"""

import re
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, field_validator

from ..logging_config import get_logger

logger = get_logger(__name__)


class Direction(str, Enum):
    """Valid directions for movement and looking."""

    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


class CommandType(str, Enum):
    """Valid command types for MythosMUD."""

    LOOK = "look"
    GO = "go"
    SAY = "say"
    LOCAL = "local"
    GLOBAL = "global"
    SYSTEM = "system"
    EMOTE = "emote"
    ME = "me"
    POSE = "pose"
    ALIAS = "alias"
    ALIASES = "aliases"
    UNALIAS = "unalias"
    HELP = "help"
    MUTE = "mute"
    UNMUTE = "unmute"
    MUTE_GLOBAL = "mute_global"
    UNMUTE_GLOBAL = "unmute_global"
    ADD_ADMIN = "add_admin"
    MUTES = "mutes"
    # Admin teleport commands (confirmation removed for immediate execution)
    TELEPORT = "teleport"
    GOTO = "goto"
    # Utility commands
    WHO = "who"
    STATUS = "status"
    INVENTORY = "inventory"
    QUIT = "quit"
    # Communication commands
    WHISPER = "whisper"
    REPLY = "reply"


class BaseCommand(BaseModel):
    """
    Base class for all MythosMUD commands.

    Provides common validation and security features for all commands.
    """

    model_config = {
        # Security: reject unknown fields to prevent injection
        "extra": "forbid",
        # Use enum values for validation
        "use_enum_values": True,
        # Validate assignment
        "validate_assignment": True,
    }


class LookCommand(BaseCommand):
    """Command for looking around or in a specific direction."""

    command_type: Literal[CommandType.LOOK] = CommandType.LOOK
    direction: Direction | None = Field(None, description="Direction to look")

    @field_validator("direction")
    @classmethod
    def validate_direction(cls, v):
        """Validate direction is one of the allowed values."""
        if v is not None and v not in Direction:
            raise ValueError(f"Invalid direction: {v}. Must be one of: {list(Direction)}")
        return v


class GoCommand(BaseCommand):
    """Command for moving in a specific direction."""

    command_type: Literal[CommandType.GO] = CommandType.GO
    direction: Direction = Field(..., description="Direction to move")

    @field_validator("direction")
    @classmethod
    def validate_direction(cls, v):
        """Validate direction is one of the allowed values."""
        if v not in Direction:
            raise ValueError(f"Invalid direction: {v}. Must be one of: {list(Direction)}")
        return v


class SayCommand(BaseCommand):
    """Command for saying something to other players in the room."""

    command_type: Literal[CommandType.SAY] = CommandType.SAY
    message: str = Field(..., min_length=1, max_length=500, description="Message to say")

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate message content for security."""
        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]

        if found_chars:
            logger.warning("Dangerous characters detected in say message", chars=found_chars, message_preview=v[:50])
            raise ValueError(f"Message contains invalid characters: {found_chars}")

        # Check for command injection patterns
        # Use more specific patterns to avoid false positives on legitimate text
        injection_patterns = [
            r"\b(and|or)\s*=\s*['\"]?\w+",  # SQL injection with value
            r"__import__\(|eval\(|exec\(|system\(|os\.",  # Python injection with parentheses
            r"%[a-zA-Z]\s*[^\s]*",  # Format string injection with content
        ]

        for pattern in injection_patterns:
            if re.search(pattern, v, re.IGNORECASE):
                logger.warning(
                    "Command injection pattern detected in say message", pattern=pattern, message_preview=v[:50]
                )
                raise ValueError("Message contains suspicious patterns")

        return v.strip()


class LocalCommand(BaseCommand):
    """Command for speaking in the local channel (sub-zone)."""

    command_type: Literal[CommandType.LOCAL] = CommandType.LOCAL
    message: str = Field(..., min_length=1, max_length=500, description="Message to send to local channel")

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate message content for security (same as say command)."""
        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]

        if found_chars:
            logger.warning("Dangerous characters detected in local message", chars=found_chars, message_preview=v[:50])
            raise ValueError(f"Message contains invalid characters: {found_chars}")

        # Check for command injection patterns
        # Use more specific patterns to avoid false positives on legitimate text
        injection_patterns = [
            r"\b(and|or)\s*=\s*['\"]?\w+",  # SQL injection with value
            r"__import__\(|eval\(|exec\(|system\(|os\.",  # Python injection with parentheses
            r"%[a-zA-Z]\s*[^\s]*",  # Format string injection with content
        ]

        for pattern in injection_patterns:
            if re.search(pattern, v, re.IGNORECASE):
                logger.warning(
                    "Command injection pattern detected in local message", pattern=pattern, message_preview=v[:50]
                )
                raise ValueError("Message contains suspicious patterns")

        return v.strip()


class SystemCommand(BaseCommand):
    """Command for sending system messages (admin only)."""

    command_type: Literal[CommandType.SYSTEM] = CommandType.SYSTEM
    message: str = Field(..., min_length=1, max_length=2000, description="System message to broadcast")

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate system message content for security."""
        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]

        if found_chars:
            logger.warning("Dangerous characters detected in system message", chars=found_chars, message_preview=v[:50])
            raise ValueError(f"Message contains invalid characters: {found_chars}")

        # Check for command injection patterns
        # Use more specific patterns to avoid false positives on legitimate text
        injection_patterns = [
            r"\b(and|or)\s*=\s*['\"]?\w+",  # SQL injection with value
            r"__import__\(|eval\(|exec\(|system\(|os\.",  # Python injection with parentheses
            r"%[a-zA-Z]\s*[^\s]*",  # Format string injection with content
        ]

        for pattern in injection_patterns:
            if re.search(pattern, v, re.IGNORECASE):
                logger.warning(
                    "Command injection pattern detected in system message", pattern=pattern, message_preview=v[:50]
                )
                raise ValueError("Message contains suspicious patterns")

        return v.strip()


class EmoteCommand(BaseCommand):
    """Command for performing an emote or action."""

    command_type: Literal[CommandType.EMOTE] = CommandType.EMOTE
    action: str = Field(..., min_length=1, max_length=200, description="Action to perform")

    @field_validator("action")
    @classmethod
    def validate_action(cls, v):
        """Validate emote action for security."""
        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]

        if found_chars:
            logger.warning("Dangerous characters detected in emote action", chars=found_chars, action_preview=v[:50])
            raise ValueError(f"Action contains invalid characters: {found_chars}")

        # Check for command injection patterns
        # Use more specific patterns to avoid false positives on legitimate text
        injection_patterns = [
            r"\b(and|or)\s*=\s*['\"]?\w+",  # SQL injection with value
            r"__import__\(|eval\(|exec\(|system\(|os\.",  # Python injection with parentheses
            r"%[a-zA-Z]\s*[^\s]*",  # Format string injection with content
        ]

        for pattern in injection_patterns:
            if re.search(pattern, v, re.IGNORECASE):
                logger.warning(
                    "Command injection pattern detected in emote action", pattern=pattern, action_preview=v[:50]
                )
                raise ValueError("Action contains suspicious patterns")

        return v.strip()


class MeCommand(BaseCommand):
    """Command for describing an action (alternative to emote)."""

    command_type: Literal[CommandType.ME] = CommandType.ME
    action: str = Field(..., min_length=1, max_length=200, description="Action to describe")

    @field_validator("action")
    @classmethod
    def validate_action(cls, v):
        """Validate me action for security (same as emote)."""
        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]

        if found_chars:
            logger.warning("Dangerous characters detected in me action", chars=found_chars, action_preview=v[:50])
            raise ValueError(f"Action contains invalid characters: {found_chars}")

        # Check for command injection patterns
        injection_patterns = [
            r"\b(and|or)\s*=\s*",  # SQL injection
            r"__import__|eval|exec|system|os\.",  # Python injection
            r"%[a-zA-Z]",  # Format string injection
        ]

        for pattern in injection_patterns:
            if re.search(pattern, v, re.IGNORECASE):
                logger.warning(
                    "Command injection pattern detected in me action", pattern=pattern, action_preview=v[:50]
                )
                raise ValueError("Action contains suspicious patterns")

        return v.strip()


class PoseCommand(BaseCommand):
    """Command for setting or displaying pose/status."""

    command_type: Literal[CommandType.POSE] = CommandType.POSE
    pose: str | None = Field(None, max_length=100, description="Pose description")

    @field_validator("pose")
    @classmethod
    def validate_pose(cls, v):
        """Validate pose description for security."""
        if v is None:
            return v

        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]

        if found_chars:
            logger.warning("Dangerous characters detected in pose", chars=found_chars, pose_preview=v[:50])
            raise ValueError(f"Pose contains invalid characters: {found_chars}")

        return v.strip()


class AliasCommand(BaseCommand):
    """Command for creating or viewing command aliases."""

    command_type: Literal[CommandType.ALIAS] = CommandType.ALIAS
    alias_name: str = Field(..., min_length=1, max_length=20, description="Alias name")
    command: str | None = Field(None, max_length=200, description="Command to alias")

    @field_validator("alias_name")
    @classmethod
    def validate_alias_name(cls, v):
        """Validate alias name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", v):
            raise ValueError("Alias name must start with a letter and contain only letters, numbers, and underscores")
        return v

    @field_validator("command")
    @classmethod
    def validate_command(cls, v):
        """Validate command content for security."""
        if v is None:
            return v

        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]

        if found_chars:
            logger.warning("Dangerous characters detected in alias command", chars=found_chars, command_preview=v[:50])
            raise ValueError(f"Alias command contains invalid characters: {found_chars}")

        return v.strip()


class AliasesCommand(BaseCommand):
    """Command for listing all aliases."""

    command_type: Literal[CommandType.ALIASES] = CommandType.ALIASES


class UnaliasCommand(BaseCommand):
    """Command for removing an alias."""

    command_type: Literal[CommandType.UNALIAS] = CommandType.UNALIAS
    alias_name: str = Field(..., min_length=1, max_length=20, description="Alias name to remove")

    @field_validator("alias_name")
    @classmethod
    def validate_alias_name(cls, v):
        """Validate alias name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", v):
            raise ValueError("Alias name must start with a letter and contain only letters, numbers, and underscores")
        return v


class HelpCommand(BaseCommand):
    """Command for getting help on commands."""

    command_type: Literal[CommandType.HELP] = CommandType.HELP
    topic: str | None = Field(None, max_length=50, description="Help topic")


class MuteCommand(BaseCommand):
    """Command for muting a player."""

    command_type: Literal[CommandType.MUTE] = CommandType.MUTE
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to mute")
    duration_minutes: int | None = Field(None, ge=1, le=10080, description="Mute duration in minutes")  # Max 1 week
    reason: str | None = Field(None, max_length=200, description="Mute reason")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", v):
            raise ValueError(
                "Player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
            )
        return v

    @field_validator("reason")
    @classmethod
    def validate_reason(cls, v):
        """Validate mute reason for security."""
        if v is None:
            return v

        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]

        if found_chars:
            logger.warning("Dangerous characters detected in mute reason", chars=found_chars, reason_preview=v[:50])
            raise ValueError(f"Mute reason contains invalid characters: {found_chars}")

        return v.strip()


class UnmuteCommand(BaseCommand):
    """Command for unmuting a player."""

    command_type: Literal[CommandType.UNMUTE] = CommandType.UNMUTE
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to unmute")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", v):
            raise ValueError(
                "Player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
            )
        return v


class MuteGlobalCommand(BaseCommand):
    """Command for globally muting a player."""

    command_type: Literal[CommandType.MUTE_GLOBAL] = CommandType.MUTE_GLOBAL
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to globally mute")
    duration_minutes: int | None = Field(None, ge=1, le=10080, description="Mute duration in minutes")  # Max 1 week
    reason: str | None = Field(None, max_length=200, description="Mute reason")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", v):
            raise ValueError(
                "Player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
            )
        return v

    @field_validator("reason")
    @classmethod
    def validate_reason(cls, v):
        """Validate mute reason for security."""
        if v is None:
            return v

        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]

        if found_chars:
            logger.warning(
                "Dangerous characters detected in global mute reason", chars=found_chars, reason_preview=v[:50]
            )
            raise ValueError(f"Global mute reason contains invalid characters: {found_chars}")

        return v.strip()


class UnmuteGlobalCommand(BaseCommand):
    """Command for globally unmuting a player."""

    command_type: Literal[CommandType.UNMUTE_GLOBAL] = CommandType.UNMUTE_GLOBAL
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to globally unmute")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", v):
            raise ValueError(
                "Player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
            )
        return v


class AddAdminCommand(BaseCommand):
    """Command for adding admin privileges to a player."""

    command_type: Literal[CommandType.ADD_ADMIN] = CommandType.ADD_ADMIN
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to make admin")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", v):
            raise ValueError(
                "Player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
            )
        return v


class MutesCommand(BaseCommand):
    """Command for showing current mute status."""

    command_type: Literal[CommandType.MUTES] = CommandType.MUTES


class TeleportCommand(BaseCommand):
    """Command for teleporting a player to the admin's location."""

    command_type: Literal[CommandType.TELEPORT] = CommandType.TELEPORT
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to teleport")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", v):
            raise ValueError(
                "Player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
            )
        return v


class GotoCommand(BaseCommand):
    """Command for teleporting the admin to a player's location."""

    command_type: Literal[CommandType.GOTO] = CommandType.GOTO
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to teleport to")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", v):
            raise ValueError(
                "Player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
            )
        return v


# Confirmation command classes removed - teleport commands now execute immediately
# TODO: Add ConfirmTeleportCommand and ConfirmGotoCommand as future feature for enhanced safety


class WhoCommand(BaseCommand):
    """Command for listing online players."""

    command_type: Literal[CommandType.WHO] = CommandType.WHO
    filter_name: str | None = Field(None, max_length=50, description="Optional player name filter")

    @field_validator("filter_name")
    @classmethod
    def validate_filter_name(cls, v):
        """Validate filter name format using existing validation infrastructure."""
        if v is None:
            return v

        # Use existing command safety validation
        from ..utils.command_parser import validate_command_safety

        if not validate_command_safety(v):
            logger.warning("Dangerous content detected in who filter", filter_preview=v[:50])
            raise ValueError("Filter contains dangerous content")

        return v.strip()


class StatusCommand(BaseCommand):
    """Command for viewing player status."""

    command_type: Literal[CommandType.STATUS] = CommandType.STATUS


class InventoryCommand(BaseCommand):
    """Command for viewing player inventory."""

    command_type: Literal[CommandType.INVENTORY] = CommandType.INVENTORY


class QuitCommand(BaseCommand):
    """Command for quitting the game."""

    command_type: Literal[CommandType.QUIT] = CommandType.QUIT


class WhisperCommand(BaseCommand):
    """Command for whispering to a specific player."""

    command_type: Literal[CommandType.WHISPER] = CommandType.WHISPER
    target: str = Field(..., min_length=1, max_length=50, description="Target player name")
    message: str = Field(..., min_length=1, max_length=2000, description="Whisper message content")

    @field_validator("target")
    @classmethod
    def validate_target(cls, v):
        """Validate target player name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", v):
            raise ValueError(
                "Target player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
            )
        return v

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate message content for security."""
        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]
        if found_chars:
            logger.warning("Dangerous content detected in whisper message", dangerous_chars=found_chars)
            raise ValueError(f"Message contains dangerous characters: {found_chars}")

        # Check for command injection attempts
        if re.search(
            r"\b(whisper|w|reply|say|local|global|system|me|pose|emote|look|go|who|status|inventory|quit|help|alias|aliases|unalias|mute|unmute|mute_global|unmute_global|add_admin|mutes|teleport|goto)\b",
            v,
            re.IGNORECASE,
        ):
            logger.warning("Potential command injection detected in whisper message", message_preview=v[:50])
            raise ValueError("Message contains potential command injection")

        return v.strip()


class ReplyCommand(BaseCommand):
    """Command for replying to the last whisper received."""

    command_type: Literal[CommandType.REPLY] = CommandType.REPLY
    message: str = Field(..., min_length=1, max_length=2000, description="Reply message content")

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate message content for security."""
        # Check for potentially dangerous characters
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]
        found_chars = [char for char in dangerous_chars if char in v]
        if found_chars:
            logger.warning("Dangerous content detected in reply message", dangerous_chars=found_chars)
            raise ValueError(f"Message contains dangerous characters: {found_chars}")

        # Check for command injection attempts
        if re.search(
            r"\b(whisper|w|reply|say|local|global|system|me|pose|emote|look|go|who|status|inventory|quit|help|alias|aliases|unalias|mute|unmute|mute_global|unmute_global|add_admin|mutes|teleport|goto)\b",
            v,
            re.IGNORECASE,
        ):
            logger.warning("Potential command injection detected in reply message", message_preview=v[:50])
            raise ValueError("Message contains potential command injection")

        return v.strip()


# Union type for all commands
Command = (
    LookCommand
    | GoCommand
    | SayCommand
    | LocalCommand
    | SystemCommand
    | EmoteCommand
    | MeCommand
    | PoseCommand
    | AliasCommand
    | AliasesCommand
    | UnaliasCommand
    | HelpCommand
    | MuteCommand
    | UnmuteCommand
    | MuteGlobalCommand
    | UnmuteGlobalCommand
    | AddAdminCommand
    | MutesCommand
    | TeleportCommand
    | GotoCommand
    | WhoCommand
    | StatusCommand
    | InventoryCommand
    | QuitCommand
    | WhisperCommand
    | ReplyCommand
)
