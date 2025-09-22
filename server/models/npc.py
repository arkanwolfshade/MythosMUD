"""
NPC database models for MythosMUD.

This module defines the SQLAlchemy models for NPC definitions, spawn rules,
and relationships that support the NPC subsystem.
"""

import json
from datetime import UTC, datetime
from enum import Enum
from typing import Any

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import declarative_base, relationship

from ..npc_metadata import npc_metadata

Base = declarative_base(metadata=npc_metadata)


class NPCDefinitionType(str, Enum):
    """Enumeration of valid NPC definition types."""

    SHOPKEEPER = "shopkeeper"
    QUEST_GIVER = "quest_giver"
    PASSIVE_MOB = "passive_mob"
    AGGRESSIVE_MOB = "aggressive_mob"


class NPCRelationshipType(str, Enum):
    """Enumeration of valid NPC relationship types."""

    ALLY = "ally"
    ENEMY = "enemy"
    NEUTRAL = "neutral"
    FOLLOWER = "follower"


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
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Basic information
    name = Column(String(100), nullable=False, index=True)
    description = Column(Text)

    # NPC type and classification
    npc_type = Column(
        String(20),
        nullable=False,
        index=True,
        comment="Type of NPC: shopkeeper, quest_giver, passive_mob, aggressive_mob",
    )

    # Location information
    sub_zone_id = Column(String(50), nullable=False, index=True)
    room_id = Column(String(50), nullable=True)

    # Population control
    required_npc = Column(Boolean, default=False, nullable=False, index=True)
    max_population = Column(Integer, default=1, nullable=False)
    spawn_probability = Column(Float, default=1.0, nullable=False)

    # Configuration stored as JSON (SQLite compatible)
    base_stats = Column(
        Text, nullable=False, default="{}", comment="Base statistics for the NPC (HP, MP, attributes, etc.)"
    )
    behavior_config = Column(
        Text, nullable=False, default="{}", comment="Behavior-specific configuration (aggression, wandering, etc.)"
    )
    ai_integration_stub = Column(Text, nullable=False, default="{}", comment="Future AI integration configuration")

    # Timestamps
    created_at = Column(DateTime, default=lambda: datetime.now(UTC).replace(tzinfo=None), nullable=False)
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC).replace(tzinfo=None),
        nullable=False,
        onupdate=lambda: datetime.now(UTC).replace(tzinfo=None),
    )

    # Relationships
    spawn_rules = relationship("NPCSpawnRule", back_populates="npc_definition", cascade="all, delete-orphan")
    relationships_as_npc1 = relationship(
        "NPCRelationship", foreign_keys="NPCRelationship.npc_id_1", back_populates="npc_1"
    )
    relationships_as_npc2 = relationship(
        "NPCRelationship", foreign_keys="NPCRelationship.npc_id_2", back_populates="npc_2"
    )

    def __repr__(self) -> str:
        """String representation of the NPC definition."""
        return f"<NPCDefinition(id={self.id}, name={self.name}, type={self.npc_type})>"

    def get_base_stats(self) -> dict[str, Any]:
        """Get base stats as dictionary."""
        try:
            return json.loads(self.base_stats)
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_base_stats(self, stats: dict[str, Any]) -> None:
        """Set base stats from dictionary."""
        self.base_stats = json.dumps(stats)

    def get_behavior_config(self) -> dict[str, Any]:
        """Get behavior configuration as dictionary."""
        try:
            return json.loads(self.behavior_config)
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_behavior_config(self, config: dict[str, Any]) -> None:
        """Set behavior configuration from dictionary."""
        self.behavior_config = json.dumps(config)

    def get_ai_integration_stub(self) -> dict[str, Any]:
        """Get AI integration stub configuration as dictionary."""
        try:
            return json.loads(self.ai_integration_stub)
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
        return current_population < self.max_population


class NPCSpawnRule(Base):
    """
    NPC spawn rule model.

    Defines conditions under which NPCs should be spawned, including
    player count requirements and environmental conditions.
    """

    __tablename__ = "npc_spawn_rules"

    # Primary key
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Foreign key to NPC definition
    npc_definition_id = Column(
        Integer, ForeignKey("npc_definitions.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # Sub-zone information
    sub_zone_id = Column(String(50), nullable=False, index=True)

    # Player count requirements
    min_players = Column(Integer, default=0, nullable=False)
    max_players = Column(Integer, default=999, nullable=False)

    # Spawn conditions stored as JSON
    spawn_conditions = Column(
        Text, nullable=False, default="{}", comment="Environmental and time-based spawn conditions"
    )

    # Relationships
    npc_definition = relationship("NPCDefinition", back_populates="spawn_rules")

    def __repr__(self) -> str:
        """String representation of the spawn rule."""
        return f"<NPCSpawnRule(id={self.id}, npc_def_id={self.npc_definition_id}, sub_zone={self.sub_zone_id})>"

    def get_spawn_conditions(self) -> dict[str, Any]:
        """Get spawn conditions as dictionary."""
        try:
            return json.loads(self.spawn_conditions)
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_spawn_conditions(self, conditions: dict[str, Any]) -> None:
        """Set spawn conditions from dictionary."""
        self.spawn_conditions = json.dumps(conditions)

    def can_spawn_for_player_count(self, player_count: int) -> bool:
        """Check if this rule allows spawning for given player count."""
        return self.min_players <= player_count <= self.max_players

    def check_spawn_conditions(self, game_state: dict[str, Any]) -> bool:
        """Check if current game state meets spawn conditions."""
        conditions = self.get_spawn_conditions()
        if not conditions:
            return True

        # Simple condition checking - can be enhanced
        for key, value in conditions.items():
            if key not in game_state:
                return False

            game_value = game_state[key]

            # Handle different condition types
            if isinstance(value, list):
                if game_value not in value:
                    return False
            elif isinstance(value, dict):
                # Range checking
                if "min" in value and game_value < value["min"]:
                    return False
                if "max" in value and game_value > value["max"]:
                    return False
            else:
                if game_value != value:
                    return False

        return True


class NPCRelationship(Base):
    """
    NPC relationship model.

    Defines relationships between NPCs, including alliances, enmities,
    and social dynamics that affect NPC behavior.
    """

    __tablename__ = "npc_relationships"
    __table_args__ = (
        UniqueConstraint("npc_id_1", "npc_id_2", name="idx_npc_relationships_unique"),
        CheckConstraint("relationship_type IN ('ally', 'enemy', 'neutral', 'follower')", name="chk_relationship_type"),
    )

    # Primary key
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Foreign keys to NPC definitions
    npc_id_1 = Column(Integer, ForeignKey("npc_definitions.id", ondelete="CASCADE"), nullable=False, index=True)
    npc_id_2 = Column(Integer, ForeignKey("npc_definitions.id", ondelete="CASCADE"), nullable=False, index=True)

    # Relationship type and strength
    relationship_type = Column(
        String(20), nullable=False, comment="Type of relationship: ally, enemy, neutral, follower"
    )
    relationship_strength = Column(
        Float, default=0.5, nullable=False, comment="Strength of the relationship (0.0 to 1.0)"
    )

    # Relationships
    npc_1 = relationship("NPCDefinition", foreign_keys=[npc_id_1], back_populates="relationships_as_npc1")
    npc_2 = relationship("NPCDefinition", foreign_keys=[npc_id_2], back_populates="relationships_as_npc2")

    def __repr__(self) -> str:
        """String representation of the relationship."""
        return f"<NPCRelationship(npc1={self.npc_id_1}, npc2={self.npc_id_2}, type={self.relationship_type})>"

    def is_positive_relationship(self) -> bool:
        """Check if this is a positive relationship (ally or follower)."""
        return self.relationship_type in [NPCRelationshipType.ALLY, NPCRelationshipType.FOLLOWER]

    def is_negative_relationship(self) -> bool:
        """Check if this is a negative relationship (enemy)."""
        return self.relationship_type == NPCRelationshipType.ENEMY

    def is_neutral_relationship(self) -> bool:
        """Check if this is a neutral relationship."""
        return self.relationship_type == NPCRelationshipType.NEUTRAL

    def get_relationship_modifier(self) -> float:
        """Get relationship modifier for behavior calculations."""
        if self.is_positive_relationship():
            return self.relationship_strength
        elif self.is_negative_relationship():
            return -self.relationship_strength
        else:
            return 0.0
