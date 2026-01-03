"""
Channel management commands for Advanced Chat Channels.

This module provides handlers for channel management commands like /channel.
"""

from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..database import get_async_session
from ..services.player_preferences_service import PlayerPreferencesService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)

VALID_CHANNELS = {"local", "global", "whisper", "system"}


async def handle_channel_command(
    command_data: dict, current_user: dict, request: Any, _alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the channel command for switching channels or setting default channel.

    Usage:
        /channel <channel_name> - Switch to channel (UI operation, but can set default)
        /channel default <channel_name> - Set default channel

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        _alias_storage: Alias storage instance (unused, required by command handler interface)
        player_name: Player name for logging

    Returns:
        dict: Channel command result
    """
    logger.debug("Processing channel command", player_name=player_name, command_data=command_data)

    app = getattr(request, "app", None)
    persistence = getattr(app.state, "persistence", None) if app else None
    if not persistence:
        logger.warning("Channel command failed - no persistence", player_name=player_name)
        return {"result": "Channel preferences are not available."}

    username = get_username_from_user(current_user)
    player = persistence.get_player_by_name(username)
    if not player:
        logger.warning("Channel command failed - player not found", player_name=player_name, username=username)
        return {"result": "Player not found."}

    # Extract channel from command_data
    channel = command_data.get("channel") or command_data.get("action")
    if not channel:
        return {"result": "Usage: /channel <channel_name> or /channel default <channel_name>"}

    channel = channel.lower().strip()

    # Handle "default" action
    if channel == "default":
        default_channel = command_data.get("action") or command_data.get("channel")
        if not default_channel:
            return {"result": "Usage: /channel default <channel_name>"}
        default_channel = default_channel.lower().strip()
        if default_channel not in VALID_CHANNELS:
            return {"result": f"Invalid channel. Valid channels: {', '.join(sorted(VALID_CHANNELS))}"}

        # Set default channel
        async for session in get_async_session():
            try:
                prefs_service = PlayerPreferencesService()
                result = await prefs_service.update_default_channel(session, player.player_id, default_channel)
                await session.commit()

                if result.get("success"):
                    logger.info("Default channel updated", player_name=player_name, channel=default_channel)
                    return {"result": f"Default channel set to {default_channel}."}
                else:
                    error = result.get("error", "Unknown error")
                    logger.warning("Failed to update default channel", player_name=player_name, error=error)
                    return {"result": f"Error setting default channel: {error}"}
            except SQLAlchemyError as e:
                await session.rollback()
                logger.error("Error updating default channel", player_name=player_name, error=str(e))
                return {"result": f"Error setting default channel: {str(e)}"}

        return {"result": "Error: Could not access database."}

    # Validate channel name
    if channel not in VALID_CHANNELS:
        return {"result": f"Invalid channel. Valid channels: {', '.join(sorted(VALID_CHANNELS))}"}

    # For now, just acknowledge the channel switch (UI handles the actual switching)
    # In the future, this could set the default channel as well
    logger.debug("Channel switch requested", player_name=player_name, channel=channel)
    return {"result": f"Switching to {channel} channel. (Use /channel default {channel} to set as default)"}


__all__ = [
    "handle_channel_command",
]
