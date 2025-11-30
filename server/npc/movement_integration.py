"""
NPC movement integration with existing game systems.

This module provides integration between NPCs and the existing movement system,
including event publishing and room management.

As noted in the Pnakotic Manuscripts, proper movement integration is essential
for maintaining the integrity of our eldritch dimensional architecture.
"""

from ..events import EventBus, NPCEnteredRoom, NPCLeftRoom
from ..game.movement_service import MovementService
from ..logging.enhanced_logging_config import get_logger
from ..persistence import get_persistence

logger = get_logger(__name__)


class NPCMovementIntegration:
    """
    Integration layer for NPC movement with existing game systems.

    This class provides enhanced movement capabilities for NPCs that integrate
    with the existing MovementService and event system.
    """

    def __init__(self, event_bus: EventBus | None = None, persistence=None):
        """
        Initialize NPC movement integration.

        Args:
            event_bus: Optional EventBus instance for publishing events
            persistence: Optional persistence layer instance
        """
        self.event_bus = event_bus
        self.persistence = persistence or get_persistence(event_bus)
        self.movement_service = MovementService(event_bus) if event_bus else None

        logger.debug("NPC movement integration initialized")

    def move_npc_to_room(self, npc_id: str, from_room_id: str, to_room_id: str) -> bool:
        """
        Move an NPC to a different room with full integration.

        This method provides enhanced NPC movement that:
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
            if not from_room_id or not to_room_id:
                logger.warning(
                    "Invalid room IDs for NPC movement", npc_id=npc_id, from_room=from_room_id, to_room=to_room_id
                )
                return False

            if from_room_id == to_room_id:
                logger.debug("NPC already in target room", npc_id=npc_id, room_id=to_room_id)
                return True

            # Get room objects
            from_room = self.persistence.get_room(from_room_id)
            to_room = self.persistence.get_room(to_room_id)

            if not from_room:
                logger.warning("Source room not found", npc_id=npc_id, from_room=from_room_id)
                return False

            if not to_room:
                logger.warning("Destination room not found", npc_id=npc_id, to_room=to_room_id)
                return False

            # Remove NPC from source room
            if from_room.has_npc(npc_id):
                from_room.npc_left(npc_id)
                logger.debug("Removed NPC from source room", npc_id=npc_id, from_room=from_room_id)

            # Add NPC to destination room
            if not to_room.has_npc(npc_id):
                to_room.npc_entered(npc_id)
                logger.debug("Added NPC to destination room", npc_id=npc_id, to_room=to_room_id)

            # CRITICAL FIX: Update NPC instance room tracking for occupant queries
            # Get NPC instance from lifecycle manager and update current_room/current_room_id
            try:
                from ..services.npc_instance_service import get_npc_instance_service

                npc_instance_service = get_npc_instance_service()
                if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                    lifecycle_manager = npc_instance_service.lifecycle_manager
                    if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                        npc_instance = lifecycle_manager.active_npcs[npc_id]
                        npc_instance.current_room = to_room_id
                        # Also set current_room_id for compatibility
                        if hasattr(npc_instance, "current_room_id"):
                            npc_instance.current_room_id = to_room_id
                        logger.debug(
                            "Updated NPC instance room tracking",
                            npc_id=npc_id,
                            new_room_id=to_room_id,
                        )
            except Exception as update_error:
                logger.warning(
                    "Error updating NPC instance room tracking",
                    npc_id=npc_id,
                    error=str(update_error),
                )

            # Event publication is handled by Room methods; avoid duplicate publishes

            logger.info("NPC moved successfully", npc_id=npc_id, from_room=from_room_id, to_room=to_room_id)
            return True

        except Exception as e:
            logger.error("Error moving NPC", npc_id=npc_id, error=str(e))
            return False

    def _publish_movement_events(self, npc_id: str, from_room_id: str, to_room_id: str):
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

        except Exception as e:
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
        except Exception as e:
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
            room = self.persistence.get_room(room_id)
            if room:
                return room.get_npcs()
            return []
        except Exception as e:
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
            from_room = self.persistence.get_room(from_room_id)
            to_room = self.persistence.get_room(to_room_id)

            if not from_room or not to_room:
                return False

            # Check if NPC is in source room
            if not from_room.has_npc(npc_id):
                logger.warning("NPC not in source room", npc_id=npc_id, from_room=from_room_id)
                return False

            # Check if destination room has space (could add capacity limits here)
            # For now, assume unlimited capacity

            return True

        except Exception as e:
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
            room = self.persistence.get_room(room_id)
            if room:
                return room.exits
            return {}
        except Exception as e:
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
            from_room = self.persistence.get_room(from_room_id)
            if from_room and to_room_id in from_room.exits.values():
                return [from_room_id, to_room_id]

            # Could implement proper pathfinding here
            return None

        except Exception as e:
            logger.error("Error finding path between rooms", from_room=from_room_id, to_room=to_room_id, error=str(e))
            return None
