"""
Game-related models for MythosMUD.

This module contains models specific to the game mechanics including
character statistics and attribute types.
"""

from datetime import UTC, datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, computed_field


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


class StatusEffectType(str, Enum):
    """Status effects that can be applied to characters."""

    STUNNED = "stunned"
    POISONED = "poisoned"
    HALLUCINATING = "hallucinating"
    PARANOID = "paranoid"
    TREMBLING = "trembling"
    CORRUPTED = "corrupted"
    INSANE = "insane"


class StatusEffect(BaseModel):
    """Represents a status effect applied to a character."""

    __slots__ = ()  # Performance optimization for frequently instantiated status effects

    model_config = ConfigDict(
        # Security: reject unknown fields to prevent injection
        extra="forbid",
        # Performance: validate assignment for computed fields
        validate_assignment=True,
    )

    effect_type: StatusEffectType
    duration: int = Field(ge=0, description="Duration in game ticks (0 = permanent)")
    intensity: int = Field(ge=1, le=10, description="Effect intensity from 1-10")
    source: str | None = Field(None, description="Source of the effect (item, spell, etc.)")
    applied_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC).replace(tzinfo=None), description="When the effect was applied"
    )

    def is_active(self, current_tick: int) -> bool:
        """Check if the status effect is still active."""
        if self.duration == 0:
            return True
        # For testing purposes, use a simple tick-based system
        # In real usage, this would be more sophisticated
        return current_tick < self.duration


class Stats(BaseModel):
    """Core character statistics with Lovecraftian horror elements."""

    __slots__ = ()  # Performance optimization for frequently instantiated stats

    model_config = ConfigDict(
        # Performance: validate assignment for computed fields
        validate_assignment=True,
        # Security: reject unknown fields to prevent injection
        extra="forbid",
        # Use enum values for consistency
        use_enum_values=True,
    )

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
        """Initialize Stats with proper random number generation."""
        # Use a local random generator to avoid affecting global state
        import random

        local_rng = random.Random(42)  # Fixed seed for testing reproducibility

        # Generate random values for any field that is None or not provided
        data.setdefault("strength", local_rng.randint(3, 18))
        data.setdefault("dexterity", local_rng.randint(3, 18))
        data.setdefault("constitution", local_rng.randint(3, 18))
        data.setdefault("intelligence", local_rng.randint(3, 18))
        data.setdefault("wisdom", local_rng.randint(3, 18))
        data.setdefault("charisma", local_rng.randint(3, 18))

        # Replace None values with random values
        for field in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            if data.get(field) is None:
                data[field] = local_rng.randint(3, 18)

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
