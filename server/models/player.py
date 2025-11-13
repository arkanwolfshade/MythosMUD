"""
Player model for game data.

This module defines the Player model that stores game-specific data
for each user, including stats, inventory, and current location.
"""

import json
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, cast

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, relationship

from .base import Base  # ARCHITECTURE FIX Phase 3.1: Use shared Base

# Forward references for type checking (resolves circular imports)
# Note: SQLAlchemy will resolve string references via shared registry at runtime
if TYPE_CHECKING:
    from .sanity import (
        PlayerSanity,
        SanityAdjustmentLog,
        SanityCooldown,
        SanityExposureState,
    )
    from .user import User


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
        default='{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "position": "standing"}',
    )
    inventory = Column(Text(), nullable=False, default="[]")
    status_effects = Column(Text(), nullable=False, default="[]")

    # Location and progression
    current_room_id = Column(String(length=50), nullable=False, default="earth_arkhamcity_sanitarium_room_foyer_001")
    respawn_room_id = Column(
        String(length=100), nullable=True, default="earth_arkhamcity_sanitarium_room_foyer_001"
    )  # Player's respawn location (NULL = use default)
    experience_points = Column(Integer(), default=0, nullable=False)
    level = Column(Integer(), default=1, nullable=False)

    # Admin status
    is_admin = Column(Integer(), default=0, nullable=False)

    # ARCHITECTURE FIX Phase 3.1: Relationships defined directly in model (no circular imports)
    # Using simple string reference - SQLAlchemy resolves via registry after all models imported
    user: Mapped["User"] = relationship(
        "User", back_populates="player", overlaps="player"
    )  # SQLite doesn't have BOOLEAN, use INTEGER

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
            stats = cast(dict[str, Any], json.loads(cast(str, self.stats)))
        except (json.JSONDecodeError, TypeError):
            stats = {
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
                "position": "standing",
            }
            return stats

        if "position" not in stats:
            stats["position"] = "standing"
            try:
                self.set_stats(stats)
            except Exception:
                # Fallback silently if persistence update fails during read-time normalization
                pass

        return stats

    def set_stats(self, stats: dict[str, Any]) -> None:
        """Set player stats from dictionary."""
        self.stats = json.dumps(stats)  # type: ignore[assignment]

    def get_inventory(self) -> list[dict[str, Any]]:
        """Get player inventory as list."""
        try:
            return cast(list[dict[str, Any]], json.loads(cast(str, self.inventory)))
        except (json.JSONDecodeError, TypeError):
            return []

    def set_inventory(self, inventory: list[dict[str, Any]]) -> None:
        """Set player inventory from list."""
        self.inventory = json.dumps(inventory)  # type: ignore[assignment]

    def get_status_effects(self) -> list[dict[str, Any]]:
        """Get player status effects as list."""
        try:
            return cast(list[dict[str, Any]], json.loads(cast(str, self.status_effects)))
        except (json.JSONDecodeError, TypeError):
            return []

    def set_status_effects(self, status_effects: list[dict[str, Any]]) -> None:
        """Set player status effects from list."""
        self.status_effects = json.dumps(status_effects)  # type: ignore[assignment]

    def get_equipped_items(self) -> dict[str, Any]:
        """Return equipped items mapping."""
        equipped = getattr(self, "_equipped_items", None)
        if equipped is None:
            return {}
        if isinstance(equipped, str):
            try:
                equipped_dict = cast(dict[str, Any], json.loads(equipped))
            except (TypeError, json.JSONDecodeError):
                equipped_dict = {}
            self._equipped_items = equipped_dict
            return equipped_dict
        return cast(dict[str, Any], equipped)

    def set_equipped_items(self, equipped: dict[str, Any]) -> None:
        """Assign equipped items mapping."""
        self._equipped_items = equipped

    def add_experience(self, amount: int) -> None:
        """Add experience points to the player."""
        self.experience_points += amount  # type: ignore[assignment]
        # Simple level calculation (can be enhanced)
        self.level = (self.experience_points // 100) + 1  # type: ignore[assignment]

    def is_alive(self) -> bool:
        """Check if player is alive (HP > 0)."""
        stats = self.get_stats()
        return bool(stats.get("current_health", 0) > 0)

    def is_mortally_wounded(self) -> bool:
        """
        Check if player is mortally wounded (0 >= HP > -10).

        Returns:
            True if player has 0 to -9 HP (mortally wounded state)
        """
        stats = self.get_stats()
        current_hp = stats.get("current_health", 0)
        return bool(0 >= current_hp > -10)

    def is_dead(self) -> bool:
        """
        Check if player is dead (HP <= -10).

        Returns:
            True if player has -10 HP or below
        """
        stats = self.get_stats()
        current_hp = stats.get("current_health", 0)
        return bool(current_hp <= -10)

    def get_health_state(self) -> str:
        """
        Get player's current health state.

        Returns:
            "alive" if HP > 0
            "mortally_wounded" if 0 >= HP > -10
            "dead" if HP <= -10
        """
        stats = self.get_stats()
        current_hp = stats.get("current_health", 0)

        if current_hp > 0:
            return "alive"
        elif current_hp > -10:
            return "mortally_wounded"
        else:
            return "dead"

    def is_admin_user(self) -> bool:
        """Check if player has admin privileges."""
        return bool(self.is_admin)

    def set_admin_status(self, admin_status: bool) -> None:
        """Set player's admin status."""
        self.is_admin = 1 if admin_status else 0  # type: ignore[assignment]

    def get_health_percentage(self) -> float:
        """Get player health as percentage."""
        stats = self.get_stats()
        current_health = stats.get("current_health", 100)
        max_health = 100  # Could be made configurable
        return float((current_health / max_health) * 100)

    sanity: Mapped["PlayerSanity"] = relationship(
        "PlayerSanity",
        back_populates="player",
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True,
    )

    sanity_adjustments: Mapped[list["SanityAdjustmentLog"]] = relationship(
        "SanityAdjustmentLog",
        back_populates="player",
        cascade="all, delete-orphan",
        order_by="desc(SanityAdjustmentLog.created_at)",
    )

    sanity_exposures: Mapped[list["SanityExposureState"]] = relationship(
        "SanityExposureState",
        back_populates="player",
        cascade="all, delete-orphan",
    )

    sanity_cooldowns: Mapped[list["SanityCooldown"]] = relationship(
        "SanityCooldown",
        back_populates="player",
        cascade="all, delete-orphan",
    )
