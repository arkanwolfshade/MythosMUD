"""
Logout and quit command handlers for MythosMUD.

This module contains handlers for quit and logout commands.
"""

import inspect
import uuid
from datetime import UTC, datetime
from typing import Any, cast

from fastapi import Request

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..persistence.protocols import PlayerRepositoryProtocol
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from ..utils.player_cache import cache_player, get_cached_player
from .rest_command import check_player_in_combat

logger = get_logger(__name__)

QUIT_COMBAT_BLOCKED_MESSAGE = "You cannot quit during combat. End combat first."
LOGOUT_COMBAT_BLOCKED_MESSAGE = "You cannot logout during combat. End combat first."


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


def _coerce_player_uuid(player_id: object) -> uuid.UUID:
    """Normalize player_id to uuid.UUID.

    Production Player.player_id is a UUID string (as_uuid=False). Tests and some
    mocks pass a uuid.UUID instance; uuid.UUID() only accepts str/bytes.
    """
    if isinstance(player_id, uuid.UUID):
        return player_id
    if isinstance(player_id, str):
        return uuid.UUID(player_id)
    raise TypeError(f"player_id must be UUID or str, got {type(player_id).__name__}")


def _is_coroutine_object(value: object) -> bool:
    """True when value is an awaitable coroutine (not a Player)."""
    return inspect.iscoroutine(value)


async def _get_player_for_logout(
    request: Request, persistence: PlayerRepositoryProtocol | None, lookup_name: str
) -> Player | None:
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
            fetched: object = await persistence.get_player_by_name(lookup_name)
            if _is_coroutine_object(fetched):
                logger.error("get_player_by_name returned a coroutine instead of player", lookup_name=lookup_name)
                return None
            player = cast(Player | None, fetched)
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


def _get_app_services(request: Any) -> tuple[Any | None, Any | None]:
    app = request.app if request else None
    if not app:
        return None, None
    if hasattr(app.state, "container") and app.state.container:
        return app.state.container.async_persistence, app.state.container.connection_manager
    return getattr(app.state, "persistence", None), getattr(app.state, "connection_manager", None)


async def _resolve_disconnect_player_id(connection_manager: Any, player_name: str) -> uuid.UUID | None:
    persistence = getattr(connection_manager, "async_persistence", None)
    if persistence:
        player = await persistence.get_player_by_name(player_name)
        if player:
            return uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id
    player_info = connection_manager.get_online_player_by_display_name(player_name)
    if not player_info:
        return None
    player_id_str = player_info.get("player_id")
    if not player_id_str:
        return None
    return uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str


async def _force_disconnect_player(connection_manager: Any, player_name: str, *, mark_intentional: bool) -> None:
    player_id = await _resolve_disconnect_player_id(connection_manager, player_name)
    if not player_id:
        logger.warning("Could not resolve player_id for disconnect", player_name=player_name)
        return
    if mark_intentional:
        connection_manager.intentional_disconnects.add(player_id)
    await connection_manager.force_disconnect_player(player_id)


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
        await _force_disconnect_player(connection_manager, player_name, mark_intentional=mark_intentional)
        logger.info("Player disconnected from all connections", intentional=mark_intentional, player_name=player_name)
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: WebSocketDisconnect/ClientDisconnected on already-closed sockets must not break logout
        logger.error("Error disconnecting player", error=str(e), error_type=type(e).__name__)


async def _is_player_in_combat_for_logout(request: Request | None, player: Player | None) -> bool:
    """Check whether `player` is currently in combat, for the quit/logout combat guards.

    Without this guard, `quit`/`logout` mark the disconnect intentional and skip the
    disconnect-grace zombie window (`disconnect_grace_period.py`) entirely -- a clean,
    instant escape from a fight that `rest` already blocks via the same underlying check
    (`rest_command.check_player_in_combat`). `#297`.
    """
    if not request or not player:
        return False
    app = getattr(request, "app", None)
    if not app:
        return False
    player_id = _coerce_player_uuid(player.player_id)
    return await check_player_in_combat(player_id, app)


async def _mark_quit_intentional(request: Any, username: str) -> None:
    app = request.app if request else None
    if not app:
        return
    connection_manager = getattr(app.state, "connection_manager", None)
    persistence = getattr(app.state, "persistence", None)
    if not connection_manager or not persistence:
        return
    try:
        player = await persistence.get_player_by_name(username)
        if not player:
            return
        player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id
        connection_manager.intentional_disconnects.add(player_id)
    except (AttributeError, ValueError, TypeError) as e:
        logger.debug("Could not mark quit as intentional", error=str(e))


async def handle_quit_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Request,
    _alias_storage: AliasStorage | None,
    _player_name: str,
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
    _args: list[Any] = command_data.get("args", [])

    logger.debug("Processing quit command")
    username = get_username_from_user(current_user)
    persistence, _ = _get_app_services(request)
    player = None
    if persistence:
        try:
            player = await persistence.get_player_by_name(username)
            if player:
                player.last_active = datetime.now(UTC)
                await persistence.save_player(player)
        except (OSError, ValueError, TypeError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error updating last active on quit", error=str(e), error_type=type(e).__name__)

    if await _is_player_in_combat_for_logout(request, player):
        logger.info("Quit blocked - player in combat")
        return {"result": QUIT_COMBAT_BLOCKED_MESSAGE}

    if request:
        await _mark_quit_intentional(request, username)

    logger.info("Player quitting")
    return {"result": "Goodbye! You have been disconnected from the game."}


async def _prepare_player_for_logout(
    request: Any,
    persistence: Any,
    connection_manager: Any,
    lookup_name: str,
    player_name: str,
) -> None:
    player = await _get_player_for_logout(request, persistence, lookup_name)
    if not player:
        return
    position_value = _get_player_position_from_connection_manager(connection_manager, player, player_name)
    _sync_player_position(player, position_value)
    await _update_and_save_player_last_active(persistence, player)
    if connection_manager:
        player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id
        connection_manager.intentional_disconnects.add(player_id)


async def handle_logout_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Request,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Handle the logout command for cleanly disconnecting from the game.

    This command performs a complete logout process including:
    - Updating player's last active timestamp
    - Cleaning up server-side session data
    - Disconnecting all connections
    - Returning success confirmation

    :param command_data: Command data dictionary containing args and other info.
    :param current_user: Current user information.
    :param request: FastAPI request object.
    :param _alias_storage: Alias storage instance (unused, for signature compatibility).
    :param player_name: Player name for logging.
    :return: Logout command result with success status and metadata.
    """
    # Extract args from command_data (not used in this command)
    _args: list[Any] = command_data.get("args", [])

    logger.debug("Processing logout command")

    try:
        persistence, connection_manager = _get_app_services(request)
        lookup_name = player_name or get_username_from_user(current_user)

        player = await _get_player_for_logout(request, persistence, lookup_name)
        if await _is_player_in_combat_for_logout(request, player):
            logger.info("Logout blocked - player in combat")
            return {"result": LOGOUT_COMBAT_BLOCKED_MESSAGE}

        await _prepare_player_for_logout(request, persistence, connection_manager, lookup_name, player_name)
        await _disconnect_player_connections(connection_manager, player_name, mark_intentional=True)
        logger.info("Player logged out successfully")
        return {
            "result": "Logged out successfully",
            "session_terminated": True,
            "connections_closed": True,
            "message": "You have been logged out and disconnected from the game.",
        }

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Unexpected error during logout", error=str(e), error_type=type(e).__name__, exc_info=True)

        # Even if there's an error, we should still indicate logout success
        # The client will handle the cleanup
        return {
            "result": "Logged out successfully",
            "session_terminated": True,
            "connections_closed": True,
            "message": "You have been logged out from the game.",
        }
