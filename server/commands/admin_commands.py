"""
Administrative commands for MythosMUD.

This module contains handlers for administrative commands including:
- Mute/unmute functionality
- Admin management
- Teleport and goto functionality with proper validation and security
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging.admin_actions_logger import get_admin_actions_logger
from ..logging.enhanced_logging_config import get_logger
from ..realtime.envelope import build_event
from ..realtime.websocket_handler import broadcast_room_update
from ..time.time_service import get_mythos_chronicle
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)

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


# --- Admin Command Routing ---


async def handle_admin_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Entry point for general admin commands that expose subcommands like `admin status`.
    """
    subcommand = (command_data.get("subcommand") or "").lower()

    if subcommand == "status":
        return await _handle_admin_status_command(command_data, current_user, request, alias_storage, player_name)
    if subcommand == "time":
        return await _handle_admin_time_command(command_data, current_user, request, alias_storage, player_name)

    logger.warning("Unknown admin subcommand requested", player_name=player_name, subcommand=subcommand)
    return {"result": f"Unknown admin subcommand '{subcommand}'."}


async def _handle_admin_status_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Provide contextual status information about the caller's administrative privileges.
    """
    app = request.app if request else None
    if not app:
        logger.warning("Admin status command failed - no application context", player_name=player_name)
        return {"result": "Admin status information is not available."}

    player_service = getattr(app.state, "player_service", None)
    user_manager = getattr(app.state, "user_manager", None)

    if not player_service:
        logger.warning("Admin status command failed - no player service", player_name=player_name)
        return {"result": "Admin status information is not available."}

    try:
        player_record = await player_service.resolve_player_name(player_name)
    except Exception as exc:
        logger.error(
            "Admin status command failed while resolving player name",
            player_name=player_name,
            error=str(exc),
            error_type=type(exc).__name__,
        )
        return {"result": f"Unable to resolve player '{player_name}': {str(exc)}"}

    if not player_record:
        logger.warning("Admin status command failed - player record not found", player_name=player_name)
        return {"result": f"Player '{player_name}' not found."}

    # Determine identifiers for downstream checks
    player_identifier = getattr(player_record, "id", None)
    if player_identifier is None:
        player_identifier = getattr(player_record, "player_id", None)

    is_admin_database = bool(getattr(player_record, "is_admin", False))
    is_admin_runtime: bool | None = None

    if user_manager and player_identifier is not None:
        try:
            is_admin_runtime = user_manager.is_admin(player_identifier)
        except Exception as exc:
            logger.error(
                "Admin status cache lookup failed",
                player_name=player_name,
                # Structlog handles UUID objects automatically, no need to convert to string
                player_identifier=player_identifier,
                error=str(exc),
                error_type=type(exc).__name__,
            )
            is_admin_runtime = None

    is_admin_effective = bool(is_admin_database or (is_admin_runtime is True))

    header = f"ADMIN STATUS FOR {player_record.name.upper()}"
    privilege_line = f"Admin privileges: {'Active' if is_admin_effective else 'Inactive'}"
    database_line = f"- Database record: {'Active' if is_admin_database else 'Inactive'}"
    runtime_line = (
        f"- Session cache: {'Active' if is_admin_runtime else 'Inactive'}"
        if is_admin_runtime is not None
        else "- Session cache: Unavailable"
    )

    if is_admin_effective:
        guidance_lines = [
            "You currently have access to administrative utilities such as teleportation, moderation, and system management commands.",
            "Remember to log critical actions using the appropriate audit-approved procedures.",
        ]
    else:
        guidance_lines = [
            "You do not currently have administrative privileges.",
            "If you believe this is an error, contact a senior archivist for review.",
        ]

    message_lines = [header, "", privilege_line, database_line, runtime_line, ""]
    message_lines.extend(guidance_lines)
    result_text = "\n".join(message_lines)

    try:
        admin_logger = get_admin_actions_logger()
        admin_logger.log_admin_command(
            admin_name=player_name,
            command="admin status",
            success=True,
            additional_data={
                "is_admin_effective": is_admin_effective,
                "is_admin_database": is_admin_database,
                "is_admin_runtime": is_admin_runtime,
            },
        )
    except Exception as exc:
        logger.warning(
            "Failed to log admin status command",
            player_name=player_name,
            error=str(exc),
            error_type=type(exc).__name__,
        )

    return {"result": result_text}


async def _handle_admin_time_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """Expose current Mythos time metadata, active holidays, and freeze diagnostics."""

    app = request.app if request else None
    chronicle = get_mythos_chronicle()
    mythos_dt = chronicle.get_current_mythos_datetime()
    components = chronicle.get_calendar_components(mythos_dt)

    holiday_service = getattr(app.state, "holiday_service", None) if app and hasattr(app, "state") else None
    active_holidays: list[str] = []
    upcoming: list[str] = []
    if holiday_service:
        try:
            holiday_service.refresh_active(mythos_dt)
            active_holidays = holiday_service.get_active_holiday_names()
            upcoming = holiday_service.get_upcoming_summary()
        except Exception as exc:
            logger.warning("Admin time command failed to refresh holiday state", error=str(exc))

    last_freeze = chronicle.get_last_freeze_state()
    if last_freeze:
        freeze_line = (
            f"Last freeze: {last_freeze.real_timestamp.isoformat()} (Mythos {last_freeze.mythos_timestamp.isoformat()})"
        )
    else:
        freeze_line = "Last freeze: no recorded freeze events"

    active_text = ", ".join(active_holidays) if active_holidays else "None active"
    upcoming_lines = upcoming or ["No upcoming holidays recorded"]

    lines = [
        "MYTHOS TEMPORAL STATUS",
        "",
        f"Current Mythos time: {mythos_dt.strftime('%Y-%m-%d %H:%M')} ({components.daypart}, {components.season})",
        f"Week {components.week_of_month} of {components.month_name}, day {components.day_of_week + 1} ({components.day_name})",
        f"Active holidays: {active_text}",
        "Next triggers:",
    ]
    lines.extend([f"- {entry}" for entry in upcoming_lines])
    lines.append(freeze_line)

    return {"result": "\n".join(lines)}


# --- Admin Permission Validation ---


async def validate_admin_permission(player, player_name: str) -> bool:
    """
    Validate that a player has admin permissions.

    Args:
        player: Player object to check
        player_name: Player name for logging

    Returns:
        bool: True if player has admin permissions, False otherwise
    """
    try:
        if not player:
            logger.warning("Admin permission check failed - no player object", player_name=player_name)

            # Log the failed permission check
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data={"error": "No player object"},
            )
            return False

        # Check if player has admin privileges
        if not hasattr(player, "is_admin") or not player.is_admin:
            # Determine the specific reason for failure
            if not hasattr(player, "is_admin"):
                error_msg = "No is_admin attribute"
                logger.warning(
                    "Admin permission check failed - player has no is_admin attribute", player_name=player_name
                )
                additional_data = {"error": error_msg, "player_type": type(player).__name__}
            else:
                error_msg = f"is_admin value: {player.is_admin}"
                logger.info("Admin permission denied", player_name=player_name, error_msg=error_msg)
                additional_data = {"player_type": type(player).__name__, "is_admin_value": player.is_admin}

            # Log the failed permission check
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data=additional_data,
            )
            return False

        # Log the successful permission check
        admin_logger = get_admin_actions_logger()
        admin_logger.log_permission_check(
            player_name=player_name,
            action="admin_teleport",
            has_permission=True,
            additional_data={"player_type": type(player).__name__, "is_admin_value": player.is_admin},
        )

        logger.info("Admin permission granted", player_name=player_name, is_admin_value=player.is_admin)
        return True

    except Exception as e:
        logger.error("Error checking admin permissions", player_name=player_name, error=str(e))

        # Log the failed permission check
        try:
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data={"error": str(e), "player_type": type(player).__name__ if player else "None"},
            )
        except Exception as log_error:
            logger.error("Failed to log permission check error", error=str(log_error))

        return False


# --- Teleport Utility Functions ---


async def get_online_player_by_display_name(display_name: str, connection_manager) -> dict | None:
    """
    Get online player information by display name.

    Args:
        display_name: Display name to search for
        connection_manager: Connection manager instance

    Returns:
        dict: Player information if found, None otherwise
    """
    if not connection_manager:
        logger.warning("Connection manager not available for online player lookup")
        return None

    return connection_manager.get_online_player_by_display_name(display_name)


def create_teleport_effect_message(
    player_name: str,
    effect_type: str,
    *,
    teleport_type: str,
    direction: str | None = None,
    arrival_direction: str | None = None,
) -> str:
    """
    Create teleport effect message for visual display.

    Args:
        player_name: Name of the player being teleported
        effect_type: Type of effect ('arrival' or 'departure')
        teleport_type: Type of teleport ('teleport' or 'goto')
        direction: Optional direction text for departure messages
        arrival_direction: Optional direction text for arrival messages

    Returns:
        str: Formatted teleport effect message
    """
    if teleport_type == "teleport":
        if effect_type == "departure":
            if direction:
                return f"{player_name} leaves the room heading {direction}."
            return f"{player_name} disappears in a ripple of distorted air."
        if effect_type == "arrival":
            if arrival_direction:
                return f"{player_name} arrives from the {arrival_direction}."
            return f"{player_name} arrives in a shimmer of eldritch energy."
    elif teleport_type == "goto":
        if effect_type == "departure":
            return f"{player_name} vanishes in a flash of pale light."
        if effect_type == "arrival":
            if arrival_direction:
                return f"{player_name} arrives from the {arrival_direction}."
            return f"{player_name} appears beside you in a rush of displaced air."

    return f"{player_name} is affected by mysterious forces."


async def broadcast_teleport_effects(
    connection_manager,
    player_name: str,
    from_room_id: str,
    to_room_id: str,
    teleport_type: str,
    *,
    direction: str | None = None,
    arrival_direction: str | None = None,
    target_player_id: str | None = None,
) -> None:
    """
    Broadcast teleport visual effects to players in affected rooms.

    Args:
        connection_manager: Connection manager instance
        player_name: Name of the player being teleported
        from_room_id: Room ID the player is leaving
        to_room_id: Room ID the player is arriving at
        teleport_type: Type of teleport ('teleport' or 'goto')
        direction: Optional direction for departure messaging
        arrival_direction: Optional reverse direction for arrival messaging
    """
    try:
        departure_message = create_teleport_effect_message(
            player_name,
            "departure",
            teleport_type=teleport_type,
            direction=direction,
            arrival_direction=arrival_direction,
        )

        arrival_message = create_teleport_effect_message(
            player_name,
            "arrival",
            teleport_type=teleport_type,
            direction=direction,
            arrival_direction=arrival_direction,
        )

        if hasattr(connection_manager, "broadcast_to_room"):
            departure_event = build_event(
                "system",
                {"message": departure_message, "message_type": "info"},
                room_id=from_room_id,
                connection_manager=connection_manager,
            )
            arrival_event = build_event(
                "system",
                {"message": arrival_message, "message_type": "info"},
                room_id=to_room_id,
                connection_manager=connection_manager,
            )
            await connection_manager.broadcast_to_room(
                from_room_id, departure_event, exclude_player=str(target_player_id) if target_player_id else None
            )
            await connection_manager.broadcast_to_room(
                to_room_id, arrival_event, exclude_player=str(target_player_id) if target_player_id else None
            )

        logger.debug(
            "Teleport effects broadcast", player_name=player_name, from_room_id=from_room_id, to_room_id=to_room_id
        )

    except Exception as e:
        logger.error("Failed to broadcast teleport effects", player_name=player_name, error=str(e))


async def notify_player_of_teleport(
    connection_manager,
    target_player_name: str,
    admin_name: str,
    notification_type: str,
    *,
    message: str | None = None,
) -> None:
    """
    Notify a player that they are being teleported by an admin.

    Args:
        connection_manager: Connection manager instance
        target_player_name: Name of the player being teleported
        admin_name: Name of the admin performing the teleport
        notification_type: Type of notification ('teleported_to' or 'teleported_from')
        message: Optional preformatted message to deliver
    """
    try:
        if message is None:
            if notification_type == "teleported_to":
                message = f"You have been teleported to {admin_name}'s location by an administrator."
            else:
                message = f"You have been teleported away from {admin_name} by an administrator."

        target_player_info = connection_manager.get_online_player_by_display_name(target_player_name)
        if target_player_info:
            player_id = target_player_info.get("player_id")
            if player_id and hasattr(connection_manager, "send_personal_message"):
                event = build_event(
                    "system",
                    {"message": message, "message_type": "info"},
                    player_id=str(player_id),
                    connection_manager=connection_manager,
                )
                await connection_manager.send_personal_message(player_id, event)

        logger.debug("Teleport notification sent", target_player_name=target_player_name, admin_name=admin_name)

    except Exception as e:
        logger.error("Failed to notify player of teleport", target_player_name=target_player_name, error=str(e))


# --- Mute Command Handlers ---


async def handle_mute_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the mute command for muting other players.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Mute command result
    """
    logger.debug("Processing mute command", player_name=player_name, command_data=command_data)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Mute command failed - no user manager", player_name=player_name)
        return {"result": "Mute functionality is not available."}

    # Extract target player and duration from command_data
    # For now, the target player might be in different fields - let's check
    target_player = command_data.get("target_player") or command_data.get("target_name")
    duration_minutes = command_data.get("duration_minutes")

    if not target_player:
        # If target player is not in command_data, this is a validation issue
        logger.warning("Mute command with no target player", player_name=player_name, command_data=command_data)
        return {"result": "Usage: mute <player_name> [duration_in_minutes]"}

    duration = int(duration_minutes) if duration_minutes else None  # None means permanent

    try:
        # Get player service from app state
        player_service = app.state.player_service if app else None
        if not player_service:
            return {"result": "Player service not available."}

        # Get current player's actual player object and ID
        current_player_obj = await player_service.resolve_player_name(player_name)
        if not current_player_obj:
            return {"result": "Current player not found."}
        current_user_id = str(current_player_obj.id)

        # Resolve target player name to Player object
        target_player_obj = await player_service.resolve_player_name(target_player)
        if not target_player_obj:
            return {"result": f"Player '{target_player}' not found."}

        success = user_manager.mute_player(
            muter_id=current_user_id,
            muter_name=player_name,
            target_id=target_player_obj.id,
            target_name=target_player,
            duration_minutes=duration,
            reason="",
        )
        if success:
            duration_text = f"for {duration} minutes" if duration else "permanently"
            logger.info(
                "Player muted successfully",
                admin_name=player_name,
                target_player=target_player,
                duration_text=duration_text,
            )
            return {"result": f"You have muted {target_player} {duration_text}."}
        else:
            logger.warning("Mute command failed", admin_name=player_name, target_player=target_player)
            return {"result": f"Failed to mute {target_player}."}
    except Exception as e:
        logger.error("Mute command error", admin_name=player_name, target_player=target_player, error=str(e))
        return {"result": f"Error muting {target_player}: {str(e)}"}


async def handle_unmute_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the unmute command for unmuting other players.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Unmute command result
    """
    logger.debug("Processing unmute command", player_name=player_name, command_data=command_data)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Unmute command failed - no user manager", player_name=player_name)
        return {"result": "Unmute functionality is not available."}

    # Extract target player from command_data
    target_player = command_data.get("target_player")

    if not target_player:
        # If target player is not in command_data, this is a validation issue
        logger.warning("Unmute command with no target player", player_name=player_name, command_data=command_data)
        return {"result": "Usage: unmute <player_name>"}

    try:
        # Get player service from app state
        player_service = app.state.player_service if app else None
        if not player_service:
            return {"result": "Player service not available."}

        # Get current player's actual player object and ID
        current_player_obj = await player_service.resolve_player_name(player_name)
        if not current_player_obj:
            return {"result": "Current player not found."}
        current_user_id = str(current_player_obj.id)

        # Resolve target player name to Player object
        target_player_obj = await player_service.resolve_player_name(target_player)
        if not target_player_obj:
            return {"result": f"Player '{target_player}' not found."}

        success = user_manager.unmute_player(
            unmuter_id=current_user_id,
            unmuter_name=player_name,
            target_id=target_player_obj.id,
            target_name=target_player,
        )
        if success:
            logger.info("Player unmuted successfully", admin_name=player_name, target_player=target_player)
            return {"result": f"You have unmuted {target_player}."}
        else:
            logger.warning("Unmute command failed", admin_name=player_name, target_player=target_player)
            return {"result": f"Failed to unmute {target_player}."}
    except Exception as e:
        logger.error("Unmute command error", admin_name=player_name, target_player=target_player, error=str(e))
        return {"result": f"Error unmuting {target_player}: {str(e)}"}


async def handle_mute_global_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the mute_global command for global muting.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Mute global command result
    """
    # Extract args from command_data
    args: list = command_data.get("args", [])

    logger.debug("Processing mute_global command", player_name=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Mute global command failed - no user manager", player_name=player_name)
        return {"result": "Global mute functionality is not available."}

    try:
        success = user_manager.mute_global(get_username_from_user(current_user))
        if success:
            logger.info("Global mute activated", admin_name=player_name)
            return {"result": "Global mute has been activated."}
        else:
            logger.warning("Global mute command failed", player_name=player_name)
            return {"result": "Failed to activate global mute."}
    except Exception as e:
        logger.error("Global mute command error", player_name=player_name, error=str(e))
        return {"result": f"Error activating global mute: {str(e)}"}


async def handle_unmute_global_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the unmute_global command for removing global mute.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Unmute global command result
    """
    # Extract args from command_data
    args: list = command_data.get("args", [])

    logger.debug("Processing unmute_global command", player_name=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Unmute global command failed - no user manager", player_name=player_name)
        return {"result": "Global unmute functionality is not available."}

    try:
        success = user_manager.unmute_global(get_username_from_user(current_user))
        if success:
            logger.info("Global mute deactivated", admin_name=player_name)
            return {"result": "Global mute has been deactivated."}
        else:
            logger.warning("Global unmute command failed", player_name=player_name)
            return {"result": "Failed to deactivate global mute."}
    except Exception as e:
        logger.error("Global unmute command error", player_name=player_name, error=str(e))
        return {"result": f"Error deactivating global mute: {str(e)}"}


async def handle_add_admin_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the add_admin command for adding administrators.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Add admin command result
    """
    # Extract args from command_data while supporting legacy and new validation payloads
    args: list = command_data.get("args", [])
    target_player = command_data.get("target_player")
    if not target_player and args:
        target_player = args[0]

    logger.debug("Processing add_admin command", player_name=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Add admin command failed - no user manager", player_name=player_name)
        return {"result": "Admin management is not available."}

    if not target_player:
        logger.warning("Add admin command with insufficient arguments", player_name=player_name, args=args)
        return {"result": "Usage: add_admin <player_name>"}

    try:
        success = user_manager.add_admin(target_player, get_username_from_user(current_user))
        if success:
            logger.info("Admin added successfully", admin_name=player_name, target_player=target_player)
            return {"result": f"{target_player} has been granted administrator privileges."}
        else:
            logger.warning("Add admin command failed", admin_name=player_name, target_player=target_player)
            return {"result": f"Failed to grant administrator privileges to {target_player}."}
    except Exception as e:
        logger.error("Add admin command error", admin_name=player_name, target_player=target_player, error=str(e))
        return {"result": f"Error granting administrator privileges: {str(e)}"}


async def handle_mutes_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the mutes command for listing current mutes.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Mutes command result
    """
    # Extract args from command_data
    args: list = command_data.get("args", [])

    logger.debug("Processing mutes command", player_name=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Mutes command failed - no user manager", player_name=player_name)
        return {"result": "Mute information is not available."}

    try:
        mutes = user_manager.get_player_mutes(get_username_from_user(current_user))
        if mutes:
            mute_list = []
            for mute in mutes:
                if mute.get("expires_at"):
                    mute_list.append(f"{mute['target_player']} (expires: {mute['expires_at']})")
                else:
                    mute_list.append(f"{mute['target_player']} (permanent)")

            result = "Current mutes:\n" + "\n".join(mute_list)
            logger.debug("Mutes listed successfully", player_name=player_name, count=len(mutes))
            return {"result": result}
        else:
            logger.debug("No mutes found", player_name=player_name)
            return {"result": "No active mutes found."}
    except Exception as e:
        logger.error("Mutes command error", player_name=player_name, error=str(e))
        return {"result": f"Error retrieving mute information: {str(e)}"}


# --- Teleport Command Handlers ---


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
            admin_room = persistence.get_room(current_player.current_room_id) if persistence else None
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
                target_room = persistence.get_room(target_room_id)
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
                except Exception as exc:
                    logger.debug(
                        "Failed to remove teleport target from prior room occupants",
                        player_id=target_player_identifier,
                        room_id=original_room_id,
                        error=str(exc),
                    )

                try:
                    connection_manager.room_manager.add_room_occupant(target_player_identifier, target_room_id)
                except Exception as exc:
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
                except Exception as exc:
                    logger.debug(
                        "Failed to reconcile room presence after teleport",
                        player_id=target_player_identifier,
                        error=str(exc),
                    )

                if persistence:
                    try:
                        source_room = persistence.get_room(original_room_id)
                        if source_room:
                            source_room.player_left(target_player_identifier)
                    except Exception as exc:
                        logger.debug(
                            "Failed to mark teleport target as leaving source room",
                            player_id=target_player_identifier,
                            room_id=original_room_id,
                            error=str(exc),
                        )

                    try:
                        destination_room = persistence.get_room(target_room_id)
                        if destination_room:
                            destination_room.player_entered(target_player_identifier)
                    except Exception as exc:
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

        except Exception as e:
            admin_logger = get_admin_actions_logger()
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

            logger.error(
                "Teleport execution failed", admin_name=player_name, target_player_name=target_player_name, error=str(e)
            )
            return {"result": f"Failed to teleport {target_player_name}: {str(e)}"}
    except Exception as e:
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
            f"Goto executed successfully - {player_name} teleported to {target_player_name} at {target_room_id}"
        )
        return {"result": f"You teleport to {target_player_name}'s location."}

    except Exception as e:
        # Log the failed goto action
        admin_logger = get_admin_actions_logger()
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
            f"Teleport executed successfully - {player_name} teleported {target_player_name} to {target_room_id}"
        )
        return {"result": f"You have successfully teleported {target_player_name} to your location."}

    except Exception as e:
        # Log the failed teleport action
        admin_logger = get_admin_actions_logger()
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
            f"Goto executed successfully - {player_name} teleported to {target_player_name} at {target_room_id}"
        )
        return {"result": f"You have successfully teleported to {target_player_name}'s location."}

    except Exception as e:
        # Log the failed goto action
        admin_logger = get_admin_actions_logger()
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

        logger.error(
            "Goto execution failed", admin_name=player_name, target_player_name=target_player_name, error=str(e)
        )
        return {"result": f"Failed to teleport to {target_player_name}: {str(e)}"}
