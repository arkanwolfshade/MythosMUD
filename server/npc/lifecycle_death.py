"""
NPC death event handling for lifecycle.

Extracted from lifecycle_manager to keep file NLOC under complexity limits.
"""

from typing import Any

from server.events.event_types import NPCDied, RoomOccupantsRefreshRequested

from ..structured_logging.enhanced_logging_config import get_logger
from .lifecycle_types import NPCLifecycleEvent, NPCLifecycleState

logger = get_logger(__name__)


def handle_npc_died_impl(manager: Any, event: NPCDied) -> None:
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
        definition = record.definition

        if event.npc_id in manager.active_npcs:
            npc_instance = manager.active_npcs[event.npc_id]
            room_id = getattr(npc_instance, "room_id", event.room_id)

            if manager.population_controller:
                manager.population_controller.despawn_npc(event.npc_id)
            del manager.active_npcs[event.npc_id]

            if manager.persistence:
                room = manager.persistence.get_room_by_id(room_id)
                if room:
                    room.npc_left(event.npc_id)
                    logger.debug("NPC removed from room after death", npc_id=event.npc_id, room_id=room_id)

            if manager.event_bus:
                manager.event_bus.publish(RoomOccupantsRefreshRequested(room_id=room_id))

        record.change_state(NPCLifecycleState.DESPAWNED, f"death: {event.cause}")
        record.add_event(NPCLifecycleEvent.DESPAWNED, {"reason": f"death: {event.cause}"})

        respawn_queued = manager.respawn_npc(
            npc_id=event.npc_id,
            delay=None,
            reason=f"respawn_after_death: {event.cause}",
        )

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

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC death handling must be graceful
        logger.error("Error handling NPC death event", npc_id=event.npc_id, error=str(e))
