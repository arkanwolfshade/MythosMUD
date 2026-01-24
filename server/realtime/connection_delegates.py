"""
Delegation helpers for connection manager.

This module provides helper functions that delegate to specialized
components, reducing boilerplate in the main ConnectionManager class.
"""

import uuid
from typing import Any, cast

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def delegate_error_handler(
    error_handler: Any,
    method_name: str,
    default_error: dict[str, Any],
    *args: Any,
    **kwargs: Any,
) -> dict[str, Any]:
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
    method = getattr(error_handler, method_name)
    result: dict[str, Any] = cast(dict[str, Any], await method(*args, **kwargs))
    return result


async def cleanup_dead_websocket_impl(
    player_id: Any,
    connection_id: str,
    manager: Any,  # ConnectionManager
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
            websocket = manager.active_websockets[connection_id]
            # Guard against None websocket (can happen during cleanup)
            if websocket is None:
                del manager.active_websockets[connection_id]
                return

            # Check if WebSocket is still connected before attempting to close
            # This prevents "Unexpected ASGI message 'websocket.close'" errors
            is_connected = False
            try:
                is_connected = websocket.client_state.name == "CONNECTED"
            except (AttributeError, ValueError, TypeError):
                # If we can't determine state, assume it's disconnected
                is_connected = False

            if is_connected:
                logger.info("Closing dead WebSocket", connection_id=connection_id, player_id=player_id)
                try:
                    import asyncio

                    await asyncio.wait_for(websocket.close(code=1000, reason="Connection cleaned up"), timeout=2.0)
                    logger.info("Successfully closed dead WebSocket", connection_id=connection_id, player_id=player_id)
                except (TimeoutError, RuntimeError, ConnectionError) as e:
                    error_message = str(e)
                    # Suppress warnings for expected errors when WebSocket is already closed
                    if (
                        "close message has been sent" not in error_message.lower()
                        and "cannot call" not in error_message.lower()
                        and "unexpected asgi message 'websocket.close'" not in error_message.lower()
                        and "response already completed" not in error_message.lower()
                    ):
                        logger.warning(
                            "Error closing dead WebSocket",
                            connection_id=connection_id,
                            player_id=player_id,
                            error=error_message,
                        )
            else:
                logger.debug(
                    "WebSocket already closed, skipping close call", connection_id=connection_id, player_id=player_id
                )
            del manager.active_websockets[connection_id]

        # Remove from player's connection list
        if player_id in manager.player_websockets and connection_id in manager.player_websockets[player_id]:
            manager.player_websockets[player_id].remove(connection_id)
            if not manager.player_websockets[player_id]:
                del manager.player_websockets[player_id]

        # Remove connection metadata
        if connection_id in manager.connection_metadata:
            del manager.connection_metadata[connection_id]

        # Clean up rate limit data
        manager.rate_limiter.remove_connection_message_data(connection_id)

        logger.info("Cleaned up dead WebSocket connection", connection_id=connection_id, player_id=player_id)
    except (AttributeError, ValueError, TypeError) as e:
        logger.error("Error cleaning up dead WebSocket", connection_id=connection_id, player_id=player_id, error=str(e))


async def validate_token_impl(token: str, player_id: Any, manager: Any) -> bool:
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
        from ..exceptions import DatabaseError

        payload = decode_access_token(token)
        if not payload or "sub" not in payload:
            logger.debug("Token validation failed: invalid payload", player_id=player_id)
            return False

        user_id = str(payload["sub"]).strip()
        if not manager.async_persistence:
            logger.warning("Cannot validate token: persistence not available", player_id=player_id)
            return False

        player = await manager.async_persistence.get_player_by_user_id(user_id)
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
    health_monitor: Any,
    method_name: str,
    active_websockets: dict[str, Any],
    connection_metadata: dict[str, Any],
    player_websockets: dict[str, Any],
) -> None:
    """Generic delegate for health monitor methods."""
    if health_monitor is None:
        logger.error("Health monitor not initialized")
        return
    method = getattr(health_monitor, method_name)
    await method(
        active_websockets=active_websockets,
        connection_metadata=connection_metadata,
        player_websockets=player_websockets,
    )


def delegate_health_monitor_sync(
    health_monitor: Any,
    method_name: str,
    active_websockets: dict[str, Any],
    connection_metadata: dict[str, Any],
    player_websockets: dict[str, Any],
) -> None:
    """Generic delegate for synchronous health monitor methods."""
    if health_monitor is None:
        logger.error("Health monitor not initialized")
        return
    method = getattr(health_monitor, method_name)
    method(
        active_websockets=active_websockets,
        connection_metadata=connection_metadata,
        player_websockets=player_websockets,
    )


async def delegate_connection_cleaner(
    connection_cleaner: Any,
    method_name: str,
    default_error: dict[str, Any],
    *args: Any,
    **kwargs: Any,
) -> dict[str, Any]:
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
    method = getattr(connection_cleaner, method_name)
    result: dict[str, Any] = cast(dict[str, Any], await method(*args, **kwargs))
    return result


def delegate_connection_cleaner_sync(
    connection_cleaner: Any,
    method_name: str,
    **kwargs: Any,
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
    method = getattr(connection_cleaner, method_name)
    method(**kwargs)


async def delegate_game_state_provider(
    game_state_provider: Any,
    method_name: str,
    default_return: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
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
    method = getattr(game_state_provider, method_name)
    return await method(*args, **kwargs)


def delegate_game_state_provider_sync(
    game_state_provider: Any,
    method_name: str,
    default_return: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
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
    method = getattr(game_state_provider, method_name)
    return method(*args, **kwargs)


async def delegate_message_broadcaster(
    message_broadcaster: Any,
    method_name: str,
    default_return: dict[str, Any],
    player_websockets: dict[str, Any],
    *args: Any,
    **kwargs: Any,
) -> dict[str, Any]:
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
    method = getattr(message_broadcaster, method_name)
    # Special handling for broadcast_global which expects (event, exclude_player, player_websockets)
    if method_name == "broadcast_global":
        # Extract event and exclude_player from args or kwargs
        if args:
            event = args[0]
            exclude_player = args[1] if len(args) > 1 else kwargs.get("exclude_player")
        else:
            event = kwargs.pop("event", None)
            exclude_player = kwargs.pop("exclude_player", None)
        # Convert exclude_player UUID to string if needed (MessageBroadcaster expects str | None)
        if exclude_player is not None and isinstance(exclude_player, uuid.UUID):
            exclude_player = str(exclude_player)
        result: dict[str, Any] = cast(dict[str, Any], await method(event, exclude_player, player_websockets))
        return result
    # Special handling for broadcast_to_room which expects (room_id, event, exclude_player, player_websockets)
    if method_name == "broadcast_to_room":
        # Extract room_id, event, and exclude_player from kwargs
        room_id = kwargs.pop("room_id", None)
        event = kwargs.pop("event", None)
        exclude_player = kwargs.pop("exclude_player", None)
        # broadcast_to_room accepts uuid.UUID | str | None, so no conversion needed
        result2: dict[str, Any] = cast(dict[str, Any], await method(room_id, event, exclude_player, player_websockets))
        return result2
    # For other methods, use the standard pattern (player_websockets first)
    result3: dict[str, Any] = cast(dict[str, Any], await method(player_websockets, *args, **kwargs))
    return result3


async def delegate_personal_message_sender(
    personal_message_sender: Any,
    method_name: str,
    default_return: dict[str, Any],
    player_websockets: dict[str, Any],
    active_websockets: dict[str, Any],
    *args: Any,
    **kwargs: Any,
) -> dict[str, Any]:
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
    method = getattr(personal_message_sender, method_name)
    # Special handling for send_message which expects (player_id, event, player_websockets, active_websockets)
    if method_name == "send_message":
        # Extract player_id and event from kwargs
        player_id = kwargs.pop("player_id", None)
        event = kwargs.pop("event", None)
        result: dict[str, Any] = cast(
            dict[str, Any], await method(player_id, event, player_websockets, active_websockets)
        )
        return result
    # For other methods, use the standard pattern (player_websockets, active_websockets first)
    result2: dict[str, Any] = cast(dict[str, Any], await method(player_websockets, active_websockets, *args, **kwargs))
    return result2


def delegate_personal_message_sender_sync(
    personal_message_sender: Any,
    method_name: str,
    default_return: dict[str, Any],
    player_websockets: dict[str, Any],
    *args: Any,
    **kwargs: Any,
) -> dict[str, Any]:
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
    method = getattr(personal_message_sender, method_name)
    result: dict[str, Any] = cast(dict[str, Any], method(player_websockets, *args, **kwargs))
    return result


async def delegate_room_event_handler(
    room_event_handler: Any,
    method_name: str,
    *args: Any,
    **kwargs: Any,
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
    method = getattr(room_event_handler, method_name)
    await method(*args, **kwargs)
