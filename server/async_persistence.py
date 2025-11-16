"""
Async persistence layer for MythosMUD.

This module provides an async version of the persistence layer using asyncpg
for true async PostgreSQL database operations without blocking the event loop.
"""

import json
import os
from typing import Any

import asyncpg

from .exceptions import DatabaseError, ValidationError
from .logging.enhanced_logging_config import get_logger
from .models.player import Player
from .models.profession import Profession
from .utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class AsyncPersistenceLayer:
    """
    Async persistence layer using asyncpg for true async PostgreSQL operations.

    This provides async database operations that don't block the event loop.
    """

    def __init__(self, db_path: str | None = None, log_path: str | None = None, event_bus=None):
        """Initialize the async persistence layer."""
        if db_path:
            self.db_path = db_path
        elif os.environ.get("DATABASE_URL"):
            from .database import get_database_path

            self.db_path = str(get_database_path())
        else:
            context = create_error_context()
            context.metadata["operation"] = "async_persistence_init"
            log_and_raise(
                ValidationError,
                "DATABASE_URL environment variable must be set",
                context=context,
                details={"config_file": "server/env.example"},
                user_friendly="Database configuration is missing",
            )

        self.log_path = log_path
        self._event_bus = event_bus
        self._logger = get_logger(__name__)
        # PostgreSQL-only: Verify we have a PostgreSQL URL
        if self.db_path and not self.db_path.startswith("postgresql"):
            context = create_error_context()
            context.metadata["operation"] = "async_persistence_init"
            log_and_raise(
                ValidationError,
                f"Unsupported database URL: {self.db_path}. Only PostgreSQL is supported.",
                context=context,
                user_friendly="Database configuration error - PostgreSQL required",
            )
        self._load_room_cache()

    def _load_room_cache(self) -> None:
        """Load room cache using environment-aware world loader."""
        try:
            # Prefer the unified world loader which respects LOGGING_ENVIRONMENT
            from .world_loader import ROOMS_BASE_PATH, load_hierarchical_world

            world_data = load_hierarchical_world()
            rooms = world_data.get("rooms", {})

            # Store raw room dicts keyed by id for quick existence checks
            self._room_cache = dict(rooms)

            self._logger.info(
                "Room cache loaded",
                room_count=len(self._room_cache),
                rooms_base_path=str(ROOMS_BASE_PATH),
            )
        except (OSError, json.JSONDecodeError) as e:
            self._logger.error("Error loading room cache", error=str(e), error_type=type(e).__name__)
            self._room_cache = {}
        except Exception as e:
            # Fallback to empty cache on unexpected errors to avoid startup failure
            self._logger.error("Unexpected error loading room cache", error=str(e))
            self._room_cache = {}

    async def get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_player_by_name"
        context.metadata["player_name"] = name

        try:
            # PostgreSQL connection
            # Parse URL: postgresql+asyncpg://user:pass@host:port/db
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            row_dict = None
            try:
                row = await conn.fetchrow("SELECT * FROM players WHERE name = $1", name)
                if row:
                    row_dict = dict(row)
            finally:
                await conn.close()
            if row_dict:
                player_data = self._convert_row_to_player_data(row_dict)
                player = Player(**player_data)
                self.validate_and_fix_player_room(player)
                return player
            return None

        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by name '{name}': {e}",
                context=context,
                details={"player_name": name, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    async def get_player_by_id(self, player_id: str) -> Player | None:
        """Get a player by ID using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_player_by_id"
        player_id = str(player_id)
        context.metadata["player_id"] = player_id

        try:
            # PostgreSQL connection
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            try:
                # asyncpg uses $1, $2, etc. for parameters
                row = await conn.fetchrow("SELECT * FROM players WHERE player_id = $1", player_id)
                if row:
                    row_dict = dict(row)
                    player_data = self._convert_row_to_player_data(row_dict)
                    player = Player(**player_data)
                    self.validate_and_fix_player_room(player)
                    return player
                return None
            finally:
                await conn.close()

        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by ID '{player_id}': {e}",
                context=context,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    async def get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get a player by user ID using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_player_by_user_id"
        context.metadata["user_id"] = user_id

        try:
            # PostgreSQL connection
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            try:
                # asyncpg uses $1, $2, etc. for parameters
                row = await conn.fetchrow("SELECT * FROM players WHERE user_id = $1", user_id)
                if row:
                    row_dict = dict(row)
                    player_data = self._convert_row_to_player_data(row_dict)
                    player = Player(**player_data)
                    self.validate_and_fix_player_room(player)
                    return player
                return None
            finally:
                await conn.close()

        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by user ID '{user_id}': {e}",
                context=context,
                details={"user_id": user_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    async def save_player(self, player: Player) -> None:
        """Save a player using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_save_player"
        context.metadata["player_name"] = player.name
        context.metadata["player_id"] = str(player.player_id)

        try:
            # PostgreSQL connection
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            try:
                # Convert player to database format
                player_data = self._convert_player_to_db_data(player)

                # Use INSERT ... ON CONFLICT for upsert behavior (PostgreSQL)
                await conn.execute(
                    """INSERT INTO players
                        (player_id, user_id, name, current_room_id, profession_id,
                         experience_points, level, stats, inventory, status_effects,
                         created_at, last_active, is_admin)
                        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)
                        ON CONFLICT (player_id) DO UPDATE SET
                        user_id = EXCLUDED.user_id,
                        name = EXCLUDED.name,
                        current_room_id = EXCLUDED.current_room_id,
                        profession_id = EXCLUDED.profession_id,
                        experience_points = EXCLUDED.experience_points,
                        level = EXCLUDED.level,
                        stats = EXCLUDED.stats,
                        inventory = EXCLUDED.inventory,
                        status_effects = EXCLUDED.status_effects,
                        created_at = EXCLUDED.created_at,
                        last_active = EXCLUDED.last_active,
                        is_admin = EXCLUDED.is_admin""",
                    str(player_data["player_id"]),
                    str(player_data["user_id"]),
                    player_data["name"],
                    player_data["current_room_id"],
                    player_data["profession_id"],
                    player_data["experience_points"],
                    player_data["level"],
                    json.dumps(player_data["stats"]),
                    json.dumps(player_data["inventory"]),
                    json.dumps(player_data["status_effects"]),
                    player_data["created_at"],
                    player_data["last_active"],
                    player_data["is_admin"],
                )

                self._logger.debug("Player saved successfully", player_id=str(player.player_id))
            finally:
                await conn.close()

        except asyncpg.IntegrityConstraintViolationError as e:
            log_and_raise(
                DatabaseError,
                f"Unique constraint error saving player: {e}",
                context=context,
                details={"player_name": player.name, "player_id": str(player.player_id), "error": str(e)},
                user_friendly="Player name already exists",
            )
        except asyncpg.PostgresError as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving player: {e}",
                context=context,
                details={"player_name": player.name, "player_id": str(player.player_id), "error": str(e)},
                user_friendly="Failed to save player",
            )
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Unexpected error saving player: {e}",
                context=context,
                details={"player_name": player.name, "player_id": str(player.player_id), "error": str(e)},
                user_friendly="Failed to save player",
            )

    async def list_players(self) -> list[Player]:
        """List all players using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_list_players"

        try:
            # PostgreSQL connection
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            try:
                rows = await conn.fetch("SELECT * FROM players")

                players = []
                for row in rows:
                    try:
                        row_dict = dict(row)
                        player_data = self._convert_row_to_player_data(row_dict)
                        player = Player(**player_data)
                        self.validate_and_fix_player_room(player)
                        players.append(player)
                    except (ValueError, TypeError, KeyError) as e:
                        self._logger.warning(
                            "Error converting player data",
                            error=str(e),
                            error_type=type(e).__name__,
                            row_id=dict(row).get("player_id") if row else None,
                        )
                        continue

                return players
            finally:
                await conn.close()

        except asyncpg.PostgresError as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing players: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve player list",
            )

    async def get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players in a specific room using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_players_in_room"
        context.metadata["room_id"] = room_id

        try:
            # PostgreSQL connection
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            try:
                rows = await conn.fetch("SELECT * FROM players WHERE current_room_id = $1", room_id)

                players = []
                for row in rows:
                    try:
                        row_dict = dict(row)
                        player_data = self._convert_row_to_player_data(row_dict)
                        player = Player(**player_data)
                        self.validate_and_fix_player_room(player)
                        players.append(player)
                    except (ValueError, TypeError, KeyError) as e:
                        self._logger.warning(
                            "Error converting player data",
                            error=str(e),
                            error_type=type(e).__name__,
                            row_id=dict(row).get("player_id") if row else None,
                        )
                        continue

                return players
            finally:
                await conn.close()

        except asyncpg.PostgresError as e:
            log_and_raise(
                DatabaseError,
                f"Database error getting players in room: {e}",
                context=context,
                details={"room_id": room_id, "error": str(e)},
                user_friendly="Failed to retrieve players in room",
            )

    async def save_players(self, players: list[Player]) -> None:
        """Save multiple players using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_save_players"
        context.metadata["player_count"] = len(players)

        try:
            # PostgreSQL connection
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            try:
                for player in players:
                    try:
                        player_data = self._convert_player_to_db_data(player)

                        # Use INSERT ... ON CONFLICT for upsert behavior (PostgreSQL)
                        await conn.execute(
                            """INSERT INTO players
                        (player_id, user_id, name, current_room_id, profession_id,
                         experience_points, level, stats, inventory, status_effects,
                         created_at, last_active, is_admin)
                        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)
                        ON CONFLICT (player_id) DO UPDATE SET
                        user_id = EXCLUDED.user_id,
                        name = EXCLUDED.name,
                        current_room_id = EXCLUDED.current_room_id,
                        profession_id = EXCLUDED.profession_id,
                        experience_points = EXCLUDED.experience_points,
                        level = EXCLUDED.level,
                        stats = EXCLUDED.stats,
                        inventory = EXCLUDED.inventory,
                        status_effects = EXCLUDED.status_effects,
                        created_at = EXCLUDED.created_at,
                        last_active = EXCLUDED.last_active,
                        is_admin = EXCLUDED.is_admin""",
                            str(player_data["player_id"]),
                            str(player_data["user_id"]),
                            player_data["name"],
                            player_data["current_room_id"],
                            player_data["profession_id"],
                            player_data["experience_points"],
                            player_data["level"],
                            json.dumps(player_data["stats"]),
                            json.dumps(player_data["inventory"]),
                            json.dumps(player_data["status_effects"]),
                            player_data["created_at"],
                            player_data["last_active"],
                            player_data["is_admin"],
                        )
                    except (ValueError, TypeError, KeyError) as e:
                        self._logger.warning(
                            "Error saving player",
                            error=str(e),
                            error_type=type(e).__name__,
                            player_id=str(player.player_id),
                        )
                        continue

                self._logger.debug("Players saved successfully", player_count=len(players))
            finally:
                await conn.close()

        except asyncpg.PostgresError as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving players: {e}",
                context=context,
                details={"player_count": len(players), "error": str(e)},
                user_friendly="Failed to save players",
            )

    async def delete_player(self, player_id: str) -> bool:
        """Delete a player using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_delete_player"
        context.metadata["player_id"] = player_id

        try:
            # PostgreSQL connection
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            try:
                # First check if player exists
                row = await conn.fetchrow("SELECT name FROM players WHERE player_id = $1", player_id)

                if not row:
                    self._logger.warning("Player not found for deletion", player_id=player_id)
                    return False

                player_name = row["name"]

                # Delete the player
                deleted_count = await conn.execute("DELETE FROM players WHERE player_id = $1", player_id)

                # asyncpg.execute returns status string like "DELETE 1", parse count
                deleted_int = int(deleted_count.split()[-1]) if deleted_count.split()[-1].isdigit() else 0

                if deleted_int > 0:
                    self._logger.info("Player deleted successfully", player_id=player_id, player_name=player_name)
                    return True
                else:
                    self._logger.warning("No player was deleted", player_id=player_id)
                    return False
            finally:
                await conn.close()

        except asyncpg.PostgresError as e:
            log_and_raise(
                DatabaseError,
                f"Database error deleting player: {e}",
                context=context,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to delete player",
            )

    async def get_professions(self) -> list[Profession]:
        """Get all available professions using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_professions"

        try:
            # PostgreSQL connection
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            try:
                rows = await conn.fetch("SELECT * FROM professions WHERE is_available = true ORDER BY id")

                professions = []
                for row in rows:
                    try:
                        row_dict = dict(row)
                        profession_data = self._convert_row_to_profession_data(row_dict)
                        profession = Profession(**profession_data)
                        professions.append(profession)
                    except (ValueError, TypeError, KeyError) as e:
                        self._logger.warning(
                            "Error converting profession data",
                            error=str(e),
                            error_type=type(e).__name__,
                            row_id=dict(row).get("id") if row else None,
                        )
                        continue

                return professions
            finally:
                await conn.close()

        except asyncpg.PostgresError as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving professions: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve professions",
            )

    async def get_profession_by_id(self, profession_id: int) -> Profession | None:
        """Get a profession by ID using async database operations."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_profession_by_id"
        context.metadata["profession_id"] = profession_id

        try:
            # PostgreSQL connection
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://").replace(
                "postgresql+psycopg2://", "postgresql://"
            )
            conn = await asyncpg.connect(url)
            try:
                row = await conn.fetchrow("SELECT * FROM professions WHERE id = $1", profession_id)

                if row:
                    row_dict = dict(row)
                    profession_data = self._convert_row_to_profession_data(row_dict)
                    profession = Profession(**profession_data)
                    return profession
                return None
            finally:
                await conn.close()

        except asyncpg.PostgresError as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving profession: {e}",
                context=context,
                details={"profession_id": profession_id, "error": str(e)},
                user_friendly="Failed to retrieve profession",
            )

    def _convert_row_to_player_data(self, row: dict[str, Any]) -> dict[str, Any]:
        """Convert a database row to player data dictionary.

        Accepts dict from PostgreSQL asyncpg (dict-like row objects).
        """
        # AI Agent: CRITICAL FIX - Do NOT pre-parse JSON fields!
        #           Player model expects stats/inventory/status_effects as JSON STRINGS,
        #           not dicts. The Player.get_stats() method handles parsing.
        #           Pre-parsing causes get_stats() to fail and return default values.
        return {
            "player_id": row["player_id"],
            "user_id": row["user_id"],
            "name": row["name"],
            "current_room_id": row["current_room_id"],
            "profession_id": row["profession_id"],
            "experience_points": row["experience_points"],
            "level": row["level"],
            "stats": row["stats"] or "{}",  # Keep as JSON string, not dict!
            "inventory": row["inventory"] or "[]",  # Keep as JSON string, not dict!
            "status_effects": row["status_effects"] or "[]",  # Keep as JSON string, not dict!
            "created_at": row["created_at"],
            "last_active": row["last_active"],
            "is_admin": bool(row["is_admin"]),
        }

    def _convert_player_to_db_data(self, player: Player) -> dict[str, Any]:
        """Convert a player object to database data dictionary."""
        return {
            "player_id": str(player.player_id),
            "user_id": str(player.user_id),
            "name": player.name,
            "current_room_id": player.current_room_id,
            "profession_id": player.profession_id,
            "experience_points": player.experience_points,
            "level": player.level,
            "stats": player.get_stats(),
            "inventory": player.get_inventory(),
            "status_effects": player.get_status_effects(),
            "created_at": player.created_at.isoformat()
            if hasattr(player.created_at, "isoformat")
            else str(player.created_at),
            "last_active": player.last_active.isoformat()
            if hasattr(player.last_active, "isoformat")
            else str(player.last_active),
            "is_admin": int(player.is_admin) if hasattr(player, "is_admin") and player.is_admin is not None else 0,
        }

    def _convert_row_to_profession_data(self, row: dict[str, Any]) -> dict[str, Any]:
        """Convert a database row to profession data dictionary.

        Accepts dict from PostgreSQL asyncpg (dict-like row objects).
        """
        return {
            "id": row["id"],
            "name": row["name"],
            "description": row["description"],
            "flavor_text": row["flavor_text"],
            "is_available": bool(row["is_available"]),
        }

    def validate_and_fix_player_room(self, player: Player) -> None:
        """Validate and fix player room if needed."""
        if not hasattr(player, "current_room_id") or not player.current_room_id:
            player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"  # type: ignore[assignment]
            self._logger.warning("Fixed player with missing room", player_id=str(player.player_id))

        # Check if room exists in cache
        if hasattr(self, "_room_cache") and player.current_room_id not in self._room_cache:
            self._logger.warning(
                "Player in unknown room", player_id=str(player.player_id), room_id=player.current_room_id
            )


# DEPRECATED: Module-level global singleton removed - use ApplicationContainer instead
# Keeping these functions for backward compatibility during migration
_async_persistence_instance: AsyncPersistenceLayer | None = None


def get_async_persistence() -> AsyncPersistenceLayer:
    """
    Get the global async persistence instance.

    DEPRECATED: Use ApplicationContainer.async_persistence instead.
    This function exists only for backward compatibility during migration.

    Returns:
        AsyncPersistenceLayer: The async persistence instance
    """
    global _async_persistence_instance
    if _async_persistence_instance is None:
        _async_persistence_instance = AsyncPersistenceLayer()
    return _async_persistence_instance


def reset_async_persistence() -> None:
    """
    Reset the global async persistence instance for testing.

    DEPRECATED: Use ApplicationContainer.reset_instance() instead.
    This function exists only for backward compatibility during migration.
    """
    global _async_persistence_instance
    _async_persistence_instance = None
