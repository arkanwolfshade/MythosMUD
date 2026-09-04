"""
Flee spell effect: voluntary flee mechanics (success roll, lose-attack-on-fail, end combat + move).

Shared with /flee command via execute_voluntary_flee. Used by SpellEffects when effect_type is FLEE.
"""

import uuid
from typing import Any

from server.schemas.shared import TargetMatch, TargetType
from server.services.combat_flee_handler import execute_voluntary_flee


def _flee_effect_services_available(
    combat_service: Any,
    movement_service: Any,
    get_room_by_id: Any,
) -> bool:
    """True if combat, movement, and get_room_by_id are all configured for flee effect."""
    return bool(combat_service and movement_service and get_room_by_id)


def _flee_effect_validate_room_exits(
    combat: Any,
    get_room_by_id: Any,
) -> tuple[str | None, str | None]:
    """Return (room_id, None) if combat room has exits; else (None, error_message)."""
    room_id = str(combat.room_id)
    room = get_room_by_id(room_id)
    if not room:
        return None, "Target's room could not be determined."
    exits = getattr(room, "exits", None) or {}
    if not exits:
        return None, "There is no escape from this room!"
    return room_id, None


def _flee_effect_invalid_target_type_response() -> dict[str, Any]:
    return {
        "success": False,
        "message": "Flee effect can only target entities (player or NPC).",
        "effect_applied": False,
    }


def _flee_effect_services_unavailable_response() -> dict[str, Any]:
    return {
        "success": False,
        "message": "Flee effect is not available (combat or movement services not configured).",
        "effect_applied": False,
    }


def _flee_effect_invalid_target_response() -> dict[str, Any]:
    return {"success": False, "message": "Invalid target for flee effect.", "effect_applied": False}


def _flee_effect_not_in_combat_response(target: TargetMatch) -> dict[str, Any]:
    return {
        "success": False,
        "message": f"{target.target_name} is not in combat.",
        "effect_applied": False,
    }


def _flee_effect_room_error_response(room_error: str) -> dict[str, Any]:
    return {"success": False, "message": room_error, "effect_applied": False}


def _flee_effect_success_response(target: TargetMatch) -> dict[str, Any]:
    return {
        "success": True,
        "message": f"{target.target_name} flees to safety!",
        "effect_applied": True,
    }


def _flee_effect_failure_response(target: TargetMatch) -> dict[str, Any]:
    return {
        "success": True,
        "message": f"{target.target_name} fails to flee and loses their attack this round!",
        "effect_applied": True,
    }


async def run_flee_effect(
    combat_service: Any,
    movement_service: Any,
    get_room_by_id: Any,
    target: TargetMatch,
) -> dict[str, Any]:
    """
    Apply flee effect: same mechanics as /flee (success roll, lose-attack-on-fail, end combat + move).

    Supports player and NPC targets; NPC flee uses same logic (move_npc future).
    """
    if target.target_type not in (TargetType.PLAYER, TargetType.NPC):
        return _flee_effect_invalid_target_type_response()
    if not _flee_effect_services_available(combat_service, movement_service, get_room_by_id):
        return _flee_effect_services_unavailable_response()
    try:
        fleeing_id = uuid.UUID(target.target_id)
    except (ValueError, TypeError):
        return _flee_effect_invalid_target_response()

    combat = await combat_service.get_combat_by_participant(fleeing_id)
    if not combat:
        return _flee_effect_not_in_combat_response(target)
    _room_id, room_error = _flee_effect_validate_room_exits(combat, get_room_by_id)
    if room_error:
        return _flee_effect_room_error_response(room_error)

    success = await execute_voluntary_flee(
        combat_service,
        get_room_by_id,
        movement_service,
        combat,
        fleeing_id,
    )
    if success:
        return _flee_effect_success_response(target)
    return _flee_effect_failure_response(target)
