"""
Logout and quit command handlers for MythosMUD.

This module contains handlers for quit and logout commands.
"""

import inspect
import uuid
from datetime import UTC, datetime
from typing import Any

from ..alias_storage import AliasStorage
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from ..utils.player_cache import cache_player, get_cached_player

logger = get_logger(__name__)


def _clear_corrupted_cache_entry(request: Any, lookup_name: str) -> None:
    """
    Clear a corrupted cache entry if it exists.

    Args:
        request: FastAPI request object
        lookup_name: Player name to clear from cache
    """
    if not request or not hasattr(request, "state"):
        return

    cache = getattr(request.state, "_command_player_cache", None)
    if isinstance(cache, dict):
        cache.pop(lookup_name, None)


async def _get_player_for_logout(request: Any, persistence: Any, lookup_name: str) -> Any:
    """
    Get player for logout, handling cache corruption and persistence fallback.

    Args:
        request: FastAPI request object
        persistence: Persistence layer instance
        lookup_name: Player name to look up

    Returns:
        Player object or None if not found
    """
    player = get_cached_player(request, lookup_name)

    # Ensure player is not a coroutine (defensive check)
    if player is not None and inspect.iscoroutine(player):
        logger.warning("Cached player is a coroutine, clearing cache and fetching fresh", lookup_name=lookup_name)
        _clear_corrupted_cache_entry(request, lookup_name)
        player = None

    if persistence and player is None:
        try:
            player = await persistence.get_player_by_name(lookup_name)
            # Double-check we're not caching a coroutine
            if inspect.iscoroutine(player):
                logger.error("get_player_by_name returned a coroutine instead of player", lookup_name=lookup_name)
                return None
            cache_player(request, lookup_name, player)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Player fetch errors unpredictable, must return None
            logger.error("Error fetching player for logout", error=str(e), error_type=type(e).__name__)
            return None

    return player


def _get_player_position_from_connection_manager(connection_manager: Any, player: Any, player_name: str) -> str | None:
    """
    Get player's current position from connection manager.

    Args:
        connection_manager: Connection manager instance
        player: Player object
        player_name: Player display name

    Returns:
        Position value or None if not found
    """
    if not connection_manager:
        return None

    player_identifier = getattr(player, "player_id", None)
    player_info = None

    if player_identifier:
        player_info = connection_manager.online_players.get(str(player_identifier))

    if not player_info:
        player_info = connection_manager.get_online_player_by_display_name(player_name)

    return player_info.get("position") if player_info else None


def _sync_player_position(player: Any, position_value: str | None) -> None:
    """
    Synchronize player's position from connection manager to player stats.

    Args:
        player: Player object
        position_value: Position value to sync (can be None)
    """
    if not position_value:
        return

    stats = player.get_stats()
    if stats.get("position") != position_value:
        stats["position"] = position_value
        player.set_stats(stats)


async def _update_and_save_player_last_active(persistence: Any, player: Any) -> None:
    """
    Update and save player's last active timestamp.

    Args:
        persistence: Persistence layer instance
        player: Player object
    """
    if not persistence:
        return

    player.last_active = datetime.now(UTC)
    await persistence.save_player(player)
    logger.info("Player logout - updated last active")


async def _disconnect_player_connections(
    connection_manager: Any, player_name: str, mark_intentional: bool = True
) -> None:
    """
    Disconnect player from all connections.

    Args:
        connection_manager: Connection manager instance
        player_name: Player name to disconnect
        mark_intentional: If True, mark disconnect as intentional (no grace period)
    """
    if not connection_manager:
        logger.warning("Connection manager not available for logout")
        return

    try:
        # Get player ID to mark as intentional disconnect and to call force_disconnect_player
        persistence = getattr(connection_manager, "async_persistence", None)
        player_id = None
        if persistence:
            player = await persistence.get_player_by_name(player_name)
            if player:
                player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id
                # Mark as intentional disconnect (no grace period)
                if mark_intentional:
                    connection_manager.intentional_disconnects.add(player_id)
                    logger.debug("Marked disconnect as intentional", player_id=player_id, player_name=player_name)

        if player_id:
            await connection_manager.force_disconnect_player(player_id)
        else:
            # Fallback: try to get player_id from online_players
            player_info = connection_manager.get_online_player_by_display_name(player_name)
            if player_info:
                player_id_str = player_info.get("player_id")
                if player_id_str:
                    player_id = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
                    if mark_intentional:
                        connection_manager.intentional_disconnects.add(player_id)
                    await connection_manager.force_disconnect_player(player_id)
                else:
                    logger.warning("Could not resolve player_id for disconnect", player_name=player_name)
            else:
                logger.warning("Player not found online for disconnect", player_name=player_name)

        logger.info("Player disconnected from all connections", intentional=mark_intentional, player_name=player_name)
    except (AttributeError, RuntimeError, ValueError, TypeError) as e:
        logger.error("Error disconnecting player", error=str(e), error_type=type(e).__name__)


async def handle_quit_command(
    command_data: dict, current_user: dict, request: Any, _alias_storage: AliasStorage | None, _player_name: str
) -> dict[str, str]:
    """
    Handle the quit command for disconnecting from the game.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Quit command result
    """
    # Extract args from command_data (not used in this command)
    _args: list = command_data.get("args", [])

    logger.debug("Processing quit command")

    # Update last active timestamp before quitting
    app = request.app if request else None
    # Prefer container, fallback to app.state for backward compatibility
    persistence = None
    if app and hasattr(app.state, "container") and app.state.container:
        persistence = app.state.container.async_persistence
    elif app:
        persistence = getattr(app.state, "persistence", None)

    if persistence:
        try:
            player = await persistence.get_player_by_name(get_username_from_user(current_user))
            if player:
                player.last_active = datetime.now(UTC)
                await persistence.save_player(player)
                logger.info("Player quit - updated last active")
        except (OSError, ValueError, TypeError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Exception catch-all for last active update errors, must handle gracefully
            logger.error("Error updating last active on quit", error=str(e), error_type=type(e).__name__)

    # Mark disconnect as intentional (no grace period) for /quit command
    app = request.app if request else None
    if app:
        connection_manager = getattr(app.state, "connection_manager", None)
        persistence = getattr(app.state, "persistence", None)
        if connection_manager and persistence:
            try:
                player = await persistence.get_player_by_name(get_username_from_user(current_user))
                if player:
                    player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id
                    connection_manager.intentional_disconnects.add(player_id)
                    logger.debug("Marked quit as intentional disconnect", player_id=player_id)
            except (AttributeError, ValueError, TypeError) as e:
                logger.debug("Could not mark quit as intentional", error=str(e))

    logger.info("Player quitting")
    return {"result": "Goodbye! You have been disconnected from the game."}


async def handle_logout_command(
    command_data: dict, current_user: dict, request: Any, _alias_storage: AliasStorage | None, player_name: str
) -> dict[str, Any]:
    """
    Handle the logout command for cleanly disconnecting from the game.

    This command performs a complete logout process including:
    - Updating player's last active timestamp
    - Cleaning up server-side session data
    - Disconnecting all connections
    - Returning success confirmation

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Logout command result with success status and metadata
    """
    # Extract args from command_data (not used in this command)
    _args: list = command_data.get("args", [])

    logger.debug("Processing logout command")

    try:
        app = request.app if request else None
        # Prefer container, fallback to app.state for backward compatibility
        persistence = None
        if app and hasattr(app.state, "container") and app.state.container:
            persistence = app.state.container.async_persistence
        elif app:
            persistence = getattr(app.state, "persistence", None)
        # Prefer container, fallback to app.state for backward compatibility
        connection_manager = None
        if app and hasattr(app.state, "container") and app.state.container:
            connection_manager = app.state.container.connection_manager
        elif app:
            connection_manager = getattr(app.state, "connection_manager", None)

        lookup_name = player_name or get_username_from_user(current_user)
        player = await _get_player_for_logout(request, persistence, lookup_name)

        if player:
            position_value = _get_player_position_from_connection_manager(connection_manager, player, player_name)
            _sync_player_position(player, position_value)
            await _update_and_save_player_last_active(persistence, player)

            # Mark disconnect as intentional (no grace period)
            player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id
            if connection_manager:
                connection_manager.intentional_disconnects.add(player_id)
                logger.debug("Marked logout as intentional disconnect", player_id=player_id, player_name=player_name)

        await _disconnect_player_connections(connection_manager, player_name, mark_intentional=True)

        logger.info("Player logged out successfully")

        return {
            "result": "Logged out successfully",
            "session_terminated": True,
            "connections_closed": True,
            "message": "You have been logged out and disconnected from the game.",
        }

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Logout errors unpredictable, must handle gracefully
        logger.error("Unexpected error during logout", error=str(e), error_type=type(e).__name__, exc_info=True)

        # Even if there's an error, we should still indicate logout success
        # The client will handle the cleanup
        return {
            "result": "Logged out successfully",
            "session_terminated": True,
            "connections_closed": True,
            "message": "You have been logged out from the game.",
        }
