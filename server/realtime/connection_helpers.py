"""
Helper utilities for connection manager.

This module provides utility functions and helpers used by the connection manager
for various operations like UUID conversion, sequence numbers, and deprecated methods.
"""

# pylint: disable=too-many-locals  # Reason: Connection helpers require many intermediate variables for complex connection operations

from typing import Any, cast

import aiofiles  # pylint: disable=import-error

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def convert_uuids_to_strings(obj: Any) -> Any:
    """
    Recursively convert UUID objects to strings for JSON serialization.

    Args:
        obj: Object to convert

    Returns:
        Object with UUIDs converted to strings
    """
    if isinstance(obj, dict):
        return {k: convert_uuids_to_strings(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert_uuids_to_strings(item) for item in obj]
    if hasattr(obj, "__class__") and "UUID" in obj.__class__.__name__:
        return str(obj)
    return obj


def _optimize_payload(event: dict[str, Any], player_id: Any) -> dict[str, Any]:
    """
    Optimize payload size for transmission.

    Args:
        event: The event data to optimize
        player_id: The player's ID for logging

    Returns:
        Optimized event payload
    """
    serializable_event = convert_uuids_to_strings(event)

    try:
        from .payload_optimizer import get_payload_optimizer

        optimizer = get_payload_optimizer()
        serializable_event = optimizer.optimize_payload(serializable_event)
    except ValueError as size_error:
        logger.error(
            "Payload too large to send",
            player_id=player_id,
            error=str(size_error),
            event_type=event.get("event_type"),
        )
        serializable_event = {
            "type": "error",
            "error_type": "payload_too_large",
            "message": "Message payload too large to transmit",
            "details": {"max_size": optimizer.max_payload_size},
        }
    except (DatabaseError, AttributeError) as opt_error:
        logger.warning(
            "Payload optimization failed, using original",
            player_id=player_id,
            error=str(opt_error),
        )

    result: dict[str, Any] = cast(dict[str, Any], serializable_event)
    return result


async def _send_to_websockets(
    player_id: Any,
    serializable_event: dict[str, Any],
    manager: Any,  # ConnectionManager
    delivery_status: dict[str, Any],
) -> bool:
    """
    Send event to all active websockets for a player.

    Args:
        player_id: The player's ID
        serializable_event: The event to send
        manager: ConnectionManager instance
        delivery_status: Status dict to update

    Returns:
        True if any connection attempts were made
    """
    had_connection_attempts = False

    if player_id not in manager.player_websockets:
        return had_connection_attempts

    connection_ids = manager.player_websockets[player_id].copy()
    for connection_id in connection_ids:
        if connection_id not in manager.active_websockets:
            continue

        had_connection_attempts = True
        websocket = manager.active_websockets[connection_id]
        # Guard against None websocket (can happen during cleanup)
        if websocket is None:
            continue
        try:
            await websocket.send_json(serializable_event)
            delivery_status["websocket_delivered"] += 1
            delivery_status["active_connections"] += 1
        except (DatabaseError, AttributeError) as ws_error:
            logger.warning(
                "WebSocket send failed",
                player_id=player_id,
                connection_id=connection_id,
                error=str(ws_error),
            )
            delivery_status["websocket_failed"] += 1
            await manager._cleanup_dead_websocket(player_id, connection_id)  # pylint: disable=protected-access  # Reason: Accessing protected method _cleanup_dead_websocket is necessary for connection cleanup, this is part of the connection manager internal API

    return had_connection_attempts


def _queue_message_if_needed(
    player_id: Any,
    serializable_event: dict[str, Any],
    manager: Any,  # ConnectionManager
    event: dict[str, Any],
) -> None:
    """
    Queue message for later delivery if no active connections.

    Args:
        player_id: The player's ID
        serializable_event: The event to queue
        manager: ConnectionManager instance
        event: Original event for logging
    """
    player_id_str = str(player_id)
    if player_id_str not in manager.message_queue.pending_messages:
        manager.message_queue.pending_messages[player_id_str] = []
    manager.message_queue.pending_messages[player_id_str].append(serializable_event)
    logger.debug(
        "No active connections, queued message for later delivery",
        player_id=player_id,
        event_type=event.get("event_type"),
    )


def _update_delivery_status(
    delivery_status: dict[str, Any],
    had_connection_attempts: bool,
) -> None:
    """
    Update final delivery status based on connection results.

    Args:
        delivery_status: Status dict to update
        had_connection_attempts: Whether any connection attempts were made
    """
    if not delivery_status["active_connections"]:
        if had_connection_attempts and delivery_status["websocket_failed"] > 0:
            delivery_status["success"] = False
        else:
            delivery_status["success"] = True
    else:
        delivery_status["success"] = delivery_status["websocket_delivered"] > 0


async def send_personal_message_old_impl(
    player_id: Any,
    event: dict[str, Any],
    manager: Any,  # ConnectionManager
) -> dict[str, Any]:
    """
    Send a personal message to a player via WebSocket (deprecated implementation).

    Args:
        player_id: The player's ID
        event: The event data to send
        manager: ConnectionManager instance

    Returns:
        dict: Delivery status
    """
    delivery_status = {
        "success": False,
        "websocket_delivered": 0,
        "websocket_failed": 0,
        "total_connections": 0,
        "active_connections": 0,
    }

    try:
        serializable_event = _optimize_payload(event, player_id)

        if event.get("event_type") == "game_state":
            logger.info("Sending game_state event", player_id=player_id, event_data=serializable_event)

        websocket_count = len(manager.player_websockets.get(player_id, []))
        delivery_status["total_connections"] = websocket_count

        had_connection_attempts = await _send_to_websockets(player_id, serializable_event, manager, delivery_status)

        if not delivery_status["active_connections"]:
            _queue_message_if_needed(player_id, serializable_event, manager, event)

        _update_delivery_status(delivery_status, had_connection_attempts)

        logger.debug("Message delivery status", player_id=player_id, delivery_status=delivery_status)
        return delivery_status

    except (DatabaseError, AttributeError) as e:
        logger.error("Failed to send personal message", player_id=player_id, error=str(e))
        delivery_status["success"] = False
        return delivery_status


async def handle_new_login_impl(player_id: Any, manager: Any) -> None:
    """
    Handle a new login by terminating all existing connections.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    try:
        logger.info("NEW LOGIN detected for player, terminating existing connections", player_id=player_id)

        import json
        from datetime import datetime
        from pathlib import Path

        login_log_entry = {
            "timestamp": datetime.now().isoformat(),
            "player_id": str(player_id),
            "event_type": "NEW_LOGIN",
            "connections_before": {
                "websocket": player_id in manager.player_websockets,
                "online": player_id in manager.online_players,
            },
        }

        # CRITICAL: Use absolute path from project root to prevent permission issues in CI
        # Find project root by looking for pyproject.toml
        current_file = Path(__file__).resolve()
        project_root = current_file.parent
        while project_root.parent != project_root:
            if (project_root / "pyproject.toml").exists():
                break
            project_root = project_root.parent

        # Get environment from config (defaults to development)
        try:
            from ..config import get_config

            config = get_config()
            environment = config.logging.environment
        except (ImportError, AttributeError):
            # Fallback to development if config not available
            environment = "development"

        login_log_dir = project_root / "logs" / environment
        try:
            login_log_dir.mkdir(parents=True, exist_ok=True)
        except (OSError, PermissionError) as dir_error:
            # Log but don't fail - login logging is non-critical
            logger.debug("Could not create login log directory", error=str(dir_error), log_dir=str(login_log_dir))
            # Skip logging if directory can't be created
            await manager.force_disconnect_player(player_id)
            return

        login_log_path = login_log_dir / "new_logins.log"

        try:
            async with aiofiles.open(login_log_path, "a", encoding="utf-8") as f:
                await f.write(json.dumps(login_log_entry) + "\n")
        except (OSError, PermissionError) as log_error:
            # Log but don't fail - login logging is non-critical
            logger.debug("Could not write login log", error=str(log_error), log_path=str(login_log_path))

        await manager.force_disconnect_player(player_id)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error handling new login", player_id=player_id, error=str(e), exc_info=True)


async def broadcast_room_event_impl(
    event_type: str,
    room_id: str,
    data: dict[str, Any],
    manager: Any,  # ConnectionManager
) -> dict[str, Any]:
    """Broadcast a room-specific event to all players in the room."""
    try:
        from ..exceptions import (
            DatabaseError as DBError,  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Renamed to avoid shadowing outer scope
        )
        from .envelope import build_event

        event = build_event(event_type, data)
        result: dict[str, Any] = cast(dict[str, Any], await manager.broadcast_to_room(room_id, event))
        return result
    except (DBError, AttributeError) as e:
        logger.error("Error broadcasting room event", error=str(e), event_type=event_type, room_id=room_id)
        return {
            "room_id": room_id,
            "total_targets": 0,
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
            "error": str(e),
        }


async def broadcast_global_event_impl(
    event_type: str,
    data: dict[str, Any],
    manager: Any,  # ConnectionManager
) -> dict[str, Any]:
    """Broadcast a global event to all connected players."""
    try:
        from ..exceptions import (
            DatabaseError as DBError,  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Renamed to avoid shadowing outer scope
        )
        from .envelope import build_event

        event = build_event(event_type, data)
        result: dict[str, Any] = cast(dict[str, Any], await manager.broadcast_global(event))
        return result
    except (DBError, AttributeError) as e:
        logger.error("Error broadcasting global event", error=str(e), event_type=event_type)
        return {
            "total_players": 0,
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
            "error": str(e),
        }


def mark_player_seen_impl(player_id: Any, manager: Any) -> None:
    """Update last-seen timestamp for a player and all their connections."""
    try:
        import asyncio
        import time

        from ..exceptions import (
            DatabaseError as DBError,  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Renamed to avoid shadowing outer scope
        )

        now_ts = time.time()
        manager.last_seen[player_id] = now_ts

        # Update last_seen for all connection metadata
        if player_id in manager.player_websockets:
            for connection_id in manager.player_websockets[player_id]:
                if connection_id in manager.connection_metadata:
                    manager.connection_metadata[connection_id].last_seen = now_ts

        if manager.async_persistence:
            last_update = manager.last_active_update_times.get(player_id, 0.0)
            if now_ts - last_update >= manager.last_active_update_interval:
                try:
                    manager.last_active_update_times[player_id] = now_ts
                    try:
                        loop = asyncio.get_running_loop()
                        loop.create_task(manager.async_persistence.update_player_last_active(player_id))
                    except RuntimeError:
                        pass
                except (DBError, AttributeError) as update_error:
                    logger.warning(
                        "Failed to persist last_active update",
                        player_id=player_id,
                        error=str(update_error),
                    )
    except (DatabaseError, AttributeError) as e:
        logger.error("Error marking player seen", player_id=player_id, error=str(e))
