"""
Player model for game data.

This module defines the Player model that stores game-specific data
for each user, including stats, inventory, and current location.
"""

import json
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base

from ..metadata import metadata

Base = declarative_base(metadata=metadata)


class Player(Base):
    """
    Player model for game data.

    Stores all game-specific data for a user including stats,
    inventory, current location, and experience.
    """

    __tablename__ = "players"
    __table_args__ = {"extend_existing": True}

    # Primary key - TEXT (matches database schema)
    player_id = Column(String(length=255), primary_key=True)

    # Foreign key to users table
    user_id = Column(String(length=255), ForeignKey("users.id"), unique=True, nullable=False)

    # Player information
    name = Column(String(length=50), unique=True, nullable=False, index=True)

    # Game data stored as JSON in TEXT fields (SQLite compatible)
    stats = Column(
        Text(),
        nullable=False,
        default='{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100}',
    )
    inventory = Column(Text(), nullable=False, default="[]")
    status_effects = Column(Text(), nullable=False, default="[]")

    # Location and progression
    current_room_id = Column(String(length=50), nullable=False, default="earth_arkhamcity_intersection_derby_high")
    experience_points = Column(Integer(), default=0, nullable=False)
    level = Column(Integer(), default=1, nullable=False)

    # Admin status
    is_admin = Column(Integer(), default=0, nullable=False)  # SQLite doesn't have BOOLEAN, use INTEGER

    # Profession
    profession_id = Column(Integer(), default=0, nullable=False)

    # Timestamps (persist naive UTC)
    created_at = Column(DateTime(), default=lambda: datetime.now(UTC).replace(tzinfo=None), nullable=False)
    last_active = Column(DateTime(), default=lambda: datetime.now(UTC).replace(tzinfo=None), nullable=False)

    def __repr__(self) -> str:
        """String representation of the player."""
        return f"<Player(player_id={self.player_id}, name={self.name}, level={self.level})>"

    def get_stats(self) -> dict[str, Any]:
        """Get player stats as dictionary."""
        try:
            return json.loads(self.stats)
        except (json.JSONDecodeError, TypeError):
            return {
                "strength": 10,
                "dexterity": 10,
                "constitution": 10,
                "intelligence": 10,
                "wisdom": 10,
                "charisma": 10,
                "sanity": 100,
                "occult_knowledge": 0,
                "fear": 0,
                "corruption": 0,
                "cult_affiliation": 0,
                "current_health": 100,
            }

    def set_stats(self, stats: dict[str, Any]) -> None:
        """Set player stats from dictionary."""
        self.stats = json.dumps(stats)

    def get_inventory(self) -> list[dict[str, Any]]:
        """Get player inventory as list."""
        try:
            return json.loads(self.inventory)
        except (json.JSONDecodeError, TypeError):
            return []

    def set_inventory(self, inventory: list[dict[str, Any]]) -> None:
        """Set player inventory from list."""
        self.inventory = json.dumps(inventory)

    def get_status_effects(self) -> list[dict[str, Any]]:
        """Get player status effects as list."""
        try:
            return json.loads(self.status_effects)
        except (json.JSONDecodeError, TypeError):
            return []

    def set_status_effects(self, status_effects: list[dict[str, Any]]) -> None:
        """Set player status effects from list."""
        self.status_effects = json.dumps(status_effects)

    def add_experience(self, amount: int) -> None:
        """Add experience points to the player."""
        self.experience_points += amount
        # Simple level calculation (can be enhanced)
        self.level = (self.experience_points // 100) + 1

    def is_alive(self) -> bool:
        """Check if player is alive."""
        stats = self.get_stats()
        return stats.get("health", 0) > 0

    def is_admin_user(self) -> bool:
        """Check if player has admin privileges."""
        return bool(self.is_admin)

    def set_admin_status(self, admin_status: bool) -> None:
        """Set player's admin status."""
        self.is_admin = 1 if admin_status else 0

    def get_health_percentage(self) -> float:
        """Get player health as percentage."""
        stats = self.get_stats()
        current_health = stats.get("health", 100)
        max_health = 100  # Could be made configurable
        return (current_health / max_health) * 100
