"""
Flee command flow: preconditions and execution.

Extracted from combat.py to reduce file nloc (Lizard limit 500).
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING, Protocol, cast

from server.commands.combat_app_protocols import AppWithState
from server.commands.combat_helpers import FleePreconditionError
from server.models.combat import CombatInstance

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

# Structural Protocol stubs use Ellipsis per PEP 544; pylint W2301 flags "unnecessary" ... when a
# docstring is present, so we narrow the suppression to this block only.
# pylint: disable=unnecessary-ellipsis


class _PlayerPositionServiceLike(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Surface used when forcing standing before flee."""

    async def change_position(self, player_name: str, position: str) -> object:
        """Set position; flee ignores the return value."""
        ...


class _FleeCommandHandlerLike(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Handler surface for flee (avoids importing CombatCommandHandler; breaks import cycles)."""

    # Read-only properties: matches CombatCommandHandler (bare protocol attrs type as mutable
    # instance vars and do not unify with @property descriptors).
    @property
    def combat_service(self) -> CombatService | None:
        """Combat service if wired."""
        ...

    @property
    def movement_service(self) -> object | None:
        """Movement service if wired."""
        ...

    @property
    def player_position_service(self) -> object | None:
        """Player position service if wired (duck-typed; see _ensure_flee_standing)."""
        ...

    async def check_and_interrupt_rest(
        self, request_app: AppWithState | None, player_name: str, current_user: Mapping[str, object]
    ) -> dict[str, str] | None:
        """Interrupt rest / block during grace; return message dict or None."""
        ...

    async def get_player_and_room(
        self, request_app: AppWithState | None, current_user: Mapping[str, object]
    ) -> tuple[object, object, dict[str, str] | None]:
        """Load player and room or an error payload."""
        ...

    def get_room_data(self, room_id: str) -> object | None:
        """Room record for exit graph checks."""
        ...


class _PlayerForFlee(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Player attributes used by flee preconditions."""

    player_id: str | uuid.UUID
    current_room_id: str | object | None

    def get_stats(self) -> dict[str, object]:
        """Stats dict (position used for standing check)."""
        ...


# pylint: enable=unnecessary-ellipsis


async def _ensure_flee_standing(
    handler: _FleeCommandHandlerLike, player: _PlayerForFlee, player_name: str
) -> dict[str, str] | None:
    """If not standing, stand and return error message; else return None."""
    stats = player.get_stats() if hasattr(player, "get_stats") else {}
    position_raw = (stats or {}).get("position", "standing")
    position = str(position_raw) if position_raw is not None else "standing"
    if position != "standing":
        if handler.player_position_service:
            pos_svc = cast(_PlayerPositionServiceLike, handler.player_position_service)
            _ = await pos_svc.change_position(player_name, "standing")
        return {"result": "You scrabble to your feet! Try /flee again to escape."}
    return None


def _get_flee_player_uuid(player: _PlayerForFlee) -> tuple[uuid.UUID | None, dict[str, str] | None]:
    """Resolve player_id to UUID; return (uuid, None) or (None, error_dict)."""
    player_id = player.player_id
    if not isinstance(player_id, str):
        return (player_id, None)
    try:
        return (uuid.UUID(player_id), None)
    except (ValueError, TypeError):
        return (None, {"result": "You are not recognized by the cosmic forces."})


def _get_flee_room_id(handler: _FleeCommandHandlerLike, room_id: str) -> tuple[str | None, dict[str, str] | None]:
    """Ensure room exists and has exits; return (room_id, None) or (None, error_dict)."""
    room_data = handler.get_room_data(room_id)
    if not room_data:
        return None, {"result": "You are in an unknown room."}
    raw_exits = getattr(room_data, "exits", None)
    exits: dict[str, str] = {}
    if isinstance(raw_exits, dict):
        typed_exits = cast(dict[object, object], raw_exits)
        exits = {str(k): str(v) for k, v in typed_exits.items()}
    if not exits:
        return None, {"result": "There is no escape!"}
    return room_id, None


async def _validate_flee_combat_and_room(
    handler: _FleeCommandHandlerLike, player_id: uuid.UUID, player: _PlayerForFlee
) -> tuple[CombatInstance | None, str | None, dict[str, str] | None]:
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
    if resolved_room_id is None:
        return None, None, {"result": "Could not resolve room for flee."}
    if not handler.movement_service:
        return None, None, {"result": "Movement is not available."}
    return combat, resolved_room_id, None


async def _resolve_flee_preconditions(
    handler: _FleeCommandHandlerLike,
    request_app: AppWithState | None,
    current_user: Mapping[str, object],
    player_name: str,
) -> tuple[_PlayerForFlee, uuid.UUID, CombatInstance, str]:
    """
    Resolve player, player_id, combat, and room_id for flee.
    Returns (player, player_id, combat, room_id).
    Raises FleePreconditionError with error_result dict on any precondition failure.
    """
    player, _room, player_error = await handler.get_player_and_room(request_app, current_user)
    if player_error:
        raise FleePreconditionError(player_error)
    standing_error = await _ensure_flee_standing(handler, cast(_PlayerForFlee, player), player_name)
    if standing_error:
        raise FleePreconditionError(standing_error)
    player_id, uuid_error = _get_flee_player_uuid(cast(_PlayerForFlee, player))
    if uuid_error:
        raise FleePreconditionError(uuid_error)
    if player_id is None:
        raise FleePreconditionError({"result": "You are not recognized by the cosmic forces."})
    combat, room_id, combat_error = await _validate_flee_combat_and_room(
        handler, player_id, cast(_PlayerForFlee, player)
    )
    if combat_error:
        raise FleePreconditionError(combat_error)
    if room_id is None:
        raise RuntimeError("room_id must be set when _validate_flee_combat_and_room returns no error")
    if combat is None:
        raise RuntimeError("combat must be set when _validate_flee_combat_and_room returns no error")
    return (cast(_PlayerForFlee, player), player_id, combat, room_id)


async def run_handle_flee_command(
    handler: _FleeCommandHandlerLike,
    _command_data: dict[str, object],
    current_user: Mapping[str, object],
    request: object | None,
    alias_storage: object | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /flee command: leave combat and move to random adjacent room.
    Standing check (players must stand first), success roll; on failure you remain in combat
    and lose your attack for this round, on success end combat and move.
    """
    _ = alias_storage
    # Lazy import: avoids import cycle combat_handler -> combat_flee -> combat_flee_handler -> ...
    from server.services.combat_flee_handler import execute_voluntary_flee

    request_app = cast(
        AppWithState | None,
        getattr(request, "app", None) if request is not None else None,
    )
    rest_check_result = await handler.check_and_interrupt_rest(request_app, player_name, current_user)
    if rest_check_result:
        return rest_check_result
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
