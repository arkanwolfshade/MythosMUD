"""
Attack flow and combat action queuing for CombatService.

Extracted from combat_service.py to keep module line count under limit.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatResult
from server.services.aggro_threat import add_damage_threat
from server.services.nats_exceptions import NATSError
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def handle_combat_completion(service: CombatService, combat: CombatInstance, combat_ended: bool) -> None:
    """Handle combat completion or continuation."""
    if combat_ended:
        logger.info(
            "Combat ending - starting end combat process",
            combat_id=combat.combat_id,
            room_id=combat.room_id,
        )
        try:
            await service.end_combat(combat.combat_id, "Combat ended - one participant defeated")
            logger.info("Combat end process completed successfully", combat_id=combat.combat_id)
        except (
            NATSError,
            ValueError,
            RuntimeError,
            AttributeError,
            ConnectionError,
            TypeError,
            KeyError,
        ) as end_combat_error:
            logger.error(
                "Error ending combat - preventing disconnect",
                combat_id=combat.combat_id,
                room_id=combat.room_id,
                error=str(end_combat_error),
                exc_info=True,
            )
    else:
        from server.app.game_tick_processing import (  # noqa: E402  # Lazy import to avoid circular dependency
            get_current_tick,
        )

        combat.next_turn_tick = get_current_tick() + combat.turn_interval_ticks
        logger.debug("Combat attack processed, auto-progression enabled", combat_id=combat.combat_id)


async def queue_combat_action(
    service: CombatService,
    combat_id: UUID,
    participant_id: UUID,
    action_type: str,
    target_id: UUID | None = None,
    damage: int | None = None,
    spell_id: str | None = None,
    spell_name: str | None = None,
) -> bool:
    """Queue a combat action for a participant to execute in the next round."""
    from server.models.combat import CombatAction  # noqa: PLC0415  # Local import to avoid circular dependency

    combat = service.get_combat(combat_id)
    if not combat:
        logger.warning("Combat not found for action queuing", combat_id=combat_id, participant_id=participant_id)
        return False
    if participant_id not in combat.participants:
        logger.warning(
            "Participant not in combat",
            combat_id=combat_id,
            participant_id=participant_id,
            action_type=action_type,
        )
        return False
    action = CombatAction(
        combat_id=combat_id,
        attacker_id=participant_id,
        target_id=target_id or UUID("00000000-0000-0000-0000-000000000000"),
        action_type=action_type,
        damage=damage or 10,
        spell_id=spell_id,
        spell_name=spell_name,
    )
    combat.queue_action(participant_id, action)
    logger.info(
        "Combat action queued",
        combat_id=combat_id,
        participant_id=participant_id,
        action_type=action_type,
        round=action.round,
    )
    return True


def _effective_room_for_melee(
    room: str | None,
    participant_id: UUID,
    combat_room_id: str,
    participants: dict[UUID, CombatParticipant],
) -> str | None:
    """Use combat_room_id when room is None and participant is in this combat; else return room (or None)."""
    if room is not None:
        return room
    if participant_id in participants:
        return combat_room_id
    return None


def _melee_location_fail_reason(
    attacker: CombatParticipant,
    target: CombatParticipant,
    attacker_room: str | None,
    target_room: str | None,
    combat_room_id: str,
) -> str:
    """Build reason string when melee location validation fails."""
    return (
        f"Combat ended: participant rooms do not match combat room. "
        f"Attacker {attacker.name!r} is in room {attacker_room!r}, "
        f"target {target.name!r} is in room {target_room!r}, "
        f"combat room is {combat_room_id!r}."
    )


async def validate_melee_location(
    service: CombatService,
    combat: CombatInstance,
    attacker: CombatParticipant,
    target: CombatParticipant,
) -> tuple[bool, str | None]:
    """
    Validate that both participants are still in combat.room_id (melee requires same room).
    Returns (True, None) if valid, (False, reason) if invalid.
    """
    combat_room_id = combat.room_id
    attacker_room = await service.get_participant_current_room(attacker)
    target_room = await service.get_participant_current_room(target)
    attacker_effective = _effective_room_for_melee(
        attacker_room, attacker.participant_id, combat_room_id, combat.participants
    )
    target_effective = _effective_room_for_melee(
        target_room, target.participant_id, combat_room_id, combat.participants
    )
    if attacker_effective is None and target_effective is None:
        return True, None
    if attacker_effective != combat_room_id or target_effective != combat_room_id:
        return False, _melee_location_fail_reason(
            attacker, target, attacker_effective, target_effective, combat_room_id
        )
    return True, None


async def validate_melee_or_end_combat(
    service: CombatService,
    combat: CombatInstance,
    current_participant: CombatParticipant,
    target: CombatParticipant,
    attacker_id: UUID,
    target_id: UUID,
) -> CombatResult | None:
    """Validate melee location; if invalid, end combat and return early result. Otherwise return None."""
    valid, reason = await service.validate_melee_location(combat, current_participant, target)
    if not valid and reason:
        logger.warning(
            "Melee room validation failed, ending combat",
            combat_id=combat.combat_id,
            attacker_id=attacker_id,
            target_id=target_id,
            reason=reason,
        )
        await service.end_combat(combat.combat_id, reason)
        return CombatResult(
            success=False,
            damage=0,
            target_died=False,
            combat_ended=True,
            message=reason,
            combat_id=combat.combat_id,
        )
    return None


async def apply_damage_and_check_involuntary_flee(
    service: CombatService,
    combat: CombatInstance,
    current_participant: CombatParticipant,
    target: CombatParticipant,
    damage: int,
) -> tuple[bool, bool, CombatResult | None]:
    """Apply attack damage and check for involuntary flee. Returns (target_died, mortally_wounded, early_result)."""
    _, target_died, target_mortally_wounded = await service.apply_attack_damage(combat, target, damage)
    if target.participant_type != CombatParticipantType.PLAYER:
        return (target_died, target_mortally_wounded, None)
    should_flee = await service.check_involuntary_flee(target, damage, combat)
    if not should_flee:
        return (target_died, target_mortally_wounded, None)
    logger.info(
        "Involuntary flee triggered",
        player_id=target.participant_id,
        player_name=target.name,
        damage=damage,
        max_dp=target.max_dp,
    )
    await service.end_combat(combat.combat_id, f"{target.name} flees in terror from the attack")
    early = CombatResult(
        success=True,
        damage=damage,
        target_died=False,
        combat_ended=True,
        message=f"{target.name} flees in panic from {current_participant.name}'s attack!",
        combat_id=combat.combat_id,
    )
    return (target_died, target_mortally_wounded, early)


async def finalize_attack_result(
    service: CombatService,
    combat: CombatInstance,
    current_participant: CombatParticipant,
    target: CombatParticipant,
    damage: int,
    target_died: bool,
    target_mortally_wounded: bool,
    target_id: UUID,
) -> CombatResult:
    """Build result, handle state changes, events, XP, and combat completion."""
    # ADR-016: add damage threat to NPC's hate list when this attack hit an NPC (passive_mob/aggression_level in aggro_threat)
    if target.participant_type == CombatParticipantType.NPC:
        add_damage_threat(
            combat,
            target.participant_id,
            current_participant.participant_id,
            damage,
            npc_participant=target,
        )
    combat_ended = combat.is_combat_over()
    health_info = f" ({target.current_dp}/{target.max_dp} DP)"
    attack_message = f"{current_participant.name} attacks {target.name} for {damage} damage{health_info}"
    result = CombatResult(
        success=True,
        damage=damage,
        target_died=target_died,
        combat_ended=combat_ended,
        message=attack_message,
        combat_id=combat.combat_id,
    )
    await service.handle_target_state_changes(target, current_participant, target_mortally_wounded, target_died, combat)
    xp_awarded = await service.handle_attack_events_and_xp(
        current_participant, target, damage, combat, target_died, target_id
    )
    result.xp_awarded = xp_awarded if xp_awarded is not None else 0
    if target_died:
        await service.award_xp_to_player(current_participant, target, target_id, result.xp_awarded)
    await service.handle_combat_completion(combat, combat_ended)
    return result


async def process_attack(
    service: CombatService,
    attacker_id: UUID,
    target_id: UUID,
    damage: int = 10,
    is_initial_attack: bool = False,
    damage_type: str = "physical",
) -> CombatResult:
    """Process an attack action in combat."""
    combat, current_participant, target = await service.validate_and_get_combat_participants(
        attacker_id, target_id, is_initial_attack
    )
    early = await service.validate_melee_or_end_combat(combat, current_participant, target, attacker_id, target_id)
    if early is not None:
        return early
    logger.info(
        "Processing attack",
        attacker_name=current_participant.name,
        target_name=target.name,
        damage=damage,
        damage_type=damage_type,
    )
    target_died, target_mortally_wounded, early = await service.apply_damage_and_check_involuntary_flee(
        combat, current_participant, target, damage
    )
    if early is not None:
        return early
    return await service.finalize_attack_result(
        combat, current_participant, target, damage, target_died, target_mortally_wounded, target_id
    )


if TYPE_CHECKING:
    from server.services.combat_service import CombatService
