"""Pydantic contracts for item prototype metadata (ADR-026).

Known mechanical objects under ``metadata``; lore keys remain allowed on the
parent via ``extra=\"allow\"``. Legacy combat still reads ``WeaponStats`` integers
on ``metadata.weapon`` until Phase 3.
"""

from __future__ import annotations

from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


class WeaponMetadata(BaseModel):
    """Weapon stats: rich CoC-like fields plus legacy WeaponStats integers."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

    min_damage: int | None = Field(default=None, ge=0)
    max_damage: int | None = Field(default=None, ge=0)
    modifier: int | None = None
    damage_types: list[str] | None = None
    magical: bool | None = None
    damage_expr: str | None = Field(default=None, min_length=1, max_length=64)
    attacks: float | None = Field(default=None, ge=0)
    range: str | None = Field(default=None, min_length=1, max_length=64)
    ammo: int | None = Field(default=None, ge=0)
    skill: str | None = Field(default=None, min_length=1, max_length=80)
    skill_bonus: int | None = None


class ArmorMetadata(BaseModel):
    """Armor points and coverage."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

    armor_points: int | None = Field(default=None, ge=0)
    coverage: str | None = Field(default=None, min_length=1, max_length=80)
    notes: str | None = Field(default=None, max_length=512)


class TomeMetadata(BaseModel):
    """Tome / manuscript mechanical numbers (Mythos-tuned)."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

    sanity_loss_expr: str | None = Field(default=None, min_length=1, max_length=64)
    mythos_gain: int | None = Field(default=None, ge=0)
    study_hours: float | None = Field(default=None, ge=0)
    spells: list[str] | None = None


class EquipmentBonus(BaseModel):
    """Single skill bonus granted by equipment."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

    skill: str = Field(min_length=1, max_length=80)
    bonus: int


class EquipmentMetadata(BaseModel):
    """Non-weapon equipment bonuses."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

    skill_bonuses: list[EquipmentBonus] | None = None
    notes: str | None = Field(default=None, max_length=512)


class CatalogMetadata(BaseModel):
    """Catalog namespace, canonical/variant linkage, opaque private source key."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

    namespace: str = Field(min_length=1, max_length=64)
    canonical_id: str | None = Field(default=None, min_length=1, max_length=120)
    variant_of: str | None = Field(default=None, min_length=1, max_length=120)
    era: str | None = Field(default=None, min_length=1, max_length=64)
    source_key: str | None = Field(default=None, min_length=1, max_length=120)


class ItemMetadata(BaseModel):
    """Validated known keys under item prototype metadata (ADR-026).

    Additional lore properties are allowed and ignored by these models.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="allow")

    weapon: WeaponMetadata | None = None
    armor: ArmorMetadata | None = None
    tome: TomeMetadata | None = None
    equipment: EquipmentMetadata | None = None
    catalog: CatalogMetadata | None = None
