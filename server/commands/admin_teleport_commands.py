"""
Admin teleport command handlers for MythosMUD.

This module provides handlers for teleport and goto administrative commands.
"""

# pylint: disable=too-many-locals,too-many-return-statements  # Reason: Command handlers require many intermediate variables for complex game logic and multiple return statements for early validation returns

from typing import Any

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


async def handle_teleport_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
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

        current_player = await player_service.get_player_by_name(player_name)
        if not current_player:
            logger.warning("Teleport command failed - current player not found", player_name=player_name)
            return {"result": "Player not found."}

        if not await validate_admin_permission(current_player, player_name):
            return {"result": "You do not have permission to use teleport commands."}

        target_player_name = command_data.get("target_player")
        if not target_player_name:
            return {"result": "Usage: teleport <player_name> [direction]"}

        direction_value = command_data.get("direction")
        direction_value = str(direction_value).lower() if direction_value else None

        direction_result = resolve_teleport_direction(direction_value, persistence, current_player, player_name)
        if isinstance(direction_result, dict):
            return direction_result

        target_room_id, target_room_name = direction_result

        # Resolve target player
        target_result = await resolve_target_player(
            player_service, connection_manager, target_player_name, current_player, direction_value
        )
        if isinstance(target_result, dict):
            return target_result

        target_player, target_player_info = target_result

        try:
            # Update player location
            location_result = await update_teleport_location(
                player_service,
                target_player,
                target_player_name,
                target_room_id,
                target_player_info,
                connection_manager,
                persistence,
            )
            if isinstance(location_result, dict):
                return location_result

            original_room_id = location_result

            await broadcast_teleport_updates(
                connection_manager,
                target_player_info,
                target_room_id,
                target_player_name,
                player_name,
                direction_value,
                target_room_name,
                original_room_id,
            )

            log_teleport_success(
                player_name,
                target_player_name,
                direction_value,
                target_room_id,
                original_room_id,
                current_player.current_room_id,
            )

            admin_message = build_teleport_message(target_player_name, direction_value)
            return {"result": admin_message}

        except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
            admin_logger = get_admin_actions_logger()
            try:
                admin_logger.log_teleport_action(
                    admin_name=player_name,
                    target_player=target_player_name,
                    action_type="teleport",
                    from_room=target_player.current_room_id,
                    to_room=current_player.current_room_id,
                    success=False,
                    error_message=str(e),
                    additional_data={
                        "admin_room_id": current_player.current_room_id,
                        "target_room_id": target_player.current_room_id,
                        "direction": direction_value,
                    },
                )
            except (OSError, AttributeError, TypeError):
                pass  # Ignore logging errors if command itself failed

            logger.error(
                "Teleport execution failed", admin_name=player_name, target_player_name=target_player_name, error=str(e)
            )
            return {"result": f"Failed to teleport {target_player_name}: {str(e)}"}
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


async def handle_confirm_teleport_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
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

    app = request.app if request else None
    player_service = app.state.player_service if app else None

    current_player, error_result = await validate_confirm_teleport_context(app, player_service, player_name)
    if error_result:
        return error_result

    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: confirm teleport <player_name>"}

    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning("Confirm teleport command failed - no connection manager", player_name=player_name)
        return {"result": "Connection manager not available."}

    target_player_info, target_player, error_result = await resolve_target_player_for_teleport(
        target_player_name, connection_manager, player_service
    )
    if error_result:
        return error_result

    # After error check, target_player and target_player_info should not be None, but verify for mypy
    if target_player is None or target_player_info is None:
        logger.warning(
            "Confirm teleport command failed - target player resolution returned None", player_name=player_name
        )
        return {"result": f"Failed to resolve target player '{target_player_name}'."}

    if current_player is None:
        logger.warning("Confirm teleport command failed - current player is None", player_name=player_name)
        return {"result": "Current player information is not available."}

    if target_player.current_room_id == current_player.current_room_id:
        return {"result": f"{target_player_name} is already in your location."}

    persistence = getattr(app.state, "persistence", None) if app else None
    try:
        return await execute_confirm_teleport(
            target_player_name,
            target_player,
            target_player_info,
            current_player,
            player_service,
            connection_manager,
            player_name,
            persistence,
        )

    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        # Log the failed teleport action
        # target_player and current_player are guaranteed to be non-None here (checked before execute_confirm_teleport)
        if target_player is not None and current_player is not None:
            admin_logger = get_admin_actions_logger()
            try:
                admin_logger.log_teleport_action(
                    admin_name=player_name,
                    target_player=target_player_name,
                    action_type="teleport",
                    from_room=target_player.current_room_id,
                    to_room=current_player.current_room_id,
                    success=False,
                    error_message=str(e),
                    additional_data={
                        "admin_room_id": current_player.current_room_id,
                        "target_room_id": target_player.current_room_id,
                    },
                )
            except (OSError, AttributeError, TypeError):
                pass  # Ignore logging errors if command itself failed

        logger.error(
            "Teleport execution failed", admin_name=player_name, target_player_name=target_player_name, error=str(e)
        )
        return {"result": f"Failed to teleport {target_player_name}: {str(e)}"}


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

    app = request.app if request else None
    player_service = app.state.player_service if app else None

    current_player, error_result = await validate_confirm_goto_context(app, player_service, player_name)
    if error_result:
        return error_result

    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: confirm goto <player_name>"}

    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning("Confirm goto command failed - no connection manager", player_name=player_name)
        return {"result": "Connection manager not available."}

    _, target_player, error_result = await resolve_target_player_for_goto(
        target_player_name, connection_manager, player_service
    )
    if error_result:
        return error_result

    # After error check, target_player and current_player should not be None, but verify for mypy
    if target_player is None:
        logger.warning("Confirm goto command failed - target player resolution returned None", player_name=player_name)
        return {"result": f"Failed to resolve target player '{target_player_name}'."}

    if current_player is None:
        logger.warning("Confirm goto command failed - current player is None", player_name=player_name)
        return {"result": "Current player information is not available."}

    if current_player.current_room_id == target_player.current_room_id:
        return {"result": f"You are already in the same location as {target_player_name}."}

    persistence = getattr(app.state, "persistence", None) if app else None
    try:
        return await execute_confirm_goto(
            player_name,
            current_player,
            target_player_name,
            target_player,
            player_service,
            connection_manager,
            persistence,
        )

    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        # Log the failed goto action
        # target_player and current_player are guaranteed to be non-None here (checked before execute_confirm_goto)
        if target_player is not None and current_player is not None:
            admin_logger = get_admin_actions_logger()
            try:
                admin_logger.log_teleport_action(
                    admin_name=player_name,
                    target_player=target_player_name,
                    action_type="goto",
                    from_room=current_player.current_room_id,
                    to_room=target_player.current_room_id,
                    success=False,
                    error_message=str(e),
                    additional_data={
                        "admin_room_id": current_player.current_room_id,
                        "target_room_id": target_player.current_room_id,
                    },
                )
            except (OSError, AttributeError, TypeError):
                pass  # Ignore logging errors if command itself failed

        logger.error(
            "Goto execution failed", admin_name=player_name, target_player_name=target_player_name, error=str(e)
        )
        return {"result": f"Failed to teleport to {target_player_name}: {str(e)}"}


__all__ = [
    "handle_teleport_command",
    "handle_goto_command",
    "handle_confirm_teleport_command",
    "handle_confirm_goto_command",
    "DIRECTION_OPPOSITES",
]
