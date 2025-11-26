"""
Command models for MythosMUD using Pydantic for validation.

This module provides type-safe command models with comprehensive validation
to prevent command injection and ensure data integrity.
"""

import re
from enum import Enum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..logging.enhanced_logging_config import get_logger
from ..validators.security_validator import (
    validate_action_content,
    validate_alias_name,
    validate_combat_target,
    validate_command_content,
    validate_filter_name,
    validate_help_topic,
    validate_message_content,
    validate_player_name,
    validate_pose_content,
    validate_reason_content,
    validate_target_player,
)

logger = get_logger(__name__)


class Direction(str, Enum):
    """Valid directions for movement and looking."""

    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    UP = "up"
    DOWN = "down"
    NORTHEAST = "northeast"
    NORTHWEST = "northwest"
    SOUTHEAST = "southeast"
    SOUTHWEST = "southwest"


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
    ADMIN = "admin"
    MUTES = "mutes"
    # Admin teleport commands (confirmation removed for immediate execution)
    TELEPORT = "teleport"
    GOTO = "goto"
    # Utility commands
    WHO = "who"
    STATUS = "status"
    WHOAMI = "whoami"
    INVENTORY = "inventory"
    PICKUP = "pickup"
    DROP = "drop"
    PUT = "put"
    GET = "get"
    EQUIP = "equip"
    UNEQUIP = "unequip"
    QUIT = "quit"
    LOGOUT = "logout"
    SIT = "sit"
    STAND = "stand"
    LIE = "lie"
    GROUND = "ground"
    TIME = "time"
    # Communication commands
    WHISPER = "whisper"
    REPLY = "reply"
    # Admin server management commands
    SHUTDOWN = "shutdown"
    # Combat commands
    ATTACK = "attack"
    PUNCH = "punch"
    KICK = "kick"
    STRIKE = "strike"
    SUMMON = "summon"


class BaseCommand(BaseModel):
    """
    Base class for all MythosMUD commands.

    Provides common validation and security features for all commands.
    """

    __slots__ = ()  # Performance optimization for frequently instantiated commands

    model_config = ConfigDict(
        # Security: reject unknown fields to prevent injection
        extra="forbid",
        # Use enum values for validation
        use_enum_values=True,
        # Validate assignment
        validate_assignment=True,
    )


class LookCommand(BaseCommand):
    """Command for looking around, in a specific direction, or at an NPC."""

    command_type: Literal[CommandType.LOOK] = CommandType.LOOK
    direction: Direction | None = Field(default=None, description="Direction to look")
    target: str | None = Field(default=None, description="Target to look at (NPC name or direction)")
    target_type: Literal["player", "npc", "item", "container", "direction"] | None = Field(
        default=None, description="Explicit target type specification"
    )
    look_in: bool = Field(default=False, description="Flag for container inspection mode")
    instance_number: int | None = Field(
        default=None, ge=1, description="Instance number for targeting specific items/containers when multiple exist"
    )

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
        """Validate message content for security using centralized validation."""
        return validate_message_content(v)


class LocalCommand(BaseCommand):
    """Command for speaking in the local channel (sub-zone)."""

    command_type: Literal[CommandType.LOCAL] = CommandType.LOCAL
    message: str = Field(..., min_length=1, max_length=500, description="Message to send to local channel")

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate message content for security using centralized validation."""
        return validate_message_content(v)


class SystemCommand(BaseCommand):
    """Command for sending system messages (admin only)."""

    command_type: Literal[CommandType.SYSTEM] = CommandType.SYSTEM
    message: str = Field(..., min_length=1, max_length=2000, description="System message to broadcast")

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate system message content for security using centralized validation."""
        return validate_message_content(v)


class EmoteCommand(BaseCommand):
    """Command for performing an emote or action."""

    command_type: Literal[CommandType.EMOTE] = CommandType.EMOTE
    action: str = Field(..., min_length=1, max_length=200, description="Action to perform")

    @field_validator("action")
    @classmethod
    def validate_action(cls, v):
        """Validate emote action for security using centralized validation."""
        return validate_action_content(v)


class MeCommand(BaseCommand):
    """Command for describing an action (alternative to emote)."""

    command_type: Literal[CommandType.ME] = CommandType.ME
    action: str = Field(..., min_length=1, max_length=200, description="Action to describe")

    @field_validator("action")
    @classmethod
    def validate_action(cls, v):
        """Validate me action for security using centralized validation."""
        return validate_action_content(v)


class PoseCommand(BaseCommand):
    """Command for setting or displaying pose/status."""

    command_type: Literal[CommandType.POSE] = CommandType.POSE
    pose: str | None = Field(None, max_length=100, description="Pose description")

    @field_validator("pose")
    @classmethod
    def validate_pose(cls, v):
        """Validate pose description for security using centralized validation."""
        if v is None:
            return v
        return validate_pose_content(v)


class AliasCommand(BaseCommand):
    """Command for creating or viewing command aliases."""

    command_type: Literal[CommandType.ALIAS] = CommandType.ALIAS
    alias_name: str = Field(..., min_length=1, max_length=20, description="Alias name")
    command: str | None = Field(None, max_length=200, description="Command to alias")

    @field_validator("alias_name")
    @classmethod
    def validate_alias_name_field(cls, v):
        """Validate alias name format using centralized validation."""
        return validate_alias_name(v)

    @field_validator("command")
    @classmethod
    def validate_command(cls, v):
        """Validate command content for security using centralized validation."""
        if v is None:
            return v
        return validate_command_content(v)


class AliasesCommand(BaseCommand):
    """Command for listing all aliases."""

    command_type: Literal[CommandType.ALIASES] = CommandType.ALIASES


class UnaliasCommand(BaseCommand):
    """Command for removing an alias."""

    command_type: Literal[CommandType.UNALIAS] = CommandType.UNALIAS
    alias_name: str = Field(..., min_length=1, max_length=20, description="Alias name to remove")

    @field_validator("alias_name")
    @classmethod
    def validate_alias_name_field(cls, v):
        """Validate alias name format using centralized validation."""
        return validate_alias_name(v)


class HelpCommand(BaseCommand):
    """Command for getting help on commands."""

    command_type: Literal[CommandType.HELP] = CommandType.HELP
    topic: str | None = Field(None, max_length=50, description="Help topic")

    @field_validator("topic")
    @classmethod
    def validate_topic(cls, v):
        """Validate help topic format using centralized validation."""
        if v is None:
            return v
        return validate_help_topic(v)


class MuteCommand(BaseCommand):
    """Command for muting a player."""

    command_type: Literal[CommandType.MUTE] = CommandType.MUTE
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to mute")
    duration_minutes: int | None = Field(None, ge=1, le=10080, description="Mute duration in minutes")  # Max 1 week
    reason: str | None = Field(None, max_length=200, description="Mute reason")

    @field_validator("player_name")
    @classmethod
    def validate_player_name_field(cls, v):
        """Validate player name format using centralized validation."""
        return validate_player_name(v)

    @field_validator("reason")
    @classmethod
    def validate_reason(cls, v):
        """Validate mute reason for security using centralized validation."""
        if v is None:
            return v
        return validate_reason_content(v)


class UnmuteCommand(BaseCommand):
    """Command for unmuting a player."""

    command_type: Literal[CommandType.UNMUTE] = CommandType.UNMUTE
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to unmute")

    @field_validator("player_name")
    @classmethod
    def validate_player_name_field(cls, v):
        """Validate player name format using centralized validation."""
        return validate_player_name(v)


class MuteGlobalCommand(BaseCommand):
    """Command for globally muting a player."""

    command_type: Literal[CommandType.MUTE_GLOBAL] = CommandType.MUTE_GLOBAL
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to globally mute")
    duration_minutes: int | None = Field(None, ge=1, le=10080, description="Mute duration in minutes")  # Max 1 week
    reason: str | None = Field(None, max_length=200, description="Mute reason")

    @field_validator("player_name")
    @classmethod
    def validate_player_name_field(cls, v):
        """Validate player name format using centralized validation."""
        return validate_player_name(v)

    @field_validator("reason")
    @classmethod
    def validate_reason(cls, v):
        """Validate mute reason for security using centralized validation."""
        if v is None:
            return v
        return validate_reason_content(v)


class UnmuteGlobalCommand(BaseCommand):
    """Command for globally unmuting a player."""

    command_type: Literal[CommandType.UNMUTE_GLOBAL] = CommandType.UNMUTE_GLOBAL
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to globally unmute")

    @field_validator("player_name")
    @classmethod
    def validate_player_name_field(cls, v):
        """Validate player name format using centralized validation."""
        return validate_player_name(v)


class AddAdminCommand(BaseCommand):
    """Command for adding admin privileges to a player."""

    command_type: Literal[CommandType.ADD_ADMIN] = CommandType.ADD_ADMIN
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to make admin")

    @field_validator("player_name")
    @classmethod
    def validate_player_name_field(cls, v):
        """Validate player name format using centralized validation."""
        return validate_player_name(v)


class MutesCommand(BaseCommand):
    """Command for showing current mute status."""

    command_type: Literal[CommandType.MUTES] = CommandType.MUTES


class AdminCommand(BaseCommand):
    """Command for administrative utilities with subcommands."""

    command_type: Literal[CommandType.ADMIN] = CommandType.ADMIN
    subcommand: str = Field(..., min_length=1, max_length=30, description="Admin subcommand to execute")
    args: list[str] = Field(default_factory=list, description="Additional arguments for admin subcommands")

    @field_validator("subcommand")
    @classmethod
    def validate_subcommand(cls, v: str) -> str:
        """Validate and normalize admin subcommand names."""
        allowed_subcommands = {"status"}
        normalized = v.lower()
        if normalized not in allowed_subcommands:
            raise ValueError(f"Invalid admin subcommand: {v}. Allowed subcommands: {sorted(allowed_subcommands)}")
        return normalized


class SummonCommand(BaseCommand):
    """Administrative command for summoning prototypes into the current room."""

    command_type: Literal[CommandType.SUMMON] = CommandType.SUMMON
    prototype_id: str = Field(..., min_length=1, max_length=120, description="Prototype identifier to conjure")
    quantity: int = Field(
        default=1,
        ge=1,
        le=5,
        description="Number of instances to summon (capped to prevent ritual abuse).",
    )
    target_type: Literal["item", "npc"] = Field(
        default="item",
        description="Hint for whether the summon should create items or NPCs.",
    )

    @field_validator("prototype_id")
    @classmethod
    def validate_prototype_id(cls, value: str) -> str:
        candidate = value.strip()
        if not re.match(r"^[a-zA-Z0-9._-]+$", candidate):
            raise ValueError("Prototype ID must contain only letters, numbers, dots, underscores, or hyphens.")
        return candidate


class TeleportCommand(BaseCommand):
    """Command for teleporting a player to the admin's location."""

    command_type: Literal[CommandType.TELEPORT] = CommandType.TELEPORT
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to teleport")
    direction: Direction | None = Field(
        default=None, description="Optional direction to send the player relative to the admin's location"
    )

    @field_validator("player_name")
    @classmethod
    def validate_player_name_field(cls, v):
        """Validate player name format using centralized validation."""
        return validate_player_name(v)

    @field_validator("direction")
    @classmethod
    def validate_direction_field(cls, v):
        """Ensure provided direction is part of the allowed set."""
        if v is None:
            return v
        if v not in Direction:
            raise ValueError(f"Invalid direction: {v}. Must be one of: {list(Direction)}")
        return v


class GotoCommand(BaseCommand):
    """Command for teleporting the admin to a player's location."""

    command_type: Literal[CommandType.GOTO] = CommandType.GOTO
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to teleport to")

    @field_validator("player_name")
    @classmethod
    def validate_player_name_field(cls, v):
        """Validate player name format using centralized validation."""
        return validate_player_name(v)


# Confirmation command classes removed - teleport commands now execute immediately
# TODO: Add ConfirmTeleportCommand and ConfirmGotoCommand as future feature for enhanced safety


class WhoCommand(BaseCommand):
    """Command for listing online players."""

    command_type: Literal[CommandType.WHO] = CommandType.WHO
    filter_name: str | None = Field(None, max_length=50, description="Optional player name filter")

    @field_validator("filter_name")
    @classmethod
    def validate_filter_name_field(cls, v):
        """Validate filter name format using centralized validation."""
        if v is None:
            return v
        return validate_filter_name(v)


class StatusCommand(BaseCommand):
    """Command for viewing player status."""

    command_type: Literal[CommandType.STATUS] = CommandType.STATUS


class TimeCommand(BaseCommand):
    """Command for viewing the current Mythos time."""

    command_type: Literal[CommandType.TIME] = CommandType.TIME


class WhoamiCommand(BaseCommand):
    """Command for viewing the caller's status (alias of status)."""

    command_type: Literal[CommandType.WHOAMI] = CommandType.WHOAMI


class InventoryCommand(BaseCommand):
    """Command for showing player inventory."""

    command_type: Literal[CommandType.INVENTORY] = CommandType.INVENTORY


class PickupCommand(BaseCommand):
    """Command for picking up items from room drops."""

    command_type: Literal[CommandType.PICKUP] = CommandType.PICKUP
    index: int | None = Field(
        None,
        ge=1,
        description="Index of the room drop to collect (1-based).",
    )
    search_term: str | None = Field(
        None,
        min_length=1,
        max_length=120,
        description="Name fragment or prototype identifier for fuzzy selection.",
    )
    quantity: int | None = Field(None, ge=1, description="Quantity to pick up (defaults to full stack)")

    def model_post_init(self, __context: object) -> None:
        super().model_post_init(__context)
        if self.index is None and (self.search_term is None or not self.search_term.strip()):
            raise ValueError("Pickup command requires an item number or name.")

        if self.search_term is not None:
            stripped = self.search_term.strip()
            if not stripped:
                raise ValueError("Pickup search term cannot be empty.")
            object.__setattr__(self, "search_term", stripped)


class DropCommand(BaseCommand):
    """Command for dropping items from inventory into the room."""

    command_type: Literal[CommandType.DROP] = CommandType.DROP
    index: int = Field(..., ge=1, description="Index of the inventory slot to drop")
    quantity: int | None = Field(None, ge=1, description="Quantity to drop (defaults to full stack)")


class PutCommand(BaseCommand):
    """Command for putting items from inventory into a container."""

    command_type: Literal[CommandType.PUT] = CommandType.PUT
    item: str = Field(..., min_length=1, description="Item name or inventory index to put")
    container: str = Field(..., min_length=1, description="Container name to put item into")
    quantity: int | None = Field(None, ge=1, description="Quantity to put (defaults to full stack)")


class GetCommand(BaseCommand):
    """Command for getting items from a container into inventory."""

    command_type: Literal[CommandType.GET] = CommandType.GET
    item: str = Field(..., min_length=1, description="Item name or container index to get")
    container: str = Field(..., min_length=1, description="Container name to get item from")
    quantity: int | None = Field(None, ge=1, description="Quantity to get (defaults to full stack)")


class EquipCommand(BaseCommand):
    """Command for equipping an item from inventory."""

    command_type: Literal[CommandType.EQUIP] = CommandType.EQUIP
    index: int | None = Field(
        None,
        ge=1,
        description="Inventory slot index to equip (1-based).",
    )
    search_term: str | None = Field(
        None,
        min_length=1,
        max_length=120,
        description="Name fragment or prototype identifier to resolve inventory item.",
    )
    target_slot: str | None = Field(None, max_length=30, description="Optional slot override")

    def model_post_init(self, __context: object) -> None:
        super().model_post_init(__context)
        if self.index is None and (self.search_term is None or not self.search_term.strip()):
            raise ValueError("Equip command requires an item number or name.")

        if self.search_term is not None:
            stripped = self.search_term.strip()
            if not stripped:
                raise ValueError("Equip search term cannot be empty.")
            object.__setattr__(self, "search_term", stripped)

    @field_validator("target_slot")
    @classmethod
    def validate_slot(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized = value.strip().lower()
        if not normalized:
            raise ValueError("Slot cannot be empty")
        return normalized


class UnequipCommand(BaseCommand):
    """Command for unequipping an item back to inventory."""

    command_type: Literal[CommandType.UNEQUIP] = CommandType.UNEQUIP
    slot: str | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="Slot to unequip (optional when providing item name).",
    )
    search_term: str | None = Field(
        default=None,
        min_length=1,
        max_length=120,
        description="Name fragment identifying the equipped item to remove.",
    )

    def model_post_init(self, __context: object) -> None:
        super().model_post_init(__context)
        if (self.slot is None or not self.slot.strip()) and (self.search_term is None or not self.search_term.strip()):
            raise ValueError("Unequip command requires a slot or item name.")

        if self.slot is not None:
            normalized = self.slot.strip().lower()
            if not normalized:
                raise ValueError("Slot cannot be empty")
            object.__setattr__(self, "slot", normalized)

        if self.search_term is not None:
            stripped = self.search_term.strip()
            if not stripped:
                raise ValueError("Unequip item name cannot be empty.")
            object.__setattr__(self, "search_term", stripped)


class QuitCommand(BaseCommand):
    """Command for quitting the game."""

    command_type: Literal[CommandType.QUIT] = CommandType.QUIT


class LogoutCommand(BaseCommand):
    """Command for logging out of the game."""

    command_type: Literal[CommandType.LOGOUT] = CommandType.LOGOUT


class SitCommand(BaseCommand):
    """Command for taking a seated position."""

    command_type: Literal[CommandType.SIT] = CommandType.SIT


class StandCommand(BaseCommand):
    """Command for returning to a standing posture."""

    command_type: Literal[CommandType.STAND] = CommandType.STAND


class LieCommand(BaseCommand):
    """Command for lying down (optionally expressed as 'lie down')."""

    command_type: Literal[CommandType.LIE] = CommandType.LIE
    modifier: str | None = Field(default=None, description="Optional modifier such as 'down'")

    @field_validator("modifier")
    @classmethod
    def validate_modifier(cls, value: str | None) -> str | None:
        """Validate optional modifier for the lie command."""
        if value is None:
            return value
        normalized = value.strip().lower()
        allowed_modifiers = {"down"}
        if normalized not in allowed_modifiers:
            raise ValueError(f"Invalid modifier for lie command: {value}")
        return normalized


class GroundCommand(BaseCommand):
    """Command for grounding a catatonic ally back to lucidity."""

    command_type: Literal[CommandType.GROUND] = CommandType.GROUND
    target_player: str = Field(..., min_length=1, max_length=50, description="Player to stabilise")

    @field_validator("target_player")
    @classmethod
    def validate_target_player(cls, value: str) -> str:
        """Validate the target player name using shared validation rules."""
        return validate_player_name(value)


class ShutdownCommand(BaseCommand):
    """
    Command for shutting down the server (admin only).

    Args can be:
    - Empty: Default 10 second countdown
    - Number: Countdown duration in seconds
    - "cancel": Cancel active shutdown
    """

    command_type: Literal[CommandType.SHUTDOWN] = CommandType.SHUTDOWN
    args: list[str] = Field(default_factory=list, description="Optional countdown seconds or 'cancel'")


class WhisperCommand(BaseCommand):
    """Command for whispering to a specific player."""

    command_type: Literal[CommandType.WHISPER] = CommandType.WHISPER
    target: str = Field(..., min_length=1, max_length=50, description="Target player name")
    message: str = Field(..., min_length=1, max_length=2000, description="Whisper message content")

    @field_validator("target")
    @classmethod
    def validate_target(cls, v):
        """Validate target player name format using centralized validation."""
        return validate_target_player(v)

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate message content for security using centralized validation."""
        return validate_message_content(v)


class ReplyCommand(BaseCommand):
    """Command for replying to the last whisper received."""

    command_type: Literal[CommandType.REPLY] = CommandType.REPLY
    message: str = Field(..., min_length=1, max_length=2000, description="Reply message content")

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate message content for security using centralized validation."""
        return validate_message_content(v)


class AttackCommand(BaseCommand):
    """Command for attacking a target."""

    command_type: Literal[CommandType.ATTACK] = CommandType.ATTACK
    target: str | None = Field(None, min_length=1, max_length=50, description="Target to attack")

    @field_validator("target")
    @classmethod
    def validate_target(cls, v):
        """Validate combat target name format using centralized validation."""
        if v is None:
            return None
        return validate_combat_target(v)


class PunchCommand(BaseCommand):
    """Command for punching a target."""

    command_type: Literal[CommandType.PUNCH] = CommandType.PUNCH
    target: str | None = Field(None, min_length=1, max_length=50, description="Target to punch")

    @field_validator("target")
    @classmethod
    def validate_target(cls, v):
        """Validate combat target name format using centralized validation."""
        if v is None:
            return None
        return validate_combat_target(v)


class KickCommand(BaseCommand):
    """Command for kicking a target."""

    command_type: Literal[CommandType.KICK] = CommandType.KICK
    target: str | None = Field(None, min_length=1, max_length=50, description="Target to kick")

    @field_validator("target")
    @classmethod
    def validate_target(cls, v):
        """Validate combat target name format using centralized validation."""
        if v is None:
            return None
        return validate_combat_target(v)


class StrikeCommand(BaseCommand):
    """Command for striking a target."""

    command_type: Literal[CommandType.STRIKE] = CommandType.STRIKE
    target: str | None = Field(None, min_length=1, max_length=50, description="Target to strike")

    @field_validator("target")
    @classmethod
    def validate_target(cls, v):
        """Validate combat target name format using centralized validation."""
        if v is None:
            return None
        return validate_combat_target(v)


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
    | PickupCommand
    | DropCommand
    | PutCommand
    | GetCommand
    | EquipCommand
    | UnequipCommand
    | QuitCommand
    | LogoutCommand
    | SitCommand
    | StandCommand
    | LieCommand
    | GroundCommand
    | ShutdownCommand
    | WhisperCommand
    | ReplyCommand
    | AttackCommand
    | PunchCommand
    | KickCommand
    | StrikeCommand
)
