"""Helper functions for goto command operations."""

# pylint: disable=too-many-arguments  # Reason: Goto helpers require many parameters for context and validation

from typing import Any

from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger
from .admin_teleport_utils import (
    broadcast_teleport_effects,
    get_online_player_by_display_name,
    notify_player_of_teleport,
)
from .teleport_helpers import update_player_room_location

logger = get_logger(__name__)


async def validate_goto_context(
    app: Any, player_service: Any, connection_manager: Any, player_name: str
) -> tuple[Any, dict[str, str] | None]:
    """Validate goto command context and get current player."""
    if not app:
        logger.warning("Goto command failed - no app context", player_name=player_name)
        return None, {"result": "Goto functionality is not available."}

    if not player_service:
        logger.warning("Goto command failed - no player service", player_name=player_name)
        return None, {"result": "Player service not available."}

    current_player = await player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning("Goto command failed - current player not found", player_name=player_name)
        return None, {"result": "Player not found."}

    from .admin_permission_utils import validate_admin_permission

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return None, {"result": "You do not have permission to use goto commands."}

    if not connection_manager:
        logger.warning("Goto command failed - no connection manager", player_name=player_name)
        return None, {"result": "Connection manager not available."}

    return current_player, None


async def resolve_goto_target(
    target_player_name: str, player_service: Any, connection_manager: Any
) -> tuple[Any, dict[str, str] | None]:
    """Resolve target player for goto command."""
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return None, {"result": f"Player '{target_player_name}' is not online or not found."}

    target_player = await player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(
            "Goto command failed - target player not found in database", target_player_name=target_player_name
        )
        return None, {"result": f"Player '{target_player_name}' not found in database."}

    return target_player, None


async def execute_goto_teleport(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Goto helpers require many parameters for context and teleport execution
    player_service: Any,
    connection_manager: Any,
    current_player: Any,
    target_player: Any,
    target_player_name: str,
    player_name: str,
    persistence: Any | None = None,
) -> dict[str, str]:
    """Execute the goto teleport operation. Room state is notified via EventBus (Room.player_entered/player_left)."""
    original_room_id = current_player.current_room_id
    target_room_id = target_player.current_room_id

    # Update admin player's location
    success = await player_service.update_player_location(player_name, target_room_id)
    if not success:
        logger.error("Failed to update admin player location", player_name=player_name)
        return {"result": f"Failed to teleport to {target_player_name}: database update failed."}

    # Update connection manager's online player info for admin
    admin_player_info = connection_manager.get_online_player_by_display_name(player_name)
    if admin_player_info:
        admin_player_info["room_id"] = target_room_id
        await update_player_room_location(
            connection_manager,
            str(admin_player_info["player_id"]),
            original_room_id,
            target_room_id,
            persistence,
        )

    # Broadcast visual effects
    await broadcast_teleport_effects(
        connection_manager,
        player_name,
        original_room_id,
        target_room_id,
        "goto",
        direction=None,
        arrival_direction=None,
        target_player_id=str(admin_player_info.get("player_id")) if admin_player_info else None,
    )

    # Notify target player
    await notify_player_of_teleport(
        connection_manager,
        target_player_name,
        player_name,
        "teleported_to",
        message=f"{player_name} appears at your location.",
    )

    # Log the successful goto action
    admin_logger = get_admin_actions_logger()
    admin_logger.log_teleport_action(
        admin_name=player_name,
        target_player=target_player_name,
        action_type="goto",
        from_room=original_room_id,
        to_room=target_room_id,
        success=True,
        additional_data={
            "admin_room_id": current_player.current_room_id,
            "target_room_id": target_player.current_room_id,
        },
    )

    logger.info(
        "Goto executed successfully",
        player_name=player_name,
        target_player_name=target_player_name,
        target_room_id=target_room_id,
    )
    return {"result": f"You teleport to {target_player_name}'s location."}


def log_goto_failure(
    player_name: str, target_player_name: str, current_player: Any, target_player: Any, error: Exception
) -> None:
    """Log failed goto action."""
    admin_logger = get_admin_actions_logger()
    try:
        admin_logger.log_teleport_action(
            admin_name=player_name,
            target_player=target_player_name,
            action_type="goto",
            from_room=current_player.current_room_id,
            to_room=target_player.current_room_id,
            success=False,
            error_message=str(error),
            additional_data={
                "admin_room_id": current_player.current_room_id,
                "target_room_id": target_player.current_room_id,
            },
        )
    except (OSError, AttributeError, TypeError):
        pass  # Ignore logging errors if command itself failed

    logger.error(
        "Goto execution failed", admin_name=player_name, target_player_name=target_player_name, error=str(error)
    )


async def validate_confirm_goto_context(
    app: Any, player_service: Any, player_name: str
) -> tuple[Any | None, dict[str, str] | None]:
    """Validate app context and get current player with admin permissions. Returns (current_player, error_result)."""
    if not app:
        logger.warning("Confirm goto command failed - no app context", player_name=player_name)
        return None, {"result": "Goto functionality is not available."}

    if not player_service:
        logger.warning("Confirm goto command failed - no player service", player_name=player_name)
        return None, {"result": "Player service not available."}

    current_player = await player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning("Confirm goto command failed - current player not found", player_name=player_name)
        return None, {"result": "Player not found."}

    from .admin_permission_utils import validate_admin_permission

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return None, {"result": "You do not have permission to use goto commands."}

    return current_player, None


async def resolve_target_player_for_goto(
    target_player_name: str, connection_manager: Any, player_service: Any
) -> tuple[dict[str, Any] | None, Any | None, dict[str, str] | None]:
    """Resolve target player (online check and database lookup). Returns (target_player_info, target_player, error_result)."""
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return None, None, {"result": f"Player '{target_player_name}' is not online or not found."}

    target_player = await player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(
            "Confirm goto command failed - target player not found in database", target_player_name=target_player_name
        )
        return None, None, {"result": f"Player '{target_player_name}' not found in database."}

    return target_player_info, target_player, None


async def execute_confirm_goto(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Goto helpers require many parameters for context and goto execution
    player_name: str,
    current_player: Any,
    target_player_name: str,
    target_player: Any,
    player_service: Any,
    connection_manager: Any,
    persistence: Any | None = None,
) -> dict[str, str]:
    """Execute the goto teleportation (update location, room occupancy via EventBus, effects, logging)."""
    original_room_id = current_player.current_room_id
    target_room_id = target_player.current_room_id

    success = await player_service.update_player_location(player_name, target_room_id)
    if not success:
        logger.error("Failed to update admin player location", player_name=player_name)
        return {"result": f"Failed to teleport to {target_player_name}: database update failed."}

    admin_player_info = connection_manager.get_online_player_by_display_name(player_name)
    if admin_player_info:
        admin_player_info["room_id"] = target_room_id
        await update_player_room_location(
            connection_manager,
            str(admin_player_info["player_id"]),
            original_room_id,
            target_room_id,
            persistence,
        )

    await broadcast_teleport_effects(
        connection_manager,
        player_name,
        original_room_id,
        target_room_id,
        "goto",
        direction=None,
        arrival_direction=None,
        target_player_id=str(admin_player_info.get("player_id")) if admin_player_info else None,
    )

    admin_logger = get_admin_actions_logger()
    admin_logger.log_teleport_action(
        admin_name=player_name,
        target_player=target_player_name,
        action_type="goto",
        from_room=original_room_id,
        to_room=target_room_id,
        success=True,
        additional_data={
            "admin_room_id": current_player.current_room_id,
            "target_room_id": target_player.current_room_id,
        },
    )

    logger.info(
        "Goto executed successfully",
        player_name=player_name,
        target_player_name=target_player_name,
        target_room_id=target_room_id,
    )
    return {"result": f"You have successfully teleported to {target_player_name}'s location."}
