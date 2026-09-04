"""
Exploration command models for MythosMUD.

This module provides command models for movement and looking around.
"""

from typing import Literal

from pydantic import Field, field_validator

from .command_base import BaseCommand, CommandType, Direction


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
    def validate_direction(cls: type["LookCommand"], v: Direction | None) -> Direction | None:
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
    def validate_direction(cls: type["GoCommand"], v: Direction) -> Direction:
        """Validate direction is one of the allowed values."""
        if v not in Direction:
            raise ValueError(f"Invalid direction: {v}. Must be one of: {list(Direction)}")
        return v
