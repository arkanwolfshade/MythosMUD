"""
Room subscription management for MythosMUD.

This module provides room subscription functionality for tracking
which players are subscribed to which rooms and managing room occupants.
"""

from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class RoomSubscriptionManager:
    """
    Manages room subscriptions and occupant tracking.

    This class handles room subscriptions, occupant tracking, and
    provides utilities for room-based operations.
    """

    def __init__(self):
        """Initialize the room subscription manager."""
        # Room subscriptions (room_id -> set of player_ids)
        self.room_subscriptions: dict[str, set[str]] = {}
        # Room occupants (room_id -> set of player_ids)
        self.room_occupants: dict[str, set[str]] = {}
        # Reference to persistence layer (set during initialization)
        self.persistence = None

    def set_persistence(self, persistence):
        """Set the persistence layer reference."""
        self.persistence = persistence

    def subscribe_to_room(self, player_id: str, room_id: str) -> bool:
        """
        Subscribe a player to a room.

        Args:
            player_id: The player's ID
            room_id: The room's ID

        Returns:
            bool: True if subscription was successful, False otherwise
        """
        try:
            canonical_id = self._canonical_room_id(room_id) or room_id
            if canonical_id not in self.room_subscriptions:
                self.room_subscriptions[canonical_id] = set()

            self.room_subscriptions[canonical_id].add(player_id)
            logger.debug("Player subscribed to room", player_id=player_id, room_id=canonical_id)
            return True

        except Exception as e:
            logger.error("Error subscribing player to room", player_id=player_id, room_id=room_id, error=str(e))
            return False

    def unsubscribe_from_room(self, player_id: str, room_id: str) -> bool:
        """
        Unsubscribe a player from a room.

        Args:
            player_id: The player's ID
            room_id: The room's ID

        Returns:
            bool: True if unsubscription was successful, False otherwise
        """
        try:
            canonical_id = self._canonical_room_id(room_id) or room_id
            if canonical_id in self.room_subscriptions:
                self.room_subscriptions[canonical_id].discard(player_id)
                if not self.room_subscriptions[canonical_id]:
                    del self.room_subscriptions[canonical_id]

            logger.debug("Player unsubscribed from room", player_id=player_id, room_id=canonical_id)
            return True

        except Exception as e:
            logger.error("Error unsubscribing player from room", player_id=player_id, room_id=room_id, error=str(e))
            return False

    def get_room_subscribers(self, room_id: str) -> set[str]:
        """
        Get all players subscribed to a room.

        Args:
            room_id: The room's ID

        Returns:
            Set[str]: Set of player IDs subscribed to the room
        """
        try:
            canonical_id = self._canonical_room_id(room_id) or room_id
            return self.room_subscriptions.get(canonical_id, set()).copy()
        except Exception as e:
            logger.error("Error getting subscribers for room", room_id=room_id, error=str(e))
            return set()

    def add_room_occupant(self, player_id: str, room_id: str) -> bool:
        """
        Add a player as an occupant of a room.

        Args:
            player_id: The player's ID
            room_id: The room's ID

        Returns:
            bool: True if occupant was added successfully, False otherwise
        """
        try:
            canonical_id = self._canonical_room_id(room_id) or room_id
            if canonical_id not in self.room_occupants:
                self.room_occupants[canonical_id] = set()

            self.room_occupants[canonical_id].add(player_id)
            logger.debug("Player added as occupant of room", player_id=player_id, room_id=canonical_id)
            return True

        except Exception as e:
            logger.error("Error adding occupant to room", player_id=player_id, room_id=room_id, error=str(e))
            return False

    def remove_room_occupant(self, player_id: str, room_id: str) -> bool:
        """
        Remove a player as an occupant of a room.

        Args:
            player_id: The player's ID
            room_id: The room's ID

        Returns:
            bool: True if occupant was removed successfully, False otherwise
        """
        try:
            canonical_id = self._canonical_room_id(room_id) or room_id
            if canonical_id in self.room_occupants:
                self.room_occupants[canonical_id].discard(player_id)
                if not self.room_occupants[canonical_id]:
                    del self.room_occupants[canonical_id]

            logger.debug("Player removed as occupant of room", player_id=player_id, room_id=canonical_id)
            return True

        except Exception as e:
            logger.error("Error removing occupant from room", player_id=player_id, room_id=room_id, error=str(e))
            return False

    def get_room_occupants(self, room_id: str, online_players: dict[str, Any]) -> list[dict[str, Any]]:
        """
        Get list of occupants in a room.

        Args:
            room_id: The room ID
            online_players: Dictionary of online players

        Returns:
            List[Dict[str, Any]]: List of occupant information
        """
        try:
            occupants: list[dict[str, Any]] = []

            # Resolve to canonical id and check set presence
            canonical_id = self._canonical_room_id(room_id) or room_id
            if canonical_id not in self.room_occupants:
                return occupants

            # Only include online players currently tracked in this room
            for player_id in self.room_occupants[canonical_id]:
                if player_id in online_players:
                    occupants.append(online_players[player_id])

            return occupants

        except Exception as e:
            logger.error("Error getting occupants for room", room_id=room_id, error=str(e))
            return []

    def remove_player_from_all_rooms(self, player_id: str) -> bool:
        """
        Remove a player from all room subscriptions and occupant lists.

        Args:
            player_id: The player's ID

        Returns:
            bool: True if player was removed from all rooms successfully, False otherwise
        """
        try:
            # Remove from room subscriptions
            for room_id in list(self.room_subscriptions.keys()):
                if player_id in self.room_subscriptions[room_id]:
                    self.room_subscriptions[room_id].discard(player_id)
                    if not self.room_subscriptions[room_id]:
                        del self.room_subscriptions[room_id]

            # Remove from room occupants
            for room_id in list(self.room_occupants.keys()):
                if player_id in self.room_occupants[room_id]:
                    self.room_occupants[room_id].discard(player_id)
                    if not self.room_occupants[room_id]:
                        del self.room_occupants[room_id]

            logger.debug("Player removed from all rooms", player_id=player_id)
            return True

        except Exception as e:
            logger.error("Error removing player from all rooms", player_id=player_id, error=str(e))
            return False

    def reconcile_room_presence(self, room_id: str, online_players: dict[str, Any]) -> bool:
        """
        Ensure room_occupants only contains currently online players.

        Args:
            room_id: The room's ID
            online_players: Dictionary of online players

        Returns:
            bool: True if reconciliation was successful, False otherwise
        """
        try:
            canonical_id = self._canonical_room_id(room_id) or room_id
            if canonical_id in self.room_occupants:
                current = self.room_occupants[canonical_id]
                pruned = {pid for pid in current if pid in online_players}
                self.room_occupants[canonical_id] = pruned
                logger.debug(
                    "Reconciled room presence",
                    room_id=canonical_id,
                    current_count=len(current),
                    pruned_count=len(pruned),
                )
            return True

        except Exception as e:
            logger.error("Error reconciling room presence", room_id=room_id, error=str(e))
            return False

    def _canonical_room_id(self, room_id: str | None) -> str | None:
        """
        Resolve a room id to the canonical Room.id value, when possible.

        Args:
            room_id: The room ID to resolve

        Returns:
            Optional[str]: The canonical room ID or the original ID if resolution fails
        """
        try:
            if not room_id:
                return room_id
            if self.persistence is not None:
                room = self.persistence.get_room(room_id)
                if room is not None and getattr(room, "id", None):
                    return room.id
        except Exception as e:
            logger.error("Error resolving canonical room id", room_id=room_id, error=str(e))
        return room_id

    def get_stats(self) -> dict[str, Any]:
        """
        Get room subscription statistics.

        Returns:
            Dict[str, Any]: Statistics about room subscriptions and occupants
        """
        try:
            total_subscriptions = sum(len(subscribers) for subscribers in self.room_subscriptions.values())
            total_occupants = sum(len(occupants) for occupants in self.room_occupants.values())

            return {
                "total_rooms_with_subscriptions": len(self.room_subscriptions),
                "total_rooms_with_occupants": len(self.room_occupants),
                "total_subscriptions": total_subscriptions,
                "total_occupants": total_occupants,
                "average_subscriptions_per_room": total_subscriptions / len(self.room_subscriptions)
                if self.room_subscriptions
                else 0,
                "average_occupants_per_room": total_occupants / len(self.room_occupants) if self.room_occupants else 0,
            }
        except Exception as e:
            logger.error("Error getting room subscription stats", error=str(e))
            return {}
