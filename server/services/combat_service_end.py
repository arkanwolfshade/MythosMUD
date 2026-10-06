"""
End combat logic for CombatService.

Extracted from combat_service.py to keep module line count under limit.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from server.models.combat import CombatParticipantType, CombatStatus
from server.services.aggro_threat import clear_aggro_for_combat, remove_entity_from_aggro
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def end_combat(
    service: "CombatService",  # noqa: RUF013, UP037  # Forward ref; type only in TYPE_CHECKING
    combat_id: UUID,
    reason: str = "Combat ended",
) -> None:
    """
    End a combat instance.

    Args:
        service: CombatService instance (authoritative state).
        combat_id: ID of the combat to end.
        reason: Reason for ending combat.
    """
    combat = service.get_combat(combat_id)
    if not combat:
        logger.warning("Attempted to end non-existent combat", combat_id=combat_id)
        return

    logger.info("Ending combat", combat_id=combat_id, reason=reason)

    # Clear aggro state (ADR-016) so hate lists and current targets are not retained
    clear_aggro_for_combat(combat)

    combat.status = CombatStatus.ENDED
    service.cleanup_combat_tracking(combat)
    await service.notify_player_combat_ended(combat_id)

    logger.debug(
        "Preparing combat ended event",
        combat_id=combat_id,
        room_id=combat.room_id,
        participant_count=len(combat.participants),
    )

    service.check_connection_state(combat.room_id)
    await service.publish_combat_ended_event(combat, reason)

    logger.info("Combat ended successfully", combat_id=combat_id)


async def remove_participant(
    service: "CombatService",  # noqa: RUF013, UP037  # Forward ref; type only in TYPE_CHECKING
    combat_id: UUID,
    participant_id: UUID,
    reason: str = "Participant left combat",
) -> bool:
    """
    Remove one player from a combat, ending it only when nobody is left to fight (#833).

    If no other living player remains, this is just ``end_combat`` (the leaver stays on the roster so the
    ended event still reaches them, exactly as in a 1v1). Otherwise only that player is dropped: queued
    actions, hate-list entries, target links and combat tracking go with them and the fight continues.

    Returns:
        True if the combat ended, False if it continues or the participant was not in it.
    """
    combat = service.get_combat(combat_id)
    if not combat or participant_id not in combat.participants:
        return False

    others_alive = [
        p
        for pid, p in combat.participants.items()
        if pid != participant_id and p.participant_type == CombatParticipantType.PLAYER and not p.is_dead()
    ]
    if not others_alive:
        await end_combat(service, combat_id, reason)
        return True

    logger.info("Participant leaving combat", combat_id=combat_id, participant_id=participant_id, reason=reason)
    combat.clear_queued_actions(participant_id)
    _ = combat.round_actions.pop(participant_id, None)
    remove_entity_from_aggro(combat, participant_id)
    del combat.participants[participant_id]
    combat.turn_order = [pid for pid in combat.turn_order if pid != participant_id]
    await service.untrack_participant(participant_id)
    return False


if TYPE_CHECKING:
    from server.services.combat_service import CombatService
