"""
Player repository for async persistence operations.

This module provides async database operations for player CRUD, queries,
and inventory management using SQLAlchemy ORM with PostgreSQL.
"""

# pylint: disable=too-few-public-methods,too-many-lines  # Reason: Repository class with focused responsibility, minimal public interface. Player repository requires extensive database operations for comprehensive player persistence.

import json
import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, cast

from sqlalchemy import func, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player import Player, PlayerInventory
from server.schemas.inventory_schema import InventorySchemaValidationError, validate_inventory_payload
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import create_error_context, log_and_raise
from server.utils.retry import retry_with_backoff

if TYPE_CHECKING:
    from server.events import EventBus
    from server.models.room import Room

logger = get_logger(__name__)


class InventoryPayload:
    """Type hint for inventory payload structure."""

    inventory: list[dict[str, Any]]
    equipped: dict[str, Any]
    version: int


class PlayerRepository:
    """
    Repository for player persistence operations.

    Handles all player-related database operations including CRUD,
    batch operations, inventory management, and room validation.
    Uses async SQLAlchemy ORM for non-blocking database access.
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

    def validate_and_fix_player_room(self, player: Player) -> bool:
        """
        Validate player's current room and fix if invalid.

        Args:
            player: Player to validate

        Returns:
            bool: True if room was fixed, False if valid

        Note: This is synchronous as it only accesses the in-memory cache
        """
        if player.current_room_id not in self._room_cache:
            self._logger.warning(
                "Player in invalid room, moving to Arkham Square",
                player_id=player.player_id,
                player_name=player.name,
                invalid_room_id=player.current_room_id,
            )
            player.current_room_id = "arkham_square"
            return True
        return False

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
        context = create_error_context()
        context.metadata["operation"] = "get_player_by_name"
        context.metadata["player_name"] = name

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # Use case-insensitive comparison and exclude deleted characters
                stmt = (
                    select(Player)
                    .options(selectinload(Player.inventory_record))
                    .where(func.lower(Player.name) == func.lower(name))
                    .where(Player.is_deleted.is_(False))  # Use is_() for SQLAlchemy boolean comparison
                )
                result = await session.execute(stmt)
                player = result.scalar_one_or_none()
                if player:
                    self.validate_and_fix_player_room(player)
                    result_player: Player | None = cast(Player | None, player)
                    return result_player
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by name '{name}': {e}",
                context=context,
                details={"player_name": name, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )
        return None

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
        context = create_error_context()
        context.metadata["operation"] = "get_player_by_id"
        context.metadata["player_id"] = player_id

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # SQLAlchemy's UUID type (even with as_uuid=False) handles UUID object comparisons automatically.
                # The database column is UUID type, and SQLAlchemy converts UUID objects appropriately for comparison.
                # The as_uuid=False parameter only affects the Python return type (string vs UUID), not comparison behavior.
                stmt = (
                    select(Player).options(selectinload(Player.inventory_record)).where(Player.player_id == player_id)
                )
                result = await session.execute(stmt)
                player = result.scalar_one_or_none()
                if player:
                    self.validate_and_fix_player_room(player)
                    result_player: Player | None = cast(Player | None, player)
                    return result_player
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by ID '{player_id}': {e}",
                context=context,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )
        return None

    async def get_players_by_user_id(self, user_id: str) -> list[Player]:
        """
        Get all players (including deleted) for a user ID.

        MULTI-CHARACTER: Returns list of all characters for a user, including soft-deleted ones.
        Use get_active_players_by_user_id() to get only active characters.

        Args:
            user_id: User ID

        Returns:
            list[Player]: List of player objects (may be empty)

        Raises:
            DatabaseError: If database operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "get_players_by_user_id"
        context.metadata["user_id"] = user_id

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(Player).where(Player.user_id == user_id)
                result = await session.execute(stmt)
                players = list(result.scalars().all())
                # Validate and fix room for each player
                for player in players:
                    self.validate_and_fix_player_room(player)
                return players
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving players by user ID '{user_id}': {e}",
                context=context,
                details={"user_id": user_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    async def get_active_players_by_user_id(self, user_id: str) -> list[Player]:
        """
        Get active (non-deleted) players for a user ID.

        MULTI-CHARACTER: Returns only active characters, excluding soft-deleted ones.

        Args:
            user_id: User ID

        Returns:
            list[Player]: List of active player objects (may be empty)

        Raises:
            DatabaseError: If database operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "get_active_players_by_user_id"
        context.metadata["user_id"] = user_id

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = (
                    select(Player)
                    .where(Player.user_id == user_id)
                    .where(Player.is_deleted.is_(False))  # Use is_() for SQLAlchemy boolean comparison
                )
                result = await session.execute(stmt)
                players = list(result.scalars().all())
                # Validate and fix room for each player
                for player in players:
                    self.validate_and_fix_player_room(player)
                return players
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving active players by user ID '{user_id}': {e}",
                context=context,
                details={"user_id": user_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    # Backward compatibility alias
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
        context = create_error_context()
        context.metadata["operation"] = "save_player"
        context.metadata["player_name"] = player.name
        context.metadata["player_id"] = player.player_id

        try:
            # Ensure is_admin is an integer (PostgreSQL requires integer, not boolean)
            if isinstance(getattr(player, "is_admin", None), bool):
                player.is_admin = 1 if player.is_admin else 0

            inventory_json, equipped_json = self._prepare_inventory_payload(player)
            record = getattr(player, "inventory_record", None)
            if record is None:
                record = PlayerInventory(
                    player_id=str(player.player_id),
                    inventory_json=inventory_json,
                    equipped_json=equipped_json,
                )
                player.inventory_record = record
            else:
                record.inventory_json = inventory_json
                record.equipped_json = equipped_json

            session_maker = get_session_maker()
            async with session_maker() as session:
                # Use merge() for upsert behavior - inserts if new, updates if exists
                await session.merge(player)
                await session.commit()
                self._logger.debug("Player saved successfully", player_id=player.player_id)
                return
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving player: {e}",
                context=context,
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
        context = create_error_context()
        context.metadata["operation"] = "list_players"

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(Player)
                result = await session.execute(stmt)
                players = list(result.scalars().all())
                # Validate and fix room for each player
                for player in players:
                    self.validate_and_fix_player_room(player)
                return players
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing players: {e}",
                context=context,
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
        context = create_error_context()
        context.metadata["operation"] = "get_players_in_room"
        context.metadata["room_id"] = room_id

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(Player).where(Player.current_room_id == room_id)
                result = await session.execute(stmt)
                players = list(result.scalars().all())
                # Validate and fix room for each player
                for player in players:
                    self.validate_and_fix_player_room(player)
                return players
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error getting players in room: {e}",
                context=context,
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
        context = create_error_context()
        context.metadata["operation"] = "save_players"
        context.metadata["player_count"] = len(players)

        try:
            # Ensure is_admin is an integer for all players
            for player in players:
                if isinstance(getattr(player, "is_admin", None), bool):
                    player.is_admin = 1 if player.is_admin else 0

            session_maker = get_session_maker()
            async with session_maker() as session:
                for player in players:
                    await session.merge(player)
                await session.commit()
                self._logger.debug("Batch saved players", player_count=len(players))
                return
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving players: {e}",
                context=context,
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
        context = create_error_context()
        context.metadata["operation"] = "soft_delete_player"
        context.metadata["player_id"] = player_id

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # Check if player exists
                stmt = select(Player).where(Player.player_id == player_id)
                result = await session.execute(stmt)
                player = result.scalar_one_or_none()

                if not player:
                    self._logger.debug("Soft delete attempted for non-existent player", player_id=player_id)
                    return False

                # Soft delete the player
                player.is_deleted = True
                player.deleted_at = datetime.now(UTC).replace(tzinfo=None)
                await session.commit()
                self._logger.info("Player soft-deleted successfully", player_id=player_id)

                return True
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error soft-deleting player {player_id}: {e}",
                context=context,
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
        context = create_error_context()
        context.metadata["operation"] = "delete_player"
        context.metadata["player_id"] = player_id

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # Check if player exists
                stmt = select(Player).where(Player.player_id == player_id)
                result = await session.execute(stmt)
                player = result.scalar_one_or_none()

                if not player:
                    self._logger.debug("Delete attempted for non-existent player", player_id=player_id)
                    return False

                # Delete the player
                await session.delete(player)
                await session.commit()
                self._logger.info("Player deleted successfully", player_id=player_id)

                # Note: Player deletion events are not currently published
                # If needed in the future, create a PlayerDeletedEvent and publish it here
                # if self._event_bus:
                #     from server.events.event_types import PlayerDeletedEvent
                #     event = PlayerDeletedEvent(player_id=player_id)
                #     self._event_bus.publish(event)

                return True
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error deleting player {player_id}: {e}",
                context=context,
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
        context = create_error_context()
        context.metadata["operation"] = "update_player_last_active"
        context.metadata["player_id"] = player_id

        try:
            if last_active is None:
                last_active = datetime.now(UTC)

            # Ensure timezone-aware timestamp in UTC, then convert to naive for database
            if last_active.tzinfo is None:
                last_active = last_active.replace(tzinfo=UTC)
            else:
                # Convert to UTC if it has a different timezone
                last_active = last_active.astimezone(UTC)

            # Convert to naive UTC datetime for TIMESTAMP WITHOUT TIME ZONE column
            # This matches the pattern used in the Player model's default value
            last_active_naive = last_active.replace(tzinfo=None)

            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = update(Player).where(Player.player_id == player_id).values(last_active=last_active_naive)
                await session.execute(stmt)
                await session.commit()
                self._logger.debug("Updated player last_active", player_id=player_id, last_active=last_active_naive)
                return
        except (DatabaseError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating last_active for player '{player_id}': {e}",
                context=context,
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
        context = create_error_context()
        context.metadata["operation"] = "get_players_batch"
        context.metadata["player_count"] = len(player_ids)

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(Player).where(Player.player_id.in_(player_ids))
                result = await session.execute(stmt)
                players = list(result.scalars().all())

                # Validate and fix room for each player
                for player in players:
                    self.validate_and_fix_player_room(player)

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
                context=context,
                details={"player_count": len(player_ids), "error": str(e)},
                user_friendly="Failed to retrieve players",
            )

    def _prepare_inventory_payload(self, player: Player) -> tuple[str, str]:
        """
        Validate and serialize inventory payload for storage.

        Args:
            player: Player with inventory to prepare

        Returns:
            tuple[str, str]: JSON strings for (inventory, equipped)

        Raises:
            InventorySchemaValidationError: If validation fails
        """
        inventory_raw: Any = player.get_inventory()
        if isinstance(inventory_raw, str):
            try:
                inventory_raw = json.loads(inventory_raw)
            except (TypeError, json.JSONDecodeError) as exc:
                raise InventorySchemaValidationError(f"Invalid inventory JSON: {exc}") from exc

        if not isinstance(inventory_raw, list):
            raise InventorySchemaValidationError("Inventory payload must be an array of stacks")

        equipped_raw: Any = player.get_equipped_items() or {}
        if isinstance(equipped_raw, str):
            try:
                equipped_raw = json.loads(equipped_raw)
            except (TypeError, json.JSONDecodeError) as exc:
                raise InventorySchemaValidationError(f"Invalid equipped JSON: {exc}") from exc

        if not isinstance(equipped_raw, dict):
            raise InventorySchemaValidationError("Equipped payload must be an object")

        payload_dict: dict[str, Any] = {
            "inventory": cast(list[dict[str, Any]], inventory_raw),
            "equipped": cast(dict[str, Any], equipped_raw),
            "version": 1,
        }
        validate_inventory_payload(payload_dict)

        inventory_json = json.dumps(payload_dict["inventory"])
        equipped_json = json.dumps(payload_dict["equipped"])

        # Log what's being saved to help debug inventory persistence issues
        logger.debug(
            "Preparing inventory payload for save",
            player_id=str(player.player_id),
            player_name=player.name,
            inventory_length=len(payload_dict["inventory"]),
            inventory_items=[
                {
                    "item_name": item.get("item_name"),
                    "item_id": item.get("item_id"),
                    "slot_type": item.get("slot_type"),
                    "quantity": item.get("quantity"),
                }
                for item in payload_dict["inventory"][:5]
            ],  # Log first 5 items
        )

        player.inventory = cast(Any, inventory_json)  # keep ORM column in sync
        player.set_equipped_items(payload_dict["equipped"])
        return inventory_json, equipped_json
