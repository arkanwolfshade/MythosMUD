"""
Request models for player API endpoints.

This module defines Pydantic request models used in player-related API endpoints.
"""

from typing import Any

from pydantic import Field, field_validator

from server.validators.security_validator import (
    PLAYER_NAME_MAX_LENGTH,
    PLAYER_NAME_MIN_LENGTH,
    validate_player_name,
)

from ..shared.base import SecureBaseModel


class OccupationSlot(SecureBaseModel):
    """One occupation skill slot: skill_id and fixed value (70, 60, 50, or 40)."""

    skill_id: int = Field(..., description="Skill catalog id")
    value: int = Field(..., description="Percentage (70, 60, 50, or 40)")


class PersonalInterestSlot(SecureBaseModel):
    """One personal interest skill: skill_id only (server applies base + 20)."""

    skill_id: int = Field(..., description="Skill catalog id")


class CreateCharacterRequest(SecureBaseModel):
    """Request model for character creation."""

    name: str = Field(
        ...,
        min_length=PLAYER_NAME_MIN_LENGTH,
        max_length=PLAYER_NAME_MAX_LENGTH,
        description="Character name",
    )
    stats: dict[str, Any] = Field(..., description="Rolled character stats (server applies profession stat_modifiers)")
    profession_id: int = Field(default=0, ge=0, description="Profession ID")
    occupation_slots: list[OccupationSlot] | None = Field(
        default=None,
        description="Nine slots: one 70, two 60, three 50, three 40. Omit for legacy flow.",
    )
    personal_interest: list[PersonalInterestSlot] | None = Field(
        default=None,
        description="Four skill_ids (base+20 each). Omit for legacy flow.",
    )
    start_in_tutorial: bool = Field(default=True, description="Start in tutorial instance (per-player)")

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate character name format."""
        if not v or not v.strip():
            raise ValueError("Character name cannot be empty or whitespace")
        stripped = v.strip()
        return validate_player_name(stripped)


class SelectCharacterRequest(SecureBaseModel):
    """Request model for character selection."""

    character_id: str = Field(..., description="Character ID (player_id) to select")


class RollStatsRequest(SecureBaseModel):
    """Request model for rolling character stats."""

    method: str = "3d6"
    required_class: str | None = None
    timeout_seconds: float = 5.0  # Increased from 1.0 to allow more time for automatic rerolls
    profession_id: int | None = None


class LucidityLossRequest(SecureBaseModel):
    """Request model for applying lucidity loss."""

    amount: int = Field(..., ge=0, le=100, description="Amount of lucidity to lose (0-100)")
    source: str = Field(default="unknown", description="Source of lucidity loss")


class FearRequest(SecureBaseModel):
    """Request model for applying fear."""

    amount: int = Field(..., ge=0, le=100, description="Amount of fear to apply (0-100)")
    source: str = Field(default="unknown", description="Source of fear")


class CorruptionRequest(SecureBaseModel):
    """Request model for applying corruption."""

    amount: int = Field(..., ge=0, le=100, description="Amount of corruption to apply (0-100)")
    source: str = Field(default="unknown", description="Source of corruption")


class OccultKnowledgeRequest(SecureBaseModel):
    """Request model for gaining occult knowledge."""

    amount: int = Field(..., ge=0, le=100, description="Amount of occult knowledge to gain (0-100)")
    source: str = Field(default="unknown", description="Source of occult knowledge")


class HealRequest(SecureBaseModel):
    """Request model for healing a player."""

    amount: int = Field(..., ge=0, le=1000, description="Amount of health to restore (0-1000)")


class DamageRequest(SecureBaseModel):
    """Request model for damaging a player."""

    amount: int = Field(..., ge=0, le=1000, description="Amount of damage to apply (0-1000)")
    damage_type: str = Field(default="physical", description="Type of damage")
