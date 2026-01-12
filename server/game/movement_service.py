"""
Movement service for MythosMUD.

This module provides the MovementService class that handles atomic movement
operations for players between rooms. The service ensures ACID properties
and coordinates between Room objects and the PersistenceLayer.

As noted in the Pnakotic Manuscripts, proper movement tracking is essential
for maintaining the integrity of our eldritch architecture and ensuring
that dimensional shifts are properly recorded.
"""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Movement service methods require multiple return statements for early validation returns (movement validation, permission checks, error handling). Movement service requires extensive logic for complex movement operations and state management.

import threading
import time
import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy.exc import SQLAlchemyError

from ..events import EventBus
from ..exceptions import DatabaseError, ValidationError
from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_error_context, log_and_raise
from .movement_monitor import get_movement_monitor

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer


class MovementService:
    """
    Service for handling atomic player movement operations.

    This class provides thread-safe movement operations that ensure
    ACID properties: Atomicity, Consistency, Isolation, and Durability.
    Players can never appear to be in multiple rooms simultaneously.

    As documented in the Cultes des Goules, proper movement validation
    is essential for maintaining the integrity of our dimensional
    architecture.
    """

    def __init__(
        self,
        event_bus: EventBus | None = None,
        player_combat_service=None,
        async_persistence: "AsyncPersistenceLayer | None" = None,
        exploration_service: Any = None,
    ):
        """
        Initialize the movement service.

        Args:
            event_bus: Optional EventBus instance for movement events
            player_combat_service: Optional PlayerCombatService for combat state checking
            async_persistence: Optional AsyncPersistenceLayer instance (required for persistence operations)
            exploration_service: Optional ExplorationService for tracking room exploration
        """
        self._event_bus = event_bus
        if async_persistence is None:
            raise ValueError("async_persistence is required for MovementService")
        self._persistence = async_persistence
        self._lock = threading.RLock()
        self._logger = get_logger("MovementService")
        self._player_combat_service = player_combat_service
        self._exploration_service = exploration_service

        self._logger.info(
            "MovementService initialized",
            has_combat_service=bool(player_combat_service),
            has_exploration_service=bool(exploration_service),
        )

    def _validate_move_params(self, player_id: uuid.UUID | str, from_room_id: str, to_room_id: str) -> bool:
        """Validate movement parameters. Returns False if validation fails (same room), raises on invalid params."""
        if not player_id:
            context = create_error_context()
            context.metadata["operation"] = "move_player"
            log_and_raise(
                ValidationError,
                "Player ID cannot be empty",
                context=context,
                details={"from_room_id": from_room_id, "to_room_id": to_room_id},
                user_friendly="Player ID is required",
            )

        if not from_room_id:
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "move_player"
            log_and_raise(
                ValidationError,
                "From room ID cannot be empty",
                context=context,
                details={"player_id": player_id, "to_room_id": to_room_id},
                user_friendly="Source room ID is required",
            )

        if not to_room_id:
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["from_room_id"] = from_room_id
            context.metadata["operation"] = "move_player"
            log_and_raise(
                ValidationError,
                "To room ID cannot be empty",
                context=context,
                details={"player_id": player_id, "from_room_id": from_room_id},
                user_friendly="Destination room ID is required",
            )

        if from_room_id == to_room_id:
            self._logger.warning("Player attempted to move to same room", player_id=player_id, room_id=from_room_id)
            return False

        return True

    async def _resolve_player_for_movement(
        self, player_id: uuid.UUID | str, timing_breakdown: dict[str, float]
    ) -> tuple[Any, uuid.UUID | str]:
        """Resolve player by ID or name and return player object and resolved ID."""
        self._logger.debug("MovementService using persistence instance", persistence_id=id(self._persistence))
        player_lookup_start = time.time()
        if isinstance(player_id, uuid.UUID):
            player_uuid = player_id
            player = await self._persistence.get_player_by_id(player_uuid)
        else:
            try:
                player_uuid = uuid.UUID(player_id)
                player = await self._persistence.get_player_by_id(player_uuid)
            except (ValueError, AttributeError):
                player = await self._persistence.get_player_by_name(player_id)
                if player:
                    self._logger.info("Resolved player by name", player_name=player_id, player_id=player.player_id)
        player_lookup_end = time.time()
        timing_breakdown["player_lookup_ms"] = (player_lookup_end - player_lookup_start) * 1000

        if not player:
            self._logger.error("Player not found", player_id=player_id)
            raise ValidationError(f"Player not found: {player_id}")

        resolved_player_id_str = str(player.player_id)
        try:
            resolved_player_id: uuid.UUID | str = uuid.UUID(resolved_player_id_str)
        except (ValueError, AttributeError, TypeError):
            resolved_player_id = resolved_player_id_str

        if str(resolved_player_id) != str(player_id):
            self._logger.info("Player ID resolved", player_name=player_id, player_id=resolved_player_id)

        return player, resolved_player_id

    def _get_rooms_for_movement(
        self,
        from_room_id: str,
        to_room_id: str,
        resolved_player_id: uuid.UUID | str,
        timing_breakdown: dict[str, float],
    ) -> tuple[Room, Room]:
        """Get and validate rooms for movement."""
        room_lookup_start = time.time()
        from_room = self._persistence.get_room_by_id(from_room_id)
        to_room = self._persistence.get_room_by_id(to_room_id)
        room_lookup_end = time.time()
        timing_breakdown["room_lookup_ms"] = (room_lookup_end - room_lookup_start) * 1000

        if not from_room:
            self._logger.error("From room not found", room_id=from_room_id)
            raise ValidationError(f"From room {from_room_id} not found")

        if not to_room:
            self._logger.error("To room not found", room_id=to_room_id)
            raise ValidationError(f"To room {to_room_id} not found")

        if not from_room.has_player(resolved_player_id):
            self._logger.error("Player not in room", player_id=resolved_player_id, room_id=from_room_id)
            raise ValidationError("Player not in source room")

        return from_room, to_room

    def _execute_room_transfer(
        self, from_room: Room, to_room: Room, resolved_player_id: uuid.UUID | str, timing_breakdown: dict[str, float]
    ) -> None:
        """Execute the atomic room transfer."""
        self._logger.info("Moving player", player_id=resolved_player_id, from_room=from_room.id, to_room=to_room.id)
        room_update_start = time.time()
        self._logger.debug("Removing player from room", player_id=resolved_player_id, room_id=from_room.id)
        from_room.player_left(resolved_player_id)
        self._logger.debug("Adding player to room", player_id=resolved_player_id, room_id=to_room.id)
        to_room.player_entered(resolved_player_id, force_event=True)
        room_update_end = time.time()
        timing_breakdown["room_update_ms"] = (room_update_end - room_update_start) * 1000

    async def _persist_player_location(self, player: Any, to_room_id: str, timing_breakdown: dict[str, float]) -> None:
        """Update player location in database."""
        db_write_start = time.time()
        self._logger.debug("Updating player room in database", player_id=player.player_id, room_id=to_room_id)
        setattr(player, "current_room_id", to_room_id)  # noqa: B010
        await self._persistence.save_player(player)
        db_write_end = time.time()
        timing_breakdown["db_write_ms"] = (db_write_end - db_write_start) * 1000

    def _mark_room_explored(self, resolved_player_id: uuid.UUID | str, to_room_id: str) -> None:
        """Mark destination room as explored (non-blocking)."""
        try:
            exploration_service = self._exploration_service
            if exploration_service:
                player_uuid = (
                    resolved_player_id if isinstance(resolved_player_id, uuid.UUID) else uuid.UUID(resolved_player_id)
                )
                exploration_service.mark_room_as_explored_sync(player_uuid, to_room_id)
        except (DatabaseError, SQLAlchemyError) as e:
            self._logger.warning(
                "Failed to mark room as explored (non-blocking)",
                player_id=resolved_player_id,
                room_id=to_room_id,
                error=str(e),
                error_type=type(e).__name__,
            )

    def _handle_movement_error(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Error handling requires many parameters for context and error reporting
        self,
        e: Exception,
        player_id: uuid.UUID | str,
        from_room_id: str,
        to_room_id: str,
        start_time: float,
        timing_breakdown: dict[str, float],
    ) -> None:
        """Handle movement errors with monitoring."""
        duration_ms = (time.time() - start_time) * 1000
        timing_breakdown["total_ms"] = duration_ms
        monitor = get_movement_monitor()
        self._logger.error(
            "Error moving player",
            player_id=player_id,
            error=str(e),
            total_ms=duration_ms,
            lock_wait_ms=timing_breakdown.get("lock_wait_ms", 0),
            player_lookup_ms=timing_breakdown.get("player_lookup_ms", 0),
            validation_ms=timing_breakdown.get("validation_ms", 0),
            room_lookup_ms=timing_breakdown.get("room_lookup_ms", 0),
            room_update_ms=timing_breakdown.get("room_update_ms", 0),
            db_write_ms=timing_breakdown.get("db_write_ms", 0),
        )
        context = create_error_context()
        context.metadata["player_id"] = player_id
        context.metadata["from_room_id"] = from_room_id
        context.metadata["to_room_id"] = to_room_id
        context.metadata["operation"] = "move_player"
        monitor.record_movement_attempt(str(player_id), from_room_id, to_room_id, False, duration_ms)
        log_and_raise(
            DatabaseError,
            f"Error moving player {player_id}: {e}",
            context=context,
            details={"player_id": player_id, "from_room_id": from_room_id, "to_room_id": to_room_id, "error": str(e)},
            user_friendly="Movement failed",
        )

    async def move_player(self, player_id: uuid.UUID | str, from_room_id: str, to_room_id: str) -> bool:  # pylint: disable=too-many-locals  # Reason: Movement requires many intermediate variables for complex movement logic
        """
        Move a player from one room to another atomically.

        This operation ensures ACID properties:
        - Atomicity: Either the entire move succeeds or fails
        - Consistency: Player is never in multiple rooms
        - Isolation: Concurrent moves don't interfere
        - Durability: Changes are persisted

        Args:
            player_id: The ID of the player to move (UUID or string UUID/name for backward compatibility)
            from_room_id: The ID of the room the player is leaving
            to_room_id: The ID of the room the player is entering

        Returns:
            True if the move was successful, False otherwise

        Raises:
            ValueError: If any parameters are invalid
            RuntimeError: If the move cannot be completed
        """
        if not self._validate_move_params(player_id, from_room_id, to_room_id):
            return False

        start_time = time.time()
        monitor = get_movement_monitor()
        timing_breakdown: dict[str, float] = {}

        with self._lock:
            try:
                lock_acquisition_time = time.time()
                timing_breakdown["lock_wait_ms"] = (lock_acquisition_time - start_time) * 1000

                player, resolved_player_id = await self._resolve_player_for_movement(player_id, timing_breakdown)

                validation_start = time.time()
                if not await self._validate_movement(player, from_room_id, to_room_id):
                    validation_end = time.time()
                    timing_breakdown["validation_ms"] = (validation_end - validation_start) * 1000
                    duration_ms = (time.time() - start_time) * 1000
                    self._logger.debug(
                        "Movement validation failed",
                        player_id=resolved_player_id,
                        duration_ms=duration_ms,
                        **timing_breakdown,
                    )
                    monitor.record_movement_attempt(player_id, from_room_id, to_room_id, False, duration_ms)
                    return False
                validation_end = time.time()
                timing_breakdown["validation_ms"] = (validation_end - validation_start) * 1000

                from_room, to_room = self._get_rooms_for_movement(
                    from_room_id, to_room_id, resolved_player_id, timing_breakdown
                )

                self._execute_room_transfer(from_room, to_room, resolved_player_id, timing_breakdown)
                await self._persist_player_location(player, to_room_id, timing_breakdown)

                duration_ms = (time.time() - start_time) * 1000
                timing_breakdown["total_ms"] = duration_ms
                self._logger.info(
                    "Movement timing breakdown",
                    player_id=resolved_player_id,
                    from_room=from_room_id,
                    to_room=to_room_id,
                    total_ms=duration_ms,
                    lock_wait_ms=timing_breakdown.get("lock_wait_ms", 0),
                    player_lookup_ms=timing_breakdown.get("player_lookup_ms", 0),
                    validation_ms=timing_breakdown.get("validation_ms", 0),
                    room_lookup_ms=timing_breakdown.get("room_lookup_ms", 0),
                    room_update_ms=timing_breakdown.get("room_update_ms", 0),
                    db_write_ms=timing_breakdown.get("db_write_ms", 0),
                )
                monitor.record_movement_attempt(player_id, from_room_id, to_room_id, True, duration_ms)

                self._mark_room_explored(resolved_player_id, to_room_id)

                self._logger.info("Successfully moved player", player_id=resolved_player_id, room_id=to_room_id)
                return True

            except ValidationError as e:
                duration_ms = (time.time() - start_time) * 1000
                monitor.record_movement_attempt(player_id, from_room_id, to_room_id, False, duration_ms)
                self._logger.warning("Movement validation failed", player_id=player_id, error=str(e))
                return False
            except (DatabaseError, SQLAlchemyError) as e:
                self._handle_movement_error(e, player_id, from_room_id, to_room_id, start_time, timing_breakdown)
                return False

    def _extract_player_id(self, player_obj, from_room_id: str, to_room_id: str) -> uuid.UUID | None:
        """Extract and validate player ID from player object."""
        if not player_obj:
            self._logger.error(
                "POSITION CHECK: Player object missing during validation", from_room=from_room_id, to_room=to_room_id
            )
            return None

        try:
            if not hasattr(player_obj, "player_id") or not player_obj.player_id:
                self._logger.warning(
                    "COMBAT CHECK: Player object missing player_id attribute, allowing movement",
                    from_room=from_room_id,
                    to_room=to_room_id,
                )
                return None

            return uuid.UUID(player_obj.player_id)
        except (ValueError, AttributeError, TypeError) as e:
            self._logger.warning(
                "COMBAT CHECK: Failed to extract player_id as UUID, allowing movement",
                from_room=from_room_id,
                to_room=to_room_id,
                error=str(e),
            )
            return None

    def _check_combat_state(self, player_id: uuid.UUID, from_room_id: str, to_room_id: str) -> bool:
        """Check if player is in combat (blocks movement)."""
        if not self._player_combat_service:
            self._logger.warning("COMBAT CHECK: No combat service available, allowing movement by default")
            return True

        try:
            is_in_combat = self._player_combat_service.is_player_in_combat_sync(player_id)
            if is_in_combat:
                self._logger.warning(
                    "COMBAT CHECK: BLOCKING MOVEMENT - Player is in combat",
                    player_id=player_id,
                    from_room=from_room_id,
                    to_room=to_room_id,
                )
                return False
            return True
        except (DatabaseError, SQLAlchemyError) as e:
            self._logger.warning(
                "COMBAT CHECK: Exception during combat check, allowing movement",
                player_id=player_id,
                error=str(e),
                exc_info=True,
            )
            return True

    def _check_player_posture(self, player_obj, player_id: uuid.UUID, from_room_id: str, to_room_id: str) -> bool:
        """Check if player posture allows movement (only standing allowed)."""
        posture = "standing"
        if hasattr(player_obj, "get_stats"):
            try:
                stats = player_obj.get_stats() or {}
                if not isinstance(stats, dict):
                    stats = {}
                posture_value = stats.get("position", "standing")
                posture = posture_value.lower() if isinstance(posture_value, str) else "standing"
            except (DatabaseError, SQLAlchemyError) as exc:
                self._logger.warning(
                    "POSITION CHECK: Failed to load player stats",
                    player_id=player_id,
                    error=str(exc),
                    from_room=from_room_id,
                    to_room=to_room_id,
                )
                posture = "standing"

        if posture not in {"standing"}:
            self._logger.info(
                "POSITION CHECK: Movement blocked due to posture",
                player_id=player_id,
                posture=posture,
                from_room=from_room_id,
                to_room=to_room_id,
            )
            return False
        return True

    async def _validate_player_room_membership(self, player_id: uuid.UUID, from_room: Room, from_room_id: str) -> bool:
        """Validate player is in the from_room, auto-adding if database matches."""
        if from_room.has_player(player_id):
            return True

        try:
            db_player = await self._persistence.get_player_by_id(player_id)
            if db_player and hasattr(db_player, "current_room_id") and db_player.current_room_id:
                if str(db_player.current_room_id) == from_room_id:
                    self._logger.info(
                        "Adding player to room in-memory state (database room matches)",
                        player_id=player_id,
                        room_id=from_room_id,
                    )
                    from_room.add_player_silently(player_id)
                    return True

                self._logger.error(
                    "Player not in expected room",
                    player_id=player_id,
                    expected_room=from_room_id,
                    actual_room=str(db_player.current_room_id),
                )
                return False

            self._logger.error("Player not found in database", player_id=player_id)
            return False
        except (DatabaseError, SQLAlchemyError) as e:
            self._logger.warning(
                "Failed to verify player room from database",
                player_id=player_id,
                room_id=from_room_id,
                error=str(e),
            )
            return False

    async def _validate_movement(self, player_obj, from_room_id: str, to_room_id: str) -> bool:
        """
        Validate that a movement operation is allowed.

        Args:
            player_obj: The player instance requesting movement
            from_room_id: The ID of the room the player is leaving
            to_room_id: The ID of the room the player is entering

        Returns:
            True if the movement is valid, False otherwise
        """
        player_id = self._extract_player_id(player_obj, from_room_id, to_room_id)
        if player_id is None:
            return True

        self._logger.info(
            "VALIDATION START: Checking movement",
            player_id=player_id,
            from_room=from_room_id,
            to_room=to_room_id,
            has_combat_service=bool(self._player_combat_service),
        )

        if not self._check_combat_state(player_id, from_room_id, to_room_id):
            return False

        if not self._check_player_posture(player_obj, player_id, from_room_id, to_room_id):
            return False

        from_room = self._persistence.get_room_by_id(from_room_id)
        to_room = self._persistence.get_room_by_id(to_room_id)

        if not from_room:
            self._logger.error("From room does not exist", room_id=from_room_id)
            return False

        if not to_room:
            self._logger.error("To room does not exist", room_id=to_room_id)
            return False

        if not await self._validate_player_room_membership(player_id, from_room, from_room_id):
            return False

        if to_room.has_player(player_id):
            self._logger.error("Player is already in room", player_id=player_id, room_id=to_room_id)
            return False

        if not self._validate_exit(from_room, to_room_id):
            self._logger.error("No valid exit", from_room=from_room_id, to_room=to_room_id)
            return False

        return True

    def _validate_exit(self, from_room: Room, to_room_id: str) -> bool:
        """
        Validate that there's a valid exit from the room to the target room.

        Args:
            from_room: The room the player is leaving
            to_room_id: The ID of the room the player is entering

        Returns:
            True if there's a valid exit, False otherwise
        """
        # Check if any exit in the room leads to the target room
        exits = from_room.exits
        if not exits:
            self._logger.warning("No exits found in room", room_id=from_room.id, room_name=from_room.name)
            return False

        # Check each exit direction
        for direction, target_id in exits.items():
            if target_id == to_room_id:
                self._logger.debug("Valid exit found", direction=direction, room_id=to_room_id)
                return True

        # Enhanced logging for debugging exit mismatches
        # As noted in the Pnakotic Manuscripts, dimensional gateways must be precisely aligned
        self._logger.warning(
            "Exit validation failed - room ID mismatch",
            from_room_id=from_room.id,
            from_room_name=from_room.name,
            to_room_id=to_room_id,
            available_exits=exits,
            exit_directions=list(exits.keys()),
            exit_targets=list(exits.values()),
        )

        # Check if target room exists (might be a room ID format issue)
        target_room = self._persistence.get_room_by_id(to_room_id)  # Sync method, uses cache
        if not target_room:
            self._logger.error(
                "Target room not found in persistence",
                to_room_id=to_room_id,
                from_room_id=from_room.id,
            )

        return False

    async def add_player_to_room(self, player_id: uuid.UUID | str, room_id: str) -> bool:
        """
        Add a player to a room (for initial placement, teleportation, etc.).

        Args:
            player_id: The ID of the player to add
            room_id: The ID of the room to add the player to

        Returns:
            True if the player was added successfully, False otherwise
        """
        if not player_id:
            context = create_error_context()
            context.metadata["operation"] = "add_player_to_room"
            log_and_raise(
                ValidationError,
                "Player ID cannot be empty",
                context=context,
                details={"room_id": room_id},
                user_friendly="Player ID is required",
            )

        if not room_id:
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "add_player_to_room"
            log_and_raise(
                ValidationError,
                "Room ID cannot be empty",
                context=context,
                details={"player_id": player_id},
                user_friendly="Room ID is required",
            )

        with self._lock:
            try:
                room = self._persistence.get_room_by_id(room_id)  # Sync method, uses cache
                if not room:
                    self._logger.error("Room not found", room_id=room_id)
                    return False

                # Check if player is already in the room
                if room.has_player(player_id):
                    self._logger.warning("Player already in room", player_id=player_id, room_id=room_id)
                    return True  # Consider this a success

                # Add player to room (direct addition to avoid triggering movement events during initial setup)
                room.add_player_silently(player_id)

                # Update player's room in persistence
                # Convert to UUID for get_player if needed
                if isinstance(player_id, str):
                    try:
                        player_uuid = uuid.UUID(player_id)
                    except (ValueError, AttributeError):
                        player = None
                        return True  # Consider this a success if we can't convert
                else:
                    player_uuid = player_id

                try:
                    player = await self._persistence.get_player_by_id(player_uuid)
                except (ValueError, AttributeError):
                    player = None
                if player:
                    # Use setattr to bypass mypy's strict type checking for SQLAlchemy Column descriptors
                    # At runtime, this attribute behaves as a string despite mypy seeing Column[str]
                    setattr(player, "current_room_id", room_id)  # noqa: B010
                    await self._persistence.save_player(player)

                self._logger.info("Added player to room", player_id=player_id, room_id=room_id)
                return True

            except (DatabaseError, SQLAlchemyError) as e:
                self._logger.error("Error adding player to room", player_id=player_id, room_id=room_id, error=str(e))
                context = create_error_context()
                context.metadata["player_id"] = player_id
                context.metadata["room_id"] = room_id
                context.metadata["operation"] = "add_player_to_room"
                log_and_raise(
                    DatabaseError,
                    f"Error adding player {player_id} to room {room_id}: {e}",
                    context=context,
                    details={"player_id": player_id, "room_id": room_id, "error": str(e)},
                    user_friendly="Failed to add player to room",
                )

    def _validate_remove_player_params(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """Validate parameters for remove_player_from_room operation."""
        if not player_id:
            context = create_error_context()
            context.metadata["operation"] = "remove_player_from_room"
            log_and_raise(
                ValidationError,
                "Player ID cannot be empty",
                context=context,
                details={"room_id": room_id},
                user_friendly="Player ID is required",
            )

        if not room_id:
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "remove_player_from_room"
            log_and_raise(
                ValidationError,
                "Room ID cannot be empty",
                context=context,
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
                context = create_error_context()
                context.metadata["player_id"] = player_id
                context.metadata["room_id"] = room_id
                context.metadata["operation"] = "remove_player_from_room"
                log_and_raise(
                    DatabaseError,
                    f"Error removing player {player_id} from room {room_id}: {e}",
                    context=context,
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
            context = create_error_context()
            context.metadata["operation"] = "get_player_room"
            log_and_raise(
                ValidationError, "Player ID cannot be empty", context=context, user_friendly="Player ID is required"
            )

        # Convert to UUID for get_player_by_id if needed
        player_id_uuid: uuid.UUID
        if isinstance(player_id, str):
            try:
                player_id_uuid = uuid.UUID(player_id)
            except (ValueError, AttributeError):
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
            context = create_error_context()
            context.metadata["operation"] = "get_room_players"
            log_and_raise(
                ValidationError, "Room ID cannot be empty", context=context, user_friendly="Room ID is required"
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
            context = create_error_context()
            context.metadata["operation"] = "validate_player_location"
            log_and_raise(
                ValidationError,
                "Player ID cannot be empty",
                context=context,
                details={"room_id": room_id},
                user_friendly="Player ID is required",
            )

        if not room_id:
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "validate_player_location"
            log_and_raise(
                ValidationError,
                "Room ID cannot be empty",
                context=context,
                details={"player_id": player_id},
                user_friendly="Room ID is required",
            )

        room = self._persistence.get_room_by_id(room_id)  # Sync method, uses cache
        if not room:
            return False

        return bool(room.has_player(player_id))
