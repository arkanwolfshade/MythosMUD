"""
Player model for game data.

This module defines the Player model that stores game-specific data
for each user, including stats, inventory, and current location.
"""

# pylint: disable=too-few-public-methods,too-many-lines  # Reason: SQLAlchemy models are data classes; Player aggregates stats, combat, lucidity, containers - splitting would fragment domain cohesion

import json
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, cast

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, Integer, String, Text, event, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.mutable import MutableDict, MutableList
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base  # ARCHITECTURE FIX Phase 3.1: Use shared Base
from .game import PositionState

# Forward references for type checking (resolves circular imports)
# Note: SQLAlchemy will resolve string references via shared registry at runtime
if TYPE_CHECKING:
    from .lucidity import (
        LucidityAdjustmentLog,
        LucidityCooldown,
        LucidityExposureState,
        PlayerLucidity,
    )
    from .player_spells import PlayerSpell
    from .user import User


class Player(Base):
    """
    Player model for game data.

    Stores all game-specific data for a user including stats,
    inventory, current location, and experience.
    """

    __tablename__ = "players"
    __table_args__ = {"extend_existing": True}

    # Primary key - UUID (matches user_id type for consistency)
    player_id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)

    # Foreign key to users table - use UUID to match users.id (UUID type in PostgreSQL)
    # MULTI-CHARACTER: Removed unique=True to allow multiple characters per user
    # Explicit index=True for efficient queries
    user_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("users.id"), nullable=False, index=True)

    # Player information
    # MULTI-CHARACTER: Removed unique=True - uniqueness enforced by case-insensitive partial unique index
    # in database (idx_players_name_lower_unique_active) for active characters only
    name: Mapped[str] = mapped_column(String(length=50), nullable=False, index=True)

    # Game data stored as JSONB (migrated from TEXT in migration 006)
    # BUGFIX: Use MutableDict to track in-place mutations for proper persistence
    # As documented in "Persistence and Mutation Tracking" - Dr. Armitage, 1930
    # JSONB columns require mutation tracking to detect in-place changes
    stats: Mapped[dict[str, Any]] = mapped_column(
        MutableDict.as_mutable(JSONB),
        nullable=False,
        default=lambda: {
            "strength": 50,
            "dexterity": 50,
            "constitution": 50,
            "size": 50,
            "intelligence": 50,
            "power": 50,
            "education": 50,
            "charisma": 50,
            "luck": 50,
            "lucidity": 100,
            "occult": 0,
            "corruption": 0,
            "current_dp": 20,  # DP max = (CON + SIZ) / 5 = (50 + 50) / 5 = 20
            "magic_points": 10,  # MP max = ceil(POW * 0.2) = ceil(50 * 0.2) = 10
            "position": "standing",
        },
    )
    inventory: Mapped[str] = mapped_column(Text(), nullable=False, default="[]")
    status_effects: Mapped[str] = mapped_column(Text(), nullable=False, default="[]")

    # Location and progression
    # CRITICAL FIX: Increased from 50 to 255 to accommodate hierarchical room IDs
    # Room IDs like "earth_arkhamcity_sanitarium_room_foyer_entrance_001" are 54 characters
    current_room_id: Mapped[str] = mapped_column(
        String(length=255), nullable=False, default="earth_arkhamcity_sanitarium_room_foyer_001"
    )
    respawn_room_id: Mapped[str | None] = mapped_column(
        String(length=100), nullable=True, default="earth_arkhamcity_sanitarium_room_foyer_001"
    )  # Player's respawn location (NULL = use default)
    experience_points: Mapped[int] = mapped_column(Integer(), default=0, nullable=False)
    level: Mapped[int] = mapped_column(Integer(), default=1, nullable=False)

    # Admin status
    is_admin: Mapped[int] = mapped_column(Integer(), default=0, nullable=False)

    # ARCHITECTURE FIX Phase 3.1: Relationships defined directly in model (no circular imports)
    # MULTI-CHARACTER: Changed to one-to-many relationship (uselist=True)
    # Using simple string reference - SQLAlchemy resolves via registry after all models imported
    user: Mapped["User"] = relationship("User", back_populates="players", overlaps="player")
    spells: Mapped[list["PlayerSpell"]] = relationship(
        "PlayerSpell", back_populates="player", cascade="all, delete-orphan"
    )

    # Profession - add index for queries filtering by profession
    profession_id: Mapped[int] = mapped_column(BigInteger(), default=0, nullable=False, index=True)

    # MULTI-CHARACTER: Soft deletion support
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable=True)

    # Timestamps (persist naive UTC)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), default=lambda: datetime.now(UTC).replace(tzinfo=None), nullable=False
    )
    last_active: Mapped[datetime] = mapped_column(
        DateTime(), default=lambda: datetime.now(UTC).replace(tzinfo=None), nullable=False
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize Player instance."""
        super().__init__(*args, **kwargs)
        # Initialize instance attributes
        self._equipped_items: dict[str, Any] | None = None

    def __repr__(self) -> str:
        """String representation of the player."""
        return f"<Player(player_id={self.player_id}, name={self.name}, level={self.level})>"

    def get_stats(self) -> dict[str, Any]:
        """Get player stats as dictionary.

        Returns a MutableDict instance that automatically tracks mutations
        for proper SQLAlchemy change detection and persistence.
        """
        # With JSONB + MutableDict, SQLAlchemy returns MutableDict (dict subclass)
        # Note: mypy sees self.stats as Column[Any], but at runtime SQLAlchemy returns the actual value
        try:
            if isinstance(self.stats, dict):
                # JSONB column returns dict directly
                stats = self.stats
            elif isinstance(self.stats, str):  # type: ignore[unreachable]  # Reason: isinstance check ensures str branch for backward compatibility, but mypy infers dict type from column definition and marks this branch as unreachable
                # Fallback for TEXT column (backward compatibility during migration)
                stats = json.loads(self.stats)
            else:
                # Handle None or other types
                raise TypeError(f"Unexpected stats type: {type(self.stats)}")
        except (json.JSONDecodeError, TypeError, AttributeError):
            stats = {
                "strength": 50,
                "dexterity": 50,
                "constitution": 50,
                "size": 50,
                "intelligence": 50,
                "power": 50,
                "education": 50,
                "charisma": 50,
                "luck": 50,
                "lucidity": 100,
                "occult": 0,
                "corruption": 0,
                "current_dp": 20,  # DP max = (CON + SIZ) / 5 = (50 + 50) / 5 = 20
                "magic_points": 10,  # MP max = ceil(POW * 0.2) = ceil(50 * 0.2) = 10
                "position": "standing",
            }
            return stats

        if "position" not in stats:
            stats["position"] = "standing"
            try:
                self.set_stats(stats)
            except (json.JSONDecodeError, TypeError, AttributeError):
                # Fallback silently if persistence update fails during read-time normalization
                pass

        return stats

    def set_stats(self, stats: dict[str, Any]) -> None:
        """Set player stats from dictionary.

        Accepts both plain dict and MutableDict instances.
        SQLAlchemy automatically converts plain dicts to MutableDict.
        """
        # With MutableDict.as_mutable(JSONB), SQLAlchemy automatically handles conversion
        self.stats = stats

    def get_inventory(self) -> list[dict[str, Any]]:
        """Get player inventory as list.

        Handles both JSON string (from database) and list (in-memory) formats.
        """
        try:
            # At runtime, self.inventory is the actual value (string), not the Column descriptor
            # SQLAlchemy columns return their values at runtime, not the Column object
            # We need to access the value directly, which mypy doesn't understand
            inventory_value = getattr(self, "inventory", "[]")
            if isinstance(inventory_value, list):
                # Already a list (in-memory format after persistence fix)
                return cast(list[dict[str, Any]], inventory_value)
            if isinstance(inventory_value, str):
                # JSON string (from database or legacy format)
                return cast(list[dict[str, Any]], json.loads(inventory_value))
            # Handle None or other types
            return []
        except (json.JSONDecodeError, TypeError, AttributeError):
            return []

    def set_inventory(self, inventory: list[dict[str, Any]]) -> None:
        """Set player inventory from list."""
        self.inventory = json.dumps(inventory)

    def get_status_effects(self) -> list[dict[str, Any]]:
        """Get player status effects as list."""
        try:
            return cast(list[dict[str, Any]], json.loads(self.status_effects))
        except (json.JSONDecodeError, TypeError):
            return []

    def set_status_effects(self, status_effects: list[dict[str, Any]]) -> None:
        """Set player status effects from list."""
        self.status_effects = json.dumps(status_effects)

    def get_equipped_items(self) -> dict[str, Any]:
        """Return equipped items mapping.

        On load, _equipped_items may be None; populate from inventory_record.equipped_json
        if present (player_inventories table).
        """
        equipped = getattr(self, "_equipped_items", None)
        if equipped is None:
            record = getattr(self, "inventory_record", None)
            if record is not None and getattr(record, "equipped_json", None):
                try:
                    parsed = json.loads(record.equipped_json)
                    if isinstance(parsed, dict):
                        self._equipped_items = parsed
                        return parsed
                except (json.JSONDecodeError, TypeError, AttributeError):
                    pass
            return {}
        if isinstance(equipped, str):
            try:
                equipped_dict = cast(dict[str, Any], json.loads(equipped))
            except (json.JSONDecodeError, TypeError, AttributeError):
                equipped_dict = {}
            self._equipped_items = equipped_dict
            return equipped_dict
        return cast(dict[str, Any], equipped)

    def set_equipped_items(self, equipped: dict[str, Any]) -> None:
        """Assign equipped items mapping."""
        self._equipped_items = equipped

    def add_experience(self, amount: int) -> None:
        """Add experience points to the player."""
        self.experience_points += amount
        # Simple level calculation (can be enhanced)
        self.level = (self.experience_points // 100) + 1

    def is_alive(self) -> bool:
        """Check if player is alive (DP > 0)."""
        stats = self.get_stats()
        return bool(stats.get("current_dp", 0) > 0)

    def is_mortally_wounded(self) -> bool:
        """
        Check if player is mortally wounded (0 >= DP > -10).

        Returns:
            True if player has 0 to -9 DP (mortally wounded state)
        """
        stats = self.get_stats()
        current_dp = stats.get("current_dp", 0)  # current_dp represents DP
        return bool(0 >= current_dp > -10)

    def is_dead(self) -> bool:
        """
        Check if player is dead (DP <= -10).

        Returns:
            True if player has -10 DP or below
        """
        stats = self.get_stats()
        current_dp = stats.get("current_dp", 0)  # current_dp represents DP
        return bool(current_dp <= -10)

    def get_health_state(self) -> str:
        """
        Get player's current health state.

        Returns:
            "alive" if DP > 0
            "mortally_wounded" if 0 >= DP > -10
            "dead" if DP <= -10
        """
        stats = self.get_stats()
        current_dp = stats.get("current_dp", 0)  # current_dp represents DP

        if current_dp > 0:
            return "alive"
        if current_dp > -10:
            return "mortally_wounded"
        return "dead"

    def is_admin_user(self) -> bool:
        """Check if player has admin privileges."""
        return bool(self.is_admin)

    def set_admin_status(self, admin_status: bool) -> None:
        """Set player's admin status."""
        self.is_admin = 1 if admin_status else 0

    def get_combat_stats(self) -> dict[str, int]:
        """
        Get stats used for combat participant creation.

        Returns current_dp, max_dp, and dexterity for CombatParticipantData.
        Centralizes combat stat semantics per Domain-Driven Design.
        """
        stats = self.get_stats()
        return {
            "current_dp": int(stats.get("current_dp", 100)),
            "max_dp": int(stats.get("max_dp", 100)),
            "dexterity": int(stats.get("dexterity", 10)),
        }

    def get_health_percentage(self) -> float:
        """Get player determination points (DP) as percentage."""
        stats = self.get_stats()
        current_dp = stats.get("current_dp", 20)  # current_dp represents DP
        # Calculate max DP from CON + SIZ if available, otherwise use default
        constitution = stats.get("constitution", 50)
        size = stats.get("size", 50)
        max_dp = stats.get("max_dp", (constitution + size) // 5)  # DP max = (CON + SIZ) / 5
        if not max_dp:
            max_dp = 20  # Prevent division by zero
        return float((current_dp / max_dp) * 100)

    def apply_dp_decay(self, amount: int = 1) -> tuple[int, int, bool]:
        """
        Apply DP decay (e.g. mortally wounded bleeding) with posture updates.

        Decreases DP by amount, caps at -10. When crossing to 0 or below, posture
        is set to LYING (unconscious). Encapsulates domain rules from "Corporeal
        Collapse and Unconsciousness" - Dr. Armitage, 1928.

        Args:
            amount: DP to subtract (default 1)

        Returns:
            Tuple of (old_dp, new_dp, posture_changed)
        """
        stats = self.get_stats()
        old_dp = stats.get("current_dp", 0)  # current_dp represents DP
        new_dp = max(old_dp - amount, -10)
        stats["current_dp"] = new_dp

        posture_changed = False
        if new_dp <= 0 < old_dp:
            stats["position"] = PositionState.LYING
            posture_changed = True
        elif new_dp <= 0 and stats.get("position") != PositionState.LYING:
            stats["position"] = PositionState.LYING
            posture_changed = True

        self.set_stats(stats)
        return (old_dp, new_dp, posture_changed)

    def restore_to_full_health(self) -> int:
        """
        Restore player to full health (max DP, standing posture).

        Used on respawn. Sets DP to max_dp and posture to STANDING.
        As documented in "Resurrection and Corporeal Restoration" - Dr. Armitage, 1930.

        Returns:
            Previous DP value (before restore)
        """
        stats = self.get_stats()
        old_dp: int = int(stats.get("current_dp", 0))
        max_dp = stats.get("max_dp", 100)
        stats["current_dp"] = max_dp
        stats["position"] = PositionState.STANDING
        self.set_stats(stats)
        return old_dp

    def apply_dp_change(self, new_dp: int) -> tuple[int, bool, bool]:
        """
        Apply a DP change (e.g. from combat sync) with posture updates.

        Updates current_dp to new_dp, sets posture to LYING when DP <= 0.
        Used when syncing in-memory combat state to persistent player.

        Args:
            new_dp: New DP value (typically from CombatParticipant)

        Returns:
            Tuple of (old_dp, became_mortally_wounded, became_dead)
        """
        stats = self.get_stats()
        old_dp = stats.get("current_dp", 0)
        stats["current_dp"] = new_dp
        if new_dp <= 0:
            stats["position"] = PositionState.LYING
        self.set_stats(stats)
        # R1716: two distinct variables (old_dp, new_dp) cannot be one chained comparison
        became_mortally_wounded = old_dp > 0 and (0 >= new_dp > -10)  # pylint: disable=chained-comparison
        became_dead = new_dp <= -10 and old_dp > -10
        return (old_dp, became_mortally_wounded, became_dead)

    lucidity: Mapped["PlayerLucidity"] = relationship(
        "PlayerLucidity",
        back_populates="player",
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True,
    )

    lucidity_adjustments: Mapped[list["LucidityAdjustmentLog"]] = relationship(
        "LucidityAdjustmentLog",
        back_populates="player",
        cascade="all, delete-orphan",
        order_by="desc(LucidityAdjustmentLog.created_at)",
    )

    lucidity_exposures: Mapped[list["LucidityExposureState"]] = relationship(
        "LucidityExposureState",
        back_populates="player",
        cascade="all, delete-orphan",
    )

    lucidity_cooldowns: Mapped[list["LucidityCooldown"]] = relationship(
        "LucidityCooldown",
        back_populates="player",
        cascade="all, delete-orphan",
    )

    channel_preferences: Mapped["PlayerChannelPreferences | None"] = relationship(
        "PlayerChannelPreferences",
        back_populates="player",
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True,
    )

    inventory_record: Mapped["PlayerInventory | None"] = relationship(
        "PlayerInventory",
        back_populates="player",
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True,
    )

    exploration_records: Mapped[list["PlayerExploration"]] = relationship(
        "PlayerExploration",
        back_populates="player",
        cascade="all, delete-orphan",
    )


class PlayerChannelPreferences(Base):
    """
    Player channel preferences model for Advanced Chat Channels.

    Stores player preferences for chat channels including default channel
    and muted channels list.
    """

    __tablename__ = "player_channel_preferences"

    # Primary key - UUID to match players.player_id exactly
    # CRITICAL: Must use UUID(as_uuid=False) to match Player.player_id type
    # Both use UUID(as_uuid=False) which creates UUID column type in PostgreSQL
    # The as_uuid=False parameter only affects Python type handling (strings vs UUID objects)
    player_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        primary_key=True,
    )
    default_channel: Mapped[str] = mapped_column(String(32), nullable=False, default="local")
    muted_channels: Mapped[list[str]] = mapped_column(MutableList.as_mutable(JSONB), nullable=False, default=list)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        server_default=text("CURRENT_TIMESTAMP"),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        server_default=text("CURRENT_TIMESTAMP"),
    )

    player: Mapped["Player"] = relationship("Player", back_populates="channel_preferences")


class PlayerInventory(Base):
    """
    Player inventory model for persistent storage of items.

    This matches the player_inventories table in PostgreSQL.
    """

    __tablename__ = "player_inventories"

    player_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        primary_key=True,
    )
    inventory_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    equipped_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        server_default=text("CURRENT_TIMESTAMP"),
    )

    player: Mapped["Player"] = relationship("Player", back_populates="inventory_record")


class PlayerExploration(Base):
    """
    Junction table tracking which rooms each player has explored.
    """

    __tablename__ = "player_exploration"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True, server_default=text("gen_random_uuid()"))
    player_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("players.player_id", ondelete="CASCADE"), nullable=False
    )
    room_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False
    )
    explored_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text("now()"))

    player: Mapped["Player"] = relationship("Player", back_populates="exploration_records")


# Event listener to handle legacy string stats in database
# Converts JSON strings to dicts before MutableDict coercion
# As documented in "Legacy Data Migration Patterns" - Dr. Armitage, 1931
@event.listens_for(Player, "load")
def _convert_legacy_stats_string(target: Player, _context: Any) -> None:
    """
    Convert legacy string stats to dict during SQLAlchemy load event.

    This handles legacy data where stats were stored as JSON strings
    instead of JSONB dicts. The conversion happens before MutableDict
    tries to coerce the value, preventing ValueError exceptions.

    Args:
        target: The Player instance being loaded
        _context: SQLAlchemy query context (unused but required by event signature)
    """
    if isinstance(target.stats, str):  # type: ignore[unreachable]  # Reason: isinstance check ensures str branch for backward compatibility, but mypy infers dict type from column definition and marks this branch as unreachable
        try:  # type: ignore[unreachable]  # Reason: try block is reachable at runtime when stats is str, but mypy infers dict type and marks this as unreachable
            # Parse JSON string to dict
            # MutableDict will automatically wrap this dict
            target.stats = json.loads(target.stats)
        except (json.JSONDecodeError, TypeError):
            # If parsing fails, use default stats
            target.stats = {
                "strength": 50,
                "dexterity": 50,
                "constitution": 50,
                "intelligence": 50,
                "wisdom": 50,
                "charisma": 50,
                "lucidity": 100,
                "occult_knowledge": 0,
                "fear": 0,
                "corruption": 0,
                "cult_affiliation": 0,
                "current_dp": 100,
                "position": "standing",
            }
