"""
Combat command models for MythosMUD.

This module provides command models for combat actions.
"""

from typing import Literal

from pydantic import Field, field_validator

from ..validators.security_validator import validate_combat_target
from .command_base import BaseCommand, CommandType


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
