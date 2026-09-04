"""
NPC death event handling for lifecycle.

Extracted from lifecycle_manager to keep file NLOC under complexity limits.
"""

from typing import Protocol

from structlog.stdlib import BoundLogger

from server.async_persistence import AsyncPersistenceLayer
from server.events.event_bus import EventBus
from server.events.event_types import NPCDied, RoomOccupantsRefreshRequested
from server.npc.npc_base import NPCBase
from server.npc.population_control import NPCPopulationController

from ..structured_logging.enhanced_logging_config import get_logger
from .lifecycle_types import NPCLifecycleEvent, NPCLifecycleRecord, NPCLifecycleState

logger: BoundLogger = get_logger(__name__)


class _LifecycleManagerForDeath(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Structural Protocol; mirrors NPCLifecycleManager without importing it.
    """Structural type for NPCLifecycleManager (avoids importing lifecycle_manager: import cycle)."""

    lifecycle_records: dict[str, NPCLifecycleRecord]
    active_npcs: dict[str, NPCBase]
    population_controller: NPCPopulationController | None
    persistence: AsyncPersistenceLayer | None
    event_bus: EventBus
    default_respawn_delay: float

    def respawn_npc(  # pylint: disable=missing-function-docstring  # Reason: Protocol stub; implementation is on NPCLifecycleManager.
        self, npc_id: str, delay: float | None = None, reason: str = ""
    ) -> bool: ...


def _remove_active_npc_and_notify(manager: _LifecycleManagerForDeath, event: NPCDied) -> None:
    """If NPC was active, despawn, clear room occupancy, and request room UI refresh."""
    if event.npc_id not in manager.active_npcs:
        return
    npc_instance = manager.active_npcs[event.npc_id]
    room_id = str(getattr(npc_instance, "room_id", event.room_id))

    population = manager.population_controller
    if population is not None:
        _ = population.despawn_npc(event.npc_id)
    del manager.active_npcs[event.npc_id]

    persistence = manager.persistence
    if persistence is not None:
        room = persistence.get_room_by_id(room_id)
        if room is not None:
            room.npc_left(event.npc_id)
            logger.debug("NPC removed from room after death", npc_id=event.npc_id, room_id=room_id)

    manager.event_bus.publish(RoomOccupantsRefreshRequested(room_id=room_id))


def _mark_despawned_and_queue_respawn(
    manager: _LifecycleManagerForDeath, event: NPCDied, record: NPCLifecycleRecord
) -> None:
    """Transition record to despawned and queue respawn; log outcome."""
    record.change_state(NPCLifecycleState.DESPAWNED, f"death: {event.cause}")
    record.add_event(NPCLifecycleEvent.DESPAWNED, {"reason": f"death: {event.cause}"})

    respawn_queued = manager.respawn_npc(
        npc_id=event.npc_id,
        delay=None,
        reason=f"respawn_after_death: {event.cause}",
    )
    definition = record.definition
    if respawn_queued:
        logger.info(
            "NPC queued for respawn after death",
            npc_id=event.npc_id,
            npc_name=definition.name,
            cause=event.cause,
            respawn_delay=manager.default_respawn_delay,
        )
    else:
        logger.error("Failed to queue NPC for respawn", npc_id=event.npc_id, npc_name=definition.name)


def handle_npc_died_impl(manager: _LifecycleManagerForDeath, event: NPCDied) -> None:
    """
    Handle NPC death by queuing for respawn.

    Do NOT despawn immediately; mark as inactive and queue for respawn so
    XP calculation can still read the NPC's base_stats from lifecycle records.
    """
    try:
        if event.npc_id not in manager.lifecycle_records:
            logger.warning("NPC died but no lifecycle record found", npc_id=event.npc_id)
            return

        record = manager.lifecycle_records[event.npc_id]
        _remove_active_npc_and_notify(manager, event)
        _mark_despawned_and_queue_respawn(manager, event, record)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC death handling must be graceful
        logger.error("Error handling NPC death event", npc_id=event.npc_id, error=str(e))
