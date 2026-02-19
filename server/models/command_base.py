"""
Base command models and enums for MythosMUD.

This module provides the foundational classes and enums used by all command models.
"""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class Direction(StrEnum):
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


class CommandType(StrEnum):
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
    REST = "rest"
    GROUND = "ground"
    TIME = "time"
    SKILLS = "skills"
    # Communication commands
    WHISPER = "whisper"
    REPLY = "reply"
    CHANNEL = "channel"
    # Admin server management commands
    SHUTDOWN = "shutdown"
    # Combat commands
    ATTACK = "attack"
    PUNCH = "punch"
    KICK = "kick"
    STRIKE = "strike"
    SUMMON = "summon"
    # NPC admin commands
    NPC = "npc"
    # Magic commands
    CAST = "cast"
    SPELL = "spell"
    SPELLS = "spells"
    LEARN = "learn"
    # Follow commands
    FOLLOW = "follow"
    UNFOLLOW = "unfollow"
    FOLLOWING = "following"
    # Party commands (ephemeral grouping)
    PARTY = "party"


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
