"""
Admin mute command handlers for MythosMUD.

This module provides handlers for mute/unmute administrative commands.
"""

# pylint: disable=too-many-return-statements  # Reason: Command handlers require multiple return statements for early validation returns (input validation, permission checks, error handling)

# pylint: disable=too-many-locals,too-many-return-statements  # Reason: Command handlers require many intermediate variables for complex game logic and multiple return statements for early validation returns

from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


def _mute_command_app(request: Any) -> Any | None:
    """Return FastAPI app from request, or None when request/app is missing."""
    return request.app if request else None


def _extract_mute_target(command_data: dict[str, Any]) -> str | None:
    """Extract target player name from validated command payload."""
    return command_data.get("target_player") or command_data.get("target_name")


def _parse_mute_duration_minutes(duration_minutes: Any) -> int | None:
    """Parse optional duration; None means permanent mute."""
    return int(duration_minutes) if duration_minutes else None


def _mute_duration_display(duration: int | None) -> str:
    """Human-readable duration suffix for mute success messages."""
    return f"for {duration} minutes" if duration else "permanently"


async def _resolve_muter_and_target_players(
    player_service: Any | None,
    player_name: str,
    target_player: str,
) -> tuple[str | None, Any | None, dict[str, str] | None]:
    """Resolve muter and target; return error dict when lookup fails."""
    if not player_service:
        return None, None, {"result": "Player service not available."}

    current_player_obj = await player_service.resolve_player_name(player_name)
    if not current_player_obj:
        return None, None, {"result": "Current player not found."}

    target_player_obj = await player_service.resolve_player_name(target_player)
    if not target_player_obj:
        return None, None, {"result": f"Player '{target_player}' not found."}

    return str(current_player_obj.id), target_player_obj, None


def _mute_success_result(target_player: str, duration: int | None, admin_name: str) -> dict[str, str]:
    """Build success response after mute_player returns True."""
    duration_text = _mute_duration_display(duration)
    logger.info(
        "Player muted successfully",
        admin_name=admin_name,
        target_player=target_player,
        duration_text=duration_text,
    )
    return {"result": f"You have muted {target_player} {duration_text}."}


async def _perform_mute(
    user_manager: Any,
    player_service: Any | None,
    player_name: str,
    target_player: str,
    duration: int | None,
) -> dict[str, str]:
    """Resolve players and invoke user_manager.mute_player."""
    muter_id, target_player_obj, resolve_error = await _resolve_muter_and_target_players(
        player_service, player_name, target_player
    )
    if resolve_error or muter_id is None or target_player_obj is None:
        return resolve_error or {"result": "Player resolution failed."}

    success = user_manager.mute_player(
        muter_id=muter_id,
        muter_name=player_name,
        target_id=target_player_obj.id,
        target_name=target_player,
        duration_minutes=duration,
        reason="",
    )
    if success:
        return _mute_success_result(target_player, duration, player_name)

    logger.warning("Mute command failed", admin_name=player_name, target_player=target_player)
    return {"result": f"Failed to mute {target_player}."}


async def handle_mute_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
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
    _ = current_user  # Intentionally unused - part of standard command handler interface
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    logger.debug("Processing mute command", player_name=player_name, command_data=command_data)

    app = _mute_command_app(request)
    user_manager = app.state.user_manager if app else None
    if not user_manager:
        logger.warning("Mute command failed - no user manager", player_name=player_name)
        return {"result": "Mute functionality is not available."}

    target_player = _extract_mute_target(command_data)
    if not target_player:
        logger.warning("Mute command with no target player", player_name=player_name, command_data=command_data)
        return {"result": "Usage: mute <player_name> [duration_in_minutes]"}

    duration = _parse_mute_duration_minutes(command_data.get("duration_minutes"))
    player_service = app.state.player_service if app else None

    try:
        return await _perform_mute(user_manager, player_service, player_name, target_player, duration)
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError) as e:
        logger.error("Mute command error", admin_name=player_name, target_player=target_player, error=str(e))
        return {"result": f"Error muting {target_player}: {str(e)}"}


async def handle_unmute_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
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
    _ = current_user  # Intentionally unused - part of standard command handler interface
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
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

        # Idempotent: tests and players often run `unmute` to clear stale state when no mute row exists.
        if not user_manager.is_player_muted(current_user_id, target_player_obj.id):
            logger.debug(
                "Unmute no-op; target was not muted",
                admin_name=player_name,
                target_player=target_player,
            )
            return {"result": f"You have unmuted {target_player}."}

        logger.warning("Unmute command failed", admin_name=player_name, target_player=target_player)
        return {"result": f"Failed to unmute {target_player}."}
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError) as e:
        logger.error("Unmute command error", admin_name=player_name, target_player=target_player, error=str(e))
        return {"result": f"Error unmuting {target_player}: {str(e)}"}


async def handle_mute_global_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
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
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    # Extract args from command_data
    _ = command_data.get("args", [])

    logger.debug("Processing mute_global command", player_name=player_name)

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

        logger.warning("Global mute command failed", player_name=player_name)
        return {"result": "Failed to activate global mute."}
    except (ValueError, TypeError, AttributeError, KeyError) as e:
        logger.error("Global mute command error", player_name=player_name, error=str(e))
        return {"result": f"Error activating global mute: {str(e)}"}


async def handle_unmute_global_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
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
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    # Extract args from command_data
    _ = command_data.get("args", [])

    logger.debug("Processing unmute_global command", player_name=player_name)

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

        logger.warning("Global unmute command failed", player_name=player_name)
        return {"result": "Failed to deactivate global mute."}
    except (ValueError, TypeError, AttributeError, KeyError) as e:
        logger.error("Global unmute command error", player_name=player_name, error=str(e))
        return {"result": f"Error deactivating global mute: {str(e)}"}


async def handle_add_admin_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
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
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    # Extract args from command_data while supporting legacy and new validation payloads
    args: list[Any] = command_data.get("args", [])
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

        logger.warning("Add admin command failed", admin_name=player_name, target_player=target_player)
        return {"result": f"Failed to grant administrator privileges to {target_player}."}
    except (ValueError, TypeError, AttributeError, KeyError, DatabaseError, SQLAlchemyError) as e:
        logger.error("Add admin command error", admin_name=player_name, target_player=target_player, error=str(e))
        return {"result": f"Error granting administrator privileges: {str(e)}"}


def _mute_display_target(category_name: str, target_id_or_channel: Any, mute_info: dict[str, Any]) -> str:
    """Format mute target label for display based on category."""
    if category_name == "channel_mutes":
        return f"#{mute_info.get('channel', target_id_or_channel)}"
    return str(mute_info.get("target_name", target_id_or_channel))


def _format_mute_line(category_name: str, target_id_or_channel: Any, mute_info: dict[str, Any]) -> str:
    """Format a single mute entry with expiration info."""
    target_display = _mute_display_target(category_name, target_id_or_channel, mute_info)
    expires_at = mute_info.get("expires_at")
    if expires_at:
        return f"{target_display} (expires: {expires_at})"
    return f"{target_display} (permanent)"


def _collect_mute_display_lines(mutes: dict[str, Any]) -> list[str]:
    """Collect formatted mute lines from player, channel, and global categories."""
    mute_list: list[str] = []
    for category_name, category_dict in mutes.items():
        if not category_dict:
            continue
        for target_id_or_channel, mute_info in category_dict.items():
            mute_list.append(_format_mute_line(category_name, target_id_or_channel, mute_info))
    return mute_list


async def _resolve_current_player_id_for_mutes(
    player_service: Any | None,
    player_name: str,
) -> tuple[Any | None, dict[str, str] | None]:
    """Resolve current player ID; return error dict when lookup fails."""
    if not player_service:
        return None, {"result": "Player service not available."}

    current_player_obj = await player_service.resolve_player_name(player_name)
    if not current_player_obj:
        return None, {"result": "Current player not found."}

    return current_player_obj.id, None


def _mutes_list_result(mute_list: list[str], player_name: str) -> dict[str, str]:
    """Build mutes command response from formatted lines."""
    if mute_list:
        result = "Current mutes:\n" + "\n".join(mute_list)
        logger.debug("Mutes listed successfully", player_name=player_name, count=len(mute_list))
        return {"result": result}

    logger.debug("No mutes found", player_name=player_name)
    return {"result": "No active mutes found."}


async def _perform_mutes_list(
    user_manager: Any,
    player_service: Any | None,
    player_name: str,
) -> dict[str, str]:
    """Resolve player and format their active mutes."""
    current_player_id, resolve_error = await _resolve_current_player_id_for_mutes(player_service, player_name)
    if resolve_error or current_player_id is None:
        return resolve_error or {"result": "Player resolution failed."}

    mutes = user_manager.get_player_mutes(current_player_id)
    mute_list = _collect_mute_display_lines(mutes)
    return _mutes_list_result(mute_list, player_name)


async def handle_mutes_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
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
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    # Extract args from command_data
    _ = command_data.get("args", [])

    logger.debug("Processing mutes command", player_name=player_name)

    app = _mute_command_app(request)
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Mutes command failed - no user manager", player_name=player_name)
        return {"result": "Mute information is not available."}

    try:
        player_service = app.state.player_service if app else None
        return await _perform_mutes_list(user_manager, player_service, player_name)
    except (ValueError, TypeError, AttributeError, KeyError) as e:
        logger.error("Mutes command error", player_name=player_name, error=str(e))
        return {"result": f"Error retrieving mute information: {str(e)}"}


__all__ = [
    "handle_mute_command",
    "handle_unmute_command",
    "handle_mute_global_command",
    "handle_unmute_global_command",
    "handle_add_admin_command",
    "handle_mutes_command",
]
