"""
Player state command models for MythosMUD.

This module provides command models for player state changes like quitting, logging out, and posture changes.
"""

from typing import Literal

from pydantic import Field, field_validator

from ..validators.security_validator import validate_player_name
from .command_base import BaseCommand, CommandType


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
