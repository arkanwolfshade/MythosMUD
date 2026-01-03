"""
Admin teleport command handlers for MythosMUD.

This module provides handlers for teleport and goto administrative commands.
"""

from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..realtime.websocket_handler import broadcast_room_update
from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger
from .admin_permission_utils import validate_admin_permission
from .admin_teleport_utils import (
    broadcast_teleport_effects,
    get_online_player_by_display_name,
    notify_player_of_teleport,
)

logger = get_logger(__name__)

# Direction opposites for teleport arrival messages
DIRECTION_OPPOSITES: dict[str, str] = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
    "up": "down",
    "down": "up",
    "northeast": "southwest",
    "southwest": "northeast",
    "northwest": "southeast",
    "southeast": "northwest",
}


async def handle_teleport_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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
        if not app:
            logger.warning("Teleport command failed - no app context", player_name=player_name)
            return {"result": "Teleport functionality is not available."}

        player_service = app.state.player_service if app else None
        if not player_service:
            logger.warning("Teleport command failed - no player service", player_name=player_name)
            return {"result": "Player service not available."}

        connection_manager = app.state.connection_manager if app else None
        if not connection_manager:
            logger.warning("Teleport command failed - no connection manager", player_name=player_name)
            return {"result": "Connection manager not available."}

        persistence = getattr(app.state, "persistence", None)

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

        if direction_value and not persistence:
            logger.warning(
                "Teleport command failed - direction specified but persistence unavailable", player_name=player_name
            )
            return {"result": "World data is not available for directional teleportation."}

        target_room_id = current_player.current_room_id
        target_room_name = None
        if direction_value:
            admin_room = persistence.get_room_by_id(current_player.current_room_id) if persistence else None
            if not admin_room:
                logger.warning(
                    "Teleport command failed - admin room not found",
                    player_name=player_name,
                    room_id=current_player.current_room_id,
                )
                return {"result": "Unable to determine your current location."}

            exits = getattr(admin_room, "exits", {}) or {}
            target_room_id = exits.get(direction_value)
            if not target_room_id:
                logger.warning(
                    "Teleport command failed - invalid direction",
                    player_name=player_name,
                    direction=direction_value,
                    room_id=current_player.current_room_id,
                )
                return {"result": f"There is no exit to the {direction_value} from here."}

            if persistence:
                target_room = persistence.get_room_by_id(target_room_id)
                if target_room and hasattr(target_room, "name"):
                    target_room_name = target_room.name

        target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
        if not target_player_info:
            return {"result": f"Player '{target_player_name}' is not online or not found."}

        target_player = await player_service.get_player_by_name(target_player_name)
        if not target_player:
            logger.warning(
                "Teleport command failed - target player not found in database", target_player_name=target_player_name
            )
            return {"result": f"Player '{target_player_name}' not found in database."}

        if not direction_value and target_player.current_room_id == current_player.current_room_id:
            return {"result": f"{target_player_name} is already in your location."}

        try:
            original_room_id = target_player.current_room_id
            success = await player_service.update_player_location(target_player_name, target_room_id)
            if not success:
                logger.error("Failed to update target player location", target_player_name=target_player_name)
                return {"result": f"Failed to teleport {target_player_name}: database update failed."}

            target_player.current_room_id = target_room_id

            target_player_identifier = (
                target_player_info.get("player_id")
                or getattr(target_player, "player_id", None)
                or getattr(target_player, "id", None)
            )
            if target_player_identifier is not None:
                target_player_identifier = str(target_player_identifier)
                target_player_info["current_room_id"] = target_room_id

                online_record = connection_manager.online_players.get(target_player_identifier)
                if online_record is not None:
                    online_record["current_room_id"] = target_room_id

                try:
                    connection_manager.room_manager.remove_room_occupant(target_player_identifier, original_room_id)
                except (ValueError, TypeError, AttributeError, KeyError) as exc:
                    logger.debug(
                        "Failed to remove teleport target from prior room occupants",
                        player_id=target_player_identifier,
                        room_id=original_room_id,
                        error=str(exc),
                    )

                try:
                    connection_manager.room_manager.add_room_occupant(target_player_identifier, target_room_id)
                except (ValueError, TypeError, AttributeError, KeyError) as exc:
                    logger.debug(
                        "Failed to add teleport target to destination room occupants",
                        player_id=target_player_identifier,
                        room_id=target_room_id,
                        error=str(exc),
                    )

                try:
                    connection_manager.room_manager.reconcile_room_presence(
                        original_room_id, connection_manager.online_players
                    )
                    connection_manager.room_manager.reconcile_room_presence(
                        target_room_id, connection_manager.online_players
                    )
                except (ValueError, TypeError, AttributeError, KeyError) as exc:
                    logger.debug(
                        "Failed to reconcile room presence after teleport",
                        player_id=target_player_identifier,
                        error=str(exc),
                    )

                if persistence:
                    try:
                        source_room = persistence.get_room_by_id(original_room_id)
                        if source_room:
                            source_room.player_left(target_player_identifier)
                    except (ValueError, AttributeError, TypeError) as exc:
                        logger.debug(
                            "Failed to mark teleport target as leaving source room",
                            player_id=target_player_identifier,
                            room_id=original_room_id,
                            error=str(exc),
                        )

                    try:
                        destination_room = persistence.get_room_by_id(target_room_id)
                        if destination_room:
                            destination_room.player_entered(target_player_identifier)
                    except (ValueError, AttributeError, TypeError) as exc:
                        logger.debug(
                            "Failed to mark teleport target as entering destination room",
                            player_id=target_player_identifier,
                            room_id=target_room_id,
                            error=str(exc),
                        )

            # broadcast_room_update expects player_id as string
            await broadcast_room_update(str(target_player_info["player_id"]), target_room_id)

            current_player_identifier = getattr(current_player, "player_id", getattr(current_player, "id", None))
            if current_player_identifier:
                await broadcast_room_update(str(current_player_identifier), current_player.current_room_id)

            arrival_direction = DIRECTION_OPPOSITES.get(direction_value) if direction_value else None
            await broadcast_teleport_effects(
                connection_manager,
                target_player_name,
                original_room_id,
                target_room_id,
                "teleport",
                direction=direction_value,
                arrival_direction=arrival_direction,
                target_player_id=str(target_player_info.get("player_id")) if target_player_info else None,
            )

            if direction_value:
                admin_message = f"You teleport {target_player_name} to the {direction_value}."
                target_message = f"You are teleported to the {direction_value} by {player_name}."
            else:
                admin_message = f"You teleport {target_player_name} to your location."
                destination_name = target_room_name or f"{player_name}'s location"
                target_message = f"You are teleported to {destination_name}."

            await notify_player_of_teleport(
                connection_manager, target_player_name, player_name, "teleported_to", message=target_message
            )

            admin_logger = get_admin_actions_logger()
            admin_logger.log_teleport_action(
                admin_name=player_name,
                target_player=target_player_name,
                action_type="teleport",
                from_room=original_room_id,
                to_room=target_room_id,
                success=True,
                additional_data={
                    "admin_room_id": current_player.current_room_id,
                    "target_room_id": target_room_id,
                    "direction": direction_value,
                },
            )

            logger.info(
                "Teleport executed successfully",
                admin_name=player_name,
                target_player=target_player_name,
                direction=direction_value,
                destination_room=target_room_id,
            )
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
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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
    if not app:
        logger.warning("Goto command failed - no app context", player_name=player_name)
        return {"result": "Goto functionality is not available."}

    # Get player service
    player_service = app.state.player_service if app else None
    if not player_service:
        logger.warning("Goto command failed - no player service", player_name=player_name)
        return {"result": "Player service not available."}

    # Get current player and validate admin permissions
    current_player = await player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning("Goto command failed - current player not found", player_name=player_name)
        return {"result": "Player not found."}

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return {"result": "You do not have permission to use goto commands."}

    # Extract target player from command data
    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: goto <player_name>"}

    # Get connection manager
    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning("Goto command failed - no connection manager", player_name=player_name)
        return {"result": "Connection manager not available."}

    # Find target player online
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return {"result": f"Player '{target_player_name}' is not online or not found."}

    # Get target player object
    target_player = await player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(
            "Goto command failed - target player not found in database", target_player_name=target_player_name
        )
        return {"result": f"Player '{target_player_name}' not found in database."}

    # Check if admin is already in the same room
    if current_player.current_room_id == target_player.current_room_id:
        return {"result": f"You are already in the same location as {target_player_name}."}

    # Execute goto immediately without confirmation
    try:
        # Store original location for visual effects
        original_room_id = current_player.current_room_id
        target_room_id = target_player.current_room_id

        # Update admin player's location using PlayerService
        success = await player_service.update_player_location(player_name, target_room_id)
        if not success:
            logger.error("Failed to update admin player location", player_name=player_name)
            return {"result": f"Failed to teleport to {target_player_name}: database update failed."}

        # Update connection manager's online player info for admin
        admin_player_info = connection_manager.get_online_player_by_display_name(player_name)
        if admin_player_info:
            admin_player_info["room_id"] = target_room_id

        # Broadcast room update to the admin player
        # broadcast_room_update expects player_id as string
        await broadcast_room_update(str(admin_player_info["player_id"]), target_room_id)

        target_player_identifier = getattr(target_player, "player_id", getattr(target_player, "id", None))
        if target_player_identifier:
            await broadcast_room_update(str(target_player_identifier), target_room_id)

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

    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        # Log the failed goto action
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


async def handle_confirm_teleport_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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
    if not app:
        logger.warning("Confirm teleport command failed - no app context", player_name=player_name)
        return {"result": "Teleport functionality is not available."}

    # Get player service
    player_service = app.state.player_service if app else None
    if not player_service:
        logger.warning("Confirm teleport command failed - no player service", player_name=player_name)
        return {"result": "Player service not available."}

    # Get current player and validate admin permissions
    current_player = await player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning("Confirm teleport command failed - current player not found", player_name=player_name)
        return {"result": "Player not found."}

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return {"result": "You do not have permission to use teleport commands."}

    # Extract target player from command data
    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: confirm teleport <player_name>"}

    # Get connection manager
    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning("Confirm teleport command failed - no connection manager", player_name=player_name)
        return {"result": "Connection manager not available."}

    # Find target player online
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return {"result": f"Player '{target_player_name}' is not online or not found."}

    # Get target player object
    target_player = await player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(
            "Confirm teleport command failed - target player not found in database",
            target_player_name=target_player_name,
        )
        return {"result": f"Player '{target_player_name}' not found in database."}

    # Check if target is already in the same room
    if target_player.current_room_id == current_player.current_room_id:
        return {"result": f"{target_player_name} is already in your location."}

    try:
        # Store original location for visual effects
        original_room_id = target_player.current_room_id
        target_room_id = current_player.current_room_id

        # Update target player's location using PlayerService
        success = await player_service.update_player_location(target_player_name, target_room_id)
        if not success:
            logger.error("Failed to update target player location", target_player_name=target_player_name)
            return {"result": f"Failed to teleport {target_player_name}: database update failed."}

        # Update connection manager's online player info
        if target_player_info:
            target_player_info["room_id"] = target_room_id

        # Broadcast room update to the teleported player
        # broadcast_room_update expects player_id as string
        await broadcast_room_update(str(target_player_info["player_id"]), target_room_id)

        # Broadcast visual effects
        await broadcast_teleport_effects(
            connection_manager,
            target_player_name,
            original_room_id,
            target_room_id,
            "teleport",
            direction=None,
            arrival_direction=None,
            target_player_id=str(target_player_info.get("player_id")) if target_player_info else None,
        )

        await notify_player_of_teleport(
            connection_manager,
            target_player_name,
            player_name,
            "teleported_to",
            message=f"You are teleported to {player_name}'s location.",
        )

        # Log the successful teleport action
        admin_logger = get_admin_actions_logger()
        admin_logger.log_teleport_action(
            admin_name=player_name,
            target_player=target_player_name,
            action_type="teleport",
            from_room=original_room_id,
            to_room=target_room_id,
            success=True,
            additional_data={
                "admin_room_id": current_player.current_room_id,
                "target_room_id": target_player.current_room_id,
            },
        )

        logger.info(
            "Teleport executed successfully",
            player_name=player_name,
            target_player_name=target_player_name,
            target_room_id=target_room_id,
        )
        return {"result": f"You have successfully teleported {target_player_name} to your location."}

    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        # Log the failed teleport action
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
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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
    if not app:
        logger.warning("Confirm goto command failed - no app context", player_name=player_name)
        return {"result": "Goto functionality is not available."}

    # Get player service
    player_service = app.state.player_service if app else None
    if not player_service:
        logger.warning("Confirm goto command failed - no player service", player_name=player_name)
        return {"result": "Player service not available."}

    # Get current player and validate admin permissions
    current_player = await player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning("Confirm goto command failed - current player not found", player_name=player_name)
        return {"result": "Player not found."}

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return {"result": "You do not have permission to use goto commands."}

    # Extract target player from command data
    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: confirm goto <player_name>"}

    # Get connection manager
    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning("Confirm goto command failed - no connection manager", player_name=player_name)
        return {"result": "Connection manager not available."}

    # Find target player online
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return {"result": f"Player '{target_player_name}' is not online or not found."}

    # Get target player object
    target_player = await player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(
            "Confirm goto command failed - target player not found in database", target_player_name=target_player_name
        )
        return {"result": f"Player '{target_player_name}' not found in database."}

    # Check if admin is already in the same room
    if current_player.current_room_id == target_player.current_room_id:
        return {"result": f"You are already in the same location as {target_player_name}."}

    try:
        # Store original location for visual effects
        original_room_id = current_player.current_room_id
        target_room_id = target_player.current_room_id

        # Update admin player's location using PlayerService
        success = await player_service.update_player_location(player_name, target_room_id)
        if not success:
            logger.error("Failed to update admin player location", player_name=player_name)
            return {"result": f"Failed to teleport to {target_player_name}: database update failed."}

        # Update connection manager's online player info for admin
        admin_player_info = connection_manager.get_online_player_by_display_name(player_name)
        if admin_player_info:
            admin_player_info["room_id"] = target_room_id

        # Broadcast room update to the admin player
        # broadcast_room_update expects player_id as string
        await broadcast_room_update(str(admin_player_info["player_id"]), target_room_id)

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
        return {"result": f"You have successfully teleported to {target_player_name}'s location."}

    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError, KeyError) as e:
        # Log the failed goto action
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
