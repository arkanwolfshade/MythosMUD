"""
NPC combat event publishing for CombatService.

Extracted from combat_service.py to keep module line count under limit.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from server.events.combat_events import NPCDiedEvent, NPCTookDamageEvent
from server.services.nats_exceptions import NATSError
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def publish_npc_damage_event(
    service: CombatService,
    room_id: str,
    npc_id: UUID | str,
    npc_name: str,
    damage: int,
    current_dp: int,
    max_dp: int,
    combat_id: UUID | None = None,
) -> bool:
    """
    Publish an npc_took_damage event to NATS (e.g. for steal-life or other non-combat damage).

    Uses the same event shape as combat so the client can update displayed NPC DP.
    """
    try:
        cid = combat_id if combat_id is not None else UUID(int=0)
        event = NPCTookDamageEvent(
            combat_id=cid,
            room_id=room_id,
            npc_id=npc_id,
            npc_name=npc_name,
            damage=damage,
            current_dp=current_dp,
            max_dp=max_dp,
        )
        return await service.publish_npc_took_damage_event_to_nats(event)
    except (NATSError, ValueError, RuntimeError, AttributeError, ConnectionError) as e:
        logger.error(
            "Error publishing NPC damage event",
            error=str(e),
            room_id=room_id,
            npc_name=npc_name,
            exc_info=True,
        )
        return False


async def publish_npc_died_event(
    service: CombatService,
    room_id: str,
    npc_id: UUID | str,
    npc_name: str,
    xp_reward: int = 0,
    killer_id: str | None = None,
) -> bool:
    """
    Publish an npc_died event to NATS (e.g. when steal-life or other non-combat damage kills an NPC).

    Ensures the client shows the death message in the Game Info panel and EventBus receives NPCDied.
    """
    try:
        death_event = NPCDiedEvent(
            combat_id=UUID(int=0),
            room_id=room_id,
            npc_id=npc_id,
            npc_name=npc_name,
            xp_reward=xp_reward,
            killer_id=killer_id,
        )
        return await service.publish_npc_died_event_to_nats(death_event)
    except (NATSError, ValueError, RuntimeError, AttributeError, ConnectionError) as e:
        logger.error(
            "Error publishing NPC died event",
            error=str(e),
            room_id=room_id,
            npc_name=npc_name,
            exc_info=True,
        )
        return False


if TYPE_CHECKING:
    from server.services.combat_service import CombatService
