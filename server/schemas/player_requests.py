"""
Request models for player API endpoints.

This module defines Pydantic request models used in player-related API endpoints.
"""

from pydantic import BaseModel, Field, field_validator


class CreateCharacterRequest(BaseModel):
    """Request model for character creation."""

    __slots__ = ()  # Performance optimization

    name: str = Field(..., min_length=1, max_length=50, description="Character name")
    stats: dict = Field(..., description="Character stats dictionary")
    profession_id: int = Field(default=0, ge=0, description="Profession ID")

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate character name format."""
        if not v or not v.strip():
            raise ValueError("Character name cannot be empty or whitespace")
        return v.strip()


class SelectCharacterRequest(BaseModel):
    """Request model for character selection."""

    __slots__ = ()  # Performance optimization

    character_id: str = Field(..., description="Character ID (player_id) to select")


class RollStatsRequest(BaseModel):
    """Request model for rolling character stats."""

    __slots__ = ()  # Performance optimization

    method: str = "3d6"
    required_class: str | None = None
    timeout_seconds: float = 5.0  # Increased from 1.0 to allow more time for automatic rerolls
    profession_id: int | None = None


class LucidityLossRequest(BaseModel):
    """Request model for applying lucidity loss."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=100, description="Amount of lucidity to lose (0-100)")
    source: str = Field(default="unknown", description="Source of lucidity loss")


class FearRequest(BaseModel):
    """Request model for applying fear."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=100, description="Amount of fear to apply (0-100)")
    source: str = Field(default="unknown", description="Source of fear")


class CorruptionRequest(BaseModel):
    """Request model for applying corruption."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=100, description="Amount of corruption to apply (0-100)")
    source: str = Field(default="unknown", description="Source of corruption")


class OccultKnowledgeRequest(BaseModel):
    """Request model for gaining occult knowledge."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=100, description="Amount of occult knowledge to gain (0-100)")
    source: str = Field(default="unknown", description="Source of occult knowledge")


class HealRequest(BaseModel):
    """Request model for healing a player."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=1000, description="Amount of health to restore (0-1000)")


class DamageRequest(BaseModel):
    """Request model for damaging a player."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=1000, description="Amount of damage to apply (0-1000)")
    damage_type: str = Field(default="physical", description="Type of damage")
