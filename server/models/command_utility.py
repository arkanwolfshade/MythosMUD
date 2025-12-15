"""
Utility command models for MythosMUD.

This module provides command models for utility functions like help, status, and player listing.
"""

from typing import Literal

from pydantic import Field, field_validator

from ..validators.security_validator import validate_filter_name, validate_help_topic
from .command_base import BaseCommand, CommandType


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
