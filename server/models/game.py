"""
Game-related models for MythosMUD.

This module contains models specific to the game mechanics including
character statistics and attribute types.
"""

from enum import Enum

from pydantic import BaseModel, Field, computed_field


class AttributeType(str, Enum):
    """Core attribute types for the character system."""

    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    INT = "intelligence"
    WIS = "wisdom"
    CHA = "charisma"
    SAN = "sanity"
    OCC = "occult_knowledge"
    FEAR = "fear"
    CORR = "corruption"
    CULT = "cult_affiliation"


class Stats(BaseModel):
    """Core character statistics with Lovecraftian horror elements."""

    # Physical Attributes
    strength: int = Field(ge=1, le=20, default=None, description="Physical power and combat damage")
    dexterity: int = Field(ge=1, le=20, default=None, description="Agility, reflexes, and speed")
    constitution: int = Field(ge=1, le=20, default=None, description="Health, stamina, and resistance")

    # Mental Attributes
    intelligence: int = Field(ge=1, le=20, default=None, description="Problem-solving and magical aptitude")
    wisdom: int = Field(ge=1, le=20, default=None, description="Perception, common sense, and willpower")
    charisma: int = Field(ge=1, le=20, default=None, description="Social skills and influence")

    # Horror-Specific Attributes
    sanity: int = Field(ge=0, le=100, default=100, description="Mental stability (0 = complete madness)")
    occult_knowledge: int = Field(ge=0, le=100, default=0, description="Knowledge of forbidden lore")
    fear: int = Field(ge=0, le=100, default=0, description="Susceptibility to terror and panic")

    # Special Attributes
    corruption: int = Field(ge=0, le=100, default=0, description="Taint from dark forces")
    cult_affiliation: int = Field(ge=0, le=100, default=0, description="Ties to cults and secret societies")

    # Current health (can be modified)
    current_health: int = Field(ge=0, default=100, description="Current health points")

    def __init__(self, **data):
        import random

        data.setdefault("strength", random.randint(3, 18))
        data.setdefault("dexterity", random.randint(3, 18))
        data.setdefault("constitution", random.randint(3, 18))
        data.setdefault("intelligence", random.randint(3, 18))
        data.setdefault("wisdom", random.randint(3, 18))
        data.setdefault("charisma", random.randint(3, 18))
        super().__init__(**data)

    # Derived stats - computed fields
    @computed_field
    @property
    def max_health(self) -> int:
        """Calculate max health based on constitution."""
        return self.constitution * 10

    @computed_field
    @property
    def max_sanity(self) -> int:
        """Calculate max sanity based on wisdom."""
        return self.wisdom * 5

    def get_attribute_modifier(self, attribute: AttributeType) -> int:
        """Get the modifier for a given attribute (standard D&D-style calculation)."""
        attr_value = getattr(self, attribute.value, 10)
        return (attr_value - 10) // 2

    def is_sane(self) -> bool:
        """Check if the character is still mentally stable."""
        return self.sanity > 0

    def is_corrupted(self) -> bool:
        """Check if the character has significant corruption."""
        return self.corruption >= 50

    def is_insane(self) -> bool:
        """Check if the character has lost their sanity completely."""
        return self.sanity <= 0
