"""Pydantic contracts for NPC definition base_stats catalog shapes (ADR-027).

Known mechanical objects under ``base_stats``; lore keys remain allowed on the
parent via ``extra=\"allow\"``. Legacy combat still requires DP / xp integers.
"""

# pylint: disable=too-few-public-methods  # Reason: Pydantic schema models; methods come from BaseModel

from __future__ import annotations

from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


class NpcCatalogMetadata(BaseModel):
    """Catalog namespace, canonical/variant linkage, opaque private source key."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

    namespace: str = Field(min_length=1, max_length=64)
    canonical_id: str | None = Field(default=None, min_length=1, max_length=120)
    variant_of: str | None = Field(default=None, min_length=1, max_length=120)
    era: str | None = Field(default=None, min_length=1, max_length=64)
    source_key: str | None = Field(default=None, min_length=1, max_length=120)


class NpcAttackMetadata(BaseModel):
    """Single NPC attack: rich dice fields plus legacy min/max dual-write."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

    name: str | None = Field(default=None, min_length=1, max_length=80)
    damage_expr: str | None = Field(default=None, min_length=1, max_length=64)
    min_damage: int | None = Field(default=None, ge=0)
    max_damage: int | None = Field(default=None, ge=0)
    skill: str | None = Field(default=None, min_length=1, max_length=80)
    skill_pct: int | None = Field(default=None, ge=0, le=100)


class NpcArmorMetadata(BaseModel):
    """Armor points and coverage for NPC hide / shell / plating."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

    armor_points: int | None = Field(default=None, ge=0)
    coverage: str | None = Field(default=None, min_length=1, max_length=80)
    notes: str | None = Field(default=None, max_length=512)


class NpcBaseStats(BaseModel):
    """Validated known keys under NPC base_stats (ADR-027).

    Additional lore properties are allowed and ignored by these models.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="allow")

    determination_points: int = Field(ge=0)
    max_dp: int = Field(ge=1)
    xp_value: int = Field(ge=0)
    magic_points: int | None = Field(default=None, ge=0)
    max_magic_points: int | None = Field(default=None, ge=0)
    strength: int | None = Field(default=None, ge=1)
    constitution: int | None = Field(default=None, ge=1)
    size: int | None = Field(default=None, ge=1)
    dexterity: int | None = Field(default=None, ge=1)
    intelligence: int | None = Field(default=None, ge=1)
    power: int | None = Field(default=None, ge=1)
    education: int | None = Field(default=None, ge=1)
    charisma: int | None = Field(default=None, ge=1)
    luck: int | None = Field(default=None, ge=1)
    catalog: NpcCatalogMetadata | None = None
    attacks: list[NpcAttackMetadata] | None = None
    armor: NpcArmorMetadata | None = None
