"""
Status effect spell logic (apply/remove status, force-flee, grace-period checks).

Extracted from spell_effects.py to keep the main engine under the line limit.
"""

from __future__ import annotations

import uuid
from typing import Any

from server.game.magic.spell_effect_flee import run_flee_effect
from server.models.game import StatusEffect, StatusEffectType
from server.models.spell import Spell
from server.realtime.login_grace_period import is_player_in_login_grace_period
from server.schemas.shared import TargetMatch, TargetType
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _grace_period_blocks_negative_status_effect(
    engine: Any, target_id: uuid.UUID, effect_type: StatusEffectType
) -> bool:
    """True if target is in login grace period and effect is negative (should block)."""
    negative_effect_types = {
        StatusEffectType.STUNNED,
        StatusEffectType.POISONED,
        StatusEffectType.HALLUCINATING,
        StatusEffectType.PARANOID,
        StatusEffectType.TREMBLING,
        StatusEffectType.CORRUPTED,
        StatusEffectType.DELIRIOUS,
        StatusEffectType.DOMINATED,
        StatusEffectType.CLOUD_MEMORY,
        StatusEffectType.FEAR,
        StatusEffectType.EVIL_EYE,
        StatusEffectType.BLINDED,
    }
    if effect_type not in negative_effect_types:
        return False
    if not engine.connection_manager:
        return False
    try:
        return is_player_in_login_grace_period(target_id, engine.connection_manager)
    except (AttributeError, ImportError, TypeError, ValueError):
        return False


async def _apply_status_effect_to_player(
    engine: Any,
    target_id: uuid.UUID,
    effect_type: StatusEffectType,
    duration: int,
    intensity: int,
    spell: Spell,
    target: TargetMatch,
) -> dict[str, Any]:
    """Load player, append status effect, save; return result dict or error if player not found."""
    player = await engine.player_service.persistence.get_player_by_id(target_id)
    if not player:
        return {"success": False, "message": "Target player not found", "effect_applied": False}
    status_effects = player.get_status_effects()
    new_effect = StatusEffect(
        effect_type=effect_type,
        duration=duration,
        intensity=intensity,
        source=f"spell:{spell.spell_id}",
    )
    status_effects.append(new_effect.model_dump())
    player.set_status_effects(status_effects)
    await engine.player_service.persistence.save_player(player)
    return {
        "success": True,
        "message": f"Applied {effect_type.value} to {target.target_name}",
        "effect_applied": True,
        "status_effect": effect_type.value,
    }


async def _maybe_run_force_flee_effect(engine: Any, spell: Spell, target: TargetMatch) -> dict[str, Any] | None:
    """Run flee effect when effect_data.force_flee is set; otherwise return None."""
    if not spell.effect_data.get("force_flee"):
        return None
    if not (engine.combat_service and engine.movement_service and engine.get_room_by_id):
        return {
            "success": False,
            "message": "Flee effect is not available (combat or movement services not configured).",
            "effect_applied": False,
        }
    return await run_flee_effect(
        engine.combat_service,
        engine.movement_service,
        engine.get_room_by_id,
        target,
    )


def _parse_status_effect_metadata(
    spell: Spell,
    mastery_modifier: float,
) -> tuple[StatusEffectType | None, int, int, bool, dict[str, Any] | None]:
    """Parse effect_data for status-effect type, duration, intensity, remove flag. Returns (type, duration, intensity, remove, error)."""
    effect_type_str = spell.effect_data.get("status_effect_type") or spell.effect_data.get("status_effect", "")
    raw_duration = spell.effect_data.get("duration", spell.effect_data.get("duration_seconds", 0))
    duration = int(raw_duration * mastery_modifier)
    intensity = min(10, max(1, int(spell.effect_data.get("intensity", 1) * mastery_modifier)))
    remove_effect = bool(spell.effect_data.get("remove"))
    try:
        effect_type = StatusEffectType(effect_type_str)
    except ValueError:
        return (
            None,
            duration,
            intensity,
            remove_effect,
            {
                "success": False,
                "message": f"Invalid status effect type: {effect_type_str}",
                "effect_applied": False,
            },
        )
    return (effect_type, duration, intensity, remove_effect, None)


async def _remove_player_status_effect(
    engine: Any,
    target_id: uuid.UUID,
    target: TargetMatch,
    effect_type: StatusEffectType,
) -> dict[str, Any]:
    """Remove a matching status effect from a player."""
    player = await engine.player_service.persistence.get_player_by_id(target_id)
    if not player:
        return {"success": False, "message": "Target player not found", "effect_applied": False}
    status_effects = player.get_status_effects()
    filtered_effects = [se for se in status_effects if se.get("effect_type") != effect_type.value]
    player.set_status_effects(filtered_effects)
    await engine.player_service.persistence.save_player(player)
    return {
        "success": True,
        "message": f"Removed {effect_type.value} from {target.target_name}",
        "effect_applied": True,
        "status_effect_removed": effect_type.value,
    }


async def _apply_player_status_with_grace_check(
    engine: Any,
    spell: Spell,
    target: TargetMatch,
    effect_type: StatusEffectType,
    duration: int,
    intensity: int,
    target_id: uuid.UUID,
) -> dict[str, Any]:
    """Apply a status effect, respecting login grace-period protection."""
    if _grace_period_blocks_negative_status_effect(engine, target_id, effect_type):
        logger.info(
            "Negative status effect blocked - target in login grace period",
            target_id=target.target_id,
            effect_type=effect_type.value,
        )
        return {
            "success": False,
            "message": f"Target is protected and immune to {effect_type.value}",
            "effect_applied": False,
        }
    return await _apply_status_effect_to_player(engine, target_id, effect_type, duration, intensity, spell, target)


async def _handle_player_status_effect(
    engine: Any,
    spell: Spell,
    target: TargetMatch,
    effect_type: StatusEffectType,
    duration: int,
    intensity: int,
    remove_effect: bool,
) -> dict[str, Any]:
    """Apply or remove a status effect on a player, respecting grace-period rules."""
    try:
        target_id = uuid.UUID(target.target_id)
        if remove_effect:
            return await _remove_player_status_effect(engine, target_id, target, effect_type)
        return await _apply_player_status_with_grace_check(
            engine, spell, target, effect_type, duration, intensity, target_id
        )
    except (OSError, ValueError) as e:
        logger.error("Error applying status effect", target_id=target.target_id, error=str(e))
        return {
            "success": False,
            "message": f"Failed to apply status effect: {str(e)}",
            "effect_applied": False,
        }


async def run_status_effect(
    engine: Any,
    spell: Spell,
    target: TargetMatch,
    mastery_modifier: float,
) -> dict[str, Any]:
    """Process status effect: apply/remove on player, or apply to NPC (no persistence)."""
    if target.target_type not in (TargetType.PLAYER, TargetType.NPC):
        return {"success": False, "message": "Status effects can only target entities", "effect_applied": False}

    flee_result = await _maybe_run_force_flee_effect(engine, spell, target)
    if flee_result is not None:
        return flee_result

    effect_type, duration, intensity, remove_effect, error = _parse_status_effect_metadata(spell, mastery_modifier)
    if error is not None or effect_type is None:
        return error or {
            "success": False,
            "message": "Invalid status effect configuration",
            "effect_applied": False,
        }

    if target.target_type == TargetType.PLAYER:
        return await _handle_player_status_effect(
            engine, spell, target, effect_type, duration, intensity, remove_effect
        )

    return {
        "success": True,
        "message": f"Applied {effect_type.value} to {target.target_name}",
        "effect_applied": True,
    }
