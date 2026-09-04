"""
Moderation command models for MythosMUD.

This module provides command models for player moderation and administration.
"""

from typing import Literal

from pydantic import Field, field_validator

from ..validators.security_validator import validate_player_name, validate_reason_content
from .command_base import BaseCommand, CommandType


class MuteCommand(BaseCommand):
    """Command for muting a player."""

    command_type: Literal[CommandType.MUTE] = CommandType.MUTE
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to mute")
    duration_minutes: int | None = Field(None, ge=1, le=10080, description="Mute duration in minutes")  # Max 1 week
    reason: str | None = Field(None, max_length=200, description="Mute reason")

    @field_validator("player_name")
    @classmethod
    def validate_player_name_field(cls: type["MuteCommand"], v: str) -> str:
        """Validate player name format using centralized validation."""
        return validate_player_name(v)

    @field_validator("reason")
    @classmethod
    def validate_reason(cls: type["MuteCommand"], v: str | None) -> str | None:
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
    def validate_player_name_field(cls: type["UnmuteCommand"], v: str) -> str:
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
    def validate_player_name_field(cls: type["MuteGlobalCommand"], v: str) -> str:
        """Validate player name format using centralized validation."""
        return validate_player_name(v)

    @field_validator("reason")
    @classmethod
    def validate_reason(cls: type["MuteGlobalCommand"], v: str | None) -> str | None:
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
    def validate_player_name_field(cls: type["UnmuteGlobalCommand"], v: str) -> str:
        """Validate player name format using centralized validation."""
        return validate_player_name(v)


class AddAdminCommand(BaseCommand):
    """Command for adding admin privileges to a player."""

    command_type: Literal[CommandType.ADD_ADMIN] = CommandType.ADD_ADMIN
    player_name: str = Field(..., min_length=1, max_length=50, description="Player to make admin")

    @field_validator("player_name")
    @classmethod
    def validate_player_name_field(cls: type["AddAdminCommand"], v: str) -> str:
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
        allowed_subcommands = {"status", "set", "setlucidity", "lcd", "time"}
        normalized = v.lower()
        if normalized not in allowed_subcommands:
            raise ValueError(f"Invalid admin subcommand: {v}. Allowed subcommands: {sorted(allowed_subcommands)}")
        return normalized
