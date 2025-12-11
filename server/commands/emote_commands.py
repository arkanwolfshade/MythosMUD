"""
Emote command handlers for MythosMUD.

This module contains handlers for the emote command.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _extract_emote_action(command_data: dict) -> str | None:
    """
    Extract action from command_data.

    Args:
        command_data: Command data dictionary

    Returns:
        Action string or None if not found
    """
    action = command_data.get("action")
    if action:
        return action

    parsed_command = command_data.get("parsed_command")
    if parsed_command is not None and hasattr(parsed_command, "action"):
        return parsed_command.action

    return None


def _get_emote_services(request: Any) -> tuple[Any, Any]:
    """
    Get chat service and player service from app state.

    Args:
        request: FastAPI request object

    Returns:
        Tuple of (chat_service, player_service) or (None, None) if not available
    """
    app = request.app if request else None
    state = getattr(app, "state", None) if app else None
    chat_service = getattr(state, "chat_service", None) if state else None
    player_service = getattr(state, "player_service", None) if state else None
    return chat_service, player_service


async def _validate_player_for_emote(
    player_service: Any, player_name: str
) -> tuple[Any | None, str | None, str | None, str | None]:
    """
    Validate player and extract required information for emote.

    Args:
        player_service: Player service instance
        player_name: Player name

    Returns:
        Tuple of (player_obj, current_room_id, player_id, error_message)
        If validation fails, error_message will contain the error, otherwise None
    """
    player_obj = await player_service.resolve_player_name(player_name)
    if not player_obj:
        return None, None, None, "Player not found."

    current_room_id = getattr(player_obj, "current_room_id", None)
    if not current_room_id:
        return None, None, None, "You are not in a room."

    player_id = getattr(player_obj, "id", None) or getattr(player_obj, "player_id", None)
    if not player_id:
        return None, None, None, "Player ID not found."

    return player_obj, current_room_id, player_id, None


def _format_emote_messages(action: str, player_name: str) -> tuple[str, str]:
    """
    Format emote messages for predefined or custom emotes.

    Args:
        action: Emote action string
        player_name: Player name

    Returns:
        Tuple of (self_message, formatted_action)
    """
    from ..game.emote_service import EmoteService

    emote_service = EmoteService()

    if emote_service.is_emote_alias(action):
        # Predefined emote - format messages
        self_message, _ = emote_service.format_emote_messages(action, player_name)
        _, formatted_action = emote_service.format_emote_messages(action, player_name)
        # Remove player name prefix if present
        if formatted_action.startswith(f"{player_name} "):
            formatted_action = formatted_action[len(f"{player_name} ") :]
        return self_message, formatted_action

    # Custom emote - use the action as provided
    logger.debug("Custom emote executed")
    self_message = f"{player_name} {action}"
    return self_message, action


def _handle_emote_result(
    result: dict, self_message: str, player_name: str, current_room_id: str | None
) -> dict[str, str]:
    """
    Handle the result from chat service after sending emote.

    Args:
        result: Result dictionary from chat service
        self_message: Self message string
        player_name: Player name for logging
        current_room_id: Current room ID for logging (can be None)

    Returns:
        Result dictionary with success or error message
    """
    if result.get("success"):
        logger.info(
            "Emote message sent successfully",
            player_name=player_name,
            room=current_room_id,
            message_id=result.get("message", {}).get("id"),
        )
        return {"result": self_message}

    error_msg = result.get("error", "Unknown error")
    logger.warning("Emote command failed", player=player_name, error=error_msg)
    return {"result": f"Error sending emote: {error_msg}"}


async def handle_emote_command(
    command_data: dict, _current_user: dict, request: Any, _alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the emote command for performing emotes.

    Args:
        command_data: Command data dictionary containing validated command information
        _current_user: Current user information (unused, player_name is used instead)
        request: FastAPI request object
        _alias_storage: Alias storage instance (unused, required by command handler interface)
        player_name: Player name for logging

    Returns:
        dict: Emote command result
    """
    logger.debug("Processing emote command", player=player_name)

    action = _extract_emote_action(command_data)
    if not action:
        logger.warning("Emote command with no action", player=player_name)
        return {"result": "Emote what? Usage: emote <action>"}

    logger.debug("Player performing emote", player=player_name)

    chat_service, player_service = _get_emote_services(request)
    if not chat_service or not player_service:
        logger.warning("Chat service or player service not available for emote command", player=player_name)
        return {"result": "Emote functionality is not available."}

    try:
        _, current_room_id, player_id, error_message = await _validate_player_for_emote(player_service, player_name)
        if error_message:
            return {"result": error_message}

        self_message, formatted_action = _format_emote_messages(action, player_name)

        result = await chat_service.send_emote_message(player_id, formatted_action)
        return _handle_emote_result(result, self_message, player_name, current_room_id)

    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        import traceback

        logger.error(
            "Emote command error", player=player_name, action=action, error=str(e), traceback=traceback.format_exc()
        )
        return {"result": f"Error sending emote: {str(e)}"}
