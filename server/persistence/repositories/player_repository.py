"""
Player repository for async persistence operations.

This module provides async database operations for player CRUD, queries,
and inventory management using PostgreSQL stored procedures.
"""

# pylint: disable=too-few-public-methods  # Reason: Repository class with focused responsibility, minimal public interface.

import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player import Player
from server.persistence.repositories.player_repository_mappers import row_to_player
from server.persistence.repositories.player_repository_room import (
    validate_and_fix_player_room,
    validate_and_fix_player_room_with_persistence,
)
from server.persistence.repositories.player_repository_save import PlayerSavePreparer
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise
from server.utils.retry import retry_with_backoff

if TYPE_CHECKING:
    from server.events import EventBus
    from server.models.room import Room


class PlayerRepository:
    """
    Repository for player persistence operations.

    Handles all player-related database operations including CRUD,
    batch operations, inventory management, and room validation.
    Uses PostgreSQL stored procedures for database access.
    """

    def __init__(self, room_cache: dict[str, "Room"] | None = None, event_bus: "EventBus | None" = None) -> None:
        """
        Initialize the player repository.

        Args:
            room_cache: Shared room cache for room validation (must not be None)
            event_bus: Optional EventBus for publishing player events
        """
        if room_cache is None:
            raise ValueError("room_cache must not be None - PlayerRepository requires a shared cache reference")
        self._room_cache = room_cache  # Preserve reference - do not create new dict
        self._event_bus = event_bus
        self._logger = get_logger(__name__)
        self._save_preparer = PlayerSavePreparer(self._logger)

    def validate_and_fix_player_room(self, player: Player) -> bool:
        """
        Validate player's current room and fix if invalid.

        Args:
            player: Player to validate

        Returns:
            bool: True if room was fixed, False if valid

        Note: Synchronous; uses in-memory cache. Skips when cache empty, instanced rooms,
        or tutorial bedroom. See player_repository_room module for implementation.
        """
        return validate_and_fix_player_room(self._room_cache, player, self._logger)

    async def _validate_and_fix_player_room_with_persistence(self, player: Player, session: Any) -> bool:
        """Validate and fix player room, persisting the fix if needed."""
        return await validate_and_fix_player_room_with_persistence(self._room_cache, player, session, self._logger)

    @retry_with_backoff(max_attempts=3, initial_delay=1.0, max_delay=10.0)
    async def get_player_by_name(self, name: str) -> Player | None:
        """
        Get an active player by name (case-insensitive, excludes deleted characters).

        MULTI-CHARACTER: Updated to use case-insensitive comparison and exclude soft-deleted characters.
        Character names are stored case-sensitively but checked case-insensitively for uniqueness.

        Args:
            name: Player name (case-insensitive matching)

        Returns:
            Player | None: Player object or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        "SELECT "
                        "player_id, user_id, name, inventory, status_effects, current_room_id, "
                        "respawn_room_id, experience_points, level, is_admin, profession_id, "
                        "created_at, last_active, stats, is_deleted, deleted_at, "
                        "tutorial_instance_id, inventory_json, equipped_json "
                        "FROM get_player_by_name(:name)"
                    ),
                    {"name": name},
                )
                rows = result.fetchall()
                if not rows:
                    return None
                player = row_to_player(rows[0])
                await self._validate_and_fix_player_room_with_persistence(player, session)
                return player
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by name '{name}': {e}",
                operation="get_player_by_name",
                player_name=name,
                details={"player_name": name, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    @retry_with_backoff(max_attempts=3, initial_delay=1.0, max_delay=10.0)
    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        """
        Get a player by ID.

        Args:
            player_id: Player UUID

        Returns:
            Player | None: Player object or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        "SELECT "
                        "player_id, user_id, name, inventory, status_effects, current_room_id, "
                        "respawn_room_id, experience_points, level, is_admin, profession_id, "
                        "created_at, last_active, stats, is_deleted, deleted_at, "
                        "tutorial_instance_id, inventory_json, equipped_json "
                        "FROM get_player_by_id(:id)"
                    ),
                    {"id": str(player_id)},
                )
                rows = result.fetchall()
                if not rows:
                    return None
                player = row_to_player(rows[0])
                await self._validate_and_fix_player_room_with_persistence(player, session)
                return player
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by ID '{player_id}': {e}",
                operation="get_player_by_id",
                player_id=player_id,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    async def get_players_by_user_id(self, user_id: str) -> list[Player]:
        """
        Get all players (including deleted) for a user ID.

        MULTI-CHARACTER: Returns list of all characters for a user, including soft-deleted ones.
        Use get_active_players_by_user_id() to get only active characters.

        Eager-loads inventory_record to avoid N+1 when callers access player inventory.

        Args:
            user_id: User ID

        Returns:
            list[Player]: List of player objects (may be empty)

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        "SELECT "
                        "player_id, user_id, name, inventory, status_effects, current_room_id, "
                        "respawn_room_id, experience_points, level, is_admin, profession_id, "
                        "created_at, last_active, stats, is_deleted, deleted_at, "
                        "tutorial_instance_id, inventory_json, equipped_json "
                        "FROM get_players_by_user_id(:user_id)"
                    ),
                    {"user_id": str(user_id)},
                )
                rows = result.fetchall()
                players = [row_to_player(r) for r in rows]
                for player in players:
                    await self._validate_and_fix_player_room_with_persistence(player, session)
                return players
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving players by user ID '{user_id}': {e}",
                operation="get_players_by_user_id",
                user_id=user_id,
                details={"user_id": user_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    async def get_active_players_by_user_id(self, user_id: str) -> list[Player]:
        """
        Get active (non-deleted) players for a user ID.

        MULTI-CHARACTER: Returns only active characters, excluding soft-deleted ones.

        Eager-loads inventory_record to avoid N+1 when callers access player inventory.

        Args:
            user_id: User ID

        Returns:
            list[Player]: List of active player objects (may be empty)

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        "SELECT "
                        "player_id, user_id, name, inventory, status_effects, current_room_id, "
                        "respawn_room_id, experience_points, level, is_admin, profession_id, "
                        "created_at, last_active, stats, is_deleted, deleted_at, "
                        "tutorial_instance_id, inventory_json, equipped_json "
                        "FROM get_active_players_by_user_id(:user_id)"
                    ),
                    {"user_id": str(user_id)},
                )
                rows = result.fetchall()
                players = [row_to_player(r) for r in rows]
                for player in players:
                    await self._validate_and_fix_player_room_with_persistence(player, session)
                return players
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving active players by user ID '{user_id}': {e}",
                operation="get_active_players_by_user_id",
                user_id=user_id,
                details={"user_id": user_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    async def get_player_by_user_id(self, user_id: str) -> Player | None:
        """
        Get the first active player by user ID (backward compatibility).

        MULTI-CHARACTER: This method is kept for backward compatibility.
        New code should use get_active_players_by_user_id() to get all characters.

        Args:
            user_id: User ID

        Returns:
            Player | None: First active player object or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        players = await self.get_active_players_by_user_id(user_id)
        return players[0] if players else None

    @retry_with_backoff(max_attempts=3, initial_delay=1.0, max_delay=10.0)
    async def save_player(self, player: Player) -> None:
        """
        Save or update a player.

        Args:
            player: Player to save

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            params = self._save_preparer.prepare(player)
            session_maker = get_session_maker()
            async with session_maker() as session:
                await self._save_preparer.execute(session, params)
                await session.commit()
                self._logger.debug("Player saved successfully", player_id=player.player_id)
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving player: {e}",
                operation="save_player",
                player_name=player.name,
                player_id=player.player_id,
                details={"player_name": player.name, "player_id": player.player_id, "error": str(e)},
                user_friendly="Failed to save player",
            )

    async def list_players(self) -> list[Player]:
        """
        List all players.

        Returns:
            list[Player]: List of all players

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        "SELECT "
                        "player_id, user_id, name, inventory, status_effects, current_room_id, "
                        "respawn_room_id, experience_points, level, is_admin, profession_id, "
                        "created_at, last_active, stats, is_deleted, deleted_at, "
                        "tutorial_instance_id, inventory_json, equipped_json "
                        "FROM list_players()"
                    )
                )
                rows = result.fetchall()
                players = [row_to_player(r) for r in rows]
                for player in players:
                    await self._validate_and_fix_player_room_with_persistence(player, session)
                return players
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing players: {e}",
                operation="list_players",
                details={"error": str(e)},
                user_friendly="Failed to retrieve player list",
            )

    async def get_players_in_room(self, room_id: str) -> list[Player]:
        """
        Get all players in a specific room.

        Args:
            room_id: Room identifier

        Returns:
            list[Player]: List of players in the room

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        "SELECT "
                        "player_id, user_id, name, inventory, status_effects, current_room_id, "
                        "respawn_room_id, experience_points, level, is_admin, profession_id, "
                        "created_at, last_active, stats, is_deleted, deleted_at, "
                        "tutorial_instance_id, inventory_json, equipped_json "
                        "FROM get_players_in_room(:room_id)"
                    ),
                    {"room_id": room_id},
                )
                rows = result.fetchall()
                players = [row_to_player(r) for r in rows]
                for player in players:
                    await self._validate_and_fix_player_room_with_persistence(player, session)
                return players
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error getting players in room: {e}",
                operation="get_players_in_room",
                room_id=room_id,
                details={"room_id": room_id, "error": str(e)},
                user_friendly="Failed to retrieve players in room",
            )

    async def save_players(self, players: list[Player]) -> None:
        """
        Save multiple players in a single transaction.

        Args:
            players: List of players to save

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                for player in players:
                    params = self._save_preparer.prepare(player)
                    await self._save_preparer.execute(session, params)
                await session.commit()
                self._logger.debug("Batch saved players", player_count=len(players))
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving players: {e}",
                operation="save_players",
                player_count=len(players),
                details={"player_count": len(players), "error": str(e)},
                user_friendly="Failed to save players",
            )

    async def soft_delete_player(self, player_id: uuid.UUID) -> bool:
        """
        Soft delete a player (sets is_deleted=True, deleted_at=timestamp).

        MULTI-CHARACTER: Soft deletion allows character names to be reused while preserving data.

        Args:
            player_id: Player UUID

        Returns:
            bool: True if soft-deleted, False if not found

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT soft_delete_player(:id)"),
                    {"id": str(player_id)},
                )
                deleted = result.scalar()
                await session.commit()
                if deleted:
                    self._logger.info("Player soft-deleted successfully", player_id=player_id)
                else:
                    self._logger.debug("Soft delete attempted for non-existent player", player_id=player_id)
                return bool(deleted)
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error soft-deleting player {player_id}: {e}",
                operation="soft_delete_player",
                player_id=player_id,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to delete player",
            )

    async def delete_player(self, player_id: uuid.UUID) -> bool:
        """
        Delete a player from the database.

        Args:
            player_id: Player UUID

        Returns:
            bool: True if deleted, False if not found

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT delete_player(:id)"),
                    {"id": str(player_id)},
                )
                deleted = result.scalar()
                await session.commit()
                if deleted:
                    self._logger.info("Player deleted successfully", player_id=player_id)
                else:
                    self._logger.debug("Delete attempted for non-existent player", player_id=player_id)
                return bool(deleted)
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error deleting player {player_id}: {e}",
                operation="delete_player",
                player_id=player_id,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to delete player",
            )

    async def update_player_last_active(self, player_id: uuid.UUID, last_active: datetime | None = None) -> None:
        """
        Update the last_active timestamp for a player.

        Args:
            player_id: Player UUID
            last_active: Timestamp to set (defaults to current UTC time)

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            if last_active is None:
                last_active = datetime.now(UTC)
            if last_active.tzinfo is None:
                last_active = last_active.replace(tzinfo=UTC)
            else:
                last_active = last_active.astimezone(UTC)

            session_maker = get_session_maker()
            async with session_maker() as session:
                await session.execute(
                    text("SELECT update_player_last_active(:id, :ts)"),
                    {"id": str(player_id), "ts": last_active},
                )
                await session.commit()
                self._logger.debug("Updated player last_active", player_id=player_id, last_active=last_active)
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating last_active for player '{player_id}': {e}",
                operation="update_player_last_active",
                player_id=player_id,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to update player activity",
            )

    async def get_players_batch(self, player_ids: list[uuid.UUID]) -> list[Player]:
        """
        Get multiple players by IDs in a single query.

        Args:
            player_ids: List of player UUIDs

        Returns:
            list[Player]: List of players found (may be fewer than requested)

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            if not player_ids:
                return []
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        "SELECT "
                        "player_id, user_id, name, inventory, status_effects, current_room_id, "
                        "respawn_room_id, experience_points, level, is_admin, profession_id, "
                        "created_at, last_active, stats, is_deleted, deleted_at, "
                        "tutorial_instance_id, inventory_json, equipped_json "
                        "FROM get_players_batch(:ids)"
                    ),
                    {"ids": [str(pid) for pid in player_ids]},
                )
                rows = result.fetchall()
                players = [row_to_player(r) for r in rows]
                for player in players:
                    await self._validate_and_fix_player_room_with_persistence(player, session)
                self._logger.debug(
                    "Batch loaded players",
                    requested_count=len(player_ids),
                    loaded_count=len(players),
                )
                return players
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error batch loading players: {e}",
                operation="get_players_batch",
                player_count=len(player_ids),
                details={"player_count": len(player_ids), "error": str(e)},
                user_friendly="Failed to retrieve players",
            )
