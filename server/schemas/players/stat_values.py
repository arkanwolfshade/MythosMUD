"""
Stat values schema for MythosMUD.

This module defines Pydantic models for character stat values used in character creation.
"""

from pydantic import BaseModel, ConfigDict, Field


class RolledStats(BaseModel):
    """
    Core character statistics that are rolled during character creation.

    This model represents only the base attributes that are randomly generated,
    excluding derived stats and horror-specific attributes.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    strength: int = Field(..., ge=1, description="Physical power and combat damage")
    dexterity: int = Field(..., ge=1, description="Agility, reflexes, and speed")
    constitution: int = Field(..., ge=1, description="Health, stamina, and resistance")
    size: int = Field(..., ge=1, description="Height and weight combined")
    intelligence: int = Field(..., ge=1, description="Problem-solving and magical aptitude")
    power: int = Field(..., ge=1, description="Willpower and magical potential")
    education: int = Field(..., ge=1, description="Formal learning and knowledge")
    charisma: int = Field(..., ge=1, description="Social skills and influence")
    luck: int = Field(..., ge=1, description="Fortune and chance")
