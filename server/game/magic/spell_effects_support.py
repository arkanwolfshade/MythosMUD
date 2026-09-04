"""
Support helpers for spell effects that would otherwise bloat spell_effects.py.

Contains stat-modify and object-creation helpers, keeping the main engine focused.
"""

from __future__ import annotations

import uuid
from typing import Any

from server.game.magic.spell_effects_stats import apply_stat_modifications
from server.models.game import StatusEffect, StatusEffectType
from server.models.spell import Spell
from server.schemas.shared import TargetMatch, TargetType
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _build_stat_modifications(spell: Spell) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    """
    Build normalized stat_modifications dict from spell.effect_data.

    Supports both full dict form and CoC shorthand {"stat": "...", "delta": N}.
    """
    stat_modifications = spell.effect_data.get("stat_modifications", {})
    if not stat_modifications:
        stat_name = spell.effect_data.get("stat")
        delta = spell.effect_data.get("delta")
        if stat_name and isinstance(delta, int | float):
            stat_modifications = {str(stat_name): delta}
    if not stat_modifications:
        return None, {
            "success": False,
            "message": "No stat modifications specified",
            "effect_applied": False,
        }
    return stat_modifications, None


async def _apply_stat_modify_to_player(
    engine: Any,
    spell: Spell,
    target: TargetMatch,
    mastery_modifier: float,
    stat_modifications: dict[str, Any],
    duration: int,
) -> dict[str, Any]:
    """Apply stat modifications (and optional BUFF status) to a player."""
    try:
        target_id = uuid.UUID(target.target_id)
        player = await engine.player_service.persistence.get_player_by_id(target_id)
        if not player:
            return {"success": False, "message": "Target player not found", "effect_applied": False}

        stats = player.get_stats()
        stats, stat_changes, modified_stats = apply_stat_modifications(
            stats,
            stat_modifications,
            mastery_modifier,
            spell.spell_id,
        )

        if duration > 0:
            status_effects = player.get_status_effects()
            temp_effect = StatusEffect(
                effect_type=StatusEffectType.BUFF,
                duration=duration,
                intensity=1,
                source=f"spell:{spell.spell_id}",
            )
            status_effects.append(temp_effect.model_dump())
            player.set_status_effects(status_effects)

        player.set_stats(stats)
        await engine.player_service.persistence.save_player(player)

        stat_list = ", ".join(modified_stats)
        duration_text = f" for {duration} ticks" if duration > 0 else " permanently"
        return {
            "success": True,
            "message": f"Modified {target.target_name}'s stats{duration_text}: {stat_list}",
            "effect_applied": True,
            "stat_changes": stat_changes,
            "duration": duration,
        }
    except OSError as e:
        logger.error("Error modifying stats", target_id=target.target_id, error=str(e))
        return {
            "success": False,
            "message": f"Failed to modify stats: {str(e)}",
            "effect_applied": False,
        }


async def process_stat_modify_effect(
    engine: Any,
    spell: Spell,
    target: TargetMatch,
    mastery_modifier: float,
) -> dict[str, Any]:
    """
    Process stat modification effect for a player target.

    Delegated from SpellEffects._process_stat_modify to keep spell_effects.py smaller.
    """
    if target.target_type != TargetType.PLAYER:
        return {
            "success": False,
            "message": "Stat modification can only target players",
            "effect_applied": False,
        }

    stat_modifications, error = _build_stat_modifications(spell)
    if error is not None or stat_modifications is None:
        return error or {
            "success": False,
            "message": "Invalid stat modifications configuration",
            "effect_applied": False,
        }

    duration = int(spell.effect_data.get("duration", 0))

    return await _apply_stat_modify_to_player(
        engine,
        spell,
        target,
        mastery_modifier,
        stat_modifications,
        duration,
    )


async def process_create_object_effect(
    engine: Any,
    spell: Spell,
    target: TargetMatch,
    mastery_modifier: float,
) -> dict[str, Any]:
    """Process object creation effect (delegated from SpellEffects)."""
    prototype_id = spell.effect_data.get("prototype_id")
    if not prototype_id:
        return {
            "success": False,
            "message": "No prototype ID specified for object creation",
            "effect_applied": False,
        }

    quantity_raw = int(spell.effect_data.get("quantity", 1) * mastery_modifier)
    quantity = max(1, quantity_raw)

    if target.target_type == TargetType.PLAYER:
        return await _create_object_for_player(engine, target, prototype_id, quantity)

    if target.target_type == TargetType.ROOM:
        return _create_object_for_room(spell, target)

    return {
        "success": False,
        "message": f"Object creation cannot target {target.target_type.value}",
        "effect_applied": False,
    }


async def _create_object_for_player(
    engine: Any,
    target: TargetMatch,
    prototype_id: str,
    quantity: int,
) -> dict[str, Any]:
    """Create objects in a player's inventory."""
    try:
        target_id = uuid.UUID(target.target_id)
        player = await engine.player_service.persistence.get_player_by_id(target_id)
        if not player:
            return {"success": False, "message": "Target player not found", "effect_applied": False}

        inventory = player.get_inventory()
        new_item = {
            "item_id": prototype_id,
            "prototype_id": prototype_id,
            "quantity": quantity,
            "item_name": prototype_id,  # Would be resolved from prototype registry
        }
        inventory.append(new_item)
        player.set_inventory(inventory)
        await engine.player_service.persistence.save_player(player)

        return {
            "success": True,
            "message": f"Created {quantity} {prototype_id} in {target.target_name}'s inventory",
            "effect_applied": True,
            "prototype_id": prototype_id,
            "quantity": quantity,
        }
    except OSError as e:
        logger.error("Error creating object in inventory", target_id=target.target_id, error=str(e))
        return {
            "success": False,
            "message": f"Failed to create object: {str(e)}",
            "effect_applied": False,
        }


def _create_object_for_room(spell: Spell, target: TargetMatch) -> dict[str, Any]:
    """
    Handle object creation targeting a room.

    Currently a placeholder until ItemFactory and room_manager are wired.
    """
    logger.warning(
        "Room item creation requires ItemFactory and room_manager",
        spell_id=spell.spell_id,
        room_id=target.room_id,
    )
    return {
        "success": False,
        "message": "Room item creation requires additional services (ItemFactory, room_manager)",
        "effect_applied": False,
    }
