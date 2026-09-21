"""
Combat flee handler for involuntary and voluntary flee logic.

Handles checking if players should involuntarily flee due to lucidity effects,
and the voluntary flee success roll (used by /flee command and flee effect).
"""

# pylint: disable=too-many-return-statements  # Reason: Flee handler requires multiple return statements for different flee condition checks and state evaluations

import random
import secrets
from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING, Any, Protocol, cast
from uuid import UUID

from server.database import get_async_session
from server.models.combat import (
    CombatAction,
    CombatInstance,
    CombatParticipant,
    CombatParticipantType,
    CombatResult,
    CombatStatus,
)
from server.services.lucidity_command_disruption import should_involuntary_flee
from server.services.lucidity_service import LucidityService
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

# pylint: disable=unnecessary-ellipsis  # Reason: Protocol stubs need ... for basedpyright reportReturnType


class _FleeFreeHitsCombatService(Protocol):
    """CombatService surface needed for failed-flee free hits (#820)."""

    def get_combat(self, combat_id: UUID) -> CombatInstance | None:
        """Return active combat or None."""
        ...

    async def process_attack(
        self,
        attacker_id: UUID,
        target_id: UUID,
        damage: int = 10,
        is_initial_attack: bool = False,
        damage_type: str = "physical",
    ) -> CombatResult:
        """Apply one attack; returns result including death/combat-end flags."""
        ...


# pylint: enable=unnecessary-ellipsis

logger = get_logger(__name__)

# Voluntary flee formula: base chance + bonus per exit - penalty per opponent (tune as needed)
VOLUNTARY_FLEE_BASE_CHANCE = 0.50
VOLUNTARY_FLEE_BONUS_PER_EXIT = 0.10
VOLUNTARY_FLEE_PENALTY_PER_OPPONENT = 0.10
VOLUNTARY_FLEE_MAX_CHANCE = 0.95
VOLUNTARY_FLEE_MIN_CHANCE = 0.10


def try_voluntary_flee_roll(combat: CombatInstance, fleeing_participant_id: UUID, num_exits: int) -> bool:
    """
    Roll for voluntary flee success (no side effects).

    Formula: base + (bonus * num_exits) - (penalty * num_opponents), clamped.
    Uses random.random() for game mechanics (not cryptographic).

    Args:
        combat: Current combat instance
        fleeing_participant_id: Participant attempting to flee
        num_exits: Number of valid adjacent exits

    Returns:
        True if flee succeeds, False otherwise
    """
    if num_exits <= 0:
        return False
    opponents = [
        p
        for p in combat.participants.values()
        if p.participant_id != fleeing_participant_id and p.can_act_in_combat() and not p.is_dead()
    ]
    num_opponents = len(opponents)
    chance = (
        VOLUNTARY_FLEE_BASE_CHANCE
        + (VOLUNTARY_FLEE_BONUS_PER_EXIT * num_exits)
        - (VOLUNTARY_FLEE_PENALTY_PER_OPPONENT * num_opponents)
    )
    chance = max(VOLUNTARY_FLEE_MIN_CHANCE, min(VOLUNTARY_FLEE_MAX_CHANCE, chance))
    roll = random.random()  # nosec B311: Game mechanics probability, not cryptographic
    return roll < chance


def _acting_opponents(combat: CombatInstance, fleeing_participant_id: UUID) -> list[CombatParticipant]:
    """Opponents who can act and are not dead (same filter as try_voluntary_flee_roll)."""
    return [
        p
        for p in combat.participants.values()
        if p.participant_id != fleeing_participant_id and p.can_act_in_combat() and not p.is_dead()
    ]


def _ordered_free_hit_attackers(combat: CombatInstance, fleeing_participant_id: UUID) -> list[CombatParticipant]:
    """Opponents in turn_order first, then any remaining sorted by participant_id."""
    opponents = _acting_opponents(combat, fleeing_participant_id)
    by_id = {p.participant_id: p for p in opponents}
    ordered: list[CombatParticipant] = []
    seen: set[UUID] = set()
    for pid in combat.turn_order:
        participant = by_id.get(pid)
        if participant is not None:
            ordered.append(participant)
            seen.add(pid)
    remaining = sorted(
        (p for p in opponents if p.participant_id not in seen),
        key=lambda p: p.participant_id,
    )
    ordered.extend(remaining)
    return ordered


async def _resolve_free_hit_damage(
    combat_service: _FleeFreeHitsCombatService,
    attacker: CombatParticipant,
    fleer: CombatParticipant,
) -> tuple[int, str]:
    """Resolve damage for one free hit (NPC vs player resolvers)."""
    from server.config import get_config
    from server.game.npcs.attack_damage import resolve_npc_attack_damage
    from server.services.combat_turn_participant_actions import resolve_player_attack_damage

    config = get_config()
    if attacker.participant_type == CombatParticipantType.PLAYER:
        damage, damage_type = await resolve_player_attack_damage(
            cast("CombatService", combat_service),
            attacker,
            fleer,
            config,
        )
        return damage, damage_type
    damage = resolve_npc_attack_damage(
        attacker.npc_base_stats,
        attacker.npc_behavior_config,
        fallback=config.game.basic_unarmed_damage,
    )
    return damage, "physical"


async def _deliver_one_flee_free_hit(
    combat_service: _FleeFreeHitsCombatService,
    combat_id: UUID,
    fleeing_participant_id: UUID,
    attacker_id: UUID,
) -> bool:
    """Apply one free hit. Returns False when the free-hit loop should stop."""
    combat = combat_service.get_combat(combat_id)
    if combat is None or combat.status != CombatStatus.ACTIVE:
        return False
    fleer = combat.participants.get(fleeing_participant_id)
    if fleer is None or fleer.is_dead():
        return False
    attacker = combat.participants.get(attacker_id)
    if attacker is None or not attacker.can_act_in_combat() or attacker.is_dead():
        return True

    damage, damage_type = await _resolve_free_hit_damage(combat_service, attacker, fleer)
    result = await combat_service.process_attack(
        attacker_id=attacker.participant_id,
        target_id=fleeing_participant_id,
        damage=damage,
        damage_type=damage_type,
    )
    return not (result.combat_ended or result.target_died)


async def execute_flee_failed_free_hits(
    combat_service: _FleeFreeHitsCombatService,
    combat_id: UUID,
    fleeing_participant_id: UUID,
) -> None:
    """
    On failed voluntary flee, each acting opponent gets one free attack on the fleer.

    Stops early if the fleer dies or combat ends. Order follows turn_order, then
    remaining opponents by participant_id (#820).
    """
    combat = combat_service.get_combat(combat_id)
    if combat is None:
        return

    attacker_ids = [p.participant_id for p in _ordered_free_hit_attackers(combat, fleeing_participant_id)]
    for attacker_id in attacker_ids:
        if not await _deliver_one_flee_free_hit(combat_service, combat_id, fleeing_participant_id, attacker_id):
            return


async def _handle_failed_voluntary_flee(
    combat_service: Any, combat: CombatInstance, fleeing_participant_id: UUID
) -> None:
    skip_action = CombatAction(
        combat_id=combat.combat_id,
        attacker_id=fleeing_participant_id,
        target_id=fleeing_participant_id,
        action_type="flee_skip",
        damage=0,
    )
    combat.queue_action(fleeing_participant_id, skip_action)
    logger.info(
        "Voluntary flee failed; action consumed",
        combat_id=combat.combat_id,
        fleeing_id=fleeing_participant_id,
    )
    try:
        await combat_service.execute_flee_failed_free_hits(combat.combat_id, fleeing_participant_id)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Free hit execution must not break flee failure handling
        logger.warning(
            "Error executing flee failed free hits",
            combat_id=combat.combat_id,
            fleeing_id=fleeing_participant_id,
            error=str(e),
            error_type=type(e).__name__,
        )


async def execute_voluntary_flee(
    combat_service: Any,
    get_room_by_id: Callable[[str], Any],
    movement_service: Any,
    combat: CombatInstance,
    fleeing_participant_id: UUID,
) -> bool:
    """
    Execute voluntary flee for a combat participant (shared by /flee command and flee effect).

    Assumes caller has already verified: participant is in combat, room has exits.
    On failure: participant remains in combat but loses their action for the round; returns False.
    On success: ends combat and moves the participant to a random adjacent room, returns True.
    Player movement only; NPC movement requires move_npc_callback (future).
    """
    room_id = str(combat.room_id)
    room = get_room_by_id(room_id)
    if not room:
        return False
    exits = getattr(room, "exits", None) or {}
    if not exits:
        return False
    num_exits = len(exits)
    participant = combat.participants.get(fleeing_participant_id)
    if not participant:
        return False

    # Attempting to flee should consume this participant's queued action for the round.
    # Clear any previously queued actions (e.g. attacks) so they cannot also execute.
    combat.clear_queued_actions(fleeing_participant_id)

    if not try_voluntary_flee_roll(combat, fleeing_participant_id, num_exits):
        await _handle_failed_voluntary_flee(combat_service, combat, fleeing_participant_id)
        return False

    to_room_id = str(secrets.choice(list(exits.values())))
    reason = f"{participant.name} flees from combat!"
    await combat_service.end_combat(combat.combat_id, reason)
    moved = await movement_service.move_player(fleeing_participant_id, room_id, to_room_id)
    if not moved:
        logger.warning(
            "Voluntary flee: combat ended but move_player failed",
            fleeing_id=fleeing_participant_id,
            from_room=room_id,
            to_room=to_room_id,
        )
    return bool(moved)


async def _involuntary_flee_on_cooldown(
    lucidity_service: LucidityService, participant_id: UUID, cooldown_code: str
) -> bool:
    """True if the involuntary-flee cooldown is still active."""
    cooldown = await lucidity_service.get_cooldown(participant_id, cooldown_code)
    if not cooldown or not cooldown.cooldown_expires_at:
        return False
    if cooldown.cooldown_expires_at.tzinfo is None:
        expires_at = cooldown.cooldown_expires_at.replace(tzinfo=UTC)
    else:
        expires_at = cooldown.cooldown_expires_at
    if datetime.now(UTC) < expires_at:
        logger.debug(
            "Involuntary flee on cooldown",
            player_id=participant_id,
            expires_at=expires_at.isoformat(),
        )
        return True
    return False


async def _check_involuntary_flee_with_session(
    session: Any,
    target: CombatParticipant,
    damage_percent: float,
    damage: int,
) -> bool:
    """
    Check tier, damage threshold, and cooldown; set cooldown and commit if flee allowed.
    Returns True if player should flee, False otherwise.
    """
    lucidity_service = LucidityService(session)
    lucidity_record = await lucidity_service.get_player_lucidity(target.participant_id)
    tier = lucidity_record.current_tier if lucidity_record else "lucid"
    if not should_involuntary_flee(tier, damage_percent):
        return False
    cooldown_code = "involuntary_flee"
    if await _involuntary_flee_on_cooldown(lucidity_service, target.participant_id, cooldown_code):
        return False
    cooldown_expires = datetime.now(UTC) + timedelta(minutes=2)
    cooldown_expires_naive = cooldown_expires.replace(tzinfo=None)
    await lucidity_service.set_cooldown(target.participant_id, cooldown_code, cooldown_expires_naive)
    await session.commit()
    logger.info(
        "Involuntary flee conditions met",
        player_id=target.participant_id,
        tier=tier,
        damage=damage,
        damage_percent=damage_percent,
        max_dp=target.max_dp,
    )
    return True


async def check_involuntary_flee(target: CombatParticipant, damage: int) -> bool:
    """
    Check if player should involuntarily flee due to lucidity effects.

    Deranged tier players have a 20% chance to auto-flee when taking >15% max HP damage
    in one hit, with a 2-minute cooldown.

    Args:
        target: The player participant who took damage
        damage: Amount of damage taken

    Returns:
        True if player should flee, False otherwise
    """
    try:
        if target.max_dp <= 0:
            return False
        damage_percent = damage / target.max_dp
        async for session in get_async_session():
            try:
                return await _check_involuntary_flee_with_session(session, target, damage_percent, damage)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Flee check errors unpredictable, must not fail combat
                logger.warning(
                    "Error checking involuntary flee",
                    player_id=target.participant_id,
                    error=str(e),
                    error_type=type(e).__name__,
                )
                await session.rollback()
                return False
        return False
    except Exception as e:  # pylint: disable=broad-except  # Reason: Flee check errors unpredictable, must catch all exceptions to handle various failure modes during flee validation
        logger.warning(
            "Error in involuntary flee check (session creation)",
            player_id=target.participant_id,
            error=str(e),
            error_type=type(e).__name__,
        )
        return False
