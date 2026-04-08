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

from __future__ import annotations

import random
import time
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Protocol, cast

from structlog.stdlib import BoundLogger

# pylint: disable=too-many-lines  # Reason: Lifecycle manager is a central coordination module; splitting further would scatter tightly related lifecycle logic and harm readability of the end-to-end flow.
from server.events.event_bus import EventBus
from server.events.event_types import NPCDied, NPCEnteredRoom, NPCLeftRoom, RoomOccupantsRefreshRequested
from server.models.npc import NPCDefinition
from server.npc.npc_base import NPCBase
from server.npc.population_control import NPCPopulationController
from server.schemas.calendar import ScheduleEntry

from ..structured_logging.enhanced_logging_config import get_logger
from .lifecycle_death import handle_npc_died_impl
from .lifecycle_despawn import despawn_npc_impl
from .lifecycle_periodic import cleanup_old_records_impl, run_periodic_maintenance_impl
from .lifecycle_respawn import process_respawn_queue_impl
from .lifecycle_types import NPCLifecycleEvent, NPCLifecycleRecord, NPCLifecycleState

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from .threading import NPCThreadManager


class _SpawnTrackedNPC(Protocol):
    """Protocol for NPCs that track spawn metadata and room tracking."""

    spawned_at: float
    current_room: str | None
    current_room_id: str | None


class _SpawningServiceProtocol(Protocol):
    """Protocol for spawning services used by NPCLifecycleManager."""

    def create_npc_instance(
        self,
        definition: NPCDefinition,
        room_id: str,
        npc_id: str | None = None,
    ) -> object | None:
        """Create an NPC instance or return None on failure."""


logger: BoundLogger = get_logger(__name__)

# Re-export for backward compatibility
__all__ = [
    "NPCLifecycleManager",
    "NPCLifecycleRecord",
    "NPCLifecycleState",
    "NPCLifecycleEvent",
]


class NPCLifecycleManager:  # pylint: disable=too-many-instance-attributes  # Reason: Lifecycle manager requires many state tracking and configuration attributes
    """
    Core manager for NPC lifecycle operations (single source of truth for active NPCs).

    This class coordinates spawning, despawning, respawning, and state management
    for all NPCs in the game world. It maintains the authoritative active_npcs
    dictionary that all other services query for NPC instance data.

    SERVICE HIERARCHY:
    - Level 1 (lowest/core): Core instance lifecycle management
    - Maintains: active_npcs dict (dict[str, NPCBase]) - SINGLE SOURCE OF TRUTH
    - Used by: NPCPopulationController, NPCInstanceService, and all real-time services

    ARCHITECTURE NOTES:
    - active_npcs is the ONLY authoritative source for active NPC instances
    - All NPC queries should go through this manager's active_npcs dictionary
    - Population validation should happen at NPCPopulationController level before calling spawn_npc()
    - This manager handles actual instance creation, room state mutation, and lifecycle tracking
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Lifecycle manager initialization requires many service dependencies
        self,
        event_bus: EventBus,
        population_controller: NPCPopulationController | None,
        spawning_service: _SpawningServiceProtocol,
        persistence: AsyncPersistenceLayer | None = None,
        thread_manager: NPCThreadManager | None = None,
    ) -> None:
        """
        Initialize the NPC lifecycle manager.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            population_controller: Population controller for managing NPC populations
            spawning_service: Spawning service for creating NPC instances
            persistence: Persistence layer for room access (optional, for proper room state mutation)
            thread_manager: Optional NPC thread manager for behavior execution
        """
        self.event_bus: EventBus = event_bus
        self.population_controller: NPCPopulationController | None = population_controller
        self.spawning_service: _SpawningServiceProtocol = spawning_service
        self.persistence: AsyncPersistenceLayer | None = persistence

        # Initialize thread manager for NPC behavior execution
        if thread_manager is None:
            from ..npc.threading import NPCThreadManager

            thread_manager = NPCThreadManager()
        self.thread_manager: NPCThreadManager = thread_manager

        # Lifecycle tracking
        self.lifecycle_records: dict[str, NPCLifecycleRecord] = {}
        self.active_npcs: dict[str, NPCBase] = {}
        self.respawn_queue: dict[str, Mapping[str, object]] = {}  # npc_id -> respawn_data
        self.death_suppression: dict[str, float] = {}  # npc_id -> death_timestamp
        self.active_schedule_ids: list[str] = []

        # Configuration - Import values from NPCMaintenanceConfig for consistency
        # AI Agent: CRITICAL FIX - Use configuration values instead of hardcoded values
        #           This ensures respawn delays and maintenance intervals can be adjusted
        #           centrally without modifying lifecycle manager code
        from ..config.npc_config import NPCMaintenanceConfig

        self.default_respawn_delay: float = NPCMaintenanceConfig.DEFAULT_RESPAWN_DELAY
        self.death_suppression_duration: float = NPCMaintenanceConfig.DEATH_SUPPRESSION_DURATION
        self.max_respawn_attempts: int = NPCMaintenanceConfig.MAX_RESPAWN_ATTEMPTS
        self.cleanup_interval: float = NPCMaintenanceConfig.CLEANUP_INTERVAL
        self.last_cleanup: float = time.time()

        # Pending thread starts (for async processing)
        self._pending_thread_starts: list[tuple[str, NPCDefinition]] = []

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
            "Recorded death of NPC, suppressing respawn",
            npc_id=npc_id,
            death_suppression_duration=self.death_suppression_duration,
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
        # Use service_id for tracking and cleanup (Task 2: Event Subscriber Cleanup)
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered_room, service_id="npc_lifecycle_manager")
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left_room, service_id="npc_lifecycle_manager")
        self.event_bus.subscribe(NPCDied, self._handle_npc_died, service_id="npc_lifecycle_manager")

    def _handle_npc_entered_room(self, event: NPCEnteredRoom) -> None:
        """Handle NPC entering a room."""
        if event.npc_id in self.lifecycle_records:
            record = self.lifecycle_records[event.npc_id]
            if record.current_state == NPCLifecycleState.SPAWNING:
                record.change_state(NPCLifecycleState.ACTIVE, "entered room")
                record.add_event(NPCLifecycleEvent.SPAWNED, {"room_id": event.room_id})

        # Trigger a room occupants refresh so clients see newly spawned NPCs without re-entering.
        try:
            self.event_bus.publish(RoomOccupantsRefreshRequested(room_id=event.room_id))
        except Exception:  # noqa: S110  # pylint: disable=broad-exception-caught  # Best-effort refresh; core lifecycle already ran
            logger.warning(
                "Failed to publish RoomOccupantsRefreshRequested after NPCEnteredRoom",
                npc_id=event.npc_id,
                room_id=event.room_id,
            )

    def _handle_npc_left_room(self, event: NPCLeftRoom) -> None:
        """Handle NPC leaving a room."""
        if event.npc_id in self.lifecycle_records:
            record = self.lifecycle_records[event.npc_id]
            record.add_event(NPCLifecycleEvent.DEACTIVATED, {"room_id": event.room_id})

    def _handle_npc_died(self, event: NPCDied) -> None:
        """Handle NPC death by queuing for respawn (delegates to lifecycle_death)."""
        handle_npc_died_impl(self, event)

    def apply_schedule_state(self, schedules: Sequence[ScheduleEntry]) -> None:
        """Record the schedule categories currently active for NPC routines."""

        self.active_schedule_ids = [entry.id for entry in schedules]
        logger.debug(
            "NPC schedule state updated",
            active_schedule_ids=self.active_schedule_ids,
        )

    def _set_npc_room_tracking(self, npc_instance: _SpawnTrackedNPC, _npc_id: str, room_id: str) -> None:
        """Set room tracking attributes on NPC instance."""
        npc_instance.current_room = room_id
        npc_instance.current_room_id = room_id

    def _validate_npc_room_tracking(self, npc_instance: _SpawnTrackedNPC, npc_id: str, room_id: str) -> None:
        """Validate that room tracking was set correctly."""
        current_room = npc_instance.current_room
        if not current_room or current_room != room_id:
            logger.error(
                "Failed to set NPC room tracking correctly",
                npc_id=npc_id,
                room_id=room_id,
                current_room=current_room,
                current_room_id=getattr(npc_instance, "current_room_id", None),
            )
        else:
            logger.debug(
                "NPC room tracking set successfully",
                npc_id=npc_id,
                room_id=room_id,
                current_room=current_room,
                current_room_id=getattr(npc_instance, "current_room_id", None),
            )

    def _get_room_for_spawn(self, room_id: str, npc_id: str, definition: NPCDefinition) -> object | None:
        """Get room from persistence and handle errors."""
        if self.persistence:
            room = self.persistence.get_room_by_id(room_id)
        else:
            room = None
        if not room:
            logger.warning(
                "Room not found for NPC spawn",
                room_id=room_id,
                npc_id=npc_id,
                npc_name=definition.name,
                definition_id=definition.id,
            )
        return room

    def _cleanup_failed_spawn(self, npc_id: str, room_id: str) -> None:
        """Clean up lifecycle record and active NPCs on spawn failure."""
        if npc_id in self.lifecycle_records:
            record = self.lifecycle_records[npc_id]
            record.change_state(NPCLifecycleState.ERROR, f"Room not found: {room_id}")
            record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": f"Room not found: {room_id}"})
        if npc_id in self.active_npcs:
            del self.active_npcs[npc_id]

    def _queue_npc_thread_start(self, npc_id: str, definition: NPCDefinition) -> None:
        """Queue NPC thread start, handling async event loop if available."""
        if self.thread_manager and self.thread_manager.is_running:
            try:
                import asyncio

                _ = asyncio.get_running_loop()
                _ = asyncio.create_task(self._start_npc_thread_async(npc_id, definition))
            except RuntimeError:
                self._pending_thread_starts.append((npc_id, definition))
        else:
            self._pending_thread_starts.append((npc_id, definition))
            logger.debug("Queued NPC thread start request (thread manager not started)", npc_id=npc_id)

    def spawn_npc(
        self, definition: NPCDefinition, room_id: str, reason: str = "manual"
    ) -> tuple[str | None, str | None]:
        """
        Spawn an NPC instance.

        Thin wrapper around _spawn_npc_impl to keep public method size small
        while centralizing the detailed spawn logic in a helper.
        """
        return self._spawn_npc_impl(definition, room_id, reason)

    def _spawn_npc_impl(self, definition: NPCDefinition, room_id: str, reason: str) -> tuple[str | None, str | None]:
        """Internal implementation for spawning an NPC with full error handling."""
        npc_id: str | None = None
        failure_reason: str = ""
        try:
            can_spawn, failure_reason = self._can_spawn_npc(definition, room_id, reason)
            if not can_spawn:
                logger.warning(
                    "Cannot spawn NPC",
                    npc_name=definition.name,
                    room_id=room_id,
                    failure_reason=failure_reason,
                )
                return (None, failure_reason)

            npc_id = self._generate_npc_id(definition, room_id)
            record = NPCLifecycleRecord(npc_id, definition)
            record.add_event(NPCLifecycleEvent.SPAWNED, {"room_id": room_id, "reason": reason})
            self.lifecycle_records[npc_id] = record

            npc_instance = self.spawning_service.create_npc_instance(definition, room_id, npc_id)
            if not npc_instance:
                return self._handle_spawn_service_failure(definition, room_id, record)

            self._finalize_spawn_record(npc_id, cast(NPCBase, npc_instance), room_id)

            room = self._get_room_for_spawn(room_id, npc_id, definition)
            if not room:
                failure_reason = f"room not found: {room_id}"
                self._cleanup_failed_spawn(npc_id, room_id)
                logger.error(
                    "Failed to spawn NPC",
                    npc_name=definition.name,
                    room_id=room_id,
                    failure_reason=failure_reason,
                )
                return (None, failure_reason)

            self._notify_room_and_threads(room, npc_id, definition)
            logger.info("Successfully spawned NPC", npc_id=npc_id, npc_name=definition.name, room_id=room_id)
            return (npc_id, None)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn errors unpredictable, must handle gracefully
            failure_reason = str(e)
            self._handle_spawn_exception(definition, room_id, npc_id, failure_reason)
            return (None, failure_reason)

    def _handle_spawn_service_failure(
        self,
        definition: NPCDefinition,
        room_id: str,
        record: NPCLifecycleRecord,
    ) -> tuple[str | None, str | None]:
        """Handle failure when the spawning service cannot create an NPC instance."""
        failure_reason = "spawning service failed to create NPC instance"
        record.change_state(NPCLifecycleState.ERROR, failure_reason)
        record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": failure_reason})
        logger.error(
            "Failed to spawn NPC",
            npc_name=definition.name,
            room_id=room_id,
            failure_reason=failure_reason,
        )
        return (None, failure_reason)

    def _finalize_spawn_record(self, npc_id: str, npc_instance: NPCBase, room_id: str) -> None:
        """Update in-memory state and tracking after successful NPC creation."""
        self.active_npcs[npc_id] = npc_instance
        npc_instance.npc_id = npc_id
        tracked_npc = cast(_SpawnTrackedNPC, cast(object, npc_instance))
        tracked_npc.spawned_at = time.time()
        self._set_npc_room_tracking(tracked_npc, npc_id, room_id)
        self._validate_npc_room_tracking(tracked_npc, npc_id, room_id)

    def _notify_room_and_threads(self, room: object, npc_id: str, definition: NPCDefinition) -> None:
        """Notify room of NPC entry and queue thread start if needed."""
        npc_entered = getattr(room, "npc_entered", None)
        if callable(npc_entered):
            _ = npc_entered(npc_id)
        if self.thread_manager:
            self._queue_npc_thread_start(npc_id, definition)

    def _handle_spawn_exception(
        self,
        definition: NPCDefinition,
        room_id: str,
        npc_id: str | None,
        failure_reason: str,
    ) -> None:
        """Handle logging and lifecycle updates for a failed spawn."""
        logger.error(
            "Failed to spawn NPC",
            npc_name=definition.name,
            room_id=room_id,
            failure_reason=failure_reason,
        )
        if npc_id and npc_id in self.lifecycle_records:
            record = self.lifecycle_records[npc_id]
            record.change_state(NPCLifecycleState.ERROR, failure_reason)
            record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": failure_reason})

    def despawn_npc(self, npc_id: str, reason: str = "manual") -> bool:
        """Despawn an NPC instance (delegates to lifecycle_despawn)."""
        return despawn_npc_impl(self, npc_id, reason)

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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC respawn scheduling errors unpredictable, must handle gracefully
            logger.error("Failed to schedule respawn for NPC", npc_id=npc_id, error=str(e))
            if npc_id in self.lifecycle_records:
                record = self.lifecycle_records[npc_id]
                record.change_state(NPCLifecycleState.ERROR, str(e))
                record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": str(e)})
            return False

    def process_respawn_queue(self) -> int:
        """Process the respawn queue and spawn NPCs that are ready (delegates to lifecycle_respawn)."""
        return process_respawn_queue_impl(self)

    def can_spawn_npc(self, definition: NPCDefinition, room_id: str, reason: str = "manual") -> tuple[bool, str]:
        """
        Check if an NPC can be spawned (population limits, admin bypass).

        Returns:
            Tuple of (can_spawn, failure_reason). failure_reason is empty when can_spawn is True.
        """
        return self._can_spawn_npc(definition, room_id, reason)

    def _can_spawn_npc(self, definition: NPCDefinition, room_id: str, reason: str = "manual") -> tuple[bool, str]:
        """
        Check if an NPC can be spawned.

        Args:
            definition: NPC definition
            room_id: Room where NPC should be spawned
            reason: Spawn reason; "admin_spawn" bypasses population limits

        Returns:
            Tuple of (can_spawn, failure_reason). failure_reason is empty when can_spawn is True.
        """
        if self.population_controller is None:
            return (True, "")

        # Admin spawns bypass population limits (explicit user intent)
        if reason == "admin_spawn":
            return (True, "")

        # Check population limits
        zone_key = self.population_controller.get_zone_key_from_room_id(room_id)
        stats = self.population_controller.get_population_stats(zone_key)
        if stats:
            # Check by individual NPC definition ID, not by type
            current_count = stats.npcs_by_definition.get(int(definition.id), 0)
            if not definition.can_spawn(current_count):
                failure_reason = (
                    f"population limit exceeded: current={current_count} max={definition.max_population} "
                    f"for zone={zone_key}"
                )
                return (False, failure_reason)

        # Additional checks can be added here (e.g., room capacity, special conditions)

        return (True, "")

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
        random_suffix = random.randint(1000, 9999)  # nosec B311: Game mechanics NPC ID generation, not cryptographic
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

    def get_lifecycle_statistics(self) -> dict[str, object]:
        """
        Get overall lifecycle statistics.

        Returns:
            Dictionary containing lifecycle statistics
        """
        total_npcs = len(self.lifecycle_records)
        active_npcs = len(self.active_npcs)
        respawn_queue_size = len(self.respawn_queue)

        state_counts = self._compute_state_counts()
        type_counts = self._compute_type_counts()
        total_spawns, total_despawns, total_errors = self._compute_aggregate_counts()

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

    def _compute_state_counts(self) -> dict[str, int]:
        """Return counts of lifecycle records by current_state."""
        counts: dict[str, int] = {}
        for record in self.lifecycle_records.values():
            state = record.current_state
            counts[state] = counts.get(state, 0) + 1
        return counts

    def _compute_type_counts(self) -> dict[str, int]:
        """Return counts of lifecycle records by NPC type string."""
        counts: dict[str, int] = {}
        for record in self.lifecycle_records.values():
            npc_type_str = str(record.definition.npc_type)
            counts[npc_type_str] = counts.get(npc_type_str, 0) + 1
        return counts

    def _compute_aggregate_counts(self) -> tuple[int, int, int]:
        """Return (total_spawns, total_despawns, total_errors) across all lifecycle records."""
        total_spawns = sum(record.spawn_count for record in self.lifecycle_records.values())
        total_despawns = sum(record.despawn_count for record in self.lifecycle_records.values())
        total_errors = sum(record.error_count for record in self.lifecycle_records.values())
        return total_spawns, total_despawns, total_errors

    def cleanup_old_records(self, max_age_seconds: int = 86400) -> int:
        """Clean up old lifecycle records (delegates to lifecycle_periodic)."""
        return cleanup_old_records_impl(self, max_age_seconds)

    def periodic_maintenance(self) -> dict[str, object]:
        """Perform periodic maintenance (delegates to lifecycle_periodic)."""
        return run_periodic_maintenance_impl(self)

    async def _start_npc_thread_async(self, npc_id: str, definition: NPCDefinition) -> None:
        """
        Start NPC thread asynchronously for behavior execution.

        Args:
            npc_id: ID of the NPC
            definition: NPC definition
        """
        try:
            # Ensure thread manager is started (thread_manager is always configured in __init__)
            thread_manager = self.thread_manager
            is_running = thread_manager.is_running
            if not is_running:
                import asyncio

                _ = cast(object, asyncio.create_task(thread_manager.start()))

            # Start NPC thread (fire-and-forget task on the current event loop)
            import asyncio

            _ = cast(object, asyncio.create_task(thread_manager.start_npc_thread(npc_id, definition)))
            logger.debug("Started NPC thread for behavior execution", npc_id=npc_id)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC thread startup errors unpredictable, must handle gracefully
            logger.warning("Failed to start NPC thread", npc_id=npc_id, error_message=str(e))
