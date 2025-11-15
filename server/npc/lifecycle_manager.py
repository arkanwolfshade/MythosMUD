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

import time
from collections.abc import Sequence
from enum import Enum
from typing import Any

from server.events.event_bus import EventBus
from server.events.event_types import NPCDied, NPCEnteredRoom, NPCLeftRoom
from server.models.npc import NPCDefinition
from server.npc.behaviors import NPCBase
from server.npc.population_control import NPCPopulationController
from server.npc.spawning_service import NPCSpawningService
from server.schemas.calendar import ScheduleEntry

from ..logging.enhanced_logging_config import get_logger
from ..persistence import get_persistence

logger = get_logger(__name__)


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
        self.last_error: dict[str, Any] | None = None

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
        population_controller: NPCPopulationController | None,
        spawning_service: NPCSpawningService,
        persistence=None,
    ):
        """
        Initialize the NPC lifecycle manager.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            population_controller: Population controller for managing NPC populations
            spawning_service: Spawning service for creating NPC instances
            persistence: Persistence layer for room access (optional, for proper room state mutation)
        """
        self.event_bus = event_bus
        self.population_controller = population_controller
        self.spawning_service = spawning_service
        self.persistence = persistence

        # Lifecycle tracking
        self.lifecycle_records: dict[str, NPCLifecycleRecord] = {}
        self.active_npcs: dict[str, NPCBase] = {}
        self.respawn_queue: dict[str, dict[str, Any]] = {}  # npc_id -> respawn_data
        self.death_suppression: dict[str, float] = {}  # npc_id -> death_timestamp
        self.active_schedule_ids: list[str] = []

        # Configuration - Import values from NPCMaintenanceConfig for consistency
        # AI Agent: CRITICAL FIX - Use configuration values instead of hardcoded values
        #           This ensures respawn delays and maintenance intervals can be adjusted
        #           centrally without modifying lifecycle manager code
        from ..config.npc_config import NPCMaintenanceConfig

        self.default_respawn_delay = NPCMaintenanceConfig.DEFAULT_RESPAWN_DELAY
        self.death_suppression_duration = NPCMaintenanceConfig.DEATH_SUPPRESSION_DURATION
        self.max_respawn_attempts = NPCMaintenanceConfig.MAX_RESPAWN_ATTEMPTS
        self.cleanup_interval = NPCMaintenanceConfig.CLEANUP_INTERVAL
        self.last_cleanup = time.time()

        # Periodic spawn checking
        # AI Agent: Track last spawn check time per NPC definition to prevent spam spawning
        self.last_spawn_check: dict[int, float] = {}  # npc_definition_id -> last_check_timestamp

        # Subscribe to relevant events
        self._subscribe_to_events()

        logger.info("NPC Lifecycle Manager initialized", has_persistence=bool(persistence))

    def record_npc_death(self, npc_id: str) -> None:
        """
        Record the death of an NPC to suppress respawning for 30 seconds.

        Args:
            npc_id: ID of the NPC that died
        """
        current_time = time.monotonic()
        self.death_suppression[npc_id] = current_time
        logger.info(
            f"Recorded death of NPC {npc_id}, suppressing respawn for {self.death_suppression_duration} seconds"
        )

    def is_npc_death_suppressed(self, npc_id: str) -> bool:
        """
        Check if an NPC is currently under death suppression.

        Args:
            npc_id: ID of the NPC to check

        Returns:
            True if NPC is under death suppression, False otherwise
        """
        if npc_id not in self.death_suppression:
            return False

        death_time = self.death_suppression[npc_id]
        current_time = time.monotonic()
        suppression_elapsed = current_time - death_time

        if suppression_elapsed >= self.death_suppression_duration:
            # Suppression period has expired, clean up
            del self.death_suppression[npc_id]
            return False

        return True

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered_room)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left_room)
        self.event_bus.subscribe(NPCDied, self._handle_npc_died)

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

    def _handle_npc_died(self, event: NPCDied) -> None:
        """
        Handle NPC death by queuing for respawn.

        AI Agent: CRITICAL FIX - This event handler ensures NPCs are queued for respawn
                  when they die, respecting the configured respawn delay for ALL NPCs
                  (both required and optional).

        Args:
            event: NPCDied event containing death information
        """
        try:
            # Get NPC definition from lifecycle records
            if event.npc_id not in self.lifecycle_records:
                logger.warning("NPC died but no lifecycle record found", npc_id=event.npc_id)
                return

            record = self.lifecycle_records[event.npc_id]
            definition = record.definition

            # AI Agent: CRITICAL FIX - Do NOT despawn immediately!
            #           Despawning removes the NPC from lifecycle_records, which prevents
            #           XP calculation from finding the NPC's xp_value in base_stats.
            #           Instead, mark as inactive and queue for respawn. The respawn process
            #           will handle cleanup when it spawns a new instance.

            # Mark NPC as inactive but keep lifecycle record
            if event.npc_id in self.active_npcs:
                npc_instance = self.active_npcs[event.npc_id]
                # Remove from active NPCs (so it won't be processed)
                del self.active_npcs[event.npc_id]

                # Remove from room if we have persistence
                if self.persistence:
                    room_id = getattr(npc_instance, "room_id", event.room_id)
                    room = self.persistence.get_room(room_id)
                    if room:
                        room.npc_left(event.npc_id)
                        logger.debug("NPC removed from room after death", npc_id=event.npc_id, room_id=room_id)

                # Update population controller
                if self.population_controller:
                    self.population_controller.despawn_npc(event.npc_id)

            # Update lifecycle record state (but DON'T remove it yet)
            record.change_state(NPCLifecycleState.DESPAWNED, f"death: {event.cause}")
            record.add_event(NPCLifecycleEvent.DESPAWNED, {"reason": f"death: {event.cause}"})

            # Queue for respawn (respects configured delay for both required and optional NPCs)
            # AI Agent: ALL NPCs (required or optional) must respect respawn delay
            respawn_queued = self.respawn_npc(
                npc_id=event.npc_id,
                delay=None,  # Use default delay from config
                reason=f"respawn_after_death: {event.cause}",
            )

            if respawn_queued:
                logger.info(
                    "NPC queued for respawn after death",
                    npc_id=event.npc_id,
                    npc_name=definition.name,
                    cause=event.cause,
                    respawn_delay=self.default_respawn_delay,
                )
            else:
                logger.error("Failed to queue NPC for respawn", npc_id=event.npc_id, npc_name=definition.name)

        except Exception as e:
            logger.error("Error handling NPC death event", npc_id=event.npc_id, error=str(e))

    def apply_schedule_state(self, schedules: Sequence[ScheduleEntry]) -> None:
        """Record the schedule categories currently active for NPC routines."""

        self.active_schedule_ids = [entry.id for entry in schedules]
        logger.debug(
            "NPC schedule state updated",
            active_schedule_ids=self.active_schedule_ids,
        )

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
                logger.warning("Cannot spawn NPC", npc_name=definition.name, room_id=room_id)
                return None

            # Generate NPC ID
            npc_id = self._generate_npc_id(definition, room_id)

            # Create lifecycle record
            record = NPCLifecycleRecord(npc_id, definition)
            record.add_event(NPCLifecycleEvent.SPAWNED, {"room_id": room_id, "reason": reason})
            self.lifecycle_records[npc_id] = record

            # Create NPC instance with pre-generated ID
            npc_instance = self.spawning_service._create_npc_instance(definition, room_id, npc_id)
            if not npc_instance:
                record.change_state(NPCLifecycleState.ERROR, "Failed to create NPC instance")
                record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": "Failed to create NPC instance"})
                return None

            # Store NPC instance
            self.active_npcs[npc_id] = npc_instance
            npc_instance.npc_id = npc_id
            npc_instance.spawned_at = time.time()

            # Mutate room state via Room API (single source of truth) which will publish the event
            persistence = get_persistence()
            room = persistence.get_room(room_id)
            if not room:
                logger.warning("Room not found for NPC spawn", room_id=room_id, npc_id=npc_id)
                return None

            # Single source of truth: mutate via Room API; Room will publish the event
            room.npc_entered(npc_id)

            logger.info("Successfully spawned NPC", npc_id=npc_id, npc_name=definition.name, room_id=room_id)

            return npc_id

        except Exception as e:
            logger.error("Failed to spawn NPC", npc_name=definition.name, error=str(e))
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
            logger.warning("Attempted to despawn non-existent NPC", npc_id=npc_id)
            return False

        try:
            record = self.lifecycle_records[npc_id]
            record.change_state(NPCLifecycleState.DESPAWNING, reason)

            # Get NPC instance
            npc_instance = self.active_npcs.get(npc_id)
            if npc_instance:
                room_id = getattr(npc_instance, "room_id", "unknown")

                # Remove NPC from room (which publishes NPCLeftRoom event)
                # AI: Proper domain-driven design - mutate state via domain entity, not by publishing event directly
                if self.persistence:
                    room = self.persistence.get_room(room_id)
                    if room:
                        room.npc_left(npc_id)
                        logger.debug("NPC removed from room during despawn", npc_id=npc_id, room_id=room_id)
                    else:
                        logger.warning("Room not found during NPC despawn", room_id=room_id, npc_id=npc_id)
                        # If no room found, publish event directly as fallback
                        event = NPCLeftRoom(npc_id=npc_id, room_id=room_id)
                        self.event_bus.publish(event)
                else:
                    # No persistence available - publish event directly
                    logger.debug("No persistence available for room mutation, publishing event directly")
                    event = NPCLeftRoom(npc_id=npc_id, room_id=room_id)
                    self.event_bus.publish(event)

                # Remove from active NPCs
                del self.active_npcs[npc_id]

            # Update population controller
            if self.population_controller is not None:
                self.population_controller.despawn_npc(npc_id)

            # Update lifecycle record
            record.change_state(NPCLifecycleState.DESPAWNED, reason)
            record.add_event(NPCLifecycleEvent.DESPAWNED, {"reason": reason})

            logger.info("Successfully despawned NPC", npc_id=npc_id, reason=reason)

            return True

        except Exception as e:
            logger.error("Failed to despawn NPC", npc_id=npc_id, error=str(e))
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
            logger.warning("Attempted to respawn non-existent NPC", npc_id=npc_id)
            return False

        # Check if NPC is under death suppression
        if self.is_npc_death_suppressed(npc_id):
            logger.info("NPC is under death suppression, respawn blocked", npc_id=npc_id)
            return False

        try:
            record = self.lifecycle_records[npc_id]
            definition = record.definition

            # Check if NPC is already scheduled for respawn
            if npc_id in self.respawn_queue:
                logger.debug("NPC is already scheduled for respawn", npc_id=npc_id)
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

            logger.info("Scheduled respawn for NPC", npc_id=npc_id, respawn_delay=respawn_delay)

            return True

        except Exception as e:
            logger.error("Failed to schedule respawn for NPC", npc_id=npc_id, error=str(e))
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

        # AI Agent: CRITICAL DEBUG - Log respawn queue processing details
        logger.debug(
            "Processing respawn queue",
            queue_size=len(self.respawn_queue),
            current_time=current_time,
            queue_entries=[
                {
                    "npc_id": npc_id,
                    "scheduled_time": respawn_data["scheduled_time"],
                    "ready": current_time >= respawn_data["scheduled_time"],
                    "attempts": respawn_data.get("attempts", 0),
                }
                for npc_id, respawn_data in self.respawn_queue.items()
            ],
        )

        for npc_id, respawn_data in self.respawn_queue.items():
            if current_time >= respawn_data["scheduled_time"]:
                logger.debug("Attempting respawn for NPC", npc_id=npc_id, respawn_data=respawn_data)
                # Attempt to respawn
                success = self._attempt_respawn(npc_id, respawn_data)
                if success:
                    logger.info("NPC successfully respawned from queue", npc_id=npc_id)
                    respawned_count += 1
                    npcs_to_remove.append(npc_id)
                else:
                    logger.warning(
                        "NPC respawn attempt failed", npc_id=npc_id, attempts=respawn_data.get("attempts", 0)
                    )
                    # Increment attempt count
                    respawn_data["attempts"] += 1
                    if respawn_data["attempts"] >= self.max_respawn_attempts:
                        logger.warning("Max respawn attempts reached for NPC", npc_id=npc_id)
                        npcs_to_remove.append(npc_id)
            else:
                logger.debug(
                    "NPC not yet ready for respawn",
                    npc_id=npc_id,
                    scheduled_time=respawn_data["scheduled_time"],
                    current_time=current_time,
                    time_remaining=respawn_data["scheduled_time"] - current_time,
                )

        # Remove processed NPCs from queue
        for npc_id in npcs_to_remove:
            logger.debug("Removing NPC from respawn queue", npc_id=npc_id)
            del self.respawn_queue[npc_id]

        logger.debug(
            "Respawn queue processing completed", respawned_count=respawned_count, removed_count=len(npcs_to_remove)
        )
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
                logger.debug("Cannot respawn NPC - spawn conditions not met", npc_id=npc_id)
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

                logger.info("Successfully respawned NPC", old_npc_id=npc_id, new_npc_id=new_npc_id)
                return True

            return False

        except Exception as e:
            logger.error("Failed to respawn NPC", npc_id=npc_id, error=str(e))
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
        if self.population_controller is None:
            return True  # Allow spawn if no population controller

        # Check population limits
        zone_key = self.population_controller._get_zone_key_from_room_id(room_id)
        stats = self.population_controller.get_population_stats(zone_key)
        if stats:
            # Check by individual NPC definition ID, not by type
            current_count = stats.npcs_by_definition.get(int(definition.id), 0)
            if not definition.can_spawn(current_count):
                logger.debug(
                    "NPC spawn blocked by population limit",
                    npc_id=definition.id,
                    npc_name=definition.name,
                    current_count=current_count,
                    max_population=definition.max_population,
                )
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
        state_counts: dict[str, int] = {}
        for record in self.lifecycle_records.values():
            state = record.current_state
            state_counts[state] = state_counts.get(state, 0) + 1

        # Count by NPC type
        # AI Agent note: Use npc_type.value to get string value from enum
        # str(enum) returns "NPCDefinitionType.SHOPKEEPER", but we need "shopkeeper"
        type_counts: dict[str, int] = {}
        for record in self.lifecycle_records.values():
            npc_type_str = str(record.definition.npc_type.value)
            type_counts[npc_type_str] = type_counts.get(npc_type_str, 0) + 1

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
            logger.info("Cleaned up old lifecycle records", count=len(records_to_remove))

        return len(records_to_remove)

    def periodic_maintenance(self) -> dict[str, Any]:
        """
        Perform periodic maintenance tasks.

        This method is called every 60 ticks (1 minute) from the game tick loop
        to handle NPC respawning, periodic spawn checks for optional NPCs,
        and cleanup of old lifecycle records.

        Returns:
            Dictionary containing maintenance results
        """
        current_time = time.time()
        results = {}

        # Process respawn queue
        # AI Agent: Existing respawn queue processing for NPCs that died
        respawned_count = self.process_respawn_queue()
        results["respawned_npcs"] = respawned_count

        # Check for optional NPCs that should re-roll spawn probability
        # AI Agent: New functionality - periodic spawn checks for optional NPCs
        try:
            spawn_check_results = self._check_optional_npc_spawns()
            results["spawned_npcs"] = spawn_check_results["spawned_count"]
            results["spawn_checks_performed"] = spawn_check_results["checks_performed"]
        except Exception as e:
            logger.error("Error during periodic spawn checks", error=str(e))
            results["spawned_npcs"] = 0
            results["spawn_checks_performed"] = 0

        # Cleanup old records if enough time has passed
        if current_time - self.last_cleanup > self.cleanup_interval:
            cleaned_count = self.cleanup_old_records()
            results["cleaned_records"] = cleaned_count
            self.last_cleanup = current_time

        return results

    def _check_optional_npc_spawns(self) -> dict[str, int]:
        """
        Check if optional NPCs should spawn based on periodic probability rolls.

        This method is called periodically to give optional NPCs that failed their
        initial spawn probability check another chance to appear in the game world.

        AI Agent: Implements Phase 2 - periodic spawn checks for optional NPCs.
                  This prevents the issue where optional NPCs that fail their initial
                  spawn roll never appear until server restart.

        Returns:
            Dictionary with spawn check statistics
        """
        if not self.population_controller:
            return {"spawned_count": 0, "checks_performed": 0}

        from ..config.npc_config import NPCMaintenanceConfig

        current_time = time.time()
        spawned_count = 0
        checks_performed = 0

        # Iterate through all NPC definitions
        for definition_id, definition in self.population_controller.npc_definitions.items():
            # Skip required NPCs - they're handled at startup
            if definition.is_required():
                continue

            # AI Agent: CRITICAL FIX - Skip NPCs that are already in the respawn queue
            #           This prevents periodic spawn checks from bypassing the respawn delay
            #           by immediately spawning a new instance of an NPC that just died
            npc_in_respawn_queue = any(data["definition"].id == definition_id for data in self.respawn_queue.values())
            if npc_in_respawn_queue:
                logger.debug(
                    "Skipping periodic spawn check - NPC in respawn queue",
                    npc_name=definition.name,
                    definition_id=definition_id,
                )
                continue

            # Check if enough time has passed since last spawn check for this definition
            last_check = self.last_spawn_check.get(definition_id, 0)
            if current_time - last_check < NPCMaintenanceConfig.MIN_SPAWN_CHECK_INTERVAL:
                continue

            # Update last check time
            self.last_spawn_check[definition_id] = current_time
            checks_performed += 1

            # Get the zone key from the definition's sub_zone_id
            # AI Agent: Build zone key from sub_zone_id to find proper zone configuration
            zone_key = self._get_zone_key_for_definition(definition)
            if not zone_key:
                continue

            # Get zone configuration
            zone_config = self.population_controller.get_zone_configuration(zone_key)
            if not zone_config:
                continue

            # Get current population stats
            stats = self.population_controller.get_population_stats(zone_key)
            current_count = stats.npcs_by_definition.get(definition_id, 0) if stats else 0

            # Check if we can spawn more of this NPC type
            if not definition.can_spawn(current_count):
                logger.debug(
                    "Optional NPC spawn check: population limit reached",
                    npc_name=definition.name,
                    current_count=current_count,
                    max_population=definition.max_population,
                )
                continue

            # Roll spawn probability with zone modifier
            import random

            effective_probability = zone_config.get_effective_spawn_probability(float(definition.spawn_probability))
            if random.random() <= effective_probability:
                # Determine spawn room (use the NPC's configured room_id or first room in sub-zone)
                spawn_room_id = self._get_spawn_room_for_definition(definition)
                if not spawn_room_id:
                    logger.warning("No spawn room found for optional NPC", npc_name=definition.name)
                    continue

                # Spawn the NPC
                npc_id = self.spawn_npc(definition, spawn_room_id, "periodic_spawn_check")
                if npc_id:
                    spawned_count += 1
                    logger.info(
                        "Periodic spawn check successful",
                        npc_name=definition.name,
                        npc_id=npc_id,
                        room_id=spawn_room_id,
                    )

        return {"spawned_count": spawned_count, "checks_performed": checks_performed}

    def _get_zone_key_for_definition(self, definition: NPCDefinition) -> str | None:
        """
        Get the zone key for an NPC definition based on its sub_zone_id.

        Args:
            definition: NPC definition

        Returns:
            Zone key in format "zone/sub_zone" or None if cannot be determined
        """
        if not definition.sub_zone_id:
            return None

        # AI Agent: Extract zone from sub_zone relationship
        #           sub_zone_id links to SubZone which has zone_id
        # For now, use the first spawn rule to get the zone information
        if self.population_controller and int(definition.id) in self.population_controller.spawn_rules:
            # The spawn rule has sub_zone_id which we can use to build the zone key
            # We need to query the actual sub-zone to get its zone_id
            # For now, we'll extract from the definition's room_id if available
            if definition.room_id:
                return self.population_controller._get_zone_key_from_room_id(str(definition.room_id))

        return None

    def _get_spawn_room_for_definition(self, definition: NPCDefinition) -> str | None:
        """
        Get the spawn room for an NPC definition.

        Args:
            definition: NPC definition

        Returns:
            Room ID where NPC should spawn, or None if cannot be determined
        """
        # Use the NPC's configured room_id if available
        if definition.room_id:
            return str(definition.room_id)

        # Otherwise, we'd need to query the sub-zone for available rooms
        # For now, return None if no room_id is configured
        # AI Agent: Future enhancement - query persistence layer for rooms in sub-zone
        logger.warning(
            "No room_id configured for NPC definition",
            npc_name=definition.name,
            definition_id=definition.id,
        )
        return None
