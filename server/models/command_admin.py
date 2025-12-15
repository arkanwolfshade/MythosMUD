"""
Admin command models for MythosMUD.

This module provides command models for administrative functions like teleportation and NPC management.
"""

import re
from typing import Literal

from pydantic import Field, field_validator

from ..validators.security_validator import validate_player_name
from .command_base import BaseCommand, CommandType, Direction


class NPCCommand(BaseCommand):
    """Command for NPC administrative utilities with subcommands."""

    command_type: Literal[CommandType.NPC] = CommandType.NPC
    subcommand: str | None = Field(None, min_length=1, max_length=30, description="NPC subcommand to execute")
    args: list[str] = Field(default_factory=list, description="Additional arguments for NPC subcommands")


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
