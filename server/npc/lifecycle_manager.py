"""
NPC Lifecycle Management System for MythosMUD.

This module implements comprehensive NPC lifecycle management including
spawning, despawning, respawning, and state tracking throughout an NPC's
existence in the game world.

As documented in the Cultes des Goules, proper lifecycle management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world. The lifecycle manager ensures that NPCs
have proper birth, existence, and eventual return to the void.
"""

import logging
import time
from enum import Enum
from typing import Any

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom
from server.models.npc import NPCDefinition
from server.npc.behaviors import NPCBase
from server.npc.population_control import NPCPopulationController
from server.npc.spawning_service import NPCSpawningService

logger = logging.getLogger(__name__)


class NPCLifecycleState(str, Enum):
    """Enumeration of NPC lifecycle states."""

    SPAWNING = "spawning"
    ACTIVE = "active"
    INACTIVE = "inactive"
    DESPAWNING = "despawning"
    DESPAWNED = "despawned"
    RESPAWNING = "respawning"
    ERROR = "error"


class NPCLifecycleEvent(str, Enum):
    """Enumeration of NPC lifecycle events."""

    SPAWNED = "spawned"
    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"
    DESPAWNED = "despawned"
    RESPAWNED = "respawned"
    ERROR_OCCURRED = "error_occurred"


class NPCLifecycleRecord:
    """Record of an NPC's lifecycle events and state changes."""

    def __init__(self, npc_id: str, definition: NPCDefinition):
        """
        Initialize lifecycle record.

        Args:
            npc_id: Unique identifier for the NPC
            definition: NPC definition
        """
        self.npc_id = npc_id
        self.definition = definition
        self.current_state = NPCLifecycleState.SPAWNING
        self.created_at = time.time()
        self.last_updated = time.time()
        self.events: list[dict[str, Any]] = []
        self.spawn_count = 0
        self.despawn_count = 0
        self.total_active_time = 0.0
        self.last_active_time = 0.0
        self.error_count = 0
        self.last_error = None

    def add_event(self, event_type: NPCLifecycleEvent, details: dict[str, Any] | None = None) -> None:
        """
        Add a lifecycle event to the record.

        Args:
            event_type: Type of lifecycle event
            details: Additional event details
        """
        event = {
            "event_type": event_type,
            "timestamp": time.time(),
            "state": self.current_state,
            "details": details or {},
        }
        self.events.append(event)
        self.last_updated = time.time()

        # Update counters
        if event_type == NPCLifecycleEvent.SPAWNED:
            self.spawn_count += 1
        elif event_type == NPCLifecycleEvent.DESPAWNED:
            self.despawn_count += 1
        elif event_type == NPCLifecycleEvent.ERROR_OCCURRED:
            self.error_count += 1
            self.last_error = details

    def change_state(self, new_state: NPCLifecycleState, reason: str = "") -> None:
        """
        Change the NPC's lifecycle state.

        Args:
            new_state: New lifecycle state
            reason: Reason for state change
        """
        old_state = self.current_state
        self.current_state = new_state
        self.last_updated = time.time()

        # Track active time
        if old_state == NPCLifecycleState.ACTIVE:
            self.total_active_time += time.time() - self.last_active_time
        elif new_state == NPCLifecycleState.ACTIVE:
            self.last_active_time = time.time()

        # Add state change event
        self.add_event(
            NPCLifecycleEvent.ACTIVATED if new_state == NPCLifecycleState.ACTIVE else NPCLifecycleEvent.DEACTIVATED,
            {"old_state": old_state, "new_state": new_state, "reason": reason},
        )

    def get_statistics(self) -> dict[str, Any]:
        """
        Get lifecycle statistics for this NPC.

        Returns:
            Dictionary containing lifecycle statistics
        """
        current_time = time.time()
        age = current_time - self.created_at

        return {
            "npc_id": self.npc_id,
            "definition_name": self.definition.name,
            "npc_type": self.definition.npc_type,
            "current_state": self.current_state,
            "age_seconds": age,
            "spawn_count": self.spawn_count,
            "despawn_count": self.despawn_count,
            "total_active_time": self.total_active_time,
            "error_count": self.error_count,
            "last_error": self.last_error,
            "events_count": len(self.events),
            "created_at": self.created_at,
            "last_updated": self.last_updated,
        }


class NPCLifecycleManager:
    """
    Main manager for NPC lifecycle operations.

    This class coordinates spawning, despawning, respawning, and state management
    for all NPCs in the game world, ensuring proper lifecycle tracking and
    resource management.
    """

    def __init__(
        self,
        event_bus: EventBus,
        population_controller: NPCPopulationController,
        spawning_service: NPCSpawningService,
    ):
        """
        Initialize the NPC lifecycle manager.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            population_controller: Population controller for managing NPC populations
            spawning_service: Spawning service for creating NPC instances
        """
        self.event_bus = event_bus
        self.population_controller = population_controller
        self.spawning_service = spawning_service

        # Lifecycle tracking
        self.lifecycle_records: dict[str, NPCLifecycleRecord] = {}
        self.active_npcs: dict[str, NPCBase] = {}
        self.respawn_queue: dict[str, dict[str, Any]] = {}  # npc_id -> respawn_data

        # Configuration
        self.default_respawn_delay = 300.0  # 5 minutes
        self.max_respawn_attempts = 3
        self.cleanup_interval = 3600.0  # 1 hour
        self.last_cleanup = time.time()

        # Subscribe to relevant events
        self._subscribe_to_events()

        logger.info("NPC Lifecycle Manager initialized")

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered_room)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left_room)

    def _handle_npc_entered_room(self, event: NPCEnteredRoom) -> None:
        """Handle NPC entering a room."""
        if event.npc_id in self.lifecycle_records:
            record = self.lifecycle_records[event.npc_id]
            if record.current_state == NPCLifecycleState.SPAWNING:
                record.change_state(NPCLifecycleState.ACTIVE, "entered room")
                record.add_event(NPCLifecycleEvent.SPAWNED, {"room_id": event.room_id})

    def _handle_npc_left_room(self, event: NPCLeftRoom) -> None:
        """Handle NPC leaving a room."""
        if event.npc_id in self.lifecycle_records:
            record = self.lifecycle_records[event.npc_id]
            record.add_event(NPCLifecycleEvent.DEACTIVATED, {"room_id": event.room_id})

    def spawn_npc(self, definition: NPCDefinition, room_id: str, reason: str = "manual") -> str | None:
        """
        Spawn an NPC instance.

        Args:
            definition: NPC definition to spawn
            room_id: Room where NPC should be spawned
            reason: Reason for spawning

        Returns:
            NPC ID if successful, None if failed
        """
        try:
            # Check if we can spawn this NPC
            if not self._can_spawn_npc(definition, room_id):
                logger.warning(f"Cannot spawn NPC {definition.name} in {room_id}")
                return None

            # Generate NPC ID
            npc_id = self._generate_npc_id(definition, room_id)

            # Create lifecycle record
            record = NPCLifecycleRecord(npc_id, definition)
            record.add_event(NPCLifecycleEvent.SPAWNED, {"room_id": room_id, "reason": reason})
            self.lifecycle_records[npc_id] = record

            # Create NPC instance
            npc_instance = self.spawning_service._create_npc_instance(definition, room_id)
            if not npc_instance:
                record.change_state(NPCLifecycleState.ERROR, "Failed to create NPC instance")
                record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": "Failed to create NPC instance"})
                return None

            # Store NPC instance
            self.active_npcs[npc_id] = npc_instance
            npc_instance.npc_id = npc_id
            npc_instance.spawned_at = time.time()

            # Update population controller
            self.population_controller._spawn_npc(definition, room_id)

            # Publish NPC entered room event
            event = NPCEnteredRoom(timestamp=None, event_type="", npc_id=npc_id, room_id=room_id)
            self.event_bus.publish(event)

            logger.info(f"Successfully spawned NPC: {npc_id} ({definition.name}) in {room_id}")

            return npc_id

        except Exception as e:
            logger.error(f"Failed to spawn NPC {definition.name}: {str(e)}")
            if npc_id in self.lifecycle_records:
                record = self.lifecycle_records[npc_id]
                record.change_state(NPCLifecycleState.ERROR, str(e))
                record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": str(e)})
            return None

    def despawn_npc(self, npc_id: str, reason: str = "manual") -> bool:
        """
        Despawn an NPC instance.

        Args:
            npc_id: ID of the NPC to despawn
            reason: Reason for despawning

        Returns:
            True if NPC was despawned successfully
        """
        if npc_id not in self.lifecycle_records:
            logger.warning(f"Attempted to despawn non-existent NPC: {npc_id}")
            return False

        try:
            record = self.lifecycle_records[npc_id]
            record.change_state(NPCLifecycleState.DESPAWNING, reason)

            # Get NPC instance
            npc_instance = self.active_npcs.get(npc_id)
            if npc_instance:
                room_id = getattr(npc_instance, "room_id", "unknown")

                # Publish NPC left room event
                event = NPCLeftRoom(timestamp=None, event_type="", npc_id=npc_id, room_id=room_id)
                self.event_bus.publish(event)

                # Remove from active NPCs
                del self.active_npcs[npc_id]

            # Update population controller
            self.population_controller.despawn_npc(npc_id)

            # Update lifecycle record
            record.change_state(NPCLifecycleState.DESPAWNED, reason)
            record.add_event(NPCLifecycleEvent.DESPAWNED, {"reason": reason})

            logger.info(f"Successfully despawned NPC: {npc_id} (reason: {reason})")

            return True

        except Exception as e:
            logger.error(f"Failed to despawn NPC {npc_id}: {str(e)}")
            if npc_id in self.lifecycle_records:
                record = self.lifecycle_records[npc_id]
                record.change_state(NPCLifecycleState.ERROR, str(e))
                record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": str(e)})
            return False

    def respawn_npc(self, npc_id: str, delay: float | None = None, reason: str = "automatic") -> bool:
        """
        Schedule an NPC for respawning.

        Args:
            npc_id: ID of the NPC to respawn
            delay: Respawn delay in seconds (uses default if None)
            reason: Reason for respawning

        Returns:
            True if respawn was scheduled successfully
        """
        if npc_id not in self.lifecycle_records:
            logger.warning(f"Attempted to respawn non-existent NPC: {npc_id}")
            return False

        try:
            record = self.lifecycle_records[npc_id]
            definition = record.definition

            # Check if NPC is already scheduled for respawn
            if npc_id in self.respawn_queue:
                logger.debug(f"NPC {npc_id} is already scheduled for respawn")
                return True

            # Determine respawn delay
            respawn_delay = delay or self.default_respawn_delay

            # Schedule respawn
            respawn_data = {
                "npc_id": npc_id,
                "definition": definition,
                "room_id": getattr(self.active_npcs.get(npc_id), "room_id", "unknown"),
                "scheduled_time": time.time() + respawn_delay,
                "reason": reason,
                "attempts": 0,
            }

            self.respawn_queue[npc_id] = respawn_data

            # Update lifecycle record
            record.change_state(NPCLifecycleState.RESPAWNING, reason)
            record.add_event(NPCLifecycleEvent.RESPAWNED, {"delay": respawn_delay, "reason": reason})

            logger.info(f"Scheduled respawn for NPC: {npc_id} in {respawn_delay} seconds")

            return True

        except Exception as e:
            logger.error(f"Failed to schedule respawn for NPC {npc_id}: {str(e)}")
            if npc_id in self.lifecycle_records:
                record = self.lifecycle_records[npc_id]
                record.change_state(NPCLifecycleState.ERROR, str(e))
                record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": str(e)})
            return False

    def process_respawn_queue(self) -> int:
        """
        Process the respawn queue and spawn NPCs that are ready.

        Returns:
            Number of NPCs respawned
        """
        current_time = time.time()
        respawned_count = 0
        npcs_to_remove = []

        for npc_id, respawn_data in self.respawn_queue.items():
            if current_time >= respawn_data["scheduled_time"]:
                # Attempt to respawn
                success = self._attempt_respawn(npc_id, respawn_data)
                if success:
                    respawned_count += 1
                    npcs_to_remove.append(npc_id)
                else:
                    # Increment attempt count
                    respawn_data["attempts"] += 1
                    if respawn_data["attempts"] >= self.max_respawn_attempts:
                        logger.warning(f"Max respawn attempts reached for NPC {npc_id}")
                        npcs_to_remove.append(npc_id)

        # Remove processed NPCs from queue
        for npc_id in npcs_to_remove:
            del self.respawn_queue[npc_id]

        return respawned_count

    def _attempt_respawn(self, npc_id: str, respawn_data: dict[str, Any]) -> bool:
        """
        Attempt to respawn an NPC.

        Args:
            npc_id: ID of the NPC to respawn
            respawn_data: Respawn data

        Returns:
            True if respawn was successful
        """
        try:
            definition = respawn_data["definition"]
            room_id = respawn_data["room_id"]
            reason = respawn_data["reason"]

            # Check if we can spawn this NPC
            if not self._can_spawn_npc(definition, room_id):
                logger.debug(f"Cannot respawn NPC {npc_id} - spawn conditions not met")
                return False

            # Spawn the NPC
            new_npc_id = self.spawn_npc(definition, room_id, f"respawn: {reason}")
            if new_npc_id:
                # Update the lifecycle record with new ID if different
                if new_npc_id != npc_id:
                    if npc_id in self.lifecycle_records:
                        old_record = self.lifecycle_records[npc_id]
                        self.lifecycle_records[new_npc_id] = old_record
                        del self.lifecycle_records[npc_id]

                logger.info(f"Successfully respawned NPC: {npc_id} -> {new_npc_id}")
                return True

            return False

        except Exception as e:
            logger.error(f"Failed to respawn NPC {npc_id}: {str(e)}")
            return False

    def _can_spawn_npc(self, definition: NPCDefinition, room_id: str) -> bool:
        """
        Check if an NPC can be spawned.

        Args:
            definition: NPC definition
            room_id: Room where NPC should be spawned

        Returns:
            True if NPC can be spawned
        """
        # Check population limits
        zone_key = self.population_controller._get_zone_key_from_room_id(room_id)
        stats = self.population_controller.get_population_stats(zone_key)
        if stats:
            current_count = stats.npcs_by_type.get(definition.npc_type, 0)
            if not definition.can_spawn(current_count):
                return False

        # Additional checks can be added here (e.g., room capacity, special conditions)

        return True

    def _generate_npc_id(self, definition: NPCDefinition, room_id: str) -> str:
        """
        Generate a unique NPC ID.

        Args:
            definition: NPC definition
            room_id: Room where NPC is spawned

        Returns:
            Unique NPC ID
        """
        timestamp = int(time.time())
        import random

        random_suffix = random.randint(1000, 9999)
        return f"{definition.name.lower().replace(' ', '_')}_{room_id}_{timestamp}_{random_suffix}"

    def get_npc_lifecycle_record(self, npc_id: str) -> NPCLifecycleRecord | None:
        """
        Get lifecycle record for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            Lifecycle record or None if not found
        """
        return self.lifecycle_records.get(npc_id)

    def get_lifecycle_statistics(self) -> dict[str, Any]:
        """
        Get overall lifecycle statistics.

        Returns:
            Dictionary containing lifecycle statistics
        """
        total_npcs = len(self.lifecycle_records)
        active_npcs = len(self.active_npcs)
        respawn_queue_size = len(self.respawn_queue)

        # Count by state
        state_counts = {}
        for record in self.lifecycle_records.values():
            state = record.current_state
            state_counts[state] = state_counts.get(state, 0) + 1

        # Count by NPC type
        type_counts = {}
        for record in self.lifecycle_records.values():
            npc_type = record.definition.npc_type
            type_counts[npc_type] = type_counts.get(npc_type, 0) + 1

        # Calculate average statistics
        total_spawns = sum(record.spawn_count for record in self.lifecycle_records.values())
        total_despawns = sum(record.despawn_count for record in self.lifecycle_records.values())
        total_errors = sum(record.error_count for record in self.lifecycle_records.values())

        return {
            "total_npcs": total_npcs,
            "active_npcs": active_npcs,
            "respawn_queue_size": respawn_queue_size,
            "state_counts": state_counts,
            "type_counts": type_counts,
            "total_spawns": total_spawns,
            "total_despawns": total_despawns,
            "total_errors": total_errors,
            "average_spawns_per_npc": total_spawns / total_npcs if total_npcs > 0 else 0,
            "average_despawns_per_npc": total_despawns / total_npcs if total_npcs > 0 else 0,
            "error_rate": total_errors / total_npcs if total_npcs > 0 else 0,
        }

    def cleanup_old_records(self, max_age_seconds: int = 86400) -> int:
        """
        Clean up old lifecycle records.

        Args:
            max_age_seconds: Maximum age in seconds before cleanup

        Returns:
            Number of records cleaned up
        """
        current_time = time.time()
        records_to_remove = []

        for npc_id, record in self.lifecycle_records.items():
            age = current_time - record.created_at
            if age > max_age_seconds and record.current_state in [NPCLifecycleState.DESPAWNED, NPCLifecycleState.ERROR]:
                records_to_remove.append(npc_id)

        for npc_id in records_to_remove:
            del self.lifecycle_records[npc_id]

        if records_to_remove:
            logger.info(f"Cleaned up {len(records_to_remove)} old lifecycle records")

        return len(records_to_remove)

    def periodic_maintenance(self) -> dict[str, Any]:
        """
        Perform periodic maintenance tasks.

        Returns:
            Dictionary containing maintenance results
        """
        current_time = time.time()
        results = {}

        # Process respawn queue
        respawned_count = self.process_respawn_queue()
        results["respawned_npcs"] = respawned_count

        # Cleanup old records if enough time has passed
        if current_time - self.last_cleanup > self.cleanup_interval:
            cleaned_count = self.cleanup_old_records()
            results["cleaned_records"] = cleaned_count
            self.last_cleanup = current_time

        return results
