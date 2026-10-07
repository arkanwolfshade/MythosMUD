"""
Protect command (#991): spend your round covering an ally so NPC blows aimed at them land on you.

``protect <player>`` names a same-room player who is in a fight. It joins that fight if you are not in it yet (the
same join as ``assist`` and ``attack``) and queues a ``protect`` action; the Fighting roll, the cover and the threat
share happen when the round resolves (see ``combat_protect_action``). Like taunt, it replaces whatever else you had
queued, so you do not also auto-attack that round.
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING, cast

from server.commands.combat_app_protocols import AppWithState
from server.commands.combat_assist import (
    AssistCommandHandler,
    assisted_name_from_command,
    find_ally_fight,
    load_assister,
    resolve_named_player,
)
from server.models.combat import CombatInstance, CombatParticipant
from server.services.combat_service import CombatService

if TYPE_CHECKING:
    from server.alias_storage import AliasStorage


async def _join_if_needed(
    handler: AssistCommandHandler,
    combat_service: CombatService,
    combat: CombatInstance,
    foe: CombatParticipant,
    player_uuid: uuid.UUID,
    room_id: str,
) -> dict[str, str] | None:
    """Join the ally's fight unless already in it. Returns a refusal, or None when the player is now in the fight."""
    mine = await combat_service.get_combat_by_participant(player_uuid)
    if mine is not None:
        return None if mine.combat_id == combat.combat_id else {"result": "You are already in another fight."}
    try:
        await handler.npc_combat_service.join_player_to_combat(str(player_uuid), room_id, player_uuid, combat, foe.name)
    except ValueError:
        return {"result": "You cannot join that fight."}
    return None


async def _queue_protect(
    combat_service: CombatService, combat: CombatInstance, player_uuid: uuid.UUID, ally_id: uuid.UUID
) -> dict[str, str] | None:
    """Queue the protect as the player's action for the next round. Returns a refusal, or None when queued."""
    combat.clear_queued_actions(player_uuid, round_number=combat.combat_round + 1)
    queued = await combat_service.queue_combat_action(
        combat_id=combat.combat_id,
        participant_id=player_uuid,
        action_type="protect",
        target_id=ally_id,
    )
    return None if queued else {"result": "You cannot protect right now."}


async def run_handle_protect_command(
    handler: AssistCommandHandler,
    command_data: Mapping[str, object],
    current_user: Mapping[str, object],
    request: object | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle ``protect <player>``: queue a Fighting roll to cover an ally, joining their fight if needed. Room-local."""
    _ = alias_storage
    request_app = cast(AppWithState | None, getattr(request, "app", None) if request is not None else None)
    rest_check = await handler.check_and_interrupt_rest(request_app, player_name, current_user)
    if rest_check:
        return rest_check
    protector = await load_assister(handler, request_app, current_user, verb="protect")
    if isinstance(protector, dict):
        return protector
    player_uuid, room_id, combat_service = protector

    name = assisted_name_from_command(command_data)
    if name is None:
        return {"result": "Protect whom? Name the player you want to cover."}
    ally = await resolve_named_player(handler, player_uuid, name, verb="protect")
    if isinstance(ally, dict):
        return ally
    ally_id, ally_name = ally
    found = await find_ally_fight(combat_service, ally_id, ally_name, room_id)
    if isinstance(found, dict):
        return found
    combat, foe = found

    refusal = await _join_if_needed(handler, combat_service, combat, foe, player_uuid, room_id)
    if refusal is None:
        refusal = await _queue_protect(combat_service, combat, player_uuid, ally_id)
    return refusal or {"result": f"You move to cover {ally_name}."}


__all__ = [
    "run_handle_protect_command",
]
