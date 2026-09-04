"""Validation and permission checking helpers for chat service."""

from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("communications.chat_service")


def validate_say_message(message: str) -> dict[str, Any] | None:
    """Validate say message content. Returns error dict if invalid, None if valid."""
    if not message or not message.strip():
        logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
        return {"success": False, "error": "Message cannot be empty"}

    if len(message.strip()) > 500:
        logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
        return {"success": False, "error": "Message too long (max 500 characters)"}

    return None


def validate_emote_action(action: str) -> dict[str, Any] | None:
    """Validate emote action content. Returns error dict if invalid, None if valid."""
    if not action or not action.strip():
        logger.debug("=== CHAT SERVICE DEBUG: Empty action ===")
        return {"success": False, "error": "Action cannot be empty"}

    if len(action.strip()) > 200:
        logger.debug("=== CHAT SERVICE DEBUG: Action too long ===")
        return {"success": False, "error": "Action too long (max 200 characters)"}

    return None


def validate_global_message(message: str) -> dict[str, Any] | None:
    """Validate global message content. Returns error dict if invalid, None if valid."""
    if not message or not message.strip():
        logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
        return {"success": False, "error": "Message cannot be empty"}

    if len(message.strip()) > 1000:
        logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
        return {"success": False, "error": "Message too long (max 1000 characters)"}

    return None


def check_global_level_requirement(player: Any, player_id: str) -> dict[str, Any] | None:
    """Check if player meets level requirement for global chat. Returns error dict if not, None if valid."""
    if player.level < 1:
        logger.debug(
            "=== CHAT SERVICE DEBUG: Player level too low ===",
            player_id=player_id,
            level=player.level,
        )
        return {"success": False, "error": "You must be level 1 or higher to use global chat"}
    return None


def check_channel_permissions(user_manager: Any, player_id: str, channel: str) -> dict[str, Any] | None:
    """Check if player can send messages in a channel. Returns error dict if blocked, None if allowed."""
    if user_manager.is_channel_muted(player_id, channel):
        logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===")
        return {"success": False, "error": f"You are muted in the {channel} channel"}

    if user_manager.is_globally_muted(player_id):
        logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===")
        return {"success": False, "error": "You are globally muted and cannot send messages"}

    if not user_manager.can_send_message(player_id, channel=channel):
        logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===")
        return {"success": False, "error": "You cannot send messages at this time"}

    return None


def check_say_permissions(user_manager: Any, player_id: str) -> dict[str, Any] | None:
    """Check if player can send say messages. Returns error dict if blocked, None if allowed."""
    return check_channel_permissions(user_manager, player_id, "say")
