"""
Queued protect action (#991): a Fighting roll to cover an ally, and the redirect that cover gives.

``protect <ally>`` spends the player's action for the round (it is queued like an attack and taunt, so the player
does not also auto-attack). It resolves on the player's initiative slot:

=================  ==========================================================  =====================================
Roll               Effect                                                      Room line
=================  ==========================================================  =====================================
Hard / Extreme     cover for the rest of this round and the next two           "<X> throws themselves in front of <Y>!"
Regular            cover for the rest of this round and the next one           "<X> throws themselves in front of <Y>!"
Failure / Fumble   nothing; the round is spent                                 "<X> fails to reach <Y> in time."
=================  ==========================================================  =====================================

While cover is active every NPC attack aimed at the ally lands on the protector instead (see ``intercept_for_guard``),
and the protector earns the guarding threat multiplier (see ``aggro_threat``). A successful roll also hands the
protector a share of the ally's current threat on each NPC, so the NPC tends to stay on the protector afterwards.
"""

# pyright: reportImportCycles=false
# Reason: CombatService is imported under TYPE_CHECKING for annotations only; the runtime import graph has no cycle,
# but the checker follows that edge through combat_service back to the modules that import this one.

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from server.config import get_config
from server.game.skill_service import SuccessLevel
from server.models.combat import CombatAction, CombatInstance, CombatParticipant, CombatParticipantType
from server.services.aggro_threat import add_damage_threat, get_or_create_hate_list, update_aggro
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

logger = get_logger(__name__)

#: Skills a protect rolls against (Fighting only: shoving in front of a blow is a brawling maneuver).
PROTECT_SKILL_KEYS: tuple[str, ...] = ("fighting",)

#: Grades that earn one extra round of cover over a Regular success.
_EXTRA_COVER_LEVELS = frozenset({SuccessLevel.HARD, SuccessLevel.EXTREME})


def protect_outcome_line(level: SuccessLevel, protector_name: str, ally_name: str) -> str:
    """The single room line that announces a protect's result."""
    if level.is_success:
        return f"{protector_name} throws themselves in front of {ally_name}!"
    return f"{protector_name} fails to reach {ally_name} in time."


async def _announce(combat_service: CombatService, combat: CombatInstance, line: str) -> None:
    """Send the room line, if the messaging integration is available."""
    integration = combat_service.get_npc_combat_integration_service()
    if integration is None:
        return
    _ = await integration.get_messaging_integration().broadcast_protect_result(
        str(combat.room_id), str(combat.combat_id), line
    )


def _share_threat(
    combat: CombatInstance, protector: CombatParticipant, ally: CombatParticipant
) -> list[CombatParticipant]:
    """Give the protector a share of the ally's threat on every living NPC. Returns the NPCs that were touched."""
    share = get_config().game.aggro_protect_threat_share
    touched: list[CombatParticipant] = []
    for npc in combat.participants.values():
        if npc.participant_type != CombatParticipantType.NPC or npc.is_dead():
            continue
        ally_threat = combat.npc_hate_lists.get(npc.participant_id, {}).get(ally.participant_id, 0.0)
        if ally_threat <= 0:
            continue
        hate = get_or_create_hate_list(combat, npc.participant_id)
        hate[protector.participant_id] = hate.get(protector.participant_id, 0.0) + share * ally_threat
        touched.append(npc)
    return touched


def _cover(combat: CombatInstance, protector: CombatParticipant, ally: CombatParticipant, level: SuccessLevel) -> int:
    """Record the cover. ``combat_round`` is still the round being resolved, so these rounds follow this one."""
    rounds = get_config().game.protect_cover_rounds + (1 if level in _EXTRA_COVER_LEVELS else 0)
    expires_round = combat.combat_round + rounds
    combat.set_guard(ally.participant_id, protector.participant_id, expires_round)
    return expires_round


async def _broadcast_switches(
    combat_service: CombatService, combat: CombatInstance, npcs: list[CombatParticipant]
) -> None:
    """Re-run target selection for each NPC the threat share touched and announce any switch."""
    switches: list[tuple[UUID, str, str]] = []
    for npc in npcs:
        new_target_id, did_switch = update_aggro(combat, npc, combat.room_id, combat.participants)
        if did_switch and new_target_id:
            new_target = combat.participants.get(new_target_id)
            switches.append((npc.participant_id, npc.name, new_target.name if new_target else "someone"))
    if switches:
        await combat_service.broadcast_aggro_target_switches(str(combat.room_id), combat.combat_id, switches)


async def resolve_protect_action(
    combat_service: CombatService, combat: CombatInstance, protector: CombatParticipant, action: CombatAction
) -> None:
    """
    Resolve one queued protect: roll, record the cover, share threat, announce it, and broadcast any target switch.

    Both players are re-checked here because the round may have moved on since the command was typed.
    """
    ally = combat.participants.get(action.target_id)
    if (
        ally is None
        or ally is protector
        or ally.participant_type != CombatParticipantType.PLAYER
        or ally.is_dead()
        or not protector.can_act_in_combat()
    ):
        logger.info("Queued protect dropped: ally or protector is out", combat_id=combat.combat_id)
        return
    skill_service = combat_service.skill_service
    if skill_service is None:
        logger.warning("Queued protect skipped: skill service is not linked", combat_id=combat.combat_id)
        return
    protector_room = await combat_service.get_participant_current_room(protector)
    if protector_room is None or protector_room != str(combat.room_id):
        logger.info("Queued protect dropped: protector left the combat room", combat_id=combat.combat_id)
        return

    level = await skill_service.roll_best_skill_check(protector.participant_id, PROTECT_SKILL_KEYS)
    touched: list[CombatParticipant] = []
    if level.is_success:
        _ = _cover(combat, protector, ally, level)
        touched = _share_threat(combat, protector, ally)
    logger.info(
        "Protect resolved",
        combat_id=combat.combat_id,
        protector_id=protector.participant_id,
        ally_id=ally.participant_id,
        result=level.value,
    )
    await _announce(combat_service, combat, protect_outcome_line(level, protector.name, ally.name))
    await _broadcast_switches(combat_service, combat, touched)


async def intercept_for_guard(
    combat_service: CombatService,
    combat: CombatInstance,
    attacker: CombatParticipant,
    target: CombatParticipant,
    damage: int,
) -> CombatParticipant:
    """
    Who an attack really lands on: the protector when an NPC swings at a covered player, else the intended target.

    A redirect happens once (the protector's own cover is not consulted), earns the protector damage threat on the
    attacking NPC for the blow it absorbs, and is announced with one room line.
    """
    if (
        attacker.participant_type != CombatParticipantType.NPC
        or target.participant_type != CombatParticipantType.PLAYER
    ):
        return target
    guard = combat.active_guard(target.participant_id)
    protector = combat.participants.get(guard.protector_id) if guard is not None else None
    if protector is None:
        return target
    add_damage_threat(combat, attacker.participant_id, protector.participant_id, damage, npc_participant=attacker)
    await _announce(combat_service, combat, f"{protector.name} takes the blow meant for {target.name}!")
    return protector
