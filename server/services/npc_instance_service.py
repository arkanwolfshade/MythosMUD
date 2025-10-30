"""
NPC Instance Management Service for MythosMUD.

This module provides high-level operations for managing NPC instances,
including spawning, despawning, movement, and status retrieval.

As documented in the Cultes des Goules, proper instance management is essential
for maintaining control over the eldritch entities that inhabit our world.
"""

from typing import Any

from server.events.event_bus import EventBus
from server.npc.lifecycle_manager import NPCLifecycleManager
from server.npc.population_control import NPCPopulationController
from server.npc.spawning_service import NPCSpawningService
from server.npc_database import get_npc_session
from server.services.npc_service import npc_service

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class NPCInstanceService:
    """Service for managing NPC instances."""

    def __init__(
        self,
        lifecycle_manager: NPCLifecycleManager,
        spawning_service: NPCSpawningService,
        population_controller: NPCPopulationController,
        event_bus: EventBus,
    ):
        """
        Initialize the NPC instance service.

        Args:
            lifecycle_manager: NPC lifecycle manager
            spawning_service: NPC spawning service
            population_controller: NPC population controller
            event_bus: Event bus for publishing events
        """
        self.lifecycle_manager = lifecycle_manager
        self.spawning_service = spawning_service
        self.population_controller = population_controller
        self.event_bus = event_bus

    async def spawn_npc_instance(
        self,
        definition_id: int,
        room_id: str,
        reason: str = "admin_spawn",
    ) -> dict[str, Any]:
        """
        Spawn a new NPC instance.

        Args:
            definition_id: ID of the NPC definition to spawn
            room_id: Room where the NPC should be spawned
            reason: Reason for spawning

        Returns:
            Dictionary with spawn result information

        Raises:
            ValueError: If NPC definition not found
            RuntimeError: If spawning fails
        """
        try:
            # Get the NPC definition from database
            async for session in get_npc_session():
                definition = await npc_service.get_npc_definition(session, definition_id)
                if not definition:
                    raise ValueError(f"NPC definition with ID {definition_id} not found")
                break

            # Spawn the NPC using the population controller to ensure proper population limits
            # The population controller will handle all spawning through the lifecycle manager
            npc_id = self.population_controller._spawn_npc(definition, room_id)

            if not npc_id:
                raise RuntimeError(f"Failed to spawn NPC from definition {definition_id}")

            logger.info(
                "Spawned NPC instance",
                npc_id=npc_id,
                definition_id=definition_id,
                definition_name=definition.name,
                room_id=room_id,
                reason=reason,
            )

            return {
                "success": True,
                "npc_id": npc_id,
                "definition_id": definition_id,
                "definition_name": definition.name,
                "room_id": room_id,
                "message": f"Successfully spawned {definition.name} in {room_id}",
            }

        except Exception as e:
            logger.error(
                "Error spawning NPC instance",
                error=str(e),
                definition_id=definition_id,
                room_id=room_id,
            )
            raise

    async def despawn_npc_instance(
        self,
        npc_id: str,
        reason: str = "admin_despawn",
    ) -> dict[str, Any]:
        """
        Despawn an NPC instance.

        Args:
            npc_id: ID of the NPC to despawn
            reason: Reason for despawning

        Returns:
            Dictionary with despawn result information

        Raises:
            ValueError: If NPC not found
            RuntimeError: If despawning fails
        """
        try:
            # Check if NPC exists
            if npc_id not in self.lifecycle_manager.active_npcs:
                raise ValueError(f"NPC instance {npc_id} not found")

            # Get NPC info before despawning
            npc_instance = self.lifecycle_manager.active_npcs[npc_id]
            npc_name = getattr(npc_instance, "name", "Unknown")
            room_id = getattr(npc_instance, "current_room_id", "Unknown")

            # Despawn the NPC using the lifecycle manager
            success = self.lifecycle_manager.despawn_npc(npc_id, reason)

            if not success:
                raise RuntimeError(f"Failed to despawn NPC {npc_id}")

            logger.info(
                "Despawned NPC instance",
                npc_id=npc_id,
                npc_name=npc_name,
                room_id=room_id,
                reason=reason,
            )

            return {
                "success": True,
                "npc_id": npc_id,
                "npc_name": npc_name,
                "room_id": room_id,
                "message": f"Successfully despawned {npc_name}",
            }

        except Exception as e:
            logger.error(
                "Error despawning NPC instance",
                error=str(e),
                npc_id=npc_id,
            )
            raise

    async def move_npc_instance(
        self,
        npc_id: str,
        new_room_id: str,
        reason: str = "admin_move",
    ) -> dict[str, Any]:
        """
        Move an NPC instance to a different room.

        Args:
            npc_id: ID of the NPC to move
            new_room_id: New room ID for the NPC
            reason: Reason for moving

        Returns:
            Dictionary with move result information

        Raises:
            ValueError: If NPC not found
            RuntimeError: If movement fails
        """
        try:
            # Check if NPC exists
            if npc_id not in self.lifecycle_manager.active_npcs:
                raise ValueError(f"NPC instance {npc_id} not found")

            # Get NPC info
            npc_instance = self.lifecycle_manager.active_npcs[npc_id]
            npc_name = getattr(npc_instance, "name", "Unknown")
            old_room_id = getattr(npc_instance, "current_room_id", "Unknown")

            # Move the NPC
            # Note: This would need to be implemented in the NPC instance class
            # For now, we'll simulate the move
            if hasattr(npc_instance, "move_to_room"):
                npc_instance.move_to_room(new_room_id)
            else:
                # Update the room ID directly if move_to_room method doesn't exist
                npc_instance.current_room_id = new_room_id

            logger.info(
                "Moved NPC instance",
                npc_id=npc_id,
                npc_name=npc_name,
                old_room_id=old_room_id,
                new_room_id=new_room_id,
                reason=reason,
            )

            return {
                "success": True,
                "npc_id": npc_id,
                "npc_name": npc_name,
                "old_room_id": old_room_id,
                "new_room_id": new_room_id,
                "message": f"Successfully moved {npc_name} from {old_room_id} to {new_room_id}",
            }

        except Exception as e:
            logger.error(
                "Error moving NPC instance",
                error=str(e),
                npc_id=npc_id,
                new_room_id=new_room_id,
            )
            raise

    async def get_npc_instances(self) -> list[dict[str, Any]]:
        """
        Get all active NPC instances.

        Returns:
            List of NPC instance information
        """
        try:
            instances = []

            for npc_id, npc_instance in self.lifecycle_manager.active_npcs.items():
                # Extract information from the NPC instance
                instance_info = {
                    "npc_id": npc_id,
                    "name": getattr(npc_instance, "name", "Unknown"),
                    "npc_type": getattr(npc_instance, "npc_type", "unknown"),
                    "current_room_id": getattr(npc_instance, "current_room_id", "Unknown"),
                    "is_alive": getattr(npc_instance, "is_alive", lambda: True)(),
                    "stats": getattr(npc_instance, "stats", {}),
                }

                # Add lifecycle information if available
                if npc_id in self.lifecycle_manager.lifecycle_records:
                    record = self.lifecycle_manager.lifecycle_records[npc_id]
                    instance_info.update(
                        {
                            "lifecycle_state": record.current_state.value,
                            "spawn_time": record.spawn_time,
                            "last_activity": record.last_activity,
                        }
                    )

                instances.append(instance_info)

            logger.info("Retrieved NPC instances")
            return instances

        except Exception as e:
            logger.error("Error retrieving NPC instances", error=str(e))
            raise

    async def get_npc_stats(self, npc_id: str) -> dict[str, Any]:
        """
        Get detailed stats for a specific NPC instance.

        Args:
            npc_id: ID of the NPC

        Returns:
            Dictionary with NPC stats and information

        Raises:
            ValueError: If NPC not found
        """
        try:
            # Check if NPC exists
            if npc_id not in self.lifecycle_manager.active_npcs:
                raise ValueError(f"NPC instance {npc_id} not found")

            npc_instance = self.lifecycle_manager.active_npcs[npc_id]

            # Get basic stats
            stats = {
                "npc_id": npc_id,
                "name": getattr(npc_instance, "name", "Unknown"),
                "npc_type": getattr(npc_instance, "npc_type", "unknown"),
                "current_room_id": getattr(npc_instance, "current_room_id", "Unknown"),
                "is_alive": getattr(npc_instance, "is_alive", lambda: True)(),
                "stats": getattr(npc_instance, "stats", {}),
            }

            # Add lifecycle information if available
            if npc_id in self.lifecycle_manager.lifecycle_records:
                record = self.lifecycle_manager.lifecycle_records[npc_id]
                stats.update(
                    {
                        "lifecycle_state": record.current_state.value,
                        "spawn_time": record.spawn_time,
                        "last_activity": record.last_activity,
                        "spawn_count": record.spawn_count,
                        "despawn_count": record.despawn_count,
                    }
                )

            logger.info("Retrieved NPC stats")
            return stats

        except Exception as e:
            logger.error("Error retrieving NPC stats", error=str(e))
            raise

    async def get_population_stats(self) -> dict[str, Any]:
        """
        Get NPC population statistics.

        Returns:
            Dictionary with population statistics
        """
        try:
            # Get active NPC instances
            active_instances = self.lifecycle_manager.active_npcs

            # Count by type
            by_type = {}
            by_zone = {}
            total_npcs = len(active_instances)

            for _npc_id, npc_instance in active_instances.items():
                npc_type = getattr(npc_instance, "npc_type", "unknown")
                current_room_id = getattr(npc_instance, "current_room_id", "unknown")

                # Extract zone from room_id (assuming format like "earth_arkhamcity_downtown_001")
                zone_key = self._extract_zone_from_room_id(current_room_id)

                # Count by type
                by_type[npc_type] = by_type.get(npc_type, 0) + 1

                # Count by zone
                by_zone[zone_key] = by_zone.get(zone_key, 0) + 1

            # Get spawn queue size from lifecycle manager
            spawn_queue_size = len(getattr(self.lifecycle_manager, "respawn_queue", {}))

            stats = {
                "total_npcs": total_npcs,
                "by_type": by_type,
                "by_zone": by_zone,
                "active_instances": total_npcs,
                "spawn_queue_size": spawn_queue_size,
            }

            logger.info("Retrieved NPC population stats")
            return stats

        except Exception as e:
            logger.error("Error retrieving NPC population stats", error=str(e))
            raise

    async def get_zone_stats(self) -> dict[str, Any]:
        """
        Get NPC zone statistics.

        Returns:
            Dictionary with zone statistics
        """
        try:
            # Get active NPC instances
            active_instances = self.lifecycle_manager.active_npcs

            # Group by zone
            zone_data = {}
            total_npcs = 0

            for npc_id, npc_instance in active_instances.items():
                current_room_id = getattr(npc_instance, "current_room_id", "unknown")
                zone_key = self._extract_zone_from_room_id(current_room_id)

                if zone_key not in zone_data:
                    zone_data[zone_key] = {
                        "zone_key": zone_key,
                        "npc_count": 0,
                        "spawn_modifier": 1.0,  # Default spawn modifier
                        "active_npcs": [],
                    }

                zone_data[zone_key]["npc_count"] += 1
                zone_data[zone_key]["active_npcs"].append(npc_id)
                total_npcs += 1

            # Convert to list format
            zones = list(zone_data.values())

            stats = {
                "zones": zones,
                "total_zones": len(zones),
                "total_npcs": total_npcs,
            }

            logger.info("Retrieved NPC zone stats")
            return stats

        except Exception as e:
            logger.error("Error retrieving NPC zone stats", error=str(e))
            raise

    async def get_system_stats(self) -> dict[str, Any]:
        """
        Get system-wide NPC statistics.

        Returns:
            Dictionary with system statistics
        """
        try:
            # Get basic system stats
            active_npcs = len(self.lifecycle_manager.active_npcs)
            spawn_queue_size = len(getattr(self.lifecycle_manager, "respawn_queue", {}))

            # Get lifecycle manager status
            lifecycle_status = "active" if hasattr(self.lifecycle_manager, "lifecycle_records") else "inactive"

            # Get population controller status
            population_status = "active" if hasattr(self.population_controller, "zone_configurations") else "inactive"

            # Determine overall system status
            system_status = "healthy" if active_npcs > 0 or spawn_queue_size > 0 else "idle"

            stats = {
                "system_status": system_status,
                "active_npcs": active_npcs,
                "spawn_queue_size": spawn_queue_size,
                "lifecycle_manager_status": lifecycle_status,
                "population_controller_status": population_status,
                "spawning_service_status": "active",
                "last_update": "2025-01-01T12:00:00Z",  # Could be made dynamic
            }

            logger.info("Retrieved NPC system stats", active_npcs=active_npcs, system_status=system_status)
            return stats

        except Exception as e:
            logger.error("Error retrieving NPC system stats", error=str(e))
            raise

    def _extract_zone_from_room_id(self, room_id: str) -> str:
        """
        Extract zone key from room ID.

        Args:
            room_id: Room ID like "earth_arkhamcity_downtown_001" or "earth_arkham"

        Returns:
            Zone key like "arkham/city" or "arkham/unknown" for short format
        """
        try:
            # Split room_id by underscores
            parts = room_id.split("_")

            # Look for zone patterns (e.g., "arkham", "city")
            if len(parts) >= 3:
                # Assume format: earth_zone_subzone_room
                zone = parts[1] if len(parts) > 1 else "unknown"
                subzone = parts[2] if len(parts) > 2 else "unknown"
                return f"{zone}/{subzone}"
            elif len(parts) == 2:
                # Short format: earth_zone
                return f"{parts[1]}/unknown"
            else:
                return "unknown/unknown"

        except (OSError, ValueError, TypeError) as e:
            logger.error("Error getting NPC location", room_id=room_id, error=str(e), error_type=type(e).__name__)
            return "unknown/unknown"


# Global instance - will be initialized by the application
npc_instance_service: NPCInstanceService | None = None


def get_npc_instance_service() -> NPCInstanceService:
    """Get the global NPC instance service."""
    if npc_instance_service is None:
        raise RuntimeError("NPC instance service not initialized")
    return npc_instance_service


def initialize_npc_instance_service(
    lifecycle_manager: NPCLifecycleManager,
    spawning_service: NPCSpawningService,
    population_controller: NPCPopulationController,
    event_bus: EventBus,
) -> None:
    """Initialize the global NPC instance service."""
    global npc_instance_service
    npc_instance_service = NPCInstanceService(
        lifecycle_manager=lifecycle_manager,
        spawning_service=spawning_service,
        population_controller=population_controller,
        event_bus=event_bus,
    )
    logger.info("NPC instance service initialized")
