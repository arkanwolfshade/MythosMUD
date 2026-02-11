"""
NPC movement integration with existing game systems.

This module provides integration between NPCs and the existing movement system,
including event publishing and room management.

As noted in the Pnakotic Manuscripts, proper movement integration is essential
for maintaining the integrity of our eldritch dimensional architecture.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from ..events import EventBus, NPCEnteredRoom, NPCLeftRoom
from ..structured_logging.enhanced_logging_config import get_logger

# Removed: from ..persistence import get_persistence - now using async_persistence parameter
from ..utils.room_utils import extract_subzone_from_room_id

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..game.movement_service import MovementService

logger = get_logger(__name__)


class NPCMovementIntegration:
    """
    Integration layer for NPC movement with existing game systems.

    This class provides enhanced movement capabilities for NPCs that integrate
    with the existing MovementService and event system.
    """

    def __init__(self, event_bus: EventBus | None = None, persistence: AsyncPersistenceLayer | None = None) -> None:
        """
        Initialize NPC movement integration.

        Args:
            event_bus: Optional EventBus instance for publishing events
            persistence: Optional persistence layer instance
        """
        self.event_bus = event_bus
        if persistence is None:
            raise ValueError("persistence (async_persistence) is required for NPCMovementIntegration")
        self.persistence = persistence
        # Lazy import to avoid circular dependency
        # MovementService imports from services/ which imports npc_instance_service
        # which imports from npc/__init__ which imports this module
        self.movement_service: MovementService | None = None
        if event_bus:
            from ..game.movement_service import MovementService

            self.movement_service = MovementService(event_bus=event_bus, async_persistence=persistence)

        logger.debug("NPC movement integration initialized")

    def _validate_room_ids(self, npc_id: str, from_room_id: str, to_room_id: str) -> bool:
        """
        Validate room IDs for NPC movement.

        Args:
            npc_id: ID of the NPC
            from_room_id: Source room ID
            to_room_id: Destination room ID

        Returns:
            True if room IDs are valid, False otherwise
        """
        if not from_room_id or not to_room_id:
            logger.warning(
                "Invalid room IDs for NPC movement", npc_id=npc_id, from_room=from_room_id, to_room=to_room_id
            )
            return False

        if from_room_id == to_room_id:
            logger.debug("NPC already in target room", npc_id=npc_id, room_id=to_room_id)
            return False

        return True

    def _is_npc_in_combat(self, npc_id: str) -> bool:
        """Return True if the NPC is currently in combat (blocks normal movement)."""
        try:
            from ..services.combat_service import get_combat_service

            combat_service = get_combat_service()
            if combat_service and combat_service.is_npc_in_combat_sync(npc_id):
                return True
        except (ImportError, AttributeError, RuntimeError):
            pass
        return False

    def _get_room_objects(self, npc_id: str, from_room_id: str, to_room_id: str) -> tuple[Any, Any] | None:
        """
        Get room objects and validate they exist.

        Args:
            npc_id: ID of the NPC
            from_room_id: Source room ID
            to_room_id: Destination room ID

        Returns:
            Tuple of (from_room, to_room) if both exist, None otherwise
        """
        from_room = self.persistence.get_room_by_id(from_room_id)
        to_room = self.persistence.get_room_by_id(to_room_id)

        if not from_room:
            logger.warning("Source room not found", npc_id=npc_id, from_room=from_room_id)
            return None

        if not to_room:
            logger.warning("Destination room not found", npc_id=npc_id, to_room=to_room_id)
            return None

        return from_room, to_room

    def _update_room_occupancy(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Room occupancy update requires many parameters for context and state updates
        self, npc_id: str, from_room: Any, to_room: Any, from_room_id: str, to_room_id: str
    ) -> None:
        """
        Update room occupancy by removing NPC from source and adding to destination.

        Args:
            npc_id: ID of the NPC
            from_room: Source room object
            to_room: Destination room object
            from_room_id: Source room ID
            to_room_id: Destination room ID
        """
        if from_room.has_npc(npc_id):
            from_room.npc_left(npc_id, to_room_id=to_room_id)
            logger.debug("Removed NPC from source room", npc_id=npc_id, from_room=from_room_id, to_room=to_room_id)

        if not to_room.has_npc(npc_id):
            to_room.npc_entered(npc_id, from_room_id=from_room_id)
            logger.debug("Added NPC to destination room", npc_id=npc_id, from_room=from_room_id, to_room=to_room_id)

    def _update_npc_instance_room_tracking(self, npc_id: str, to_room_id: str) -> None:
        """
        Update NPC instance room tracking for occupant queries.

        Args:
            npc_id: ID of the NPC
            to_room_id: Destination room ID
        """
        try:
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                    npc_instance = lifecycle_manager.active_npcs[npc_id]
                    npc_instance.current_room = to_room_id
                    npc_instance.current_room_id = to_room_id  # type: ignore[attr-defined]  # Reason: NPCInstance has current_room_id attribute at runtime for room tracking, but mypy stubs don't reflect this dynamic attribute

                    if not npc_instance.current_room or npc_instance.current_room != to_room_id:
                        logger.error(
                            "Failed to update NPC room tracking correctly",
                            npc_id=npc_id,
                            to_room_id=to_room_id,
                            current_room=getattr(npc_instance, "current_room", None),
                            current_room_id=getattr(npc_instance, "current_room_id", None),
                        )
                    else:
                        logger.debug(
                            "Updated NPC instance room tracking",
                            npc_id=npc_id,
                            new_room_id=to_room_id,
                        )
        except Exception as update_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC room tracking update errors unpredictable, must handle gracefully
            logger.warning(
                "Error updating NPC instance room tracking",
                npc_id=npc_id,
                error=str(update_error),
            )

    def move_npc_to_room(self, npc_id: str, from_room_id: str, to_room_id: str) -> bool:
        """
        Move an NPC to a different room with full integration.

        This method provides enhanced NPC movement that:
        - Blocks movement when NPC is in combat
        - Validates room existence
        - Updates room occupancy
        - Publishes movement events
        - Integrates with the movement service

        Args:
            npc_id: ID of the NPC to move
            from_room_id: Current room ID
            to_room_id: Destination room ID

        Returns:
            bool: True if movement was successful
        """
        try:
            if not self._validate_room_ids(npc_id, from_room_id, to_room_id):
                return False

            if self._is_npc_in_combat(npc_id):
                logger.debug(
                    "NPC movement blocked - NPC in combat",
                    npc_id=npc_id,
                    from_room=from_room_id,
                    to_room=to_room_id,
                )
                return False

            room_objects = self._get_room_objects(npc_id, from_room_id, to_room_id)
            if room_objects is None:
                return False

            from_room, to_room = room_objects

            self._update_room_occupancy(npc_id, from_room, to_room, from_room_id, to_room_id)
            self._update_npc_instance_room_tracking(npc_id, to_room_id)

            logger.info("NPC moved successfully", npc_id=npc_id, from_room=from_room_id, to_room=to_room_id)
            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC movement errors unpredictable, must return False
            logger.error("Error moving NPC", npc_id=npc_id, error=str(e))
            return False

    def _publish_movement_events(self, npc_id: str, from_room_id: str, to_room_id: str) -> None:
        """
        Publish NPC movement events.

        Args:
            npc_id: ID of the NPC
            from_room_id: Source room ID
            to_room_id: Destination room ID
        """
        try:
            # Only publish events if event bus is available
            if not self.event_bus:
                logger.debug("Event bus not available, skipping NPC movement events", npc_id=npc_id)
                return

            # Publish NPC left room event
            # AI Agent: timestamp and event_type are set automatically by BaseEvent (init=False)
            left_event = NPCLeftRoom(npc_id=npc_id, room_id=from_room_id, to_room_id=to_room_id)
            self.event_bus.publish(left_event)

            # Publish NPC entered room event
            # AI Agent: timestamp and event_type are set automatically by BaseEvent (init=False)
            entered_event = NPCEnteredRoom(
                npc_id=npc_id,
                room_id=to_room_id,
                from_room_id=from_room_id,
            )
            self.event_bus.publish(entered_event)

            logger.debug("Published NPC movement events", npc_id=npc_id, from_room=from_room_id, to_room=to_room_id)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event publishing errors unpredictable, must handle gracefully
            logger.error("Error publishing NPC movement events", npc_id=npc_id, error=str(e))

    def get_npc_room(self, npc_id: str) -> str | None:
        """
        Get the current room ID for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            Optional[str]: Room ID if found, None otherwise
        """
        try:
            # This would need to be implemented based on how NPCs are tracked
            # For now, return None as NPCs track their own room
            return None
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC room retrieval errors unpredictable, must return None
            logger.error("Error getting NPC room", npc_id=npc_id, error=str(e))
            return None

    def get_room_npcs(self, room_id: str) -> list[str]:
        """
        Get list of NPC IDs in a room.

        Args:
            room_id: ID of the room

        Returns:
            list[str]: List of NPC IDs in the room
        """
        try:
            room = self.persistence.get_room_by_id(room_id)
            if room:
                return list(room.get_npcs())
            return []
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room NPC retrieval errors unpredictable, must return empty list
            logger.error("Error getting room NPCs", room_id=room_id, error=str(e))
            return []

    def validate_npc_movement(self, npc_id: str, from_room_id: str, to_room_id: str) -> bool:
        """
        Validate that an NPC can move between rooms.

        Args:
            npc_id: ID of the NPC
            from_room_id: Source room ID
            to_room_id: Destination room ID

        Returns:
            bool: True if movement is valid
        """
        try:
            # Check if rooms exist
            from_room = self.persistence.get_room_by_id(from_room_id)
            to_room = self.persistence.get_room_by_id(to_room_id)

            if not from_room or not to_room:
                return False

            # Check if NPC is in source room
            if not from_room.has_npc(npc_id):
                logger.warning("NPC not in source room", npc_id=npc_id, from_room=from_room_id)
                return False

            # Check if destination room has space (could add capacity limits here)
            # For now, assume unlimited capacity

            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Movement validation errors unpredictable, must return False
            logger.error("Error validating NPC movement", npc_id=npc_id, error=str(e))
            return False

    def get_available_exits(self, room_id: str) -> dict[str, str]:
        """
        Get available exits from a room.

        Args:
            room_id: ID of the room

        Returns:
            dict[str, str]: Dictionary of direction -> room_id mappings
        """
        try:
            room = self.persistence.get_room_by_id(room_id)
            if room:
                result: dict[str, str] = cast(dict[str, str], room.exits)
                return result
            return {}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room exit retrieval errors unpredictable, must return empty dict
            logger.error("Error getting room exits", room_id=room_id, error=str(e))
            return {}

    def find_path_between_rooms(self, from_room_id: str, to_room_id: str) -> list[str] | None:
        """
        Find a path between two rooms.

        This is a simple implementation that could be enhanced with proper pathfinding.

        Args:
            from_room_id: Source room ID
            to_room_id: Destination room ID

        Returns:
            Optional[list[str]]: List of room IDs representing the path, or None if no path found
        """
        try:
            # Simple implementation - just return direct connection if it exists
            from_room = self.persistence.get_room_by_id(from_room_id)
            if from_room and to_room_id in from_room.exits.values():
                return [from_room_id, to_room_id]

            # Could implement proper pathfinding here
            return None

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Path finding errors unpredictable, must return None
            logger.error("Error finding path between rooms", from_room=from_room_id, to_room=to_room_id, error=str(e))
            return None

    def validate_subzone_boundary(self, npc_sub_zone_id: str, destination_room_id: str) -> bool:
        """
        Validate that a destination room is within the NPC's allowed subzone.

        This method ensures NPCs cannot move outside their designated subzone,
        maintaining proper territorial boundaries as documented in the Pnakotic Manuscripts.

        Args:
            npc_sub_zone_id: The subzone ID from the NPC definition (stable_id format)
            destination_room_id: The room ID of the destination room

        Returns:
            bool: True if the destination room is within the NPC's subzone, False otherwise
        """
        try:
            if not npc_sub_zone_id or not destination_room_id:
                logger.warning(
                    "Invalid subzone or room ID for boundary validation",
                    npc_sub_zone_id=npc_sub_zone_id,
                    destination_room_id=destination_room_id,
                )
                return False

            # Get the destination room to check its subzone
            destination_room = self.persistence.get_room_by_id(destination_room_id)
            if not destination_room:
                logger.warning(
                    "Destination room not found for subzone validation", destination_room_id=destination_room_id
                )
                return False

            # Extract subzone from destination room
            # Try using Room's sub_zone attribute first (more reliable)
            destination_subzone = destination_room.sub_zone if hasattr(destination_room, "sub_zone") else None

            # Fallback to extracting from room_id if sub_zone attribute not available
            if not destination_subzone:
                destination_subzone = extract_subzone_from_room_id(destination_room_id)

            if not destination_subzone:
                logger.warning(
                    "Could not determine subzone for destination room",
                    destination_room_id=destination_room_id,
                )
                return False

            # Compare subzones (both should be stable_id format strings)
            is_valid = destination_subzone == npc_sub_zone_id

            if not is_valid:
                logger.debug(
                    "Subzone boundary validation failed",
                    npc_sub_zone_id=npc_sub_zone_id,
                    destination_subzone=destination_subzone,
                    destination_room_id=destination_room_id,
                )

            return is_valid

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Boundary validation errors unpredictable, must return False
            logger.error(
                "Error validating subzone boundary",
                npc_sub_zone_id=npc_sub_zone_id,
                destination_room_id=destination_room_id,
                error=str(e),
            )
            return False
