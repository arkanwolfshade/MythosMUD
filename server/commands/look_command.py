"""
Look command for MythosMUD.

This module handles the look command for examining surroundings.
This is the main entry point that routes to specialized handlers.
"""

# pylint: disable=too-many-arguments,missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: Look params; Protocol stubs (PEP 544)

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, NamedTuple, Protocol, cast

from fastapi import FastAPI

from ..alias_storage import AliasStorage
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from ..utils.room_renderer import clone_room_drops
from .inventory_command_contracts import CommandResponse
from .look_container import ContainerLookArgs, _handle_container_look, _try_lookup_container_implicit
from .look_helpers import LookRequest, _is_direction
from .look_item import _handle_item_look, _try_lookup_item_implicit
from .look_npc import _try_lookup_npc_implicit
from .look_player import _handle_player_look, _try_lookup_player_implicit
from .look_room import _handle_direction_look, _handle_room_look, _try_lookup_phantom_implicit

if TYPE_CHECKING:
    from ..models.player import Player

logger = get_logger(__name__)


class _LookRoom(Protocol):
    id: object


class _LookPersistence(Protocol):
    async def get_player_by_name(self, name: str) -> Player | None: ...

    def get_room_by_id(self, room_id: str) -> _LookRoom | None: ...


class _LookRoomManager(Protocol):
    def list_room_drops(self, room_id: str) -> list[dict[str, object]]: ...


class _LookConnectionManager(Protocol):
    room_manager: _LookRoomManager | None


class _LookContainer(Protocol):
    async_persistence: _LookPersistence | None
    connection_manager: _LookConnectionManager | None
    item_prototype_registry: object | None


class LookRouteCtx(NamedTuple):
    """Shared look-command context so handlers stay under the param-count gate."""

    command_data: Mapping[str, object]
    target: str | None
    target_type: str | None
    direction: str | None
    instance_number: int | None
    room: _LookRoom
    player: Player
    persistence: _LookPersistence
    room_drops: list[dict[str, object]]
    app: FastAPI | None
    request: LookRequest | None
    player_name: str


def _opt_str(value: object) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        return value
    return str(value)


def _opt_int(value: object) -> int | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    return None


def _as_response(raw: object) -> CommandResponse | None:
    if raw is None:
        return None
    if isinstance(raw, dict):
        return cast(CommandResponse, raw)
    return None


def _container_from_app(app: FastAPI | None) -> _LookContainer | None:
    if app is None:
        return None
    raw = getattr(app.state, "container", None)
    if raw is None:
        return None
    return cast(_LookContainer, raw)


def _app_from_request(request: LookRequest | None) -> FastAPI | None:
    if request is None:
        return None
    return cast(FastAPI | None, request.app)


def _get_app_and_persistence(request: LookRequest | None) -> tuple[FastAPI | None, _LookPersistence | None]:
    """Extract app and persistence from request."""
    app = _app_from_request(request)
    container = _container_from_app(app)
    if container is not None and container.async_persistence is not None:
        return app, container.async_persistence
    if app is None:
        return None, None
    persistence = getattr(app.state, "persistence", None)
    if persistence is None:
        return app, None
    return app, cast(_LookPersistence, persistence)


async def _validate_look_prerequisites(
    persistence: _LookPersistence | None, current_user: object, player_name: str
) -> tuple[Player, _LookRoom] | None:
    """Validate and retrieve player and room for look command."""
    if not persistence:
        logger.warning("Look command failed - no persistence layer", player=player_name)
        return None

    player = await persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Look command failed - player not found", player=player_name)
        return None

    room_id = str(player.current_room_id)
    room = persistence.get_room_by_id(room_id)
    if not room:
        logger.warning("Look command failed - room not found", player=player_name, room_id=room_id)
        return None

    return player, room


def _get_room_drops(app: FastAPI | None, room_id: object, player_name: str) -> list[dict[str, object]]:
    """Get room drops from room manager."""
    room_drops: list[dict[str, object]] = []
    if not app:
        return room_drops

    container = _container_from_app(app)
    connection_manager: _LookConnectionManager | None
    if container is not None:
        connection_manager = container.connection_manager
    else:
        raw_manager = getattr(app.state, "connection_manager", None)
        connection_manager = None if raw_manager is None else cast(_LookConnectionManager, raw_manager)

    if not connection_manager:
        return room_drops

    room_manager = connection_manager.room_manager
    if room_manager is None:
        return room_drops

    try:
        drops = room_manager.list_room_drops(str(room_id))
        room_drops = clone_room_drops(drops)
    except (AttributeError, TypeError, ValueError) as exc:  # pragma: no cover - defensive logging path
        logger.debug("Failed to list room drops", player=player_name, room_id=room_id, error=str(exc))

    return room_drops


async def _setup_look_command(
    request: LookRequest | None, current_user: object, player_name: str
) -> tuple[FastAPI | None, _LookPersistence, Player, _LookRoom, list[dict[str, object]]] | None:
    """Setup and validate look command prerequisites."""
    app, persistence = _get_app_and_persistence(request)

    prerequisites = await _validate_look_prerequisites(persistence, current_user, player_name)
    if not prerequisites:
        return None

    if persistence is None:
        return None

    player, room = prerequisites
    room_drops = _get_room_drops(app, room.id, player_name)

    return (app, persistence, player, room, room_drops)


def _connection_manager_from_app(app: FastAPI | None) -> _LookConnectionManager | None:
    container = _container_from_app(app)
    if container is not None:
        return container.connection_manager
    if app is None:
        return None
    raw_manager = getattr(app.state, "connection_manager", None)
    if raw_manager is None:
        return None
    return cast(_LookConnectionManager, raw_manager)


def _prototype_registry_from_app(app: FastAPI | None) -> object | None:
    container = _container_from_app(app)
    if container is not None:
        return container.item_prototype_registry
    if app is None:
        return None
    return getattr(app.state, "prototype_registry", None)


async def _try_explicit_player_look(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Look command requires many parameters for context and target resolution
    target: str | None,
    target_type: str | None,
    instance_number: int | None,
    room: _LookRoom,
    persistence: _LookPersistence,
    player_name: str,
    app: FastAPI | None = None,
) -> CommandResponse | None:
    """Try to handle explicit player look."""
    if target_type == "player" and target:
        target_lower = target.lower()
        result = await _handle_player_look(
            target,
            target_lower,
            instance_number,
            room,
            persistence,
            player_name,
            _connection_manager_from_app(app),
        )
        return _as_response(result)
    return None


async def _try_explicit_item_look(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Look command requires many parameters for context and target resolution
    target: str | None,
    target_type: str | None,
    instance_number: int | None,
    room_drops: list[dict[str, object]],
    player: Player,
    app: FastAPI | None,
    command_data: Mapping[str, object],
    player_name: str,
) -> CommandResponse | None:
    """Try to handle explicit item look."""
    if target_type == "item" and target:
        target_lower = target.lower()
        result = await _handle_item_look(
            target,
            target_lower,
            instance_number,
            room_drops,
            player,
            _prototype_registry_from_app(app),
            dict(command_data),
            player_name,
        )
        return _as_response(result)
    return None


async def _try_explicit_container_look(ctx: LookRouteCtx) -> CommandResponse | None:
    """Try to handle explicit container look or container inspection."""
    if (ctx.target_type == "container" or bool(ctx.command_data.get("look_in", False))) and ctx.target:
        target_lower = ctx.target.lower()
        result = await _handle_container_look(
            ContainerLookArgs(
                target=ctx.target,
                target_lower=target_lower,
                instance_number=ctx.instance_number,
                room=ctx.room,
                player=ctx.player,
                persistence=ctx.persistence,
                prototype_registry=_prototype_registry_from_app(ctx.app),
                command_data=dict(ctx.command_data),
                request=ctx.request,
                player_name=ctx.player_name,
            )
        )
        return _as_response(result)
    return None


async def _handle_implicit_target_lookup(ctx: LookRouteCtx, target: str, target_lower: str) -> CommandResponse | None:
    """Handle implicit target lookup with priority resolution."""
    logger.debug("Looking at target", player=ctx.player_name, target=target)

    if _is_direction(target_lower):
        return None

    result = await _try_lookup_player_implicit(
        target,
        target_lower,
        ctx.instance_number,
        ctx.room,
        ctx.persistence,
        ctx.player_name,
        _connection_manager_from_app(ctx.app),
    )
    parsed = _as_response(result)
    if parsed:
        return parsed

    result = await _try_lookup_npc_implicit(target_lower, ctx.room, ctx.player_name, ctx.player)
    parsed = _as_response(result)
    if parsed:
        return parsed

    result = await _try_lookup_phantom_implicit(target_lower, ctx.room, ctx.player)
    parsed = _as_response(result)
    if parsed:
        return parsed

    result = await _try_lookup_item_implicit(
        target_lower, ctx.instance_number, ctx.room_drops, ctx.player, _prototype_registry_from_app(ctx.app)
    )
    parsed = _as_response(result)
    if parsed:
        return parsed

    container_result = await _try_lookup_container_implicit(
        target, target_lower, ctx.instance_number, ctx.room, ctx.player, ctx.persistence, ctx.player_name
    )
    parsed = _as_response(container_result)
    if parsed:
        return parsed

    logger.debug("No matches found for target", player=ctx.player_name, target=target, room_id=ctx.room.id)
    return {"result": f"You don't see any '{target}' here."}


async def _try_implicit_target_lookup(ctx: LookRouteCtx) -> tuple[CommandResponse | None, str | None]:
    """Try to handle implicit target lookup, returns (result, direction)."""
    if ctx.target and not ctx.target_type:
        target_lower = ctx.target.lower()
        if target_lower in ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]:
            return None, target_lower
        result = await _handle_implicit_target_lookup(ctx, ctx.target, target_lower)
        if result:
            return result, None
    return None, None


async def _try_direction_look(
    direction: str | None, room: _LookRoom, persistence: _LookPersistence, player_name: str
) -> CommandResponse | None:
    """Try to handle direction look."""
    if direction:
        result = await _handle_direction_look(direction, room, persistence, player_name)
        return _as_response(result)
    return None


async def _route_look_command(ctx: LookRouteCtx) -> CommandResponse:
    """Route look command to appropriate handler."""
    result = await _try_explicit_player_look(
        ctx.target, ctx.target_type, ctx.instance_number, ctx.room, ctx.persistence, ctx.player_name, ctx.app
    )
    if result:
        return result

    result = await _try_explicit_item_look(
        ctx.target,
        ctx.target_type,
        ctx.instance_number,
        ctx.room_drops,
        ctx.player,
        ctx.app,
        ctx.command_data,
        ctx.player_name,
    )
    if result:
        return result

    result = await _try_explicit_container_look(ctx)
    if result:
        return result

    result, new_direction = await _try_implicit_target_lookup(ctx)
    if result:
        return result
    direction = new_direction or ctx.direction

    result = await _try_direction_look(direction, ctx.room, ctx.persistence, ctx.player_name)
    if result:
        return result

    room_result = await _handle_room_look(
        ctx.room, ctx.room_drops, ctx.persistence, ctx.player_name, ctx.request, ctx.player.player_id
    )
    parsed = _as_response(room_result)
    if parsed is not None:
        return parsed
    return {"result": "You see nothing special."}


async def handle_look_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """
    Handle the look command for examining surroundings.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Look command result, including rendered text and room drop metadata
    """
    _ = alias_storage  # Unused parameter
    logger.debug("Processing look command", player=player_name, args=command_data)

    look_request = cast(LookRequest | None, request)
    setup_result = await _setup_look_command(look_request, current_user, player_name)
    if not setup_result:
        return {"result": "You see nothing special."}

    app, persistence, player, room, room_drops = setup_result

    return await _route_look_command(
        LookRouteCtx(
            command_data=command_data,
            target=_opt_str(command_data.get("target")),
            target_type=_opt_str(command_data.get("target_type")),
            direction=_opt_str(command_data.get("direction")),
            instance_number=_opt_int(command_data.get("instance_number")),
            room=room,
            player=player,
            persistence=persistence,
            room_drops=room_drops,
            app=app,
            request=look_request,
            player_name=player_name,
        )
    )


__all__ = ["handle_look_command"]
