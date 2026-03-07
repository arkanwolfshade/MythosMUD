"""
Taunt command flow: validation and execution.

Extracted from combat.py to reduce file nloc (Lizard limit 500).
"""

import uuid
from typing import Any, cast

from server.models.combat import CombatParticipantType
from server.schemas.shared import TargetType
from server.services.aggro_threat import apply_taunt, update_aggro
from server.services.combat_service_npc import find_participant_uuid_by_string_id


def _resolve_taunt_room_and_player(player: Any, room: Any) -> dict[str, str] | tuple[str, uuid.UUID]:
    """Resolve room_id and player_id. Returns error dict or (room_id, player_id)."""
    room_id = str(room.room_id) if hasattr(room, "room_id") else str(getattr(room, "id", ""))
    if not room_id:
        return {"result": "You are not in a room."}
    player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id
    return (room_id, player_id)


def _validate_taunt_target(handler: Any, target_match: Any) -> dict[str, str] | None:
    """Validate target is NPC and alive. Returns error dict or None."""
    if target_match.target_type != TargetType.NPC:
        return {"result": f"You can only taunt NPCs, not {target_match.target_type}s."}
    npc_instance = handler.get_npc_instance(target_match.target_id)
    if not npc_instance or not npc_instance.is_alive:
        return {"result": "That creature is not here or is dead."}
    return None


async def _resolve_taunt_combat_and_participant(
    handler: Any, player_id: uuid.UUID, room_id: str, target_match: Any
) -> dict[str, str] | tuple[Any, Any]:
    """Resolve combat and NPC participant. Returns error dict or (combat, npc_participant)."""
    if not handler.combat_service:
        return {"result": "Combat is not available."}
    combat = await handler.combat_service.get_combat_by_participant(player_id)
    if not combat:
        return {"result": "You must be in combat to taunt."}
    if str(combat.room_id) != room_id:
        return {"result": "You must be in the same room as the combat to taunt."}
    npc_participant_id = find_participant_uuid_by_string_id(handler.combat_service, combat, target_match.target_id)
    if npc_participant_id is None:
        return {"result": "That creature is not in this combat."}
    npc_participant = combat.participants.get(npc_participant_id)
    if not npc_participant or npc_participant.participant_type != CombatParticipantType.NPC:
        return {"result": "That creature is not in this combat."}
    return (combat, npc_participant)


async def _validate_taunt_context(
    handler: Any,
    request_app: Any,
    current_user: dict[str, Any],
    target_name: str,
) -> dict[str, str] | tuple[uuid.UUID, Any, Any, str]:
    """
    Validate taunt preconditions and resolve combat/NPC.
    Returns error dict or (player_id, combat, npc_participant, room_id).
    """
    player, room, err = await handler.get_player_and_room(request_app, current_user)
    if err:
        return cast(dict[str, str], err)
    room_result = _resolve_taunt_room_and_player(player, room)
    if isinstance(room_result, dict):
        return room_result
    room_id, player_id = room_result
    target_match, match_err = await handler.resolve_combat_target(player, target_name)
    if match_err:
        return cast(dict[str, str], match_err)
    target_err = _validate_taunt_target(handler, target_match)
    if target_err:
        return target_err
    combat_result = await _resolve_taunt_combat_and_participant(handler, player_id, room_id, target_match)
    if isinstance(combat_result, dict):
        return combat_result
    combat, npc_participant = combat_result
    return (player_id, combat, npc_participant, room_id)


def _validate_taunt_target_name(handler: Any, command_data: dict[str, Any]) -> dict[str, str] | str:
    """Validate and resolve target name from command_data. Returns error dict or target_name."""
    target_name = command_data.get("target_player") or command_data.get("target")
    err = handler.validate_target_name(target_name)
    if err:
        return cast(dict[str, str], err)
    if not target_name or not isinstance(target_name, str):
        return {"result": "You must focus your wrath upon a specific target."}
    return cast(str, target_name)


async def _apply_taunt_and_maybe_broadcast(
    handler: Any,
    combat: Any,
    npc_participant: Any,
    player_id: uuid.UUID,
    room_id: str,
) -> dict[str, str] | None:
    """Apply taunt and broadcast target switch if aggro changed. Returns error dict or None on success."""
    applied = apply_taunt(
        combat,
        npc_participant.participant_id,
        player_id,
        combat.room_id,
        room_id,
    )
    if not applied:
        return {"result": "You must be in the same room as the creature to taunt it."}
    new_target_id, did_switch = update_aggro(combat, npc_participant, combat.room_id, combat.participants)
    if did_switch and new_target_id and hasattr(handler.npc_combat_service, "_messaging_integration"):
        new_target = combat.participants.get(new_target_id)
        new_target_name = new_target.name if new_target else "someone"
        mi = getattr(handler.npc_combat_service, "_messaging_integration", None)
        if mi:
            await mi.broadcast_combat_target_switch(
                combat.room_id, str(combat.combat_id), npc_participant.name, new_target_name
            )
    return None


async def run_handle_taunt_command(
    handler: Any,
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: Any,
    player_name: str,
) -> dict[str, str]:
    """Handle taunt command: draw NPC aggro (ADR-016). Room-local only."""
    _ = alias_storage
    request_app = getattr(request, "app", None)
    rest_check = await handler.check_and_interrupt_rest(request_app, player_name, current_user)
    if rest_check:
        return cast(dict[str, str], rest_check)
    target_result = _validate_taunt_target_name(handler, command_data)
    if isinstance(target_result, dict):
        return target_result
    context = await _validate_taunt_context(handler, request_app, current_user, target_result)
    if isinstance(context, dict):
        return context
    player_id, combat, npc_participant, room_id = context
    apply_err = await _apply_taunt_and_maybe_broadcast(handler, combat, npc_participant, player_id, room_id)
    if apply_err:
        return apply_err
    return {"result": f"You taunt {npc_participant.name}, drawing its attention!"}
