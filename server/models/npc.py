"""
NPC database models for MythosMUD.

This module defines the SQLAlchemy models for NPC definitions, spawn rules,
and relationships that support the NPC subsystem.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed

import json
from datetime import datetime
from enum import StrEnum
from typing import Any, cast

from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,  # pylint: disable=unused-import  # func used in insert_default/onupdate
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from ..npc_metadata import npc_metadata


class Base(DeclarativeBase):
    """SQLAlchemy declarative base for NPC database models."""

    metadata = npc_metadata


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

    __tablename__ = "npc_definitions"
    __table_args__ = (
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
        insert_default=func.now(),
        nullable=False,  # pylint: disable=not-callable  # func.now() callable at runtime
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        insert_default=func.now(),  # pylint: disable=not-callable  # func.now() callable at runtime
        onupdate=func.now(),  # pylint: disable=not-callable  # func.now() callable at runtime
        nullable=False,
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize NPCDefinition with defaults."""
        super().__init__(*args, **kwargs)
        # Apply defaults if not provided (SQLAlchemy may set to None initially)
        _sentinel = object()
        required_npc_val = getattr(self, "required_npc", _sentinel)
        if required_npc_val is _sentinel or required_npc_val is None:
            object.__setattr__(self, "required_npc", False)
        max_population_val = getattr(self, "max_population", _sentinel)
        if max_population_val is _sentinel or max_population_val is None:
            object.__setattr__(self, "max_population", 1)
        spawn_probability_val = getattr(self, "spawn_probability", _sentinel)
        if spawn_probability_val is _sentinel or spawn_probability_val is None:
            object.__setattr__(self, "spawn_probability", 1.0)
        base_stats_val = getattr(self, "base_stats", _sentinel)
        if base_stats_val is _sentinel or base_stats_val is None:
            object.__setattr__(self, "base_stats", "{}")
        behavior_config_val = getattr(self, "behavior_config", _sentinel)
        if behavior_config_val is _sentinel or behavior_config_val is None:
            object.__setattr__(self, "behavior_config", "{}")
        ai_integration_stub_val = getattr(self, "ai_integration_stub", _sentinel)
        if ai_integration_stub_val is _sentinel or ai_integration_stub_val is None:
            object.__setattr__(self, "ai_integration_stub", "{}")

    def __repr__(self) -> str:
        """String representation of the NPC definition."""
        return f"<NPCDefinition(id={self.id}, name={self.name}, type={self.npc_type})>"

    def get_base_stats(self) -> dict[str, Any]:
        """Get base stats as dictionary."""
        try:
            return cast(dict[str, Any], json.loads(self.base_stats))
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_base_stats(self, stats: dict[str, Any]) -> None:
        """Set base stats from dictionary."""
        self.base_stats = json.dumps(stats)

    def get_behavior_config(self) -> dict[str, Any]:
        """Get behavior configuration as dictionary."""
        try:
            return cast(dict[str, Any], json.loads(self.behavior_config))
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_behavior_config(self, config: dict[str, Any]) -> None:
        """Set behavior configuration from dictionary."""
        self.behavior_config = json.dumps(config)

    def get_ai_integration_stub(self) -> dict[str, Any]:
        """Get AI integration stub configuration as dictionary."""
        try:
            return cast(dict[str, Any], json.loads(self.ai_integration_stub))
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_ai_integration_stub(self, stub: dict[str, Any]) -> None:
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

    __tablename__ = "npc_spawn_rules"

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

    def __repr__(self) -> str:
        """String representation of the spawn rule."""
        return f"<NPCSpawnRule(id={self.id}, npc_def_id={self.npc_definition_id}, sub_zone={self.sub_zone_id})>"

    def get_spawn_conditions(self) -> dict[str, Any]:
        """Get spawn conditions as dictionary."""
        try:
            return cast(dict[str, Any], json.loads(self.spawn_conditions))
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_spawn_conditions(self, conditions: dict[str, Any]) -> None:
        """Set spawn conditions from dictionary."""
        self.spawn_conditions = json.dumps(conditions)

    def can_spawn_with_population(self, current_population: int) -> bool:
        """Check if this rule allows spawning given current NPC population."""
        # At runtime, SQLAlchemy Column[int] returns int, but handle MagicMock in tests
        max_pop: int = int(self.max_population)
        return bool(current_population < max_pop)

    def _check_missing_key_condition(self, key: str, value: Any, game_state: dict[str, Any]) -> bool | None:
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

    def _check_list_condition(self, value: list[Any], game_value: Any) -> bool | None:
        """
        Check list condition.

        Returns:
            True if condition passes, False if fails, None if should skip (empty list)
        """
        if not value:
            return None
        return game_value in value

    def _check_dict_condition(self, value: dict[str, Any], game_value: Any) -> bool:
        """Check dict (range) condition."""
        if "min" in value and game_value < value["min"]:
            return False
        if "max" in value and game_value > value["max"]:
            return False
        return True

    def _check_simple_condition(self, value: Any, game_value: Any) -> bool | None:
        """
        Check simple value condition.

        Returns:
            True if condition passes, False if fails, None if should skip ("any")
        """
        if value == "any":
            return None
        result: bool = cast(bool, game_value == value)
        return result

    def check_spawn_conditions(self, game_state: dict[str, Any]) -> bool:
        """Check if current game state meets spawn conditions."""
        conditions = self.get_spawn_conditions()
        if not conditions:
            return True

        for key, value in conditions.items():
            missing_check = self._check_missing_key_condition(key, value, game_state)
            if missing_check is False:
                return False
            if missing_check is True:
                continue

            game_value = game_state[key]

            if isinstance(value, list):
                list_check = self._check_list_condition(value, game_value)
                if list_check is False:
                    return False
            elif isinstance(value, dict):
                if not self._check_dict_condition(value, game_value):
                    return False
            else:
                simple_check = self._check_simple_condition(value, game_value)
                if simple_check is False:
                    return False

        return True


class NPCRelationship(Base):
    """
    NPC relationship model.

    Defines relationships between different NPC types.
    """

    __tablename__ = "npc_relationships"
    __table_args__ = (
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

    def __repr__(self) -> str:
        """String representation of the NPC relationship."""
        return f"<NPCRelationship(id={self.id}, npc1={self.npc_id_1}, npc2={self.npc_id_2}, type={self.relationship_type})>"
