"""
Assist command (#833): join the fight a player (or, with no argument, your party leader) is in and hit their foe.

``assist`` is one-shot target resolution, not a standing order. It works out which foe the assisted player is
fighting and then goes through the ordinary attack path, which joins the fight (or refuses it); afterwards the
assister is simply a combatant who stays until the fight ends and does not follow later target switches.
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING, Protocol, cast

from server.commands.combat_app_protocols import AppWithState
from server.commands.combat_attack import execute_attack_on_npc
from server.game.party_service import PartyService
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.models.player import Player
from server.schemas.shared import TargetType
from server.services.combat_service import CombatService
from server.services.npc_combat_integration_service import NPCCombatIntegrationService
from server.services.target_resolution_service import TargetResolutionService

if TYPE_CHECKING:
    from server.alias_storage import AliasStorage


class AssistCommandHandler(Protocol):
    """
    Minimal handler surface for assist (avoids importing CombatCommandHandler: circular import).

    Implementations: CombatCommandHandler; tests may use MagicMock with cast(AssistCommandHandler, mock).
    """

    @property
    def combat_service(self) -> CombatService | None:
        """Return the combat service instance, or None if unavailable."""
        raise NotImplementedError

    @property
    def party_service(self) -> object | None:
        """Return the party service, or None if unavailable."""
        raise NotImplementedError

    #: NPC combat integration (UUID mapping, attack path).
    npc_combat_service: NPCCombatIntegrationService

    #: Same-room player resolution for ``assist <player>``.
    target_resolution_service: TargetResolutionService

    async def check_and_interrupt_rest(
        self, request_app: AppWithState | None, player_name: str, current_user: Mapping[str, object]
    ) -> dict[str, str] | None:
        """Return a blocking error dict (e.g. rest), or None if the player may act."""
        raise NotImplementedError

    async def get_player_and_room(
        self, request_app: AppWithState | None, current_user: Mapping[str, object]
    ) -> tuple[object, object, dict[str, str] | None]:
        """Load player and room from the request context, or return an error dict."""
        raise NotImplementedError

    def room_forbids_combat(self, room_id: object) -> bool:
        """True if the room forbids combat."""
        raise NotImplementedError

    def get_npc_instance(self, npc_id: str) -> object | None:
        """Return a live NPC instance, or None."""
        raise NotImplementedError


#: What the assister is told when the assisted fight is a hallucination only its owner can see (ADR-024).
_PHANTOM_REFUSAL = "You see nothing there to fight."


def _assisted_name_from_command(command_data: Mapping[str, object]) -> str | None:
    """The player name typed after ``assist``, or None for a bare ``assist``."""
    raw = command_data.get("target_player")
    if raw is None:
        raw = command_data.get("target")
    return raw.strip() or None if isinstance(raw, str) else None


async def _resolve_named_player(
    handler: AssistCommandHandler, player_uuid: uuid.UUID, name: str
) -> tuple[uuid.UUID, str] | dict[str, str]:
    """Resolve ``assist <name>`` to a same-room player. Returns (player_id, display_name) or an error dict."""
    result = await handler.target_resolution_service.resolve_target(str(player_uuid), name)
    if not result.success:
        return {"result": result.error_message or "No such player here."}
    match = result.get_single_match()
    if match is None or match.target_type != TargetType.PLAYER:
        return {"result": "You can only assist players."}
    assisted_id = uuid.UUID(str(match.target_id))
    if assisted_id == player_uuid:
        return {"result": "You can't assist yourself."}
    return assisted_id, match.target_name


def _resolve_party_leader(handler: AssistCommandHandler, player_uuid: uuid.UUID) -> uuid.UUID | dict[str, str]:
    """Resolve a bare ``assist`` to the party leader. Returns the leader's id or an error dict."""
    party_service = handler.party_service
    party = party_service.get_party_for_player(player_uuid) if isinstance(party_service, PartyService) else None
    if party is None:
        return {"result": "You are not in a party. Name the player you want to assist."}
    leader_id = uuid.UUID(str(party.leader_id))
    if leader_id == player_uuid:
        return {"result": "You lead your party. Name the player you want to assist."}
    return leader_id


def _foe_of(combat: CombatInstance, assisted_id: uuid.UUID) -> CombatParticipant | None:
    """The foe the assisted player is fighting: their tracked target, else the fight's first living non-player."""
    tracked_id = combat.player_current_target.get(assisted_id)
    tracked = combat.participants.get(tracked_id) if tracked_id is not None else None
    if tracked is not None and not tracked.is_dead():
        return tracked
    return next(
        (
            p
            for p in combat.participants.values()
            if p.participant_type != CombatParticipantType.PLAYER and not p.is_dead()
        ),
        None,
    )


async def _find_assisted_foe(
    combat_service: CombatService, assisted_id: uuid.UUID, assisted_name: str, room_id: str, player_uuid: uuid.UUID
) -> CombatParticipant | dict[str, str]:
    """Find the foe to attack, or the refusal to give. Applies the not-fighting, not-here, phantom and already rules."""
    combat = await combat_service.get_combat_by_participant(assisted_id)
    if combat is None:
        return {"result": f"{assisted_name} isn't fighting anything."}
    if str(combat.room_id) != room_id:
        return {"result": f"{assisted_name} isn't here."}
    foe = _foe_of(combat, assisted_id)
    if foe is None:
        return {"result": f"{assisted_name} isn't fighting anything."}
    if foe.participant_type == CombatParticipantType.PHANTOM:
        return {"result": _PHANTOM_REFUSAL}
    if player_uuid in combat.participants:
        return {"result": f"You are already fighting {foe.name}."}
    return foe


async def _resolve_assisted(
    handler: AssistCommandHandler, player_uuid: uuid.UUID, command_data: Mapping[str, object]
) -> tuple[uuid.UUID, str] | dict[str, str]:
    """Who is being assisted: the named player, or the party leader for a bare ``assist``."""
    name = _assisted_name_from_command(command_data)
    if name is not None:
        return await _resolve_named_player(handler, player_uuid, name)
    leader = _resolve_party_leader(handler, player_uuid)
    if isinstance(leader, dict):
        return leader
    return leader, "Your party leader"


async def _load_assister(
    handler: AssistCommandHandler, request_app: AppWithState | None, current_user: Mapping[str, object]
) -> tuple[uuid.UUID, str, CombatService] | dict[str, str]:
    """Load the assisting player and check they may fight. Returns (player_id, room_id, combat_service) or an error."""
    player, _room, error = await handler.get_player_and_room(request_app, current_user)
    if error:
        return error
    combat_service = handler.combat_service
    if not isinstance(player, Player) or combat_service is None:
        return {"result": "You cannot assist anyone right now."}
    room_id = str(player.current_room_id)
    if not player.is_alive():
        return {"result": "You are incapacitated and cannot attack."}
    if handler.room_forbids_combat(room_id):
        return {"result": "The cosmic forces forbid violence in this place."}
    return uuid.UUID(str(player.player_id)), room_id, combat_service


def _npc_string_id(handler: AssistCommandHandler, foe: CombatParticipant) -> str:
    """The NPC's string id for the attack path; falls back to the participant UUID when none was mapped."""
    mapped = handler.npc_combat_service.get_uuid_mapping().get_original_string_id(foe.participant_id)
    return mapped or str(foe.participant_id)


async def run_handle_assist_command(
    handler: AssistCommandHandler,
    command_data: Mapping[str, object],
    current_user: Mapping[str, object],
    request: object | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle ``assist [player]``: attack the foe the player (or your party leader) is fighting. Room-local."""
    _ = alias_storage
    request_app = cast(AppWithState | None, getattr(request, "app", None) if request is not None else None)
    rest_check = await handler.check_and_interrupt_rest(request_app, player_name, current_user)
    if rest_check:
        return rest_check
    assister = await _load_assister(handler, request_app, current_user)
    if isinstance(assister, dict):
        return assister
    player_uuid, room_id, combat_service = assister

    assisted = await _resolve_assisted(handler, player_uuid, command_data)
    if isinstance(assisted, dict):
        return assisted
    assisted_id, assisted_name = assisted
    foe = await _find_assisted_foe(combat_service, assisted_id, assisted_name, room_id, player_uuid)
    if isinstance(foe, dict):
        return foe

    npc_id = _npc_string_id(handler, foe)
    return await execute_attack_on_npc(
        handler, player_name, npc_id, room_id, npc_instance=handler.get_npc_instance(npc_id)
    )


__all__ = [
    "AssistCommandHandler",
    "run_handle_assist_command",
]
