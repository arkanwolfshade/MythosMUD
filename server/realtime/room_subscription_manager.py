"""
Room subscription management for MythosMUD.

This module provides room subscription functionality for tracking
which players are subscribed to which rooms and managing room occupants.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class RoomSubscriptionManager:
    """
    Manages room subscriptions and occupant tracking.

    This class handles room subscriptions, occupant tracking, and
    provides utilities for room-based operations.
    """

    def __init__(self) -> None:
        """Initialize the room subscription manager."""
        # Room subscriptions (room_id -> set of player_ids)
        self.room_subscriptions: dict[str, set[str]] = {}
        # Room occupants (room_id -> set of player_ids)
        self.room_occupants: dict[str, set[str]] = {}
        # Reference to persistence layer (set during initialization)
        self.persistence: Any | None = None
        # Non-persistent room drops (room_id -> list of stacks)
        self.room_drops: dict[str, list[dict[str, Any]]] = {}

    def set_persistence(self, persistence: Any) -> None:
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

    def list_room_drops(self, room_id: str) -> list[dict[str, Any]]:
        """
        Retrieve current room drops as a defensive copy for callers.

        Args:
            room_id: The room identifier.

        Returns:
            A deep copy of the drop stacks to prevent accidental mutation.
        """
        try:
            canonical_id = self._canonical_room_id(room_id) or room_id
            stacks = self.room_drops.get(canonical_id, [])
            return [deepcopy(stack) for stack in stacks]
        except Exception as exc:  # pragma: no cover - defensive logging
            logger.error("Error listing room drops", room_id=room_id, error=str(exc))
            return []

    def add_room_drop(self, room_id: str, stack: Mapping[str, Any]) -> None:
        """
        Append an item stack to the room drop ledger.

        Args:
            room_id: The room receiving the drop.
            stack: Mapping describing the dropped item stack.
        """
        canonical_id = self._canonical_room_id(room_id) or room_id
        try:
            drop_stack = dict(stack)
            quantity = int(drop_stack.get("quantity", 1))
            if quantity <= 0:
                raise ValueError("Quantity must be positive for room drops.")

            self.room_drops.setdefault(canonical_id, []).append(drop_stack)
            logger.info(
                "Room drop recorded",
                room_id=canonical_id,
                item_id=drop_stack.get("item_id"),
                quantity=quantity,
            )
        except Exception as exc:
            logger.error("Failed adding room drop", room_id=canonical_id, error=str(exc))

    def take_room_drop(self, room_id: str, index: int, quantity: int) -> dict[str, Any] | None:
        """
        Remove quantity of a drop entry, returning the removed stack.

        Args:
            room_id: Room identifier.
            index: Zero-based drop index.
            quantity: Quantity to remove.

        Returns:
            Detached stack representing the removed items, or None if unavailable.
        """
        canonical_id = self._canonical_room_id(room_id) or room_id
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be positive when taking room drops.")

            drop_list = self.room_drops.get(canonical_id)
            if not drop_list or not (0 <= index < len(drop_list)):
                return None

            stack = drop_list[index]
            available = int(stack.get("quantity", 1))
            removed = deepcopy(stack)
            if quantity >= available:
                removed_quantity = available
                drop_list.pop(index)
            else:
                removed_quantity = quantity
                stack["quantity"] = available - quantity
                removed["quantity"] = quantity

            if not drop_list:
                self.room_drops.pop(canonical_id, None)

            removed["quantity"] = removed_quantity
            logger.info(
                "Room drop retrieved",
                room_id=canonical_id,
                item_id=removed.get("item_id"),
                quantity=removed_quantity,
            )
            return removed
        except Exception as exc:
            logger.error("Failed retrieving room drop", room_id=canonical_id, error=str(exc))
            return None

    def adjust_room_drop(self, room_id: str, index: int, quantity: int) -> bool:
        """
        Adjust quantity for an existing drop entry; removing entry when zero.

        Args:
            room_id: Room identifier.
            index: Zero-based drop index.
            quantity: New quantity for stack (zero removes stack).

        Returns:
            True if adjustment applied, False otherwise.
        """
        canonical_id = self._canonical_room_id(room_id) or room_id
        try:
            drop_list = self.room_drops.get(canonical_id)
            if drop_list is None or not (0 <= index < len(drop_list)) or quantity < 0:
                return False

            if quantity == 0:
                drop_list.pop(index)
            else:
                drop_list[index]["quantity"] = quantity

            if drop_list:
                self.room_drops[canonical_id] = drop_list
            else:
                self.room_drops.pop(canonical_id, None)

            logger.debug("Room drop adjusted", room_id=canonical_id, index=index, quantity=quantity)
            return True
        except Exception as exc:
            logger.error("Failed adjusting room drop", room_id=canonical_id, error=str(exc))
            return False

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
        Get list of occupants (players and NPCs) in a room.

        Args:
            room_id: The room ID
            online_players: Dictionary of online players

        Returns:
            List[Dict[str, Any]]: List of occupant information (players and NPCs)
        """
        try:
            occupants: list[dict[str, Any]] = []

            # Resolve to canonical id and check set presence
            canonical_id = self._canonical_room_id(room_id) or room_id
            if canonical_id not in self.room_occupants:
                # Still check for NPCs even if no players
                canonical_id = canonical_id

            # Only include online players currently tracked in this room
            if canonical_id in self.room_occupants:
                for player_id in self.room_occupants[canonical_id]:
                    if player_id in online_players:
                        occupants.append(online_players[player_id])

            # CRITICAL FIX: Query NPCs from lifecycle manager instead of Room instance
            # Room instances are recreated from persistence and lose in-memory NPC tracking
            # NPCs are actually tracked in the lifecycle manager with their current_room/current_room_id
            npc_ids: list[str] = []
            try:
                from ..services.npc_instance_service import get_npc_instance_service

                npc_instance_service = get_npc_instance_service()
                if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                    lifecycle_manager = npc_instance_service.lifecycle_manager
                    if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                        active_npcs_dict = lifecycle_manager.active_npcs
                        # Query all active NPCs to find those in this room
                        # BUGFIX: Filter out dead NPCs (is_alive=False) to prevent showing dead NPCs in occupants
                        # As documented in investigation: 2025-11-30_session-001_npc-combat-start-failure.md
                        for npc_id, npc_instance in active_npcs_dict.items():
                            # Skip dead NPCs
                            is_alive_value = getattr(npc_instance, "is_alive", True)

                            if not is_alive_value:
                                logger.debug(
                                    "Skipping dead NPC from occupants",
                                    npc_id=npc_id,
                                    npc_name=getattr(npc_instance, "name", "unknown"),
                                    room_id=canonical_id,
                                )
                                continue

                            # Check both current_room and current_room_id for compatibility
                            current_room = getattr(npc_instance, "current_room", None)
                            current_room_id = getattr(npc_instance, "current_room_id", None)
                            npc_room_id = current_room or current_room_id
                            if npc_room_id == canonical_id:
                                npc_ids.append(npc_id)

                logger.debug(
                    "Adding NPCs to room occupants from lifecycle manager",
                    room_id=canonical_id,
                    npc_count=len(npc_ids),
                )
                for npc_id in npc_ids:
                    # Create a minimal dict for NPC occupant (matching player format)
                    # The NPC name will be resolved in broadcast_room_update via _get_npc_name_from_instance
                    occupants.append(
                        {
                            "player_id": npc_id,  # Use npc_id as player_id for compatibility
                            "player_name": npc_id,  # Will be resolved to actual name in broadcast_room_update
                            "is_npc": True,
                        }
                    )
            except Exception as npc_query_error:
                logger.warning(
                    "Error querying NPCs from lifecycle manager, falling back to room.get_npcs()",
                    room_id=canonical_id,
                    error=str(npc_query_error),
                )
                # Fallback to room.get_npcs() if lifecycle manager query fails
                # BUGFIX: Filter fallback NPCs to only include alive NPCs from active_npcs
                # As documented in investigation: 2025-11-30_session-001_npc-combat-start-failure.md
                if self.persistence:
                    room = self.persistence.get_room(canonical_id)
                    if room and hasattr(room, "get_npcs"):
                        room_npc_ids = room.get_npcs()
                        logger.debug(
                            "Adding NPCs to room occupants from room.get_npcs() fallback",
                            room_id=canonical_id,
                            npc_count=len(room_npc_ids),
                        )

                        # Filter fallback NPCs: only include those in active_npcs and alive
                        filtered_npc_ids = []
                        try:
                            from ..services.npc_instance_service import get_npc_instance_service

                            npc_instance_service = get_npc_instance_service()
                            if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                                lifecycle_manager = npc_instance_service.lifecycle_manager
                                if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                                    for npc_id in room_npc_ids:
                                        if npc_id in lifecycle_manager.active_npcs:
                                            npc_instance = lifecycle_manager.active_npcs[npc_id]
                                            # Only include alive NPCs
                                            if getattr(npc_instance, "is_alive", True):
                                                filtered_npc_ids.append(npc_id)
                                            else:
                                                logger.debug(
                                                    "Filtered dead NPC from fallback occupants",
                                                    npc_id=npc_id,
                                                    room_id=canonical_id,
                                                )
                        except Exception as filter_error:
                            logger.warning(
                                "Error filtering fallback NPCs, using all room NPCs",
                                room_id=canonical_id,
                                error=str(filter_error),
                            )
                            filtered_npc_ids = room_npc_ids

                        for npc_id in filtered_npc_ids:
                            occupants.append(
                                {
                                    "player_id": npc_id,
                                    "player_name": npc_id,
                                    "is_npc": True,
                                }
                            )

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
        if room_id is None or room_id == "":
            return room_id

        if self.persistence is None:
            return room_id

        try:
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
