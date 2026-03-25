"""
Respawn queue processing for NPC lifecycle.

Extracted from lifecycle_manager to keep file NLOC under complexity limits.
"""

import time
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def process_respawn_queue_impl(manager: Any) -> int:
    """
    Process the respawn queue and spawn NPCs that are ready.

    Args:
        manager: NPCLifecycleManager instance (avoids circular import).

    Returns:
        Number of NPCs respawned.
    """
    current_time = time.time()
    respawned_count = 0
    npcs_to_remove = []

    logger.debug(
        "Processing respawn queue",
        queue_size=len(manager.respawn_queue),
        current_time=current_time,
        queue_entries=[
            {
                "npc_id": npc_id,
                "scheduled_time": respawn_data["scheduled_time"],
                "ready": current_time >= respawn_data["scheduled_time"],
                "attempts": respawn_data.get("attempts", 0),
            }
            for npc_id, respawn_data in manager.respawn_queue.items()
        ],
    )

    for npc_id, respawn_data in list(manager.respawn_queue.items()):
        should_remove, was_respawned = _process_respawn_queue_entry(manager, npc_id, respawn_data, current_time)
        if should_remove:
            npcs_to_remove.append(npc_id)
        if was_respawned:
            respawned_count += 1

    _cleanup_respawn_queue(manager, npcs_to_remove)

    logger.debug(
        "Respawn queue processing completed", respawned_count=respawned_count, removed_count=len(npcs_to_remove)
    )
    return respawned_count


def _process_respawn_queue_entry(
    manager: Any, npc_id: str, respawn_data: dict[str, Any], current_time: float
) -> tuple[bool, bool]:
    """Process a single respawn queue entry. Returns (should_remove, was_respawned)."""
    if current_time < respawn_data["scheduled_time"]:
        logger.debug(
            "NPC not yet ready for respawn",
            npc_id=npc_id,
            scheduled_time=respawn_data["scheduled_time"],
            current_time=current_time,
            time_remaining=respawn_data["scheduled_time"] - current_time,
        )
        return False, False

    logger.debug("Attempting respawn for NPC", npc_id=npc_id, respawn_data=respawn_data)
    success = _attempt_respawn_impl(manager, npc_id, respawn_data)

    if success:
        logger.info("NPC successfully respawned from queue", npc_id=npc_id)
        return True, True

    logger.warning("NPC respawn attempt failed", npc_id=npc_id, attempts=respawn_data.get("attempts", 0))
    respawn_data["attempts"] = respawn_data.get("attempts", 0) + 1

    if respawn_data["attempts"] >= manager.max_respawn_attempts:
        logger.warning("Max respawn attempts reached for NPC", npc_id=npc_id)
        return True, False

    return False, False


def _cleanup_respawn_queue(manager: Any, npcs_to_remove: list[str]) -> None:
    """Remove processed NPCs from respawn queue."""
    for npc_id in npcs_to_remove:
        logger.debug("Removing NPC from respawn queue", npc_id=npc_id)
        del manager.respawn_queue[npc_id]


def _attempt_respawn_impl(manager: Any, npc_id: str, respawn_data: dict[str, Any]) -> bool:
    """Attempt to respawn an NPC. Returns True if respawn was successful."""
    try:
        definition = respawn_data["definition"]
        room_id = respawn_data["room_id"]
        reason = respawn_data["reason"]

        can_spawn, _ = manager.can_spawn_npc(definition, room_id, f"respawn:{reason}")
        if not can_spawn:
            logger.debug("Cannot respawn NPC - spawn conditions not met", npc_id=npc_id)
            return False

        new_npc_id, _ = manager.spawn_npc(definition, room_id, f"respawn: {reason}")
        if new_npc_id:
            if new_npc_id != npc_id and npc_id in manager.lifecycle_records:
                old_record = manager.lifecycle_records[npc_id]
                manager.lifecycle_records[new_npc_id] = old_record
                del manager.lifecycle_records[npc_id]

            logger.info("Successfully respawned NPC", old_npc_id=npc_id, new_npc_id=new_npc_id)
            return True

        return False

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC respawn errors unpredictable
        logger.error("Failed to respawn NPC", npc_id=npc_id, error=str(e))
        return False
