"""
Room occupancy operations for MovementService.

Placing, removing, and locating players in rooms outside a move between rooms: initial
placement, logout, teleport bookkeeping, and occupancy lookups. Split out of movement_service.py
(file size); MovementService inherits these methods unchanged.
"""

# pyright: reportUninitializedInstanceVariable=false
# Reason: mixin; MovementService.__init__ sets _persistence, _lock and _logger.
# pylint: disable=too-few-public-methods  # Reason: mixin; its public methods are counted on MovementService

from __future__ import annotations

import threading
import uuid
from typing import TYPE_CHECKING

from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from ..exceptions import DatabaseError, ValidationError
from ..utils.error_logging import log_and_raise

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer


class RoomOccupancyMixin:
    """Room occupancy API; the host (MovementService) provides _persistence, _lock and _logger."""

    _persistence: AsyncPersistenceLayer
    _lock: threading.RLock
    _logger: BoundLogger

    def _validate_add_player_ids(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """Validate player and room IDs for add_player_to_room."""
        if not player_id:
            log_and_raise(
                ValidationError,
                "Player ID cannot be empty",
                operation="add_player_to_room",
                details={"room_id": room_id},
                user_friendly="Player ID is required",
            )

        if not room_id:
            log_and_raise(
                ValidationError,
                "Room ID cannot be empty",
                player_id=player_id,
                operation="add_player_to_room",
                details={"player_id": player_id},
                user_friendly="Room ID is required",
            )

    async def _persist_added_player_room(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """Update player current_room_id in persistence after room add."""
        if isinstance(player_id, str):
            try:
                player_uuid = uuid.UUID(player_id)
            except ValueError, AttributeError:
                return
        else:
            player_uuid = player_id

        try:
            player = await self._persistence.get_player_by_id(player_uuid)
        except ValueError, AttributeError:
            return

        if not player:
            return

        setattr(player, "current_room_id", room_id)  # noqa: B010  # Reason: SQLAlchemy column descriptor
        await self._persistence.save_player(player)

    async def add_player_to_room(self, player_id: uuid.UUID | str, room_id: str) -> bool:
        """
        Add a player to a room (for initial placement, teleportation, etc.).

        Args:
            player_id: The ID of the player to add
            room_id: The ID of the room to add the player to

        Returns:
            True if the player was added successfully, False otherwise
        """
        self._validate_add_player_ids(player_id, room_id)

        with self._lock:
            try:
                room = self._persistence.get_room_by_id(room_id)
                if not room:
                    self._logger.error("Room not found", room_id=room_id)
                    return False

                if room.has_player(player_id):
                    self._logger.warning("Player already in room", player_id=player_id, room_id=room_id)
                    return True

                room.add_player_silently(player_id)
                await self._persist_added_player_room(player_id, room_id)

                self._logger.info("Added player to room", player_id=player_id, room_id=room_id)
                return True

            except (DatabaseError, SQLAlchemyError) as e:
                self._logger.error("Error adding player to room", player_id=player_id, room_id=room_id, error=str(e))
                log_and_raise(
                    DatabaseError,
                    f"Error adding player {player_id} to room {room_id}: {e}",
                    player_id=player_id,
                    room_id=room_id,
                    operation="add_player_to_room",
                    details={"player_id": player_id, "room_id": room_id, "error": str(e)},
                    user_friendly="Failed to add player to room",
                )

    def _validate_remove_player_params(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """Validate parameters for remove_player_from_room operation."""
        if not player_id:
            log_and_raise(
                ValidationError,
                "Player ID cannot be empty",
                operation="remove_player_from_room",
                details={"room_id": room_id},
                user_friendly="Player ID is required",
            )

        if not room_id:
            log_and_raise(
                ValidationError,
                "Room ID cannot be empty",
                player_id=player_id,
                operation="remove_player_from_room",
                details={"player_id": player_id},
                user_friendly="Room ID is required",
            )

    def remove_player_from_room(self, player_id: uuid.UUID | str, room_id: str) -> bool:
        """
        Remove a player from a room (for logout, teleportation, etc.).

        Args:
            player_id: The ID of the player to remove
            room_id: The ID of the room to remove the player from

        Returns:
            True if the player was removed successfully, False otherwise
        """
        self._validate_remove_player_params(player_id, room_id)

        with self._lock:
            try:
                room = self._persistence.get_room_by_id(room_id)  # Sync method, uses cache
                if not room:
                    self._logger.error("Room not found", room_id=room_id)
                    return False

                # Check if player is in the room
                if not room.has_player(player_id):
                    self._logger.warning("Player not in room", player_id=player_id, room_id=room_id)
                    return True  # Consider this a success

                # Remove player from room
                room.player_left(player_id)

                self._logger.info("Removed player from room", player_id=player_id, room_id=room_id)
                return True

            except (DatabaseError, SQLAlchemyError) as e:
                self._logger.error(
                    "Error removing player from room", player_id=player_id, room_id=room_id, error=str(e)
                )
                log_and_raise(
                    DatabaseError,
                    f"Error removing player {player_id} from room {room_id}: {e}",
                    player_id=player_id,
                    room_id=room_id,
                    operation="remove_player_from_room",
                    details={"player_id": player_id, "room_id": room_id, "error": str(e)},
                    user_friendly="Failed to remove player from room",
                )

    async def get_player_room(self, player_id: uuid.UUID | str) -> str | None:
        """
        Get the room ID where a player is currently located.

        Args:
            player_id: The ID of the player to look up (UUID or string)

        Returns:
            The room ID where the player is located, or None if not found
        """
        if not player_id:
            log_and_raise(
                ValidationError,
                "Player ID cannot be empty",
                operation="get_player_room",
                user_friendly="Player ID is required",
            )

        # Convert to UUID for get_player_by_id if needed
        player_id_uuid: uuid.UUID
        if isinstance(player_id, str):
            try:
                player_id_uuid = uuid.UUID(player_id)
            except ValueError, AttributeError:
                return None
        else:
            player_id_uuid = player_id

        # Get player using async persistence
        try:
            player = await self._persistence.get_player_by_id(player_id_uuid)
            if player and hasattr(player, "current_room_id") and player.current_room_id:
                return str(player.current_room_id)
        except (DatabaseError, SQLAlchemyError) as e:
            self._logger.debug("Failed to get player room", player_id=player_id_uuid, error=str(e))

        return None

    def get_room_players(self, room_id: str) -> list[str]:
        """
        Get all players currently in a room.

        Args:
            room_id: The ID of the room to check

        Returns:
            List of player IDs in the room
        """
        if not room_id:
            log_and_raise(
                ValidationError,
                "Room ID cannot be empty",
                operation="get_room_players",
                user_friendly="Room ID is required",
            )

        room = self._persistence.get_room_by_id(room_id)  # Sync method, uses cache
        if room:
            return list(room.get_players())

        return []

    def validate_player_location(self, player_id: str, room_id: str) -> bool:
        """
        Validate that a player is in the specified room.

        Args:
            player_id: The ID of the player to validate
            room_id: The ID of the room to check

        Returns:
            True if the player is in the specified room, False otherwise
        """
        if not player_id:
            log_and_raise(
                ValidationError,
                "Player ID cannot be empty",
                operation="validate_player_location",
                details={"room_id": room_id},
                user_friendly="Player ID is required",
            )

        if not room_id:
            log_and_raise(
                ValidationError,
                "Room ID cannot be empty",
                player_id=player_id,
                operation="validate_player_location",
                details={"player_id": player_id},
                user_friendly="Room ID is required",
            )

        room = self._persistence.get_room_by_id(room_id)  # Sync method, uses cache
        if not room:
            return False

        return bool(room.has_player(player_id))
