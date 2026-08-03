"""
NPC despawn logic for lifecycle.

Extracted from lifecycle_manager to keep file NLOC under complexity limits.
"""

from typing import Any

from server.events.event_types import NPCLeftRoom

from ..structured_logging.enhanced_logging_config import get_logger
from .lifecycle_types import NPCLifecycleEvent, NPCLifecycleState
from .npc_utils import extract_room_id_from_lifecycle_record, extract_room_id_from_npc

logger = get_logger(__name__)


def _resolve_despawn_room_id(manager: Any, npc_id: str, npc_instance: object) -> str:
    """Prefer live NPC room attrs, then lifecycle SPAWNED/left event room_id."""
    room_id = extract_room_id_from_npc(npc_instance)
    if room_id != "unknown":
        return room_id
    record = manager.lifecycle_records.get(npc_id)
    return extract_room_id_from_lifecycle_record(record) or "unknown"


def _remove_npc_from_room_on_despawn(manager: Any, npc_id: str, room_id: str) -> None:
    """Mutate room occupants or publish NPCLeftRoom; skip unknown rooms."""
    if not manager.persistence:
        logger.debug("No persistence available for room mutation, publishing event directly")
        if room_id != "unknown":
            manager.event_bus.publish(NPCLeftRoom(npc_id=npc_id, room_id=room_id))
        return

    room = manager.persistence.get_room_by_id(room_id) if room_id != "unknown" else None
    if room:
        room.npc_left(npc_id)
        logger.debug("NPC removed from room during despawn", npc_id=npc_id, room_id=room_id)
        return
    if room_id == "unknown":
        logger.debug("NPC despawn with unknown room; skipping room exit event", npc_id=npc_id)
        return
    logger.warning("Room not found during NPC despawn", room_id=room_id, npc_id=npc_id)
    manager.event_bus.publish(NPCLeftRoom(npc_id=npc_id, room_id=room_id))


def despawn_npc_impl(manager: Any, npc_id: str, reason: str = "manual") -> bool:
    """
    Despawn an NPC instance.

    Args:
        manager: NPCLifecycleManager instance.
        npc_id: ID of the NPC to despawn.
        reason: Reason for despawning.

    Returns:
        True if NPC was despawned successfully.
    """
    if npc_id not in manager.lifecycle_records:
        logger.warning("Attempted to despawn non-existent NPC", npc_id=npc_id)
        return False

    try:
        record = manager.lifecycle_records[npc_id]
        record.change_state(NPCLifecycleState.DESPAWNING, reason)

        npc_instance = manager.active_npcs.get(npc_id)
        if npc_instance:
            room_id = _resolve_despawn_room_id(manager, npc_id, npc_instance)

            if manager.population_controller is not None:
                manager.population_controller.despawn_npc(npc_id)

            _remove_npc_from_room_on_despawn(manager, npc_id, room_id)
            del manager.active_npcs[npc_id]

        record.change_state(NPCLifecycleState.DESPAWNED, reason)
        record.add_event(NPCLifecycleEvent.DESPAWNED, {"reason": reason})

        logger.info("Successfully despawned NPC", npc_id=npc_id, reason=reason)
        return True

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC despawn errors unpredictable
        logger.error("Failed to despawn NPC", npc_id=npc_id, error=str(e))
        if npc_id in manager.lifecycle_records:
            record = manager.lifecycle_records[npc_id]
            record.change_state(NPCLifecycleState.ERROR, str(e))
            record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": str(e)})
        return False
