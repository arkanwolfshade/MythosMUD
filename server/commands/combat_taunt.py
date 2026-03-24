"""
Taunt command flow: validation and execution.

Extracted from combat.py to reduce file nloc (Lizard limit 500).
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING, Protocol, cast

from server.commands.combat_app_protocols import AppWithState
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.schemas.shared import TargetType
from server.schemas.shared.target_resolution import TargetMatch
from server.services.aggro_threat import apply_taunt, update_aggro
from server.services.combat_service import CombatService
from server.services.combat_service_npc import find_participant_uuid_by_string_id
from server.services.npc_combat_integration_service import NPCCombatIntegrationService

if TYPE_CHECKING:
    from server.alias_storage import AliasStorage


class TauntCommandHandler(Protocol):
    """
    Minimal handler surface for taunt (avoids importing CombatCommandHandler: circular import).

    Implementations: CombatCommandHandler; tests may use MagicMock with cast(TauntCommandHandler, mock).
    """

    @property
    def combat_service(self) -> CombatService | None:
        """Return the combat service instance, or None if unavailable."""
        raise NotImplementedError

    #: NPC combat integration (messaging, broadcasts).
    npc_combat_service: NPCCombatIntegrationService

    def validate_target_name(self, target_name: str | None) -> dict[str, str] | None:
        """Return an error dict if the target name is missing or invalid."""
        raise NotImplementedError

    async def get_player_and_room(
        self, request_app: AppWithState | None, current_user: Mapping[str, object]
    ) -> tuple[object, object, dict[str, str] | None]:
        """Load player and room from the request context, or return an error dict."""
        raise NotImplementedError

    async def resolve_combat_target(
        self, player: object, target_name: str
    ) -> tuple[TargetMatch | None, dict[str, str] | None]:
        """Resolve a typed target match for the given name in the current context."""
        raise NotImplementedError

    def get_npc_instance(self, npc_id: str) -> object | None:
        """Return a live NPC instance for validation, or None."""
        raise NotImplementedError

    async def check_and_interrupt_rest(
        self, request_app: AppWithState | None, player_name: str, current_user: Mapping[str, object]
    ) -> dict[str, str] | None:
        """Return a blocking error dict (e.g. rest), or None if the player may act."""
        raise NotImplementedError


def _resolve_taunt_room_and_player(player: object, room: object) -> dict[str, str] | tuple[str, uuid.UUID]:
    """Resolve room_id and player_id. Returns error dict or (room_id, player_id)."""
    room_id = str(getattr(room, "room_id", "")) if hasattr(room, "room_id") else str(getattr(room, "id", ""))
    if not room_id:
        return {"result": "You are not in a room."}
    pid_raw = getattr(player, "player_id", None)
    if pid_raw is None:
        return {"result": "You are not in a room."}
    if isinstance(pid_raw, str):
        player_id = uuid.UUID(pid_raw)
    elif isinstance(pid_raw, uuid.UUID):
        player_id = pid_raw
    else:
        return {"result": "You are not in a room."}
    return (room_id, player_id)


def _validate_taunt_target(handler: TauntCommandHandler, target_match: TargetMatch) -> dict[str, str] | None:
    """Validate target is NPC and alive. Returns error dict or None."""
    if target_match.target_type != TargetType.NPC:
        return {"result": f"You can only taunt NPCs, not {target_match.target_type}s."}
    npc_instance = handler.get_npc_instance(target_match.target_id)
    if npc_instance is None or not bool(getattr(npc_instance, "is_alive", False)):
        return {"result": "That creature is not here or is dead."}
    return None


async def _resolve_taunt_combat_and_participant(
    handler: TauntCommandHandler, player_id: uuid.UUID, room_id: str, target_match: TargetMatch
) -> dict[str, str] | tuple[CombatInstance, CombatParticipant]:
    """Resolve combat and NPC participant. Returns error dict or (combat, npc_participant)."""
    combat_svc = handler.combat_service
    if not combat_svc:
        return {"result": "Combat is not available."}
    combat = await combat_svc.get_combat_by_participant(player_id)
    if not combat:
        return {"result": "You must be in combat to taunt."}
    if str(combat.room_id) != room_id:
        return {"result": "You must be in the same room as the combat to taunt."}
    npc_participant_id = find_participant_uuid_by_string_id(combat_svc, combat, target_match.target_id)
    if npc_participant_id is None:
        return {"result": "That creature is not in this combat."}
    npc_participant = combat.participants.get(npc_participant_id)
    if not npc_participant or npc_participant.participant_type != CombatParticipantType.NPC:
        return {"result": "That creature is not in this combat."}
    return (combat, npc_participant)


async def _validate_taunt_context(
    handler: TauntCommandHandler,
    request_app: AppWithState | None,
    current_user: Mapping[str, object],
    target_name: str,
) -> dict[str, str] | tuple[uuid.UUID, CombatInstance, CombatParticipant, str]:
    """
    Validate taunt preconditions and resolve combat/NPC.
    Returns error dict or (player_id, combat, npc_participant, room_id).
    """
    player, room, err = await handler.get_player_and_room(request_app, current_user)
    if err:
        return err
    room_result = _resolve_taunt_room_and_player(player, room)
    if isinstance(room_result, dict):
        return room_result
    resolved_room_id, player_id = room_result
    target_match, match_err = await handler.resolve_combat_target(player, target_name)
    if match_err:
        return match_err
    if target_match is None:
        return {"result": "You must focus your wrath upon a specific target."}
    target_err = _validate_taunt_target(handler, target_match)
    if target_err:
        return target_err
    combat_result = await _resolve_taunt_combat_and_participant(handler, player_id, resolved_room_id, target_match)
    if isinstance(combat_result, dict):
        return combat_result
    combat, npc_participant = combat_result
    return (player_id, combat, npc_participant, resolved_room_id)


def _validate_taunt_target_name(
    handler: TauntCommandHandler, command_data: Mapping[str, object]
) -> dict[str, str] | str:
    """Validate and resolve target name from command_data. Returns error dict or target_name."""
    target_raw = command_data.get("target_player")
    if target_raw is None:
        target_raw = command_data.get("target")
    err = handler.validate_target_name(target_raw if isinstance(target_raw, str) else None)
    if err:
        return err
    if not target_raw or not isinstance(target_raw, str):
        return {"result": "You must focus your wrath upon a specific target."}
    return target_raw


async def _apply_taunt_and_maybe_broadcast(
    handler: TauntCommandHandler,
    combat: CombatInstance,
    npc_participant: CombatParticipant,
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
    if did_switch and new_target_id and handler.npc_combat_service:
        new_target = combat.participants.get(new_target_id)
        new_target_name = new_target.name if new_target else "someone"
        mi = handler.npc_combat_service.get_messaging_integration()
        _ = await mi.broadcast_combat_target_switch(
            combat.room_id, str(combat.combat_id), npc_participant.name, new_target_name
        )
    return None


async def run_handle_taunt_command(
    handler: TauntCommandHandler,
    command_data: Mapping[str, object],
    current_user: Mapping[str, object],
    request: object | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle taunt command: draw NPC aggro (ADR-016). Room-local only."""
    _ = alias_storage
    request_app = cast(AppWithState | None, getattr(request, "app", None) if request is not None else None)
    rest_check = await handler.check_and_interrupt_rest(request_app, player_name, current_user)
    if rest_check:
        return rest_check
    target_result = _validate_taunt_target_name(handler, command_data)
    if isinstance(target_result, dict):
        return target_result
    context = await _validate_taunt_context(handler, request_app, current_user, target_result)
    if isinstance(context, dict):
        return context
    player_id, combat, npc_participant, ctx_room_id = context
    apply_err = await _apply_taunt_and_maybe_broadcast(handler, combat, npc_participant, player_id, ctx_room_id)
    if apply_err:
        return apply_err
    return {"result": f"You taunt {npc_participant.name}, drawing its attention!"}


__all__ = [
    "TauntCommandHandler",
    "run_handle_taunt_command",
]
