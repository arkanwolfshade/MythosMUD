"""
Admin teleport command handlers for MythosMUD.

This module provides handlers for teleport and goto administrative commands.
"""

# pylint: disable=too-many-locals,too-many-return-statements  # Reason: Command handlers require many intermediate variables for complex game logic and multiple return statements for early validation returns

from dataclasses import dataclass
from typing import Any, cast

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger
from .admin_permission_utils import validate_admin_permission
from .goto_helpers import (
    execute_confirm_goto,
    execute_goto_teleport,
    log_goto_failure,
    resolve_goto_target,
    resolve_target_player_for_goto,
    validate_confirm_goto_context,
    validate_goto_context,
)
from .teleport_helpers import (
    DIRECTION_OPPOSITES,
    broadcast_teleport_updates,
    build_teleport_message,
    execute_confirm_teleport,
    log_teleport_success,
    resolve_target_player,
    resolve_target_player_for_teleport,
    resolve_teleport_direction,
    resolve_teleport_services,
    update_teleport_location,
    validate_confirm_teleport_context,
)

logger = get_logger(__name__)


def _log_failed_admin_move(
    *,
    admin_name: str,
    target_player_name: str,
    action_type: str,
    from_room: str,
    to_room: str,
    error: Exception,
    direction: str | None = None,
) -> None:
    """Best-effort audit log for a failed teleport/goto action; never raises.

    Shared by handle_teleport_command, handle_confirm_teleport_command, and
    handle_confirm_goto_command (issue #787): each had a near-identical
    try/except-around-log_teleport_action block in its exception handler.
    Takes room ids rather than player objects so it doesn't need an explicit
    Any (the module's player-lookup helpers all return Any today).

    A "goto" moves the admin (from_room=admin's room); a "teleport" moves the
    target (from_room=target's room) -- admin_room_id/target_room_id are
    derived from that instead of taking two more redundant params.
    """
    admin_logger = get_admin_actions_logger()
    admin_room_id, target_room_id = (from_room, to_room) if action_type == "goto" else (to_room, from_room)
    additional_data: dict[str, str] = {
        "admin_room_id": admin_room_id,
        "target_room_id": target_room_id,
    }
    if direction is not None:
        additional_data["direction"] = direction
    try:
        admin_logger.log_teleport_action(
            admin_name=admin_name,
            target_player=target_player_name,
            action_type=action_type,
            from_room=from_room,
            to_room=to_room,
            success=False,
            error_message=str(error),
            additional_data=additional_data,
        )
    except (OSError, AttributeError, TypeError):
        pass  # Ignore logging errors if command itself failed


@dataclass(frozen=True)
class _TeleportExecutionContext:
    """Bundled teleport-command context resolved before executing the move."""

    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    current_player: Any  # pyright: ignore[reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    target_player: Any  # pyright: ignore[reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    target_player_info: Any  # pyright: ignore[reportExplicitAny]
    target_player_name: str
    target_room_id: str
    target_room_name: str | None
    direction_value: str | None


async def _resolve_teleport_execution_context(
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    player_service: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    connection_manager: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    persistence: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    command_data: dict[str, Any],
    player_name: str,
) -> tuple[_TeleportExecutionContext | None, dict[str, str] | None]:
    """Resolve current player, permissions, direction, and target player for a teleport command.

    Returns (context, None) on success, or (None, error_result) on the first failed step.
    """
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    current_player = await player_service.get_player_by_name(player_name)  # pyright: ignore[reportAny]
    if not current_player:
        logger.warning("Teleport command failed - current player not found", player_name=player_name)
        return None, {"result": "Player not found."}

    if not await validate_admin_permission(current_player, player_name):
        return None, {"result": "You do not have permission to use teleport commands."}

    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return None, {"result": "Usage: teleport <player_name> [direction]"}

    direction_value = command_data.get("direction")
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    direction_value = str(direction_value).lower() if direction_value else None  # pyright: ignore[reportAny]

    direction_result = resolve_teleport_direction(direction_value, persistence, current_player, player_name)
    if isinstance(direction_result, dict):
        return None, direction_result
    target_room_id, target_room_name = direction_result

    target_result = await resolve_target_player(
        player_service,
        connection_manager,
        # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
        # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
        target_player_name,  # pyright: ignore[reportAny]
        current_player,
        direction_value,
    )
    if isinstance(target_result, dict):
        return None, target_result
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    target_player, target_player_info = target_result  # pyright: ignore[reportAny]

    return (
        _TeleportExecutionContext(
            current_player=current_player,
            target_player=target_player,
            target_player_info=target_player_info,
            # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
            # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
            target_player_name=target_player_name,  # pyright: ignore[reportAny]
            target_room_id=target_room_id,
            target_room_name=target_room_name,
            direction_value=direction_value,
        ),
        None,
    )


def _log_teleport_execution_failure(context: "_TeleportExecutionContext", player_name: str, error: Exception) -> None:
    """Log a failed teleport execution to the admin actions log and structured logger."""
    _log_failed_admin_move(
        admin_name=player_name,
        target_player_name=context.target_player_name,
        action_type="teleport",
        # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
        # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
        from_room=cast(str, context.target_player.current_room_id),  # pyright: ignore[reportAny]
        # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
        # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
        to_room=cast(str, context.current_player.current_room_id),  # pyright: ignore[reportAny]
        error=error,
        direction=context.direction_value,
    )
    logger.error(
        "Teleport execution failed",
        admin_name=player_name,
        target_player_name=context.target_player_name,
        error=str(error),
    )


async def _execute_teleport_move(
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    player_service: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    connection_manager: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    persistence: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    context: _TeleportExecutionContext,
    player_name: str,
) -> dict[str, str]:
    """Update the target's location, broadcast the move, and log success or failure."""
    try:
        location_result = await update_teleport_location(
            player_service,
            # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
            # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
            context.target_player,  # pyright: ignore[reportAny]
            context.target_player_name,
            context.target_room_id,
            # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
            # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
            context.target_player_info,  # pyright: ignore[reportAny]
            connection_manager,
            # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
            # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
            persistence,  # pyright: ignore[reportAny]
        )
        if isinstance(location_result, dict):
            return location_result

        original_room_id = location_result

        await broadcast_teleport_updates(
            connection_manager,
            # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
            # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
            context.target_player_info,  # pyright: ignore[reportAny]
            context.target_room_id,
            context.target_player_name,
            player_name,
            context.direction_value,
            context.target_room_name,
            original_room_id,
        )

        log_teleport_success(
            player_name,
            context.target_player_name,
            context.direction_value,
            context.target_room_id,
            original_room_id,
            # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
            # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
            context.current_player.current_room_id,  # pyright: ignore[reportAny]
        )

        admin_message = build_teleport_message(context.target_player_name, context.direction_value)
        return {"result": admin_message}

    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        _log_teleport_execution_failure(context, player_name, e)
        return {"result": f"Failed to teleport {context.target_player_name}: {str(e)}"}


async def handle_teleport_command(
    command_data: dict[str, Any],
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    current_user: dict[str, Any],  # pyright: ignore[reportExplicitAny]
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the teleport command for bringing a player to the admin's location.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Teleport command result
    """
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    _ = current_user  # Intentionally unused - part of standard command handler interface

    logger.debug("Processing teleport command", player_name=player_name, command_data=command_data)

    try:
        app = request.app if request else None
        service_result = await resolve_teleport_services(app, player_name)
        if isinstance(service_result, dict):
            return service_result

        player_service, connection_manager, persistence, app = service_result

        context, error_result = await _resolve_teleport_execution_context(
            player_service, connection_manager, persistence, command_data, player_name
        )
        if error_result or context is None:
            return error_result or {"result": "Failed to resolve teleport context."}

        return await _execute_teleport_move(player_service, connection_manager, persistence, context, player_name)
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        logger.error("Exception in teleport command handler", error=str(e), exc_info=True)
        return {"result": f"Error processing teleport command: {str(e)}"}


async def handle_goto_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the goto command for teleporting the admin to a player's location.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Goto command result
    """
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    _ = current_user  # Intentionally unused - part of standard command handler interface

    logger.debug("Processing goto command", player_name=player_name, command_data=command_data)

    app = request.app if request else None
    player_service = app.state.player_service if app else None
    connection_manager = app.state.connection_manager if app else None

    # Validate context and get current player
    current_player, context_error = await validate_goto_context(app, player_service, connection_manager, player_name)
    if context_error:
        return context_error

    # Extract target player from command data
    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: goto <player_name>"}

    # Resolve target player
    target_player, target_error = await resolve_goto_target(target_player_name, player_service, connection_manager)
    if target_error:
        return target_error

    # Check if admin is already in the same room
    if current_player.current_room_id == target_player.current_room_id:
        return {"result": f"You are already in the same location as {target_player_name}."}

    persistence = getattr(app.state, "persistence", None) if app else None
    # Execute goto immediately without confirmation
    try:
        return await execute_goto_teleport(
            player_service,
            connection_manager,
            current_player,
            target_player,
            target_player_name,
            player_name,
            persistence,
        )
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        log_goto_failure(player_name, target_player_name, current_player, target_player, e)
        return {"result": f"Failed to teleport to {target_player_name}: {str(e)}"}


# Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
# Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
def _resolve_request_app_service(request: Any) -> tuple[Any, Any]:  # pyright: ignore[reportAny, reportExplicitAny]
    """Resolve the FastAPI app and its player_service from a command request."""
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    return app, player_service


# Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
# Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
def _resolve_connection_manager(app: Any, player_name: str, command_label: str) -> tuple[Any, dict[str, str] | None]:  # pyright: ignore[reportAny, reportExplicitAny]
    """Resolve the connection manager from app.state, or a 'not available' error result."""
    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning("Confirm command failed - no connection manager", player_name=player_name, command=command_label)
        return None, {"result": "Connection manager not available."}
    return connection_manager, None


async def _resolve_confirm_teleport_targets(
    target_player_name: str,
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    connection_manager: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    player_service: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    current_player: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    player_name: str,
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
) -> tuple[Any, Any, dict[str, str] | None]:  # pyright: ignore[reportExplicitAny]
    """Resolve and validate the target player for a confirm-teleport command.

    Returns (target_player, target_player_info, None) on success, or (None, None, error_result).
    """
    target_player_info, target_player, error_result = await resolve_target_player_for_teleport(
        target_player_name, connection_manager, player_service
    )
    if error_result:
        return None, None, error_result

    # After error check, target_player and target_player_info should not be None, but verify for mypy
    if target_player is None or target_player_info is None:
        logger.warning(
            "Confirm teleport command failed - target player resolution returned None", player_name=player_name
        )
        return None, None, {"result": f"Failed to resolve target player '{target_player_name}'."}

    if current_player is None:
        logger.warning("Confirm teleport command failed - current player is None", player_name=player_name)
        return None, None, {"result": "Current player information is not available."}

    return target_player, target_player_info, None


async def _execute_confirm_teleport_move(
    target_player_name: str,
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    target_player: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    target_player_info: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    current_player: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    player_service: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    connection_manager: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    player_name: str,
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    persistence: Any,  # pyright: ignore[reportAny, reportExplicitAny]
) -> dict[str, str]:
    """Execute the confirmed teleport, logging and reporting any failure."""
    try:
        return await execute_confirm_teleport(
            target_player_name,
            target_player,
            # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
            # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
            target_player_info,  # pyright: ignore[reportAny]
            current_player,
            player_service,
            connection_manager,
            player_name,
            # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
            # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
            persistence,  # pyright: ignore[reportAny]
        )
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        _log_failed_admin_move(
            admin_name=player_name,
            target_player_name=target_player_name,
            action_type="teleport",
            from_room=cast(str, target_player.current_room_id),
            to_room=cast(str, current_player.current_room_id),
            error=e,
        )
        logger.error(
            "Teleport execution failed", admin_name=player_name, target_player_name=target_player_name, error=str(e)
        )
        return {"result": f"Failed to teleport {target_player_name}: {str(e)}"}


async def handle_confirm_teleport_command(
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    command_data: dict[str, Any],  # pyright: ignore[reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    current_user: dict[str, Any],  # pyright: ignore[reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    request: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the confirm teleport command for executing the actual teleportation.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Teleport confirmation result
    """
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    _ = current_user  # Intentionally unused - part of standard command handler interface

    logger.debug("Processing confirm teleport command", player_name=player_name, command_data=command_data)

    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    app, player_service = _resolve_request_app_service(request)  # pyright: ignore[reportAny]

    current_player, error_result = await validate_confirm_teleport_context(app, player_service, player_name)
    if error_result:
        return error_result

    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: confirm teleport <player_name>"}

    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    connection_manager, error_result = _resolve_connection_manager(app, player_name, "confirm teleport")  # pyright: ignore[reportAny]
    if error_result:
        return error_result

    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    target_player, target_player_info, error_result = await _resolve_confirm_teleport_targets(  # pyright: ignore[reportAny]
        target_player_name, connection_manager, player_service, current_player, player_name
    )
    if error_result:
        return error_result
    assert current_player is not None  # narrowed by _resolve_confirm_teleport_targets' own None-check above

    if target_player.current_room_id == current_player.current_room_id:
        return {"result": f"{target_player_name} is already in your location."}

    persistence = getattr(app.state, "persistence", None) if app else None
    return await _execute_confirm_teleport_move(
        # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
        # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
        target_player_name,  # pyright: ignore[reportAny]
        target_player,
        target_player_info,
        current_player,
        player_service,
        connection_manager,
        player_name,
        persistence,
    )


async def _resolve_confirm_goto_target(
    target_player_name: str,
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    connection_manager: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    player_service: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    current_player: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    player_name: str,
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
) -> tuple[Any, dict[str, str] | None]:  # pyright: ignore[reportExplicitAny]
    """Resolve and validate the target player for a confirm-goto command.

    Returns (target_player, None) on success, or (None, error_result).
    """
    _, target_player, error_result = await resolve_target_player_for_goto(
        target_player_name, connection_manager, player_service
    )
    if error_result:
        return None, error_result

    # After error check, target_player and current_player should not be None, but verify for mypy
    if target_player is None:
        logger.warning("Confirm goto command failed - target player resolution returned None", player_name=player_name)
        return None, {"result": f"Failed to resolve target player '{target_player_name}'."}

    if current_player is None:
        logger.warning("Confirm goto command failed - current player is None", player_name=player_name)
        return None, {"result": "Current player information is not available."}

    return target_player, None


async def _execute_confirm_goto_move(
    player_name: str,
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    current_player: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    target_player_name: str,
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    target_player: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    player_service: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    connection_manager: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    persistence: Any,  # pyright: ignore[reportAny, reportExplicitAny]
) -> dict[str, str]:
    """Execute the confirmed goto, logging and reporting any failure."""
    try:
        return await execute_confirm_goto(
            player_name,
            current_player,
            target_player_name,
            target_player,
            player_service,
            connection_manager,
            # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
            # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
            persistence,  # pyright: ignore[reportAny]
        )
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        _log_failed_admin_move(
            admin_name=player_name,
            target_player_name=target_player_name,
            action_type="goto",
            from_room=cast(str, current_player.current_room_id),
            to_room=cast(str, target_player.current_room_id),
            error=e,
        )
        logger.error(
            "Goto execution failed", admin_name=player_name, target_player_name=target_player_name, error=str(e)
        )
        return {"result": f"Failed to teleport to {target_player_name}: {str(e)}"}


async def handle_confirm_goto_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the confirm goto command for executing the actual teleportation.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Goto confirmation result
    """
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    _ = current_user  # Intentionally unused - part of standard command handler interface

    logger.debug("Processing confirm goto command", player_name=player_name, command_data=command_data)

    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    app, player_service = _resolve_request_app_service(request)  # pyright: ignore[reportAny]

    current_player, error_result = await validate_confirm_goto_context(app, player_service, player_name)
    if error_result:
        return error_result

    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: confirm goto <player_name>"}

    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    connection_manager, error_result = _resolve_connection_manager(app, player_name, "confirm goto")  # pyright: ignore[reportAny]
    if error_result:
        return error_result

    # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
    # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
    target_player, error_result = await _resolve_confirm_goto_target(  # pyright: ignore[reportAny]
        target_player_name, connection_manager, player_service, current_player, player_name
    )
    if error_result:
        return error_result
    assert current_player is not None  # narrowed by _resolve_confirm_goto_target's own None-check above

    if current_player.current_room_id == target_player.current_room_id:
        return {"result": f"You are already in the same location as {target_player_name}."}

    persistence = getattr(app.state, "persistence", None) if app else None
    return await _execute_confirm_goto_move(
        player_name,
        current_player,
        # Reason: DYNAMIC_DISPATCH - resolved app/player/connection-manager objects are duck-typed
        # Appropriate because: same unsuppressed convention as this module's teleport helpers (see _announce_confirm_teleport).
        target_player_name,  # pyright: ignore[reportAny]
        target_player,
        player_service,
        connection_manager,
        persistence,
    )


__all__ = [
    "handle_teleport_command",
    "handle_goto_command",
    "handle_confirm_teleport_command",
    "handle_confirm_goto_command",
    "DIRECTION_OPPOSITES",
]
