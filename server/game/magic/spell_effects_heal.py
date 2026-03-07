"""
Heal and steal-life spell effect logic.

Extracted from spell_effects.py to keep the main engine under the line limit.
"""

from __future__ import annotations

import uuid
from typing import Any

from server.models.spell import Spell
from server.schemas.shared import TargetMatch, TargetType
from server.services.combat_service_state import get_combat_service
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _add_healing_threat_if_in_combat(
    combat_service: Any | None,
    caster_id: uuid.UUID,
    heal_amount: int,
) -> None:
    """ADR-016: Add healing threat to all NPCs in the caster's combat, if caster is in combat."""
    if not combat_service or heal_amount <= 0:
        return
    combat_id = combat_service.get_combat_id_for_participant(caster_id)
    if not combat_id:
        return
    combat = combat_service.get_combat(combat_id)
    if not combat:
        return
    from server.models.combat import CombatParticipantType
    from server.services.aggro_threat import add_heal_threat

    for participant_id, participant in combat.participants.items():
        if participant.participant_type == CombatParticipantType.NPC:
            add_heal_threat(combat, participant_id, caster_id, heal_amount, npc_participant=participant)


def _is_heal_other_self_target(spell: Spell, target: TargetMatch, caster_id: uuid.UUID) -> bool:
    """True if spell is heal_other and target is the caster (invalid)."""
    return spell.spell_id == "heal_other" and str(target.target_id) == str(caster_id)


def _is_steal_life_spell(spell: Spell) -> bool:
    """True if effect_data indicates steal-life (both damage and heal amounts)."""
    data = spell.effect_data
    dmg = data.get("damage_amount")
    heal = data.get("heal_amount", 0)
    return dmg is not None and dmg > 0 and heal > 0


def _get_npc_lifecycle_manager() -> Any | None:
    """Get NPC lifecycle manager from instance service; returns None if unavailable."""
    try:
        from server.services.npc_instance_service import get_npc_instance_service

        svc = get_npc_instance_service()
        if not hasattr(svc, "lifecycle_manager") or not svc.lifecycle_manager:
            return None
        return svc.lifecycle_manager
    except (AttributeError, ImportError, TypeError, RuntimeError):
        return None


def _lookup_npc_by_id_or_uuid(lm: Any, npc_id: str, combat_service: Any | None) -> Any | None:
    """Look up NPC in lifecycle manager by string id or via UUID->string_id mapping."""
    if npc_id in lm.active_npcs:
        return lm.active_npcs[npc_id]
    try:
        parsed = uuid.UUID(npc_id)
    except (ValueError, TypeError):
        return None
    integration = getattr(combat_service, "_npc_combat_integration_service", None) if combat_service else None
    if not integration or not hasattr(integration, "get_original_string_id"):
        return None
    string_id = integration.get_original_string_id(parsed)
    if string_id and string_id in lm.active_npcs:
        return lm.active_npcs[string_id]
    return None


def _get_npc_instance_for_steal_life(npc_id: str, combat_service: Any | None) -> Any:
    """Get NPC instance by id for steal-life; returns None if not found."""
    try:
        lm = _get_npc_lifecycle_manager()
        if not lm:
            return None
        return _lookup_npc_by_id_or_uuid(lm, npc_id, combat_service)
    except (AttributeError, ImportError, TypeError, RuntimeError) as e:
        logger.debug("Could not get NPC instance for steal-life", npc_id=npc_id, error=str(e))
    return None


async def _steal_life_resolve_target_dp(
    engine: Any, target: TargetMatch, combat_service: Any | None
) -> tuple[int | None, Any, dict[str, Any] | None]:
    """Resolve target's current DP for steal-life. Returns (current_dp, npc_instance_or_None, error_result)."""
    if target.target_type == TargetType.PLAYER:
        target_player = await engine.player_service.persistence.get_player_by_id(uuid.UUID(target.target_id))
        if not target_player:
            return (None, None, {"success": False, "message": "Target not found.", "effect_applied": False})
        current_dp = (target_player.get_stats() or {}).get("current_dp", 0)
        return (current_dp, None, None)
    if target.target_type == TargetType.NPC:
        npc_instance = _get_npc_instance_for_steal_life(str(target.target_id), combat_service)
        if not npc_instance or not getattr(npc_instance, "is_alive", True):
            return (None, None, {"success": False, "message": "Target is not available.", "effect_applied": False})
        combat_stats: dict[str, Any] = getattr(npc_instance, "get_combat_stats", lambda: {})()
        current_dp = int(combat_stats.get("current_dp", 0))
        return (current_dp, npc_instance, None)
    return (
        None,
        None,
        {"success": False, "message": "Heal can only target entities", "effect_applied": False},
    )


async def _steal_life_apply_player_damage(
    engine: Any, target: TargetMatch, actual_drain: int, damage_type: str
) -> dict[str, Any] | None:
    """Apply steal-life damage to a player target. Returns None on success."""
    try:
        await engine.player_service.damage_player(uuid.UUID(target.target_id), actual_drain, damage_type)
        return None
    except OSError as e:
        logger.error("Error damaging target for steal-life", target_id=target.target_id, error=str(e))
        return {"success": False, "message": f"Failed to drain life: {str(e)}", "effect_applied": False}


def _steal_life_apply_npc_damage_only(
    npc_instance: Any, actual_drain: int, damage_type: str, caster_id: uuid.UUID
) -> dict[str, Any] | None:
    """Apply take_damage to NPC. Returns error dict on failure, None on success."""
    ok = npc_instance.take_damage(actual_drain, damage_type, source_id=str(caster_id))
    if not ok:
        return {"success": False, "message": "Failed to drain life from target.", "effect_applied": False}
    return None


def _resolve_npc_id_for_event(npc_instance: Any, target: TargetMatch) -> uuid.UUID | str:
    """Resolve NPC id for combat events (UUID or string)."""
    try:
        return uuid.UUID(str(target.target_id))
    except (ValueError, TypeError):
        fallback = getattr(npc_instance, "npc_id", None)
        return fallback if fallback is not None else str(target.target_id)


async def _steal_life_publish_npc_events(
    combat_service: Any | None,
    room_id: Any,
    npc_instance: Any,
    target: TargetMatch,
    actual_drain: int,
    caster_id: uuid.UUID,
) -> None:
    """Publish NPC damage and optional death events after steal-life damage."""
    if not combat_service or not room_id:
        return
    stats_after: dict[str, Any] = getattr(npc_instance, "get_combat_stats", lambda: {})()
    new_dp = int(stats_after.get("current_dp", 0))
    max_dp = int(stats_after.get("max_dp", 0))
    npc_id_ev = _resolve_npc_id_for_event(npc_instance, target)
    await combat_service.publish_npc_damage_event(
        room_id=room_id,
        npc_id=npc_id_ev,
        npc_name=target.target_name,
        damage=actual_drain,
        current_dp=new_dp,
        max_dp=max_dp,
    )
    is_dead = not getattr(npc_instance, "is_alive", True)
    if not is_dead:
        stats: dict[str, Any] = getattr(npc_instance, "get_combat_stats", lambda: {})()
        is_dead = int(stats.get("current_dp", 1)) <= 0
    if is_dead:
        npc_id_str = getattr(npc_instance, "npc_id", str(target.target_id))
        await combat_service.publish_npc_died_event(
            room_id=room_id,
            npc_id=npc_id_str,
            npc_name=target.target_name,
            xp_reward=0,
            killer_id=str(caster_id),
        )
        await combat_service.end_combat_if_npc_died(npc_id_str)


async def _steal_life_apply_target_damage(
    engine: Any,
    target: TargetMatch,
    npc_instance: Any,
    actual_drain: int,
    damage_type: str,
    caster_id: uuid.UUID,
    combat_service: Any | None,
) -> dict[str, Any] | None:
    """Apply steal-life damage to target; publish NPC events if applicable. Returns None on success."""
    if target.target_type == TargetType.PLAYER:
        return await _steal_life_apply_player_damage(engine, target, actual_drain, damage_type)
    err = _steal_life_apply_npc_damage_only(npc_instance, actual_drain, damage_type, caster_id)
    if err is not None:
        return err
    room_id = getattr(npc_instance, "current_room", None)
    await _steal_life_publish_npc_events(combat_service, room_id, npc_instance, target, actual_drain, caster_id)
    return None


async def _run_steal_life(
    engine: Any,
    spell: Spell,
    target: TargetMatch,
    caster_id: uuid.UUID,
    mastery_modifier: float,
    heal_amount_raw: int,
    damage_amount_raw: int,
    combat_service: Any | None,
) -> dict[str, Any]:
    """Drain target's DP (capped at current DP) and heal caster by the same amount."""
    max_drain = int(min(heal_amount_raw, damage_amount_raw) * mastery_modifier)
    damage_type = spell.effect_data.get("damage_type", "necrotic")
    if max_drain <= 0:
        return {"success": False, "message": "Invalid steal-life amounts", "effect_applied": False}

    current_dp, npc_instance, err = await _steal_life_resolve_target_dp(engine, target, combat_service)
    if err is not None:
        return err
    if current_dp is None:
        return {"success": False, "message": "Heal can only target entities", "effect_applied": False}

    actual_drain = min(max_drain, max(0, current_dp))
    if actual_drain <= 0:
        return {
            "success": True,
            "message": f"{target.target_name} has no life to steal.",
            "effect_applied": False,
            "heal_amount": 0,
        }

    err = await _steal_life_apply_target_damage(
        engine, target, npc_instance, actual_drain, damage_type, caster_id, combat_service
    )
    if err is not None:
        return err

    try:
        await engine.player_service.heal_player(caster_id, actual_drain)
    except OSError as e:
        logger.error("Error healing caster for steal-life", caster_id=caster_id, error=str(e))
        return {"success": False, "message": f"Failed to restore life: {str(e)}", "effect_applied": False}

    _add_healing_threat_if_in_combat(combat_service, caster_id, actual_drain)
    return {
        "success": True,
        "message": f"Stole {actual_drain} life from {target.target_name}.",
        "effect_applied": True,
        "heal_amount": actual_drain,
        "damage_amount": actual_drain,
    }


async def run_heal_effect(
    engine: Any,
    spell: Spell,
    target: TargetMatch,
    caster_id: uuid.UUID,
    mastery_modifier: float,
    combat_service: Any | None = None,
) -> dict[str, Any]:
    """Process heal effect: normal heals and steal-life (damage target, heal caster)."""
    # Use global combat service when not passed (e.g. so steal-life NPC death messages still publish)
    combat_svc = combat_service if combat_service is not None else get_combat_service()
    if target.target_type not in (TargetType.PLAYER, TargetType.NPC):
        return {"success": False, "message": "Heal can only target entities", "effect_applied": False}
    if _is_heal_other_self_target(spell, target, caster_id):
        return {
            "success": False,
            "message": f"{spell.name} can only target others, not yourself.",
            "effect_applied": False,
        }
    if _is_steal_life_spell(spell):
        data = spell.effect_data
        return await _run_steal_life(
            engine,
            spell,
            target,
            caster_id,
            mastery_modifier,
            int(data.get("heal_amount", 0)),
            int(data.get("damage_amount", 0)),
            combat_svc,
        )

    heal_amount = int(spell.effect_data.get("heal_amount", 0) * mastery_modifier)
    if heal_amount <= 0:
        return {"success": False, "message": "Invalid heal amount", "effect_applied": False}
    if target.target_type == TargetType.PLAYER:
        try:
            await engine.player_service.heal_player(uuid.UUID(target.target_id), heal_amount)
            _add_healing_threat_if_in_combat(combat_svc, caster_id, heal_amount)
            return {
                "success": True,
                "message": f"Healed {target.target_name} for {heal_amount} health",
                "effect_applied": True,
                "heal_amount": heal_amount,
            }
        except OSError as e:
            logger.error("Error healing player", target_id=target.target_id, error=str(e))
            return {"success": False, "message": f"Failed to heal: {str(e)}", "effect_applied": False}
    _add_healing_threat_if_in_combat(combat_svc, caster_id, heal_amount)
    return {
        "success": True,
        "message": f"Healed {target.target_name} for {heal_amount} health",
        "effect_applied": True,
        "heal_amount": heal_amount,
    }
