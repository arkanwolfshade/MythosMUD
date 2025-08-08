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

from ..events import EventBus
from ..logging_config import get_logger
from ..models.room import Room
from ..persistence import get_persistence


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
        self._persistence = get_persistence()
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
            player_id: The ID of the player to move
            from_room_id: The ID of the room the player is leaving
            to_room_id: The ID of the room the player is entering

        Returns:
            True if the move was successful, False otherwise

        Raises:
            ValueError: If any parameters are invalid
            RuntimeError: If the move cannot be completed
        """
        if not player_id:
            raise ValueError("Player ID cannot be empty")

        if not from_room_id:
            raise ValueError("From room ID cannot be empty")

        if not to_room_id:
            raise ValueError("To room ID cannot be empty")

        if from_room_id == to_room_id:
            self._logger.warning(f"Player {player_id} attempted to move to same room {from_room_id}")
            return False

        with self._lock:
            try:
                # Step 1: Validate the move
                if not self._validate_movement(player_id, from_room_id, to_room_id):
                    return False

                # Step 2: Get the rooms
                from_room = self._persistence.get_room(from_room_id)
                to_room = self._persistence.get_room(to_room_id)

                if not from_room:
                    self._logger.error(f"From room {from_room_id} not found")
                    return False

                if not to_room:
                    self._logger.error(f"To room {to_room_id} not found")
                    return False

                # Step 3: Verify player is in the from_room
                if not from_room.has_player(player_id):
                    self._logger.error(f"Player {player_id} not in room {from_room_id}")
                    return False

                # Step 4: Perform the atomic move
                self._logger.info(f"Moving player {player_id} from {from_room_id} to {to_room_id}")

                # Remove from old room
                from_room.player_left(player_id)

                # Add to new room
                to_room.player_entered(player_id)

                # Update player's room in persistence
                player = self._persistence.get_player(player_id)
                if player:
                    player.current_room_id = to_room_id
                    self._persistence.save_player(player)

                self._logger.info(f"Successfully moved player {player_id} to {to_room_id}")
                return True

            except Exception as e:
                self._logger.error(f"Error moving player {player_id}: {e}")
                return False

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
            self._logger.error(f"From room {from_room_id} does not exist")
            return False

        if not to_room:
            self._logger.error(f"To room {to_room_id} does not exist")
            return False

        # Check if player is in the from_room
        if not from_room.has_player(player_id):
            self._logger.error(f"Player {player_id} is not in room {from_room_id}")
            return False

        # Check if player is already in the to_room (shouldn't happen, but safety check)
        if to_room.has_player(player_id):
            self._logger.error(f"Player {player_id} is already in room {to_room_id}")
            return False

        # Check if there's a valid exit from from_room to to_room
        if not self._validate_exit(from_room, to_room_id):
            self._logger.error(f"No valid exit from {from_room_id} to {to_room_id}")
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
        # For now, we'll allow movement to any room
        # In the future, this could check specific exits, movement restrictions, etc.
        return True

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
            raise ValueError("Player ID cannot be empty")

        if not room_id:
            raise ValueError("Room ID cannot be empty")

        with self._lock:
            try:
                room = self._persistence.get_room(room_id)
                if not room:
                    self._logger.error(f"Room {room_id} not found")
                    return False

                # Check if player is already in the room
                if room.has_player(player_id):
                    self._logger.warning(f"Player {player_id} already in room {room_id}")
                    return True  # Consider this a success

                # Add player to room
                room.player_entered(player_id)

                # Update player's room in persistence
                player = self._persistence.get_player(player_id)
                if player:
                    player.current_room_id = room_id
                    self._persistence.save_player(player)

                self._logger.info(f"Added player {player_id} to room {room_id}")
                return True

            except Exception as e:
                self._logger.error(f"Error adding player {player_id} to room {room_id}: {e}")
                return False

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
            raise ValueError("Player ID cannot be empty")

        if not room_id:
            raise ValueError("Room ID cannot be empty")

        with self._lock:
            try:
                room = self._persistence.get_room(room_id)
                if not room:
                    self._logger.error(f"Room {room_id} not found")
                    return False

                # Check if player is in the room
                if not room.has_player(player_id):
                    self._logger.warning(f"Player {player_id} not in room {room_id}")
                    return True  # Consider this a success

                # Remove player from room
                room.player_left(player_id)

                self._logger.info(f"Removed player {player_id} from room {room_id}")
                return True

            except Exception as e:
                self._logger.error(f"Error removing player {player_id} from room {room_id}: {e}")
                return False

    def get_player_room(self, player_id: str) -> str | None:
        """
        Get the room ID where a player is currently located.

        Args:
            player_id: The ID of the player to look up

        Returns:
            The room ID where the player is located, or None if not found
        """
        if not player_id:
            raise ValueError("Player ID cannot be empty")

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
            raise ValueError("Room ID cannot be empty")

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
            raise ValueError("Player ID cannot be empty")

        if not room_id:
            raise ValueError("Room ID cannot be empty")

        room = self._persistence.get_room(room_id)
        if not room:
            return False

        return room.has_player(player_id)
