"""
Spell data models for the magic system.

This module contains Pydantic models for spells, spell materials, and spell effects.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class SpellSchool(StrEnum):
    """Spell schools/types."""

    MYTHOS = "mythos"
    CLERICAL = "clerical"
    ELEMENTAL = "elemental"
    OTHER = "other"


class SpellTargetType(StrEnum):
    """Valid target types for spells."""

    SELF = "self"
    ENTITY = "entity"
    LOCATION = "location"
    AREA = "area"
    ALL = "all"


class SpellRangeType(StrEnum):
    """Valid range types for spells."""

    TOUCH = "touch"
    SAME_ROOM = "same_room"
    ADJACENT_ROOM = "adjacent_room"
    UNLIMITED = "unlimited"


class SpellEffectType(StrEnum):
    """Valid effect types for spells."""

    HEAL = "heal"
    DAMAGE = "damage"
    STATUS_EFFECT = "status_effect"
    STAT_MODIFY = "stat_modify"
    LUCIDITY_ADJUST = "lucidity_adjust"
    CORRUPTION_ADJUST = "corruption_adjust"
    TELEPORT = "teleport"
    CREATE_OBJECT = "create_object"


class SpellMaterial(BaseModel):
    """Material component required for casting a spell."""

    item_id: str = Field(description="ID of the item required")
    consumed: bool = Field(default=True, description="Whether the material is consumed when casting")


class Spell(BaseModel):
    """Spell definition model."""

    spell_id: str = Field(description="Unique identifier for the spell")
    name: str = Field(description="Display name of the spell")
    description: str = Field(description="Description of what the spell does")
    school: SpellSchool = Field(description="Spell school/type")
    mp_cost: int = Field(ge=0, description="Magic points cost to cast")
    lucidity_cost: int = Field(default=0, ge=0, description="Lucidity cost (Mythos spells only)")
    corruption_on_learn: int = Field(default=0, ge=0, description="Corruption gained when learning this spell")
    corruption_on_cast: int = Field(default=0, ge=0, description="Corruption gained when casting this spell")
    casting_time_seconds: int = Field(default=0, ge=0, description="Time in seconds to cast the spell")
    target_type: SpellTargetType = Field(description="What type of target this spell requires")
    range_type: SpellRangeType = Field(description="Range limitation of the spell")
    effect_type: SpellEffectType = Field(description="Type of effect this spell produces")
    effect_data: dict[str, Any] = Field(default_factory=dict, description="Effect-specific data (JSONB)")
    materials: list[SpellMaterial] = Field(default_factory=list, description="Material components required")

    def is_mythos(self) -> bool:
        """Check if this is a Mythos spell."""
        return self.school == SpellSchool.MYTHOS

    def requires_lucidity(self) -> bool:
        """Check if this spell requires lucidity cost."""
        return self.lucidity_cost > 0
