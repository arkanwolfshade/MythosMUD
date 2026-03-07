"""
Flee command flow: preconditions and execution.

Extracted from combat.py to reduce file nloc (Lizard limit 500).
"""

import uuid
from typing import Any, cast

from server.commands.combat_helpers import FleePreconditionError
from server.services.combat_flee_handler import execute_voluntary_flee


async def _ensure_flee_standing(handler: Any, player: Any, player_name: str) -> dict[str, str] | None:
    """If not standing, stand and return error message; else return None."""
    stats = player.get_stats() if hasattr(player, "get_stats") else {}
    position = (stats or {}).get("position", "standing")
    if position != "standing":
        if handler.player_position_service:
            await handler.player_position_service.change_position(player_name, "standing")
        return {"result": "You scrabble to your feet! Try /flee again to escape."}
    return None


def _get_flee_player_uuid(player: Any) -> tuple[uuid.UUID | None, dict[str, str] | None]:
    """Resolve player_id to UUID; return (uuid, None) or (None, error_dict)."""
    player_id = player.player_id
    if not isinstance(player_id, str):
        return (player_id, None)
    try:
        return (uuid.UUID(player_id), None)
    except (ValueError, TypeError):
        return (None, {"result": "You are not recognized by the cosmic forces."})


def _get_flee_room_id(handler: Any, room_id: str) -> tuple[str | None, dict[str, str] | None]:
    """Ensure room exists and has exits; return (room_id, None) or (None, error_dict)."""
    room_data = handler.get_room_data(room_id)
    if not room_data:
        return None, {"result": "You are in an unknown room."}
    exits = getattr(room_data, "exits", None) or {}
    if not exits:
        return None, {"result": "There is no escape!"}
    return room_id, None


async def _validate_flee_combat_and_room(
    handler: Any, player_id: uuid.UUID, player: Any
) -> tuple[Any, str | None, dict[str, str] | None]:
    """
    Resolve combat, room, exits, and movement service for flee.
    Returns (combat, room_id, None) or (None, None, error_dict).
    """
    if not handler.combat_service:
        return None, None, {"result": "Combat is not available."}
    combat = await handler.combat_service.get_combat_by_participant(player_id)
    if not combat:
        return None, None, {"result": "You are not in combat."}
    room_id_raw = player.current_room_id or combat.room_id
    if not room_id_raw:
        return None, None, {"result": "You are not in a room."}
    room_id = str(room_id_raw)
    resolved_room_id, room_err = _get_flee_room_id(handler, room_id)
    if room_err:
        return None, None, room_err
    assert resolved_room_id is not None
    if not handler.movement_service:
        return None, None, {"result": "Movement is not available."}
    return combat, resolved_room_id, None


async def _resolve_flee_preconditions(
    handler: Any,
    request_app: Any,
    current_user: dict[str, Any],
    player_name: str,
) -> tuple[Any, uuid.UUID, Any, str]:
    """
    Resolve player, player_id, combat, and room_id for flee.
    Returns (player, player_id, combat, room_id).
    Raises FleePreconditionError with error_result dict on any precondition failure.
    """
    player, _room, player_error = await handler.get_player_and_room(request_app, current_user)
    if player_error:
        raise FleePreconditionError(player_error)
    standing_error = await _ensure_flee_standing(handler, player, player_name)
    if standing_error:
        raise FleePreconditionError(standing_error)
    player_id, uuid_error = _get_flee_player_uuid(player)
    if uuid_error:
        raise FleePreconditionError(uuid_error)
    if player_id is None:
        raise FleePreconditionError({"result": "You are not recognized by the cosmic forces."})
    combat, room_id, combat_error = await _validate_flee_combat_and_room(handler, player_id, player)
    if combat_error:
        raise FleePreconditionError(combat_error)
    if room_id is None:
        raise RuntimeError("room_id must be set when _validate_flee_combat_and_room returns no error")
    return (player, player_id, combat, room_id)


async def run_handle_flee_command(
    handler: Any,
    _command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: Any,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /flee command: leave combat and move to random adjacent room.
    Standing check (players must stand first), success roll; on failure you remain in combat
    and lose your attack for this round, on success end combat and move.
    """
    _ = alias_storage
    request_app = request.app if request else None
    rest_check_result = await handler.check_and_interrupt_rest(request_app, player_name, current_user)
    if rest_check_result:
        return cast(dict[str, str], rest_check_result)
    try:
        _, player_id, combat, _ = await _resolve_flee_preconditions(handler, request_app, current_user, player_name)
    except FleePreconditionError as e:
        return e.error_result
    success = await execute_voluntary_flee(
        handler.combat_service,
        handler.get_room_data,
        handler.movement_service,
        combat,
        player_id,
    )
    if not success:
        return {"result": "You try to flee but fail, losing your attack for this round."}
    return {"result": "You flee to safety!"}
