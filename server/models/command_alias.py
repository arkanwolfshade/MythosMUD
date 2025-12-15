"""
Alias command models for MythosMUD.

This module provides command models for managing command aliases.
"""

from typing import Literal

from pydantic import Field, field_validator

from ..validators.security_validator import validate_alias_name, validate_command_content
from .command_base import BaseCommand, CommandType


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
