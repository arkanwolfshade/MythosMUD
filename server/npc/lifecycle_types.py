"""
NPC lifecycle state, events, and record types.

Extracted from lifecycle_manager to keep file NLOC under complexity limits.
"""

import time
from enum import StrEnum
from typing import Any

from server.models.npc import NPCDefinition

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class NPCLifecycleState(StrEnum):
    """Enumeration of NPC lifecycle states."""

    SPAWNING = "spawning"
    ACTIVE = "active"
    INACTIVE = "inactive"
    DESPAWNING = "despawning"
    DESPAWNED = "despawned"
    RESPAWNING = "respawning"
    ERROR = "error"


class NPCLifecycleEvent(StrEnum):
    """Enumeration of NPC lifecycle events."""

    SPAWNED = "spawned"
    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"
    DESPAWNED = "despawned"
    RESPAWNED = "respawned"
    ERROR_OCCURRED = "error_occurred"


class NPCLifecycleRecord:  # pylint: disable=too-many-instance-attributes  # Reason: Lifecycle record requires many fields
    """Record of an NPC's lifecycle events and state changes."""

    def __init__(self, npc_id: str, definition: NPCDefinition) -> None:
        """
        Initialize lifecycle record for an NPC.

        Args:
            npc_id: Unique identifier for the NPC.
            definition: NPC definition (type, limits, etc.).
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
        Append a lifecycle event and update counters (spawn_count, despawn_count, error_count).

        Args:
            event_type: Kind of event (e.g. SPAWNED, DESPAWNED, ERROR_OCCURRED).
            details: Optional extra data for the event.
        """
        event = {
            "event_type": event_type,
            "timestamp": time.time(),
            "state": self.current_state,
            "details": details or {},
        }
        self.events.append(event)
        self.last_updated = time.time()
        if event_type == NPCLifecycleEvent.SPAWNED:
            self.spawn_count += 1
        elif event_type == NPCLifecycleEvent.DESPAWNED:
            self.despawn_count += 1
        elif event_type == NPCLifecycleEvent.ERROR_OCCURRED:
            self.error_count += 1
            self.last_error = details

    def change_state(self, new_state: NPCLifecycleState, reason: str = "") -> None:
        """
        Set the record's lifecycle state and record active-time delta; logs ACTIVATED/DEACTIVATED event.

        Args:
            new_state: Target state (e.g. ACTIVE, DESPAWNED).
            reason: Optional reason for the state change.
        """
        old_state = self.current_state
        self.current_state = new_state
        self.last_updated = time.time()
        if old_state == NPCLifecycleState.ACTIVE:
            self.total_active_time += time.time() - self.last_active_time
        elif new_state == NPCLifecycleState.ACTIVE:
            self.last_active_time = time.time()
        self.add_event(
            NPCLifecycleEvent.ACTIVATED if new_state == NPCLifecycleState.ACTIVE else NPCLifecycleEvent.DEACTIVATED,
            {"old_state": old_state, "new_state": new_state, "reason": reason},
        )

    def get_statistics(self) -> dict[str, Any]:
        """
        Return a snapshot of this record's stats (counts, times, state, age).

        Returns:
            Dict with keys such as npc_id, definition_name, current_state, spawn_count, age_seconds, etc.
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
