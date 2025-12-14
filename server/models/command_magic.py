"""
Magic command models for MythosMUD.

This module provides command models for magic-related actions.
"""

from typing import Literal

from pydantic import Field, field_validator

from .command_base import BaseCommand, CommandType


class LearnCommand(BaseCommand):
    """Command for learning a spell."""

    command_type: Literal[CommandType.LEARN] = CommandType.LEARN
    spell_name: str = Field(..., min_length=1, max_length=100, description="Name of the spell to learn")

    @field_validator("spell_name")
    @classmethod
    def validate_spell_name(cls, v):
        """Validate spell name format."""
        if not v or not v.strip():
            raise ValueError("Spell name cannot be empty")
        return v.strip()
