"""
Support helpers for spell effects that would otherwise bloat spell_effects.py.

Contains stat-modify and object-creation helpers, keeping the main engine focused.
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, cast

from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.game.effect_store import SPELL_EFFECT_CATEGORY
from server.game.items.item_factory import ItemFactoryError
from server.game.items.item_giver import ItemGiver
from server.game.magic.spell_effect_types import SpellEffectsEngineEffectPort
from server.game.magic.spell_effects_stats import apply_stat_modifications
from server.game.player_registry import PlayerNotFoundError
from server.models.game import StatusEffectType
from server.models.player_mp import MpChange
from server.models.spell import Spell
from server.schemas.shared import InventorySchemaValidationError, TargetMatch, TargetType
from server.services.inventory_service import InventoryCapacityError
from server.services.player_mp_service import PlayerMpService, announce_mp
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.game.player_registry import PlayerRegistry

logger = get_logger(__name__)

# Effect data's names for magic points; MP has its own write path, PlayerMpService.
_MP_STAT_NAMES = ("mp", "magic_points")


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


async def _add_buff_marker(
    engine: SpellEffectsEngineEffectPort, target_id: uuid.UUID, duration: int, spell: Spell
) -> None:
    """A BUFF marker row for duration online game seconds (ADR-029 step 3b-i).

    Nothing reverts the stat change when it runs out (pre-existing).
    """
    _ = await engine.player_service.persistence.add_player_effect(
        target_id,
        StatusEffectType.BUFF.value,
        SPELL_EFFECT_CATEGORY,
        duration,
        {"intensity": 1, "source": f"spell:{spell.spell_id}"},
    )


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

        player.set_stats(stats)
        await engine.player_service.persistence.save_player(player)
        if duration > 0:
            await _add_buff_marker(cast(SpellEffectsEngineEffectPort, engine), target_id, duration, spell)

        stat_list = ", ".join(modified_stats)
        duration_text = f" for {duration} seconds" if duration > 0 else " permanently"
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


async def _change_target_mp(
    service: PlayerMpService, target_id: uuid.UUID, amount: int, receiver_id: uuid.UUID | None
) -> tuple[MpChange, MpChange | None]:
    """Add ``amount`` to the target's MP; a negative amount goes to ``receiver_id``, if any, in one transaction."""
    if amount >= 0:
        return await service.restore(target_id, amount), None
    if receiver_id is None:
        return await service.spend(target_id, -amount), None
    return await service.drain(target_id, receiver_id, -amount)


async def _apply_mp_modify(
    registry: PlayerRegistry | None,
    spell: Spell,
    target: TargetMatch,
    amount: int,
    caster_id: uuid.UUID | None,
) -> dict[str, object]:
    """Change a player's MP (Power Drain); with ``transfer_to_caster``, what they lost goes to the caster."""
    if registry is None:
        logger.error("No player registry; cannot change MP", spell_id=spell.spell_id)
        return {"success": False, "message": "Failed to modify magic points", "effect_applied": False}
    target_id = uuid.UUID(target.target_id)
    transfers = bool(spell.effect_data.get("transfer_to_caster")) and caster_id != target_id
    try:
        changed, received = await _change_target_mp(
            PlayerMpService(registry), target_id, amount, caster_id if transfers else None
        )
    except PlayerNotFoundError:
        return {"success": False, "message": "Target player not found", "effect_applied": False}
    except (DatabaseError, SQLAlchemyError) as e:
        logger.error("Error modifying MP", target_id=target.target_id, error=str(e))
        return {"success": False, "message": "Failed to modify magic points", "effect_applied": False}

    if not changed.gained:
        return {
            "success": True,
            "message": f"{target.target_name}'s magic points are unchanged.",
            "effect_applied": False,
        }
    await announce_mp(target_id, changed)
    if received is not None and caster_id is not None:
        await announce_mp(caster_id, received)
    drained = changed.gained < 0
    return {
        "success": True,
        "message": (
            f"Drained {-changed.gained} magic points from {target.target_name}"
            if drained
            else f"Restored {changed.gained} magic points to {target.target_name}"
        ),
        "effect_applied": True,
        "stat_changes": {"magic_points": changed.gained},
        "mp_transferred": received.gained if received is not None else 0,
    }


async def process_stat_modify_effect(
    engine: Any,
    spell: Spell,
    target: TargetMatch,
    mastery_modifier: float,
    *,
    caster_id: uuid.UUID | None = None,
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

    # shortcut: an effect that changes MP changes only MP (every seeded one does); split them if a spell ever mixes.
    for name in _MP_STAT_NAMES:
        if name in stat_modifications:
            registry = cast("PlayerRegistry | None", engine.player_registry)
            amount = int(cast(float, stat_modifications[name]) * mastery_modifier)
            return await _apply_mp_modify(registry, spell, target, amount, caster_id)

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
    """Create a real item (ItemFactory) in a player's inventory, committed through the registry (ADR-029)."""
    granter = cast(ItemGiver | None, engine.item_granter)
    if granter is None:
        return {"success": False, "message": "Object creation is not available", "effect_applied": False}
    try:
        await granter.grant(
            uuid.UUID(target.target_id), prototype_id, quantity, origin={"source": "spell_create_object"}
        )
    except PlayerNotFoundError:
        return {"success": False, "message": "Target player not found", "effect_applied": False}
    except InventoryCapacityError:
        return {"success": False, "message": f"{target.target_name}'s inventory is full", "effect_applied": False}
    except (ItemFactoryError, InventorySchemaValidationError, SQLAlchemyError, OSError) as e:
        logger.error("Error creating object in inventory", target_id=target.target_id, error=str(e))
        return {
            "success": False,
            "message": f"Failed to create object: {str(e)}",
            "effect_applied": False,
        }
    return {
        "success": True,
        "message": f"Created {quantity} {prototype_id} in {target.target_name}'s inventory",
        "effect_applied": True,
        "prototype_id": prototype_id,
        "quantity": quantity,
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
