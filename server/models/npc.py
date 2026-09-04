"""
NPC database models for MythosMUD.

This module defines the SQLAlchemy models for NPC definitions, spawn rules,
and relationships that support the NPC subsystem.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed

import json
from collections.abc import Mapping
from datetime import datetime
from enum import StrEnum
from typing import ClassVar, cast, override

from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Text,
    UniqueConstraint,
    func,  # pylint: disable=unused-import  # func used in insert_default/onupdate
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from ..npc_metadata import npc_metadata

_JSONDict = dict[str, object]


def _set_default_if_missing(instance: object, attr: str, default: object) -> None:
    """Apply a default attribute value when SQLAlchemy leaves it unset or None."""
    sentinel = object()
    current = getattr(instance, attr, sentinel)
    if current is sentinel or current is None:
        object.__setattr__(instance, attr, default)


_NPC_DEFINITION_DEFAULTS: tuple[tuple[str, object], ...] = (
    ("required_npc", False),
    ("max_population", 1),
    ("spawn_probability", 1.0),
    ("base_stats", "{}"),
    ("behavior_config", "{}"),
    ("ai_integration_stub", "{}"),
)


def _loads_json_dict(raw: str) -> _JSONDict:
    """Parse JSON object from string; empty dict on failure or non-object root."""
    try:
        # json.loads is typed as Any in typeshed; treat root value as object before narrowing.
        parsed = cast(object, json.loads(raw))
    except (json.JSONDecodeError, TypeError):
        return {}
    return cast(_JSONDict, parsed) if isinstance(parsed, dict) else {}


class Base(DeclarativeBase):
    """SQLAlchemy declarative base for NPC database models."""

    metadata: ClassVar[MetaData] = npc_metadata


class NPCDefinitionType(StrEnum):
    """Enumeration of valid NPC definition types."""

    SHOPKEEPER = "shopkeeper"
    QUEST_GIVER = "quest_giver"
    PASSIVE_MOB = "passive_mob"
    AGGRESSIVE_MOB = "aggressive_mob"


class NPCDefinition(Base):
    """
    NPC definition model.

    Stores static NPC data including stats, behaviors, and configuration.
    This represents the "template" from which NPC instances are spawned.
    """

    __tablename__: str = "npc_definitions"
    __table_args__: tuple[UniqueConstraint | CheckConstraint, ...] = (
        UniqueConstraint("name", "sub_zone_id", name="idx_npc_definitions_name_sub_zone"),
        CheckConstraint(
            "npc_type IN ('shopkeeper', 'quest_giver', 'passive_mob', 'aggressive_mob')", name="chk_npc_type"
        ),
    )

    # Primary key
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # Basic information
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text)

    # NPC type and classification
    npc_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True,
        comment="Type of NPC: shopkeeper, quest_giver, passive_mob, aggressive_mob",
    )

    # Location information
    sub_zone_id: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    room_id: Mapped[str | None] = mapped_column(String(50), nullable=True)

    # Population control
    required_npc: Mapped[bool] = mapped_column(Boolean, default=lambda: False, nullable=False, index=True)
    max_population: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    spawn_probability: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)

    # Configuration stored as JSON
    base_stats: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="{}",
        comment="Base statistics for the NPC (DP, MP, attributes, etc.)",
    )
    behavior_config: Mapped[str] = mapped_column(
        Text, nullable=False, default="{}", comment="Behavior-specific configuration (aggression, wandering, etc.)"
    )
    ai_integration_stub: Mapped[str] = mapped_column(
        Text, nullable=False, default="{}", comment="Future AI integration configuration"
    )

    # Timestamps (server-side per SQLAlchemy 2.x rule)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        insert_default=func.now(),  # pylint: disable=not-callable  # func.now() callable at runtime (SQLAlchemy)
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        insert_default=func.now(),  # pylint: disable=not-callable  # func.now() callable at runtime
        onupdate=func.now(),  # pylint: disable=not-callable  # func.now() callable at runtime
        nullable=False,
    )

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize NPCDefinition with defaults."""
        super().__init__(*args, **kwargs)
        for attr, default in _NPC_DEFINITION_DEFAULTS:
            _set_default_if_missing(self, attr, default)

    @override
    def __repr__(self) -> str:
        """String representation of the NPC definition."""
        return f"<NPCDefinition(id={self.id}, name={self.name}, type={self.npc_type})>"

    def get_base_stats(self) -> _JSONDict:
        """Get base stats as dictionary."""
        return _loads_json_dict(self.base_stats)

    def set_base_stats(self, stats: _JSONDict) -> None:
        """Set base stats from dictionary."""
        self.base_stats = json.dumps(stats)

    def get_behavior_config(self) -> _JSONDict:
        """Get behavior configuration as dictionary."""
        return _loads_json_dict(self.behavior_config)

    def set_behavior_config(self, config: _JSONDict) -> None:
        """Set behavior configuration from dictionary."""
        self.behavior_config = json.dumps(config)

    def get_ai_integration_stub(self) -> _JSONDict:
        """Get AI integration stub configuration as dictionary."""
        return _loads_json_dict(self.ai_integration_stub)

    def set_ai_integration_stub(self, stub: _JSONDict) -> None:
        """Set AI integration stub configuration from dictionary."""
        self.ai_integration_stub = json.dumps(stub)

    def is_required(self) -> bool:
        """Check if this NPC is required to spawn."""
        return bool(self.required_npc)

    def can_spawn(self, current_population: int) -> bool:
        """Check if this NPC can spawn given current population."""
        # At runtime, SQLAlchemy Column[int] returns int, but mypy sees Column type
        # Handle MagicMock in tests by converting to int
        max_pop: int = int(self.max_population)
        return bool(current_population < max_pop)


class NPCSpawnRule(Base):
    """
    NPC spawn rule model.

    Defines conditions under which NPCs should be spawned, including
    player count requirements and environmental conditions.
    """

    __tablename__: str = "npc_spawn_rules"

    # Primary key
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # Foreign key to NPC definition
    npc_definition_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("npc_definitions.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # Sub-zone information
    sub_zone_id: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    # NPC population requirements (min/max instances of this NPC type)
    min_population: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    max_population: Mapped[int] = mapped_column(Integer, default=999, nullable=False)

    # Spawn conditions stored as JSON
    spawn_conditions: Mapped[str] = mapped_column(
        Text, nullable=False, default="{}", comment="Environmental and time-based spawn conditions"
    )

    # Relationships removed to eliminate circular reference issues
    # npc_definition = relationship("NPCDefinition", back_populates="spawn_rules")

    @override
    def __repr__(self) -> str:
        """String representation of the spawn rule."""
        return f"<NPCSpawnRule(id={self.id}, npc_def_id={self.npc_definition_id}, sub_zone={self.sub_zone_id})>"

    def get_spawn_conditions(self) -> _JSONDict:
        """Get spawn conditions as dictionary."""
        return _loads_json_dict(self.spawn_conditions)

    def set_spawn_conditions(self, conditions: _JSONDict) -> None:
        """Set spawn conditions from dictionary."""
        self.spawn_conditions = json.dumps(conditions)

    def can_spawn_with_population(self, current_population: int) -> bool:
        """Check if this rule allows spawning given current NPC population."""
        # At runtime, SQLAlchemy Column[int] returns int, but handle MagicMock in tests
        max_pop: int = int(self.max_population)
        return bool(current_population < max_pop)

    def _check_missing_key_condition(self, key: str, value: object, game_state: Mapping[str, object]) -> bool | None:
        """
        Check if missing key condition is acceptable.

        Returns:
            True if condition passes, False if fails, None if key exists (continue checking)
        """
        if key not in game_state:
            if value == "any" or (isinstance(value, list) and not value):
                return True
            return False
        return None

    def _check_list_condition(self, value: list[object], game_value: object) -> bool | None:
        """
        Check list condition.

        Returns:
            True if condition passes, False if fails, None if should skip (empty list)
        """
        if not value:
            return None
        return game_value in value

    @staticmethod
    def _game_value_below_bound(bound: object, game_value: object) -> bool:
        """True if numeric game_value is strictly below bound."""
        return isinstance(game_value, int | float) and isinstance(bound, int | float) and game_value < bound

    @staticmethod
    def _game_value_above_bound(bound: object, game_value: object) -> bool:
        """True if numeric game_value is strictly above bound."""
        return isinstance(game_value, int | float) and isinstance(bound, int | float) and game_value > bound

    def _check_dict_condition(self, value: _JSONDict, game_value: object) -> bool:
        """Check dict (range) condition."""
        if "min" in value and self._game_value_below_bound(value["min"], game_value):
            return False
        if "max" in value and self._game_value_above_bound(value["max"], game_value):
            return False
        return True

    def _check_simple_condition(self, value: object, game_value: object) -> bool | None:
        """
        Check simple value condition.

        Returns:
            True if condition passes, False if fails, None if should skip ("any")
        """
        if value == "any":
            return None
        return bool(game_value == value)

    def _spawn_value_allows_spawn(self, value: object, game_value: object) -> bool:
        """Return False if this condition value blocks spawning; True otherwise."""
        if isinstance(value, list):
            return self._check_list_condition(cast(list[object], value), game_value) is not False
        if isinstance(value, dict):
            return self._check_dict_condition(cast(_JSONDict, value), game_value)
        simple_check = self._check_simple_condition(value, game_value)
        return simple_check is not False

    def _single_spawn_condition_ok(self, key: str, value: object, game_state: Mapping[str, object]) -> bool:
        """Evaluate one key from spawn_conditions; False means spawn blocked."""
        missing_check = self._check_missing_key_condition(key, value, game_state)
        if missing_check is False:
            return False
        if missing_check is True:
            return True
        game_value = game_state[key]
        return self._spawn_value_allows_spawn(value, game_value)

    def check_spawn_conditions(self, game_state: Mapping[str, object]) -> bool:
        """Check if current game state meets spawn conditions."""
        conditions = self.get_spawn_conditions()
        if not conditions:
            return True
        for key, val in conditions.items():
            if not self._single_spawn_condition_ok(key, val, game_state):
                return False
        return True


class NPCRelationship(Base):
    """
    NPC relationship model.

    Defines relationships between different NPC types.
    """

    __tablename__: str = "npc_relationships"
    __table_args__: tuple[UniqueConstraint | CheckConstraint, ...] = (
        UniqueConstraint("npc_id_1", "npc_id_2", name="npc_relationships_npc_id_1_npc_id_2_key"),
        CheckConstraint(
            "relationship_type IN ('ally', 'enemy', 'neutral', 'follower')",
            name="npc_relationships_relationship_type_check",
        ),
    )

    # Primary key
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # Foreign keys to NPC definitions
    npc_id_1: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("npc_definitions.id", ondelete="CASCADE"), nullable=False
    )
    npc_id_2: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("npc_definitions.id", ondelete="CASCADE"), nullable=False
    )

    # Relationship information
    relationship_type: Mapped[str] = mapped_column(String(20), nullable=False)
    relationship_strength: Mapped[float] = mapped_column(Float, default=0.5)

    @override
    def __repr__(self) -> str:
        """String representation of the NPC relationship."""
        return (
            f"<NPCRelationship(id={self.id}, npc1={self.npc_id_1}, "
            f"npc2={self.npc_id_2}, type={self.relationship_type})>"
        )
