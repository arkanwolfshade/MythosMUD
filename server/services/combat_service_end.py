"""
End combat logic for CombatService.

Extracted from combat_service.py to keep module line count under limit.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from server.models.combat import CombatStatus
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


if TYPE_CHECKING:
    from server.services.combat_service import CombatService
