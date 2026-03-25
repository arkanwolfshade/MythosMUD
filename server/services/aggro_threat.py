"""
Aggro and threat management for combat (ADR-016).

Per-NPC hate lists, threat from damage/healing/taunt, stability margin,
stealth wipe, and UpdateAggro for target resolution.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID

from server.config import get_config
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _get_aggro_config() -> Any:
    """Return game config for aggro constants."""
    return get_config().game


def get_or_create_hate_list(combat: CombatInstance, npc_id: UUID) -> dict[UUID, float]:
    """Get or create the hate list for an NPC. Mutates combat.npc_hate_lists."""
    if npc_id not in combat.npc_hate_lists:
        combat.npc_hate_lists[npc_id] = {}
    return combat.npc_hate_lists[npc_id]


def _aggression_scale(aggression_level: int | None) -> float:
    """Scale factor from aggression_level 0-10. None => 1.0 (full threat)."""
    if aggression_level is None:
        return 1.0
    level = max(0, min(10, aggression_level))
    return 0.5 + 0.05 * level


def add_damage_threat(
    combat: CombatInstance,
    npc_id: UUID,
    source_entity_id: UUID,
    amount: float,
    multiplier: float | None = None,
    npc_participant: CombatParticipant | None = None,
) -> None:
    """
    Add threat to an NPC's hate list from damage dealt.

    threat += amount * multiplier (default from config aggro_damage_threat_multiplier).
    passive_mob: no damage threat (only taunt/healing add threat). aggression_level 0-10 scales multiplier.
    """
    if amount <= 0:
        return
    participant = npc_participant or combat.participants.get(npc_id)
    if participant is not None and getattr(participant, "npc_type", None) == "passive_mob":
        logger.debug(
            "Damage threat skipped (passive_mob)",
            npc_id=str(npc_id),
            source_id=str(source_entity_id),
        )
        return
    config = _get_aggro_config()
    mult = multiplier if multiplier is not None else getattr(config, "aggro_damage_threat_multiplier", 1.0)
    scale = _aggression_scale(getattr(participant, "aggression_level", None) if participant else None)
    mult *= scale
    delta = amount * mult
    hate = get_or_create_hate_list(combat, npc_id)
    hate[source_entity_id] = hate.get(source_entity_id, 0.0) + delta
    logger.debug(
        "Damage threat added",
        npc_id=str(npc_id),
        source_id=str(source_entity_id),
        amount=amount,
        delta=delta,
    )


def add_heal_threat(
    combat: CombatInstance,
    npc_id: UUID,
    healer_entity_id: UUID,
    amount: float,
    factor: float | None = None,
    npc_participant: CombatParticipant | None = None,
) -> None:
    """
    Add threat to an NPC's hate list from healing (e.g. 0.5x heal amount).

    threat += amount * factor (default from config aggro_healing_threat_factor).
    Passive mobs still receive heal threat (healers can pull). aggression_level 0-10 scales factor.
    """
    if amount <= 0:
        return
    participant = npc_participant or combat.participants.get(npc_id)
    config = _get_aggro_config()
    fac = factor if factor is not None else getattr(config, "aggro_healing_threat_factor", 0.5)
    scale = _aggression_scale(getattr(participant, "aggression_level", None) if participant else None)
    fac *= scale
    delta = amount * fac
    hate = get_or_create_hate_list(combat, npc_id)
    hate[healer_entity_id] = hate.get(healer_entity_id, 0.0) + delta
    logger.debug(
        "Heal threat added",
        npc_id=str(npc_id),
        healer_id=str(healer_entity_id),
        amount=amount,
        delta=delta,
    )


def apply_taunt(
    combat: CombatInstance,
    npc_id: UUID,
    taunter_entity_id: UUID,
    combat_room_id: str,
    taunter_room_id: str,
) -> bool:
    """
    Set taunter's threat to current top + margin so they become top. Room-local only.

    Returns True if taunt was applied (taunter in same room as combat), False otherwise.
    """
    if combat_room_id != taunter_room_id:
        logger.debug(
            "Taunt ignored (not in same room)",
            npc_id=str(npc_id),
            taunter_id=str(taunter_entity_id),
            combat_room=combat_room_id,
            taunter_room=taunter_room_id,
        )
        return False
    hate = get_or_create_hate_list(combat, npc_id)
    current_top = max(hate.values()) if hate else 0.0
    margin = current_top * 0.10 + 1.0  # become top by at least 10% + 1
    hate[taunter_entity_id] = current_top + margin
    logger.debug(
        "Taunt applied",
        npc_id=str(npc_id),
        taunter_id=str(taunter_entity_id),
        new_threat=hate[taunter_entity_id],
    )
    return True


def apply_stealth_wipe(combat: CombatInstance, npc_id: UUID, entity_id: UUID) -> None:
    """Remove entity from NPC's hate list (or set threat to 0). Stealth = full wipe."""
    if npc_id not in combat.npc_hate_lists:
        return
    hate = combat.npc_hate_lists[npc_id]
    if entity_id in hate:
        del hate[entity_id]
        logger.debug("Stealth wipe applied", npc_id=str(npc_id), entity_id=str(entity_id))


def on_player_entered_stealth(combat: CombatInstance, player_id: UUID) -> None:
    """
    Call when a player enters stealth (ADR-016 Option A: wipe).

    Removes the player from every NPC's hate list in this combat.
    Target resolution will re-run on next NPC turn (UpdateAggro) and may switch to another.
    """
    for npc_id, participant in combat.participants.items():
        if participant.participant_type == CombatParticipantType.NPC:
            apply_stealth_wipe(combat, npc_id, player_id)
    logger.debug("Stealth wipe for player in combat", player_id=str(player_id), combat_id=str(combat.combat_id))


def clear_aggro_for_combat(combat: CombatInstance) -> None:
    """Clear all aggro state for this combat (call on combat end)."""
    combat.npc_hate_lists.clear()
    combat.npc_current_target.clear()
    logger.debug("Aggro cleared for combat", combat_id=str(combat.combat_id))


def _select_top_alive_candidate(
    hate: dict[UUID, float], participants: dict[UUID, CombatParticipant]
) -> tuple[UUID | None, float]:
    """Return (candidate_id, candidate_threat) for alive entity with max threat."""
    candidate_id: UUID | None = None
    candidate_threat: float = 0.0
    for eid, threat in hate.items():
        p = participants.get(eid)
        if p is not None and not p.is_dead() and threat > candidate_threat:
            candidate_id = eid
            candidate_threat = threat
    return candidate_id, candidate_threat


def _should_switch_to_candidate(
    current_target_id: UUID | None,
    candidate_id: UUID,
    candidate_threat: float,
    hate: dict[UUID, float],
    margin: float,
    participants: dict[UUID, CombatParticipant],
) -> bool:
    """Return True if we should switch from current target to candidate."""
    if current_target_id is None:
        return True
    current = participants.get(current_target_id)
    if current is None or current.is_dead():
        return True
    current_threat = hate.get(current_target_id, 0.0)
    threshold = current_threat * (1.0 + margin)
    # Epsilon for float comparison: 100 * 1.1 can be 110.00000000000001
    return candidate_id != current_target_id and candidate_threat >= threshold - 1e-9


def update_aggro(
    combat: CombatInstance,
    npc_participant: CombatParticipant,
    _room_id: str,  # Reserved for future room-scoped logic; kept for API consistency
    participants: dict[UUID, CombatParticipant],
    stability_margin: float | None = None,
) -> tuple[UUID | None, bool]:
    """
    Resolve current target for an NPC from hate list and stability rule.

    - Candidate = alive participant with highest threat in hate list.
    - If no current target: set candidate and return (candidate_id, True).
    - Else: switch only if candidate.threat >= current_target_threat * (1 + stability_margin).
    -     Dead participants are excluded from candidate selection; they remain in hate list.
    Optional future: trim zero-threat entries after 30s to bound hate list size.

    Returns:
        (new_target_participant_id or None, did_switch: bool)
        did_switch True means we just set or changed target; caller should emit switch message.
    """
    npc_id = npc_participant.participant_id
    config = _get_aggro_config()
    margin = stability_margin if stability_margin is not None else getattr(config, "aggro_stability_margin", 0.10)
    hate = get_or_create_hate_list(combat, npc_id)
    current_target_id = combat.npc_current_target.get(npc_id)

    candidate_id, candidate_threat = _select_top_alive_candidate(hate, participants)

    if candidate_id is None:
        combat.npc_current_target.pop(npc_id, None)
        return None, current_target_id is not None

    if current_target_id is None:
        combat.npc_current_target[npc_id] = candidate_id
        return candidate_id, True

    if _should_switch_to_candidate(current_target_id, candidate_id, candidate_threat, hate, margin, participants):
        combat.npc_current_target[npc_id] = candidate_id
        return candidate_id, True

    return current_target_id, False


def get_npc_current_target(combat: CombatInstance, npc_id: UUID) -> UUID | None:
    """Return current target participant_id for this NPC, or None."""
    return combat.npc_current_target.get(npc_id)
