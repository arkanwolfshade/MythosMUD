"""
Queued taunt action (#833): the Intimidate/Fighting roll and what each graded result does to the hate list.

``taunt`` is a combat action that spends the player's action for the round (it is queued like an attack, so the
player does not also auto-attack). It resolves on the player's initiative slot:

=================  =======================================================  ================================
Roll               Hate list                                                Room line
=================  =======================================================  ================================
Hard / Extreme     taunter becomes top, with a doubled lead                 "<X> bellows a challenge at <N>!"
Regular            taunter becomes top (the plain ADR-016 taunt)            "<X> bellows a challenge at <N>!"
Failure            no change                                                "<X>'s bluster fails to impress <N>."
Fumble             taunter is wiped from that NPC's hate list (backfire)    "<X>'s voice cracks; <N> dismisses them."
=================  =======================================================  ================================

Taunt stays room-local: the taunter must still be in the combat's room when it resolves.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from server.game.skill_service import SuccessLevel
from server.models.combat import CombatAction, CombatInstance, CombatParticipant, CombatParticipantType
from server.services.aggro_threat import apply_stealth_wipe, apply_taunt, update_aggro
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

logger = get_logger(__name__)

#: Skills a taunt rolls against; the higher one the player holds is used (a brawler or a talker can both hold aggro).
TAUNT_SKILL_KEYS: tuple[str, ...] = ("intimidate", "fighting")

#: Lead multiplier for a successful taunt; Regular is the plain taunt, Hard and Extreme double it.
_MARGIN_MULTIPLIER: dict[SuccessLevel, float] = {
    SuccessLevel.REGULAR: 1.0,
    SuccessLevel.HARD: 2.0,
    SuccessLevel.EXTREME: 2.0,
}


def taunt_outcome_line(level: SuccessLevel, taunter_name: str, npc_name: str) -> str:
    """The single room line that announces a taunt's result."""
    if level is SuccessLevel.FUMBLE:
        return f"{taunter_name}'s voice cracks; {npc_name} dismisses them."
    if level.is_success:
        return f"{taunter_name} bellows a challenge at {npc_name}!"
    return f"{taunter_name}'s bluster fails to impress {npc_name}."


def _apply_taunt_outcome(
    combat: CombatInstance, npc: CombatParticipant, taunter: CombatParticipant, level: SuccessLevel, taunter_room: str
) -> None:
    """Change the NPC's hate list according to the graded roll."""
    if level is SuccessLevel.FUMBLE:
        apply_stealth_wipe(combat, npc.participant_id, taunter.participant_id)
    elif level.is_success:
        _ = apply_taunt(
            combat,
            npc.participant_id,
            taunter.participant_id,
            str(combat.room_id),
            taunter_room,
            margin_multiplier=_MARGIN_MULTIPLIER[level],
        )


async def _announce(combat_service: CombatService, combat: CombatInstance, line: str) -> None:
    """Send the room line, if the messaging integration is available."""
    integration = combat_service.get_npc_combat_integration_service()
    if integration is None:
        return
    _ = await integration.get_messaging_integration().broadcast_taunt_result(
        str(combat.room_id), str(combat.combat_id), line
    )


async def resolve_taunt_action(
    combat_service: CombatService, combat: CombatInstance, taunter: CombatParticipant, action: CombatAction
) -> None:
    """
    Resolve one queued taunt: roll, change the hate list, announce it, and broadcast a target switch if one happened.

    The target and the taunter's room are re-checked here because the round may have moved on since the command.
    """
    npc = combat.participants.get(action.target_id)
    if npc is None or npc.participant_type != CombatParticipantType.NPC or npc.is_dead():
        logger.info("Queued taunt dropped: target is gone", combat_id=combat.combat_id, target_id=action.target_id)
        return
    skill_service = combat_service.skill_service
    if skill_service is None:
        logger.warning("Queued taunt skipped: skill service is not linked", combat_id=combat.combat_id)
        return
    taunter_room = await combat_service.get_participant_current_room(taunter)
    if taunter_room is None or taunter_room != str(combat.room_id):
        logger.info("Queued taunt dropped: taunter left the combat room", combat_id=combat.combat_id)
        return

    level = await skill_service.roll_best_skill_check(taunter.participant_id, TAUNT_SKILL_KEYS)
    _apply_taunt_outcome(combat, npc, taunter, level, taunter_room)
    logger.info(
        "Taunt resolved",
        combat_id=combat.combat_id,
        taunter_id=taunter.participant_id,
        npc_id=npc.participant_id,
        result=level.value,
    )
    await _announce(combat_service, combat, taunt_outcome_line(level, taunter.name, npc.name))

    new_target_id, did_switch = update_aggro(combat, npc, combat.room_id, combat.participants)
    if did_switch and new_target_id:
        new_target = combat.participants.get(new_target_id)
        await combat_service.broadcast_aggro_target_switches(
            str(combat.room_id),
            combat.combat_id,
            [(npc.participant_id, npc.name, new_target.name if new_target else "someone")],
        )
