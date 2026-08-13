"""
Delegation helpers for connection manager.

This module provides helper functions that delegate to specialized
components, reducing boilerplate in the main ConnectionManager class.
"""

import asyncio
import uuid
from collections.abc import Awaitable, Callable, Mapping
from typing import Protocol, cast

from fastapi import WebSocket

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from .connection_models import ConnectionMetadata
from .rate_limiter import RateLimiter

logger = get_logger(__name__)


class _PlayerIdCarrier(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Minimal player shape for token validation."""

    player_id: uuid.UUID


class _TokenPersistence(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Persistence surface used by validate_token_impl."""

    async def get_player_by_user_id(self, user_id: str) -> _PlayerIdCarrier | None:
        """Look up a player by auth user id."""


class _WebsocketCleanupManager(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """ConnectionManager surface used by cleanup_dead_websocket_impl."""

    active_websockets: dict[str, WebSocket]
    player_websockets: dict[uuid.UUID, list[str]]
    connection_metadata: dict[str, ConnectionMetadata]
    rate_limiter: RateLimiter


class _TokenValidateManager(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """ConnectionManager surface used by validate_token_impl."""

    async_persistence: object | None


def _async_callable(obj: object, method_name: str) -> Callable[..., Awaitable[object]]:
    return cast(Callable[..., Awaitable[object]], getattr(obj, method_name))


def _sync_callable(obj: object, method_name: str) -> Callable[..., object]:
    return cast(Callable[..., object], getattr(obj, method_name))


_BENIGN_CLOSE_ERROR_MARKERS = (
    "close message has been sent",
    "cannot call",
    "unexpected asgi message 'websocket.close'",
    "response already completed",
)


def _websocket_client_connected(websocket: WebSocket) -> bool:
    """Return True when ASGI client_state is CONNECTED; False if unknown."""
    try:
        client_state = cast(object, getattr(websocket, "client_state", None))
        state_name = cast(object | None, getattr(client_state, "name", None))
        return state_name == "CONNECTED"
    except (AttributeError, ValueError, TypeError):
        return False


def _is_benign_websocket_close_error(error_message: str) -> bool:
    """True for expected close races (already closed / ASGI close after complete)."""
    lowered = error_message.lower()
    return any(marker in lowered for marker in _BENIGN_CLOSE_ERROR_MARKERS)


async def _close_dead_websocket_if_open(
    websocket: WebSocket,
    connection_id: str,
    player_id: uuid.UUID,
) -> None:
    """Close an open dead WebSocket; skip or suppress expected close errors."""
    if not _websocket_client_connected(websocket):
        logger.debug(
            "WebSocket already closed, skipping close call",
            connection_id=connection_id,
            player_id=player_id,
        )
        return

    logger.info("Closing dead WebSocket", connection_id=connection_id, player_id=player_id)
    try:
        close_coro = cast(
            Awaitable[None],
            websocket.close(code=1000, reason="Connection cleaned up"),
        )
        await asyncio.wait_for(close_coro, timeout=2.0)
        logger.info("Successfully closed dead WebSocket", connection_id=connection_id, player_id=player_id)
    except (TimeoutError, RuntimeError, ConnectionError) as e:
        error_message = str(e)
        if _is_benign_websocket_close_error(error_message):
            return
        logger.warning(
            "Error closing dead WebSocket",
            connection_id=connection_id,
            player_id=player_id,
            error=error_message,
        )


def _remove_connection_from_player_list(
    manager: _WebsocketCleanupManager,
    player_id: uuid.UUID,
    connection_id: str,
) -> None:
    """Drop connection_id from player_websockets; delete empty player entries."""
    if player_id not in manager.player_websockets:
        return
    if connection_id not in manager.player_websockets[player_id]:
        return
    manager.player_websockets[player_id].remove(connection_id)
    if not manager.player_websockets[player_id]:
        del manager.player_websockets[player_id]


async def delegate_error_handler(
    error_handler: object | None,
    method_name: str,
    default_error: dict[str, object],
    *args: object,
    **kwargs: object,
) -> dict[str, object]:
    """
    Generic delegate for error handler methods.

    Args:
        error_handler: Error handler instance
        method_name: Name of method to call
        default_error: Default error response if handler not initialized
        *args: Positional arguments to pass
        **kwargs: Keyword arguments to pass

    Returns:
        dict: Error handling results
    """
    if error_handler is None:
        logger.error("Error handler not initialized")
        return default_error
    result = await _async_callable(error_handler, method_name)(*args, **kwargs)
    return cast(dict[str, object], result)


async def cleanup_dead_websocket_impl(
    player_id: uuid.UUID,
    connection_id: str,
    manager: _WebsocketCleanupManager,
) -> None:
    """
    Clean up a dead WebSocket connection.

    Args:
        player_id: The player's ID
        connection_id: The connection ID to clean up
        manager: ConnectionManager instance
    """
    try:
        if connection_id in manager.active_websockets:
            # Runtime may briefly hold None during cleanup; typed dict does not.
            websocket = cast(WebSocket | None, manager.active_websockets[connection_id])
            if websocket is None:
                del manager.active_websockets[connection_id]
                return

            # Close only while CONNECTED to avoid Unexpected ASGI websocket.close
            await _close_dead_websocket_if_open(websocket, connection_id, player_id)
            del manager.active_websockets[connection_id]

        _remove_connection_from_player_list(manager, player_id, connection_id)

        if connection_id in manager.connection_metadata:
            del manager.connection_metadata[connection_id]

        manager.rate_limiter.remove_connection_message_data(connection_id)

        logger.info("Cleaned up dead WebSocket connection", connection_id=connection_id, player_id=player_id)
    except (AttributeError, ValueError, TypeError) as e:
        logger.error("Error cleaning up dead WebSocket", connection_id=connection_id, player_id=player_id, error=str(e))


async def validate_token_impl(token: str, player_id: uuid.UUID, manager: _TokenValidateManager) -> bool:
    """
    Validate a JWT token for a connection.

    Args:
        token: JWT token to validate
        player_id: Player ID to verify token matches
        manager: ConnectionManager instance

    Returns:
        bool: True if token is valid, False otherwise
    """
    try:
        from ..auth_utils import decode_access_token

        payload = decode_access_token(token)
        if not payload or "sub" not in payload:
            logger.debug("Token validation failed: invalid payload", player_id=player_id)
            return False

        user_id = str(payload["sub"]).strip()
        persistence = cast(_TokenPersistence | None, manager.async_persistence)
        if not persistence:
            logger.warning("Cannot validate token: persistence not available", player_id=player_id)
            return False

        player = await persistence.get_player_by_user_id(user_id)
        if not player or str(player.player_id) != str(player_id):
            logger.warning(
                "Token validation failed: player mismatch",
                player_id=player_id,
                token_user_id=user_id,
            )
            return False

        return True
    except (DatabaseError, AttributeError) as e:
        logger.error("Error validating token", player_id=player_id, error=str(e), exc_info=True)
        return False


async def delegate_health_monitor(
    health_monitor: object | None,
    method_name: str,
    active_websockets: Mapping[str, WebSocket],
    connection_metadata: Mapping[str, object],
    player_websockets: Mapping[uuid.UUID, list[str]],
) -> None:
    """Generic delegate for health monitor methods."""
    if health_monitor is None:
        logger.error("Health monitor not initialized")
        return
    _ = await _async_callable(health_monitor, method_name)(
        active_websockets=active_websockets,
        connection_metadata=connection_metadata,
        player_websockets=player_websockets,
    )


def delegate_health_monitor_sync(
    health_monitor: object | None,
    method_name: str,
    active_websockets: Mapping[str, WebSocket],
    connection_metadata: Mapping[str, object],
    player_websockets: Mapping[uuid.UUID, list[str]],
) -> None:
    """Generic delegate for synchronous health monitor methods."""
    if health_monitor is None:
        logger.error("Health monitor not initialized")
        return
    _ = _sync_callable(health_monitor, method_name)(
        active_websockets=active_websockets,
        connection_metadata=connection_metadata,
        player_websockets=player_websockets,
    )


async def delegate_connection_cleaner(
    connection_cleaner: object | None,
    method_name: str,
    default_error: dict[str, object],
    *args: object,
    **kwargs: object,
) -> dict[str, object]:
    """
    Generic delegate for connection cleaner methods.

    Args:
        connection_cleaner: Connection cleaner instance
        method_name: Name of method to call
        default_error: Default error response if cleaner not initialized
        *args: Positional arguments to pass
        **kwargs: Keyword arguments to pass

    Returns:
        dict: Cleanup results
    """
    if connection_cleaner is None:
        logger.error("Connection cleaner not initialized")
        return default_error
    result = await _async_callable(connection_cleaner, method_name)(*args, **kwargs)
    return cast(dict[str, object], result)


def delegate_connection_cleaner_sync(
    connection_cleaner: object | None,
    method_name: str,
    **kwargs: object,
) -> None:
    """
    Generic delegate for synchronous connection cleaner methods.

    Args:
        connection_cleaner: Connection cleaner instance
        method_name: Name of method to call
        **kwargs: Keyword arguments to pass
    """
    if connection_cleaner is None:
        logger.error("Connection cleaner not initialized")
        return
    _ = _sync_callable(connection_cleaner, method_name)(**kwargs)


async def delegate_game_state_provider(
    game_state_provider: object | None,
    method_name: str,
    default_return: object,
    *args: object,
    **kwargs: object,
) -> object:
    """
    Generic delegate for game state provider methods.

    Args:
        game_state_provider: Game state provider instance
        method_name: Name of method to call
        default_return: Default return value if provider not initialized
        *args: Positional arguments to pass
        **kwargs: Keyword arguments to pass

    Returns:
        Result from the method call or default_return if provider not initialized
    """
    if game_state_provider is None:
        logger.error("Game state provider not initialized")
        return default_return
    return await _async_callable(game_state_provider, method_name)(*args, **kwargs)


def delegate_game_state_provider_sync(
    game_state_provider: object | None,
    method_name: str,
    default_return: object,
    *args: object,
    **kwargs: object,
) -> object:
    """
    Generic delegate for synchronous game state provider methods.

    Args:
        game_state_provider: Game state provider instance
        method_name: Name of method to call
        default_return: Default return value if provider not initialized
        *args: Positional arguments to pass
        **kwargs: Keyword arguments to pass

    Returns:
        Result from the method call or default_return if provider not initialized
    """
    if game_state_provider is None:
        logger.error("Game state provider not initialized")
        return default_return
    return _sync_callable(game_state_provider, method_name)(*args, **kwargs)


async def delegate_message_broadcaster(
    message_broadcaster: object | None,
    method_name: str,
    default_return: dict[str, object],
    player_websockets: Mapping[uuid.UUID, list[str]],
    *args: object,
    **kwargs: object,
) -> dict[str, object]:
    """
    Generic delegate for message broadcaster methods.

    Args:
        message_broadcaster: Message broadcaster instance
        method_name: Name of method to call
        default_return: Default return value if broadcaster not initialized
        player_websockets: Dictionary mapping player IDs to connection IDs
        *args: Positional arguments to pass
        **kwargs: Keyword arguments to pass

    Returns:
        dict: Broadcast results
    """
    if message_broadcaster is None:
        logger.error("Message broadcaster not initialized")
        return default_return
    method = _async_callable(message_broadcaster, method_name)
    # Special handling for broadcast_global which expects (event, exclude_player, player_websockets)
    if method_name == "broadcast_global":
        # Extract event and exclude_player from args or kwargs
        if args:
            event = args[0]
            exclude_player: object | None = args[1] if len(args) > 1 else kwargs.get("exclude_player")
        else:
            event = kwargs.pop("event", None)
            exclude_player = kwargs.pop("exclude_player", None)
        # Convert exclude_player UUID to string if needed (MessageBroadcaster expects str | None)
        if exclude_player is not None and isinstance(exclude_player, uuid.UUID):
            exclude_player = str(exclude_player)
        return cast(dict[str, object], await method(event, exclude_player, player_websockets))
    # Special handling for broadcast_to_room which expects (room_id, event, exclude_player, player_websockets)
    if method_name == "broadcast_to_room":
        # Extract room_id, event, and exclude_player from kwargs
        room_id = kwargs.pop("room_id", None)
        event = kwargs.pop("event", None)
        exclude_player = kwargs.pop("exclude_player", None)
        # broadcast_to_room accepts uuid.UUID | str | None, so no conversion needed
        return cast(dict[str, object], await method(room_id, event, exclude_player, player_websockets))
    # For other methods, use the standard pattern (player_websockets first)
    return cast(dict[str, object], await method(player_websockets, *args, **kwargs))


async def delegate_personal_message_sender(
    personal_message_sender: object | None,
    method_name: str,
    default_return: dict[str, object],
    player_websockets: Mapping[uuid.UUID, list[str]],
    active_websockets: Mapping[str, WebSocket],
    *args: object,
    **kwargs: object,
) -> dict[str, object]:
    """
    Generic delegate for personal message sender methods.

    Args:
        personal_message_sender: Personal message sender instance
        method_name: Name of method to call
        default_return: Default return value if sender not initialized
        player_websockets: Dictionary mapping player IDs to connection IDs
        active_websockets: Dictionary mapping connection IDs to WebSocket instances
        *args: Positional arguments to pass
        **kwargs: Keyword arguments to pass

    Returns:
        dict: Message sending results
    """
    if personal_message_sender is None:
        logger.error("Personal message sender not initialized")
        return default_return
    method = _async_callable(personal_message_sender, method_name)
    # Special handling for send_message which expects (player_id, event, player_websockets, active_websockets)
    if method_name == "send_message":
        # Extract player_id and event from kwargs
        player_id = kwargs.pop("player_id", None)
        event = kwargs.pop("event", None)
        return cast(dict[str, object], await method(player_id, event, player_websockets, active_websockets))
    # For other methods, use the standard pattern (player_websockets, active_websockets first)
    return cast(dict[str, object], await method(player_websockets, active_websockets, *args, **kwargs))


def delegate_personal_message_sender_sync(
    personal_message_sender: object | None,
    method_name: str,
    default_return: dict[str, object],
    player_websockets: Mapping[uuid.UUID, list[str]],
    *args: object,
    **kwargs: object,
) -> dict[str, object]:
    """
    Generic delegate for synchronous personal message sender methods.

    Args:
        personal_message_sender: Personal message sender instance
        method_name: Name of method to call
        default_return: Default return value if sender not initialized
        player_websockets: Dictionary mapping player IDs to connection IDs
        *args: Positional arguments to pass
        **kwargs: Keyword arguments to pass

    Returns:
        dict: Message sending results
    """
    if personal_message_sender is None:
        logger.error("Personal message sender not initialized")
        return default_return
    return cast(
        dict[str, object],
        _sync_callable(personal_message_sender, method_name)(player_websockets, *args, **kwargs),
    )


async def delegate_room_event_handler(
    room_event_handler: object | None,
    method_name: str,
    *args: object,
    **kwargs: object,
) -> None:
    """
    Generic delegate for room event handler methods.

    Args:
        room_event_handler: Room event handler instance
        method_name: Name of method to call
        *args: Positional arguments to pass
        **kwargs: Keyword arguments to pass
    """
    if room_event_handler is None:
        logger.error("Room event handler not initialized")
        return
    _ = await _async_callable(room_event_handler, method_name)(*args, **kwargs)
