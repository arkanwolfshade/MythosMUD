"""
Heal and steal-life spell effect logic.

Extracted from spell_effects.py to keep the main engine under the line limit.
"""

from __future__ import annotations

import uuid
from typing import cast

from structlog.stdlib import BoundLogger

from server.game.magic.spell_effect_types import (
    NpcIntegrationStringIdPort,
    NpcLifecycleManagerPort,
    NpcSpellDamageTarget,
    SpellEffectPlayer,
    SpellEffectsEngineHealPort,
)
from server.game.magic.spell_effects_internal import coerce_effect_int_times_mastery
from server.models.spell import Spell
from server.schemas.shared import TargetMatch, TargetType
from server.services.combat_service import CombatService
from server.services.combat_service_state import get_combat_service
from server.structured_logging.enhanced_logging_config import get_logger


def _coerce_effect_int(value: object) -> int:
    """Coerce JSON-ish effect values to int (no mastery scaling)."""
    if isinstance(value, bool):
        return 0
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return 0
        try:
            return int(float(stripped))
        except ValueError:
            return 0
    return 0


logger: BoundLogger = get_logger(__name__)


def _add_healing_threat_if_in_combat(
    combat_service: CombatService | None,
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
    dmg_raw = cast(object, data.get("damage_amount"))
    heal_raw = cast(object, data.get("heal_amount", 0))
    return _coerce_effect_int(dmg_raw) > 0 and _coerce_effect_int(heal_raw) > 0


def _get_npc_lifecycle_manager() -> NpcLifecycleManagerPort | None:
    """Get NPC lifecycle manager from instance service; returns None if unavailable."""
    try:
        from server.services.npc_instance_service import get_npc_instance_service

        svc = get_npc_instance_service()
        if not hasattr(svc, "lifecycle_manager") or not svc.lifecycle_manager:
            return None
        return cast(NpcLifecycleManagerPort, cast(object, svc.lifecycle_manager))
    except (AttributeError, ImportError, TypeError, RuntimeError):
        return None


def _lookup_npc_by_id_or_uuid(
    lm: NpcLifecycleManagerPort,
    npc_id: str,
    combat_service: CombatService | None,
) -> object | None:
    """Look up NPC in lifecycle manager by string id or via UUID->string_id mapping."""
    if npc_id in lm.active_npcs:
        return lm.active_npcs[npc_id]
    try:
        parsed = uuid.UUID(npc_id)
    except (ValueError, TypeError):
        return None
    if combat_service is None:
        integration_raw: object | None = None
    else:
        integration_raw = cast(object | None, getattr(combat_service, "_npc_combat_integration_service", None))
    if integration_raw is None or not hasattr(integration_raw, "get_original_string_id"):
        return None
    integration = cast(NpcIntegrationStringIdPort, integration_raw)
    string_id = integration.get_original_string_id(parsed)
    if string_id and string_id in lm.active_npcs:
        return lm.active_npcs[string_id]
    return None


def get_npc_instance_for_steal_life(
    npc_id: str,
    combat_service: CombatService | None,
) -> NpcSpellDamageTarget | None:
    """Get NPC instance by id for steal-life and spell damage; returns None if not found."""
    try:
        lm = _get_npc_lifecycle_manager()
        if not lm:
            return None
        raw = _lookup_npc_by_id_or_uuid(lm, npc_id, combat_service)
        return cast(NpcSpellDamageTarget | None, raw)
    except (AttributeError, ImportError, TypeError, RuntimeError) as exc:
        logger.debug("Could not get NPC instance for steal-life", npc_id=npc_id, error_message=str(exc))
    return None


async def _steal_life_resolve_target_dp(
    engine: SpellEffectsEngineHealPort,
    target: TargetMatch,
    combat_service: CombatService | None,
) -> tuple[int | None, NpcSpellDamageTarget | None, dict[str, object] | None]:
    """Resolve target's current DP for steal-life. Returns (current_dp, npc_instance_or_None, error_result)."""
    if target.target_type == TargetType.PLAYER:
        target_player = await engine.player_service.persistence.get_player_by_id(uuid.UUID(target.target_id))
        if not target_player:
            return (None, None, {"success": False, "message": "Target not found.", "effect_applied": False})
        player = cast(SpellEffectPlayer, target_player)
        stats = player.get_stats()
        current_dp_raw = stats.get("current_dp", 0) if stats else 0
        current_dp = _coerce_effect_int(current_dp_raw)
        return (current_dp, None, None)
    if target.target_type == TargetType.NPC:
        npc_instance = get_npc_instance_for_steal_life(str(target.target_id), combat_service)
        if not npc_instance or not npc_instance.is_alive:
            return (None, None, {"success": False, "message": "Target is not available.", "effect_applied": False})
        combat_stats = npc_instance.get_combat_stats()
        current_dp = int(combat_stats.get("current_dp", 0))
        return (current_dp, npc_instance, None)
    return (
        None,
        None,
        {"success": False, "message": "Heal can only target entities", "effect_applied": False},
    )


async def _steal_life_apply_player_damage(
    engine: SpellEffectsEngineHealPort,
    target: TargetMatch,
    actual_drain: int,
    damage_type: str,
) -> dict[str, object] | None:
    """Apply steal-life damage to a player target. Returns None on success."""
    try:
        _ = await engine.player_service.damage_player(uuid.UUID(target.target_id), actual_drain, damage_type)
        return None
    except OSError as exc:
        logger.error(
            "Error damaging target for steal-life",
            target_id=target.target_id,
            error_message=str(exc),
        )
        return {"success": False, "message": f"Failed to drain life: {str(exc)}", "effect_applied": False}


def _steal_life_apply_npc_damage_only(
    npc_instance: NpcSpellDamageTarget, actual_drain: int, damage_type: str, caster_id: uuid.UUID
) -> dict[str, object] | None:
    """Apply take_damage to NPC. Returns error dict on failure, None on success."""
    ok = npc_instance.take_damage(actual_drain, damage_type, source_id=str(caster_id))
    if not ok:
        return {"success": False, "message": "Failed to drain life from target.", "effect_applied": False}
    return None


def _resolve_npc_id_for_event(npc_instance: NpcSpellDamageTarget, target: TargetMatch) -> uuid.UUID | str:
    """Resolve NPC id for combat events (UUID or string)."""
    try:
        return uuid.UUID(str(target.target_id))
    except (ValueError, TypeError):
        return npc_instance.npc_id


async def _steal_life_publish_npc_events(
    combat_service: CombatService | None,
    room_id: str | None,
    npc_instance: NpcSpellDamageTarget,
    target: TargetMatch,
    actual_drain: int,
    caster_id: uuid.UUID,
) -> None:
    """Publish NPC damage and optional death events after steal-life damage."""
    if not combat_service or not room_id:
        return
    stats_after = npc_instance.get_combat_stats()
    new_dp = int(stats_after.get("current_dp", 0))
    max_dp = int(stats_after.get("max_dp", 0))
    npc_id_ev = _resolve_npc_id_for_event(npc_instance, target)
    _ = await combat_service.publish_npc_damage_event(
        room_id=room_id,
        npc_id=npc_id_ev,
        npc_name=target.target_name,
        damage=actual_drain,
        current_dp=new_dp,
        max_dp=max_dp,
    )
    is_dead = not npc_instance.is_alive
    if not is_dead:
        stats = npc_instance.get_combat_stats()
        is_dead = int(stats.get("current_dp", 1)) <= 0
    if is_dead:
        npc_id_str = str(npc_instance.npc_id)
        _ = await combat_service.publish_npc_died_event(
            room_id=room_id,
            npc_id=npc_id_str,
            npc_name=target.target_name,
            xp_reward=0,
            killer_id=str(caster_id),
        )
        _ = await combat_service.end_combat_if_npc_died(npc_id_str)


async def _steal_life_apply_target_damage(
    engine: SpellEffectsEngineHealPort,
    target: TargetMatch,
    npc_instance: NpcSpellDamageTarget | None,
    actual_drain: int,
    damage_type: str,
    caster_id: uuid.UUID,
    combat_service: CombatService | None,
) -> dict[str, object] | None:
    """Apply steal-life damage to target; publish NPC events if applicable. Returns None on success."""
    if target.target_type == TargetType.PLAYER:
        return await _steal_life_apply_player_damage(engine, target, actual_drain, damage_type)
    if npc_instance is None:
        return {"success": False, "message": "Target is not available.", "effect_applied": False}
    err = _steal_life_apply_npc_damage_only(npc_instance, actual_drain, damage_type, caster_id)
    if err is not None:
        return err
    room_id = npc_instance.current_room
    await _steal_life_publish_npc_events(combat_service, room_id, npc_instance, target, actual_drain, caster_id)
    return None


async def _run_steal_life(
    engine: SpellEffectsEngineHealPort,
    spell: Spell,
    target: TargetMatch,
    caster_id: uuid.UUID,
    mastery_modifier: float,
    heal_amount_raw: int,
    damage_amount_raw: int,
    combat_service: CombatService | None,
) -> dict[str, object]:
    """Drain target's DP (capped at current DP) and heal caster by the same amount."""
    max_drain = int(min(heal_amount_raw, damage_amount_raw) * mastery_modifier)
    damage_type = str(cast(object, spell.effect_data.get("damage_type", "necrotic")))
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
        _ = await engine.player_service.heal_player(caster_id, actual_drain)
    except OSError as exc:
        logger.error("Error healing caster for steal-life", caster_id=caster_id, error_message=str(exc))
        return {"success": False, "message": f"Failed to restore life: {str(exc)}", "effect_applied": False}

    _add_healing_threat_if_in_combat(combat_service, caster_id, actual_drain)
    return {
        "success": True,
        "message": f"Stole {actual_drain} life from {target.target_name}.",
        "effect_applied": True,
        "heal_amount": actual_drain,
        "damage_amount": actual_drain,
    }


async def _run_standard_heal_after_validation(
    engine: SpellEffectsEngineHealPort,
    spell: Spell,
    target: TargetMatch,
    caster_id: uuid.UUID,
    mastery_modifier: float,
    combat_svc: CombatService | None,
) -> dict[str, object]:
    """Non-steal-life heal: apply heal_amount to player or NPC-shaped target."""
    heal_raw = cast(object, spell.effect_data.get("heal_amount", 0))
    heal_amount = coerce_effect_int_times_mastery(heal_raw, mastery_modifier)
    if heal_amount <= 0:
        return {"success": False, "message": "Invalid heal amount", "effect_applied": False}
    if target.target_type == TargetType.PLAYER:
        try:
            _ = await engine.player_service.heal_player(uuid.UUID(target.target_id), heal_amount)
            _add_healing_threat_if_in_combat(combat_svc, caster_id, heal_amount)
            return {
                "success": True,
                "message": f"Healed {target.target_name} for {heal_amount} health",
                "effect_applied": True,
                "heal_amount": heal_amount,
            }
        except OSError as exc:
            logger.error(
                "Error healing player",
                target_id=target.target_id,
                error_message=str(exc),
            )
            return {"success": False, "message": f"Failed to heal: {str(exc)}", "effect_applied": False}
    _add_healing_threat_if_in_combat(combat_svc, caster_id, heal_amount)
    return {
        "success": True,
        "message": f"Healed {target.target_name} for {heal_amount} health",
        "effect_applied": True,
        "heal_amount": heal_amount,
    }


async def run_heal_effect(
    engine: SpellEffectsEngineHealPort,
    spell: Spell,
    target: TargetMatch,
    caster_id: uuid.UUID,
    mastery_modifier: float,
    combat_service: CombatService | None = None,
) -> dict[str, object]:
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
        heal_amt = _coerce_effect_int(cast(object, data.get("heal_amount", 0)))
        dmg_amt = _coerce_effect_int(cast(object, data.get("damage_amount", 0)))
        return await _run_steal_life(
            engine,
            spell,
            target,
            caster_id,
            mastery_modifier,
            heal_amt,
            dmg_amt,
            combat_svc,
        )

    return await _run_standard_heal_after_validation(engine, spell, target, caster_id, mastery_modifier, combat_svc)
