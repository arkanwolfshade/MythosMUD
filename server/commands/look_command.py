"""
Look command for MythosMUD.

This module handles the look command for examining surroundings.
This is the main entry point that routes to specialized handlers.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from ..utils.room_renderer import clone_room_drops
from .look_container import _handle_container_look, _try_lookup_container_implicit
from .look_helpers import _is_direction
from .look_item import _handle_item_look, _try_lookup_item_implicit
from .look_npc import _try_lookup_npc_implicit
from .look_player import _handle_player_look, _try_lookup_player_implicit
from .look_room import _handle_direction_look, _handle_room_look

logger = get_logger(__name__)


def _get_app_and_persistence(request: Any) -> tuple[Any, Any]:
    """Extract app and persistence from request."""
    app = request.app if request else None
    persistence = app.state.persistence if app else None
    return app, persistence


async def _validate_look_prerequisites(
    persistence: Any, current_user: dict, player_name: str
) -> tuple[Any, Any] | None:
    """Validate and retrieve player and room for look command."""
    if not persistence:
        logger.warning("Look command failed - no persistence layer", player=player_name)
        return None

    player = await persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Look command failed - player not found", player=player_name)
        return None

    room_id = player.current_room_id
    room = persistence.get_room_by_id(room_id)
    if not room:
        logger.warning("Look command failed - room not found", player=player_name, room_id=room_id)
        return None

    return player, room


def _get_room_drops(app: Any, room_id: int, player_name: str) -> list[dict[str, Any]]:
    """Get room drops from room manager."""
    room_drops: list[dict[str, Any]] = []
    if not app:
        return room_drops

    connection_manager = getattr(app.state, "connection_manager", None)
    if not connection_manager:
        return room_drops

    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager or not hasattr(room_manager, "list_room_drops"):
        return room_drops

    try:
        drops = room_manager.list_room_drops(str(room_id))
        room_drops = clone_room_drops(drops)
    except (AttributeError, TypeError, ValueError) as exc:  # pragma: no cover - defensive logging path
        logger.debug("Failed to list room drops", player=player_name, room_id=room_id, error=str(exc))

    return room_drops


async def _setup_look_command(
    request: Any, current_user: dict, player_name: str
) -> tuple[Any, Any, Any, Any, list[dict[str, Any]]] | None:
    """Setup and validate look command prerequisites."""
    app, persistence = _get_app_and_persistence(request)

    prerequisites = await _validate_look_prerequisites(persistence, current_user, player_name)
    if not prerequisites:
        return None

    player, room = prerequisites
    room_drops = _get_room_drops(app, room.id, player_name)

    return (app, persistence, player, room, room_drops)


async def _try_explicit_player_look(
    target: str | None,
    target_type: str | None,
    instance_number: int | None,
    room: Any,
    persistence: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Try to handle explicit player look."""
    if target_type == "player" and target:
        target_lower = target.lower()
        result = await _handle_player_look(target, target_lower, instance_number, room, persistence, player_name)
        if result:
            return result
    return None


async def _try_explicit_item_look(
    target: str | None,
    target_type: str | None,
    instance_number: int | None,
    room_drops: list[dict[str, Any]],
    player: Any,
    app: Any,
    command_data: dict,
    player_name: str,
) -> dict[str, Any] | None:
    """Try to handle explicit item look."""
    if target_type == "item" and target:
        target_lower = target.lower()
        prototype_registry = getattr(app.state, "prototype_registry", None) if app else None
        result = await _handle_item_look(
            target, target_lower, instance_number, room_drops, player, prototype_registry, command_data, player_name
        )
        if result:
            return result
    return None


async def _try_explicit_container_look(
    target: str | None,
    target_type: str | None,
    instance_number: int | None,
    room: Any,
    player: Any,
    persistence: Any,
    app: Any,
    command_data: dict,
    request: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Try to handle explicit container look or container inspection."""
    if (target_type == "container" or command_data.get("look_in", False)) and target:
        target_lower = target.lower()
        prototype_registry = getattr(app.state, "prototype_registry", None) if app else None
        result = await _handle_container_look(
            target,
            target_lower,
            instance_number,
            room,
            player,
            persistence,
            prototype_registry,
            command_data,
            request,
            player_name,
        )
        if result:
            return result
    return None


async def _handle_implicit_target_lookup(
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    player: Any,
    persistence: Any,
    room_drops: list[dict[str, Any]],
    app: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Handle implicit target lookup with priority resolution."""
    logger.debug("Looking at target", player=player_name, target=target)

    if _is_direction(target_lower):
        return None  # Will be handled as direction

    # Priority 1: Try players
    result = await _try_lookup_player_implicit(target, target_lower, instance_number, room, persistence, player_name)
    if result:
        return result

    # Priority 2: Try NPCs
    result = await _try_lookup_npc_implicit(target_lower, room, player_name, player)
    if result:
        return result

    # Priority 3: Try items
    prototype_registry = getattr(app.state, "prototype_registry", None) if app else None
    result = await _try_lookup_item_implicit(target_lower, instance_number, room_drops, player, prototype_registry)
    if result:
        return result

    # Priority 4: Try containers
    result = await _try_lookup_container_implicit(
        target, target_lower, instance_number, room, player, persistence, player_name
    )
    if result:
        return result

    logger.debug("No matches found for target", player=player_name, target=target, room_id=room.id)
    return {"result": f"You don't see any '{target}' here."}


async def _try_implicit_target_lookup(
    target: str | None,
    target_type: str | None,
    instance_number: int | None,
    room: Any,
    player: Any,
    persistence: Any,
    room_drops: list[dict[str, Any]],
    app: Any,
    player_name: str,
) -> tuple[dict[str, Any] | None, str | None]:
    """Try to handle implicit target lookup, returns (result, direction)."""
    if target and not target_type:
        target_lower = target.lower()
        if target_lower in ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]:
            return None, target_lower
        result = await _handle_implicit_target_lookup(
            target, target_lower, instance_number, room, player, persistence, room_drops, app, player_name
        )
        if result:
            return result, None
    return None, None


async def _try_direction_look(
    direction: str | None, room: Any, persistence: Any, player_name: str
) -> dict[str, Any] | None:
    """Try to handle direction look."""
    if direction:
        result = await _handle_direction_look(direction, room, persistence, player_name)
        if result:
            return result
    return None


async def _route_look_command(
    command_data: dict,
    target: str | None,
    target_type: str | None,
    direction: str | None,
    instance_number: int | None,
    room: Any,
    player: Any,
    persistence: Any,
    room_drops: list[dict[str, Any]],
    app: Any,
    request: Any,
    player_name: str,
) -> dict[str, Any]:
    """Route look command to appropriate handler."""
    # Try explicit handlers in order
    result = await _try_explicit_player_look(target, target_type, instance_number, room, persistence, player_name)
    if result:
        return result

    result = await _try_explicit_item_look(
        target, target_type, instance_number, room_drops, player, app, command_data, player_name
    )
    if result:
        return result

    result = await _try_explicit_container_look(
        target, target_type, instance_number, room, player, persistence, app, command_data, request, player_name
    )
    if result:
        return result

    # Handle implicit target lookup (may return direction)
    result, new_direction = await _try_implicit_target_lookup(
        target, target_type, instance_number, room, player, persistence, room_drops, app, player_name
    )
    if result:
        return result
    if new_direction:
        direction = new_direction

    # Handle direction lookups
    result = await _try_direction_look(direction, room, persistence, player_name)
    if result:
        return result

    # Look at current room (default)
    return await _handle_room_look(room, room_drops, persistence, player_name)


async def handle_look_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
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

    setup_result = await _setup_look_command(request, current_user, player_name)
    if not setup_result:
        return {"result": "You see nothing special."}

    app, persistence, player, room, room_drops = setup_result

    direction = command_data.get("direction")
    target = command_data.get("target")
    target_type = command_data.get("target_type")
    instance_number = command_data.get("instance_number")

    return await _route_look_command(
        command_data,
        target,
        target_type,
        direction,
        instance_number,
        room,
        player,
        persistence,
        room_drops,
        app,
        request,
        player_name,
    )


__all__ = ["handle_look_command"]
