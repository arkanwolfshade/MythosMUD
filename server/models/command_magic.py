"""
Magic command models for MythosMUD.

This module provides command models for magic-related actions.
"""

from typing import Literal

from pydantic import Field, field_validator

from .command_base import BaseCommand, CommandType


class CastCommand(BaseCommand):
    """Command for casting a spell."""

    command_type: Literal[CommandType.CAST] = CommandType.CAST
    spell_name: str = Field(..., min_length=1, max_length=100, description="Name of the spell to cast")
    target: str | None = Field(None, max_length=100, description="Optional target name for the spell")

    @field_validator("spell_name")
    @classmethod
    def validate_spell_name(cls: type["CastCommand"], v: str) -> str:
        """Validate spell name format."""
        if not v or not v.strip():
            raise ValueError("Spell name cannot be empty")
        return v.strip()

    @field_validator("target")
    @classmethod
    def validate_target(cls: type["CastCommand"], v: str | None) -> str | None:
        """Validate target format."""
        if v is not None:
            v = v.strip() if isinstance(v, str) else v
            if not v:
                return None
        return v


class SpellCommand(BaseCommand):
    """Command for viewing spell details."""

    command_type: Literal[CommandType.SPELL] = CommandType.SPELL
    spell_name: str = Field(..., min_length=1, max_length=100, description="Name of the spell to view")

    @field_validator("spell_name")
    @classmethod
    def validate_spell_name(cls: type["SpellCommand"], v: str) -> str:
        """Validate spell name format."""
        if not v or not v.strip():
            raise ValueError("Spell name cannot be empty")
        return v.strip()


class SpellsCommand(BaseCommand):
    """Command for listing learned spells."""

    command_type: Literal[CommandType.SPELLS] = CommandType.SPELLS


class LearnCommand(BaseCommand):
    """Command for learning a spell."""

    command_type: Literal[CommandType.LEARN] = CommandType.LEARN
    spell_name: str = Field(..., min_length=1, max_length=100, description="Name of the spell to learn")

    @field_validator("spell_name")
    @classmethod
    def validate_spell_name(cls: type["LearnCommand"], v: str) -> str:
        """Validate spell name format."""
        if not v or not v.strip():
            raise ValueError("Spell name cannot be empty")
        return v.strip()
