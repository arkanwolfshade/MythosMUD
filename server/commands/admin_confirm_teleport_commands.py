"""
Admin confirm-teleport/confirm-goto command handlers for MythosMUD.

Split out of admin_teleport_commands.py (issue #787, C0302 too-many-lines): this module
handles the "confirm teleport"/"confirm goto" flows specifically, while admin_teleport_commands.py
keeps the direct "teleport"/"goto" handlers.
"""

from typing import Any, cast

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from .admin_teleport_utils import log_failed_admin_move
from .goto_helpers import execute_confirm_goto, resolve_target_player_for_goto, validate_confirm_goto_context
from .teleport_helpers import (
    execute_confirm_teleport,
    resolve_target_player_for_teleport,
    validate_confirm_teleport_context,
)

logger = get_logger(__name__)


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
        log_failed_admin_move(
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
    if current_player is None:
        # Unreachable: _resolve_confirm_teleport_targets returns an error_result whenever
        # current_player is None, so this narrows the type without using assert (Bandit B101).
        raise RuntimeError("current_player unexpectedly None after successful target resolution")

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
        log_failed_admin_move(
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
    if current_player is None:
        # Unreachable: _resolve_confirm_goto_target returns an error_result whenever
        # current_player is None, so this narrows the type without using assert (Bandit B101).
        raise RuntimeError("current_player unexpectedly None after successful target resolution")

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
    "handle_confirm_teleport_command",
    "handle_confirm_goto_command",
]
