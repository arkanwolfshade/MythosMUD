"""
Movement service for MythosMUD.

This module provides the MovementService class that handles atomic movement
operations for players between rooms. The service ensures ACID properties
and coordinates between Room objects and the PersistenceLayer.

As noted in the Pnakotic Manuscripts, proper movement tracking is essential
for maintaining the integrity of our eldritch architecture and ensuring
that dimensional shifts are properly recorded.
"""

import threading
import time

from ..events import EventBus
from ..exceptions import DatabaseError, ValidationError
from ..logging.enhanced_logging_config import get_logger
from ..models.room import Room
from ..persistence import get_persistence
from ..utils.error_logging import create_error_context, log_and_raise
from .movement_monitor import get_movement_monitor


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

    def __init__(self, event_bus: EventBus | None = None):
        """
        Initialize the movement service.

        Args:
            event_bus: Optional EventBus instance for movement events
        """
        self._event_bus = event_bus
        # Use the existing persistence instance if available, otherwise get a new one
        self._persistence = get_persistence(event_bus)
        self._lock = threading.RLock()
        self._logger = get_logger("MovementService")

        self._logger.info("MovementService initialized")

    def move_player(self, player_id: str, from_room_id: str, to_room_id: str) -> bool:
        """
        Move a player from one room to another atomically.

        This operation ensures ACID properties:
        - Atomicity: Either the entire move succeeds or fails
        - Consistency: Player is never in multiple rooms
        - Isolation: Concurrent moves don't interfere
        - Durability: Changes are persisted

        Args:
            player_id: The ID of the player to move (can be player_id or player name)
            from_room_id: The ID of the room the player is leaving
            to_room_id: The ID of the room the player is entering

        Returns:
            True if the move was successful, False otherwise

        Raises:
            ValueError: If any parameters are invalid
            RuntimeError: If the move cannot be completed
        """
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

        start_time = time.time()
        monitor = get_movement_monitor()

        with self._lock:
            try:
                # Step 1: Resolve the player (prefer by ID, fallback to name)
                self._logger.debug("MovementService using persistence instance", persistence_id=id(self._persistence))
                player = self._persistence.get_player(player_id)
                if not player:
                    # Fallback to name lookup only if player_id doesn't look like a UUID
                    if len(player_id) != 36 or player_id.count("-") != 4:
                        player = self._persistence.get_player_by_name(player_id)
                        if player:
                            self._logger.info(
                                "Resolved player by name", player_name=player_id, player_id=player.player_id
                            )

                if not player:
                    self._logger.error("Player not found", player_id=player_id)
                    context = create_error_context()
                    context.metadata["player_id"] = player_id
                    context.metadata["from_room_id"] = from_room_id
                    context.metadata["to_room_id"] = to_room_id
                    context.metadata["operation"] = "move_player"
                    duration_ms = (time.time() - start_time) * 1000
                    monitor.record_movement_attempt(player_id, from_room_id, to_room_id, False, duration_ms)
                    log_and_raise(
                        ValidationError,
                        f"Player not found: {player_id}",
                        context=context,
                        details={"player_id": player_id, "from_room_id": from_room_id, "to_room_id": to_room_id},
                        user_friendly="Player not found",
                    )

                # Use the resolved player ID consistently
                resolved_player_id = player.player_id

                # Log the resolution for debugging
                if resolved_player_id != player_id:
                    self._logger.info("Player ID resolved", player_name=player_id, player_id=resolved_player_id)

                # Step 2: Validate the move
                if not self._validate_movement(resolved_player_id, from_room_id, to_room_id):
                    duration_ms = (time.time() - start_time) * 1000
                    monitor.record_movement_attempt(player_id, from_room_id, to_room_id, False, duration_ms)
                    return False

                # Step 3: Get the rooms
                from_room = self._persistence.get_room(from_room_id)
                to_room = self._persistence.get_room(to_room_id)

                if not from_room:
                    self._logger.error("From room not found", room_id=from_room_id)
                    context = create_error_context()
                    context.metadata["player_id"] = resolved_player_id
                    context.metadata["from_room_id"] = from_room_id
                    context.metadata["to_room_id"] = to_room_id
                    context.metadata["operation"] = "move_player"
                    duration_ms = (time.time() - start_time) * 1000
                    monitor.record_movement_attempt(player_id, from_room_id, to_room_id, False, duration_ms)
                    log_and_raise(
                        ValidationError,
                        f"From room {from_room_id} not found",
                        context=context,
                        details={
                            "player_id": resolved_player_id,
                            "from_room_id": from_room_id,
                            "to_room_id": to_room_id,
                        },
                        user_friendly="Source room not found",
                    )

                if not to_room:
                    self._logger.error("To room not found", room_id=to_room_id)
                    context = create_error_context()
                    context.metadata["player_id"] = resolved_player_id
                    context.metadata["from_room_id"] = from_room_id
                    context.metadata["to_room_id"] = to_room_id
                    context.metadata["operation"] = "move_player"
                    duration_ms = (time.time() - start_time) * 1000
                    monitor.record_movement_attempt(player_id, from_room_id, to_room_id, False, duration_ms)
                    log_and_raise(
                        ValidationError,
                        f"To room {to_room_id} not found",
                        context=context,
                        details={
                            "player_id": resolved_player_id,
                            "from_room_id": from_room_id,
                            "to_room_id": to_room_id,
                        },
                        user_friendly="Destination room not found",
                    )

                    # Step 4: Verify player is in the from_room (auto-add logic is now in _validate_movement)
                if not from_room.has_player(resolved_player_id):
                    self._logger.error("Player not in room", player_id=resolved_player_id, room_id=from_room_id)
                    duration_ms = (time.time() - start_time) * 1000
                    monitor.record_movement_attempt(player_id, from_room_id, to_room_id, False, duration_ms)
                    return False

                # Step 5: Perform the atomic move
                self._logger.info(
                    "Moving player", player_id=resolved_player_id, from_room=from_room_id, to_room=to_room_id
                )

                # Remove from old room
                self._logger.debug("Removing player from room", player_id=resolved_player_id, room_id=from_room_id)
                from_room.player_left(resolved_player_id)

                # Add to new room
                self._logger.debug("Adding player to room", player_id=resolved_player_id, room_id=to_room_id)
                to_room.player_entered(resolved_player_id)

                # Update player's room in persistence
                self._logger.debug("Updating player room in database", player_id=resolved_player_id, room_id=to_room_id)
                player.current_room_id = to_room_id
                self._persistence.save_player(player)

                # Record successful movement
                duration_ms = (time.time() - start_time) * 1000
                monitor.record_movement_attempt(player_id, from_room_id, to_room_id, True, duration_ms)

                self._logger.info("Successfully moved player", player_id=resolved_player_id, room_id=to_room_id)
                return True

            except Exception as e:
                self._logger.error("Error moving player", player_id=player_id, error=str(e))
                context = create_error_context()
                context.metadata["player_id"] = player_id
                context.metadata["from_room_id"] = from_room_id
                context.metadata["to_room_id"] = to_room_id
                context.metadata["operation"] = "move_player"
                duration_ms = (time.time() - start_time) * 1000
                monitor.record_movement_attempt(player_id, from_room_id, to_room_id, False, duration_ms)
                log_and_raise(
                    DatabaseError,
                    f"Error moving player {player_id}: {e}",
                    context=context,
                    details={
                        "player_id": player_id,
                        "from_room_id": from_room_id,
                        "to_room_id": to_room_id,
                        "error": str(e),
                    },
                    user_friendly="Movement failed",
                )

    def _validate_movement(self, player_id: str, from_room_id: str, to_room_id: str) -> bool:
        """
        Validate that a movement operation is allowed.

        Args:
            player_id: The ID of the player to move
            from_room_id: The ID of the room the player is leaving
            to_room_id: The ID of the room the player is entering

        Returns:
            True if the movement is valid, False otherwise
        """
        # Check if rooms exist
        from_room = self._persistence.get_room(from_room_id)
        to_room = self._persistence.get_room(to_room_id)

        if not from_room:
            self._logger.error("From room does not exist", room_id=from_room_id)
            return False

        if not to_room:
            self._logger.error("To room does not exist", room_id=to_room_id)
            return False

        # Check if player is in the from_room
        if not from_room.has_player(player_id):
            # Player might not be in the room's in-memory state yet
            # Check if their current_room_id matches the from_room_id
            player = self._persistence.get_player(player_id)
            if player and player.current_room_id == from_room_id:
                # Player should be in this room, add them to the in-memory state
                # Use direct state update to avoid triggering events during validation
                self._logger.info(
                    "Adding player to room in-memory state (direct update)", player_id=player_id, room_id=from_room_id
                )
                from_room._players.add(player_id)
            else:
                self._logger.error(
                    f"Player {player_id} not found in expected from_room {from_room_id}; movement invalid"
                )
                return False

        # Check if player is already in the to_room (shouldn't happen, but safety check)
        if to_room.has_player(player_id):
            self._logger.error("Player is already in room", player_id=player_id, room_id=to_room_id)
            return False

        # Check if there's a valid exit from from_room to to_room
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
            self._logger.debug("No exits found in room", room_id=from_room.id)
            return False

        # Check each exit direction
        for direction, target_id in exits.items():
            if target_id == to_room_id:
                self._logger.debug("Valid exit found", direction=direction, room_id=to_room_id)
                return True

        self._logger.debug("No valid exit", from_room=from_room.id, to_room=to_room_id, available_exits=exits)
        return False

    def add_player_to_room(self, player_id: str, room_id: str) -> bool:
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
                room = self._persistence.get_room(room_id)
                if not room:
                    self._logger.error("Room not found", room_id=room_id)
                    return False

                # Check if player is already in the room
                if room.has_player(player_id):
                    self._logger.warning("Player already in room", player_id=player_id, room_id=room_id)
                    return True  # Consider this a success

                # Add player to room (direct addition to avoid triggering movement events during initial setup)
                room._players.add(player_id)

                # Update player's room in persistence
                player = self._persistence.get_player(player_id)
                if player:
                    player.current_room_id = room_id
                    self._persistence.save_player(player)

                self._logger.info("Added player to room", player_id=player_id, room_id=room_id)
                return True

            except Exception as e:
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

    def remove_player_from_room(self, player_id: str, room_id: str) -> bool:
        """
        Remove a player from a room (for logout, teleportation, etc.).

        Args:
            player_id: The ID of the player to remove
            room_id: The ID of the room to remove the player from

        Returns:
            True if the player was removed successfully, False otherwise
        """
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

        with self._lock:
            try:
                room = self._persistence.get_room(room_id)
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

            except Exception as e:
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

    def get_player_room(self, player_id: str) -> str | None:
        """
        Get the room ID where a player is currently located.

        Args:
            player_id: The ID of the player to look up

        Returns:
            The room ID where the player is located, or None if not found
        """
        if not player_id:
            context = create_error_context()
            context.metadata["operation"] = "get_player_room"
            log_and_raise(
                ValidationError, "Player ID cannot be empty", context=context, user_friendly="Player ID is required"
            )

        player = self._persistence.get_player(player_id)
        if player:
            return player.current_room_id

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

        room = self._persistence.get_room(room_id)
        if room:
            return room.get_players()

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

        room = self._persistence.get_room(room_id)
        if not room:
            return False

        return room.has_player(player_id)
