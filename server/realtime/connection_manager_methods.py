"""
Extracted methods from ConnectionManager for better code organization.

This module contains methods that were extracted from ConnectionManager
to reduce file complexity and improve maintainability.
"""

from typing import Any
from uuid import UUID

from fastapi import WebSocket

from ..structured_logging.enhanced_logging_config import get_logger
from .connection_statistics import (
    get_online_player_by_display_name_impl,
    get_player_presence_info_impl,
    validate_player_presence_impl,
)

logger = get_logger(__name__)


# ============================================================================
# Statistics Methods
# ============================================================================


def get_memory_stats_impl(manager: Any) -> dict[str, Any]:
    """Get comprehensive memory and connection statistics."""
    return manager.statistics_aggregator.get_memory_stats(
        active_websockets=manager.active_websockets,
        player_websockets=manager.player_websockets,
        connection_timestamps=manager.connection_timestamps,
        cleanup_stats=manager.cleanup_stats,
        player_sessions=manager.player_sessions,
        session_connections=manager.session_connections,
        online_players=manager.online_players,
        last_seen=manager.last_seen,
    )


def get_dual_connection_stats_impl(manager: Any) -> dict[str, Any]:
    """Get comprehensive connection statistics."""
    return manager.statistics_aggregator.get_connection_stats(
        player_websockets=manager.player_websockets,
        connection_metadata=manager.connection_metadata,
        session_connections=manager.session_connections,
        player_sessions=manager.player_sessions,
    )


def get_performance_stats_impl(manager: Any) -> dict[str, Any]:
    """Get connection performance statistics."""
    return manager.performance_tracker.get_stats()


def get_connection_health_stats_impl(manager: Any) -> dict[str, Any]:
    """Get comprehensive connection health statistics."""
    return manager.statistics_aggregator.get_connection_health_stats(connection_metadata=manager.connection_metadata)


def get_memory_alerts_impl(manager: Any) -> list[str]:
    """Get memory-related alerts."""
    return manager.statistics_aggregator.get_memory_alerts(
        connection_timestamps=manager.connection_timestamps,
        max_connection_age=manager.memory_monitor.max_connection_age,
    )


def get_error_statistics_impl(manager: Any) -> dict[str, Any]:
    """Get error handling statistics."""
    if manager.error_handler is None:
        logger.error("Error handler not initialized")
        return {}
    return manager.error_handler.get_error_statistics(
        online_players=manager.online_players, player_websockets=manager.player_websockets
    )


def get_rate_limit_info_impl(manager: Any, player_id: UUID) -> dict[str, Any]:
    """Get rate limit information for a player."""
    return manager.rate_limiter.get_rate_limit_info(str(player_id))


def get_message_delivery_stats_impl(manager: Any, player_id: UUID) -> dict[str, Any]:
    """Get message delivery statistics for a player."""
    from .connection_delegates import delegate_personal_message_sender_sync

    return delegate_personal_message_sender_sync(
        manager.personal_message_sender,
        "get_delivery_stats",
        {"player_id": player_id},
        manager.player_websockets,
        player_id=player_id,
    )


def get_active_connection_count_impl(manager: Any) -> int:
    """Get the total number of active connections."""
    return len(manager.active_websockets)


# ============================================================================
# Presence and Player Info Methods
# ============================================================================


def get_player_presence_info_method(manager: Any, player_id: UUID) -> dict[str, Any]:
    """Get detailed presence information for a player."""
    return get_player_presence_info_impl(player_id, manager)


def validate_player_presence_method(manager: Any, player_id: UUID) -> dict[str, Any]:
    """Validate player presence and clean up any inconsistencies."""
    return validate_player_presence_impl(player_id, manager)


def get_online_players_impl(manager: Any) -> list[dict[str, Any]]:
    """Get list of online players."""
    return list(manager.online_players.values())


def get_online_player_by_display_name_method(manager: Any, display_name: str) -> dict[str, Any] | None:
    """Get online player information by display name."""
    return get_online_player_by_display_name_impl(display_name, manager)


def get_player_session_impl(manager: Any, player_id: UUID) -> str | None:
    """Get the current session ID for a player."""
    return manager.player_sessions.get(player_id)


def get_session_connections_impl(manager: Any, session_id: str) -> list[str]:
    """Get all connection IDs for a session."""
    return manager.session_connections.get(session_id, [])


def validate_session_impl(manager: Any, player_id: UUID, session_id: str) -> bool:
    """Validate that a session ID matches the player's current session."""
    return manager.player_sessions.get(player_id) == session_id


def get_connection_count_impl(manager: Any, player_id: UUID) -> dict[str, int]:
    """Get the number of connections for a player by type."""
    websocket_count = len(manager.player_websockets.get(player_id, []))
    return {"websocket": websocket_count, "total": websocket_count}


def has_websocket_connection_impl(manager: Any, player_id: UUID) -> bool:
    """Check if a player has any WebSocket connections."""
    return player_id in manager.player_websockets and len(manager.player_websockets[player_id]) > 0


def get_player_websocket_connection_id_impl(manager: Any, player_id: UUID) -> str | None:
    """Get the first WebSocket connection ID for a player (backward compatibility)."""
    if player_id in manager.player_websockets and manager.player_websockets[player_id]:
        return manager.player_websockets[player_id][0]
    return None


def get_connection_id_from_websocket_impl(manager: Any, websocket: WebSocket) -> str | None:
    """Get connection ID from a WebSocket instance."""
    for conn_id, ws in manager.active_websockets.items():
        if ws is websocket:
            return conn_id
    return None


# ============================================================================
# Broadcasting Methods
# ============================================================================


async def broadcast_to_room_impl(
    manager: Any, room_id: str, event: dict[str, Any], exclude_player: UUID | str | None = None
) -> dict[str, Any]:
    """Broadcast a message to all players in a room."""
    from .connection_delegates import delegate_message_broadcaster

    return await delegate_message_broadcaster(
        manager.message_broadcaster,
        "broadcast_to_room",
        {"room_id": room_id, "total_targets": 0},
        manager.player_websockets,
        room_id=room_id,
        event=event,
        exclude_player=exclude_player,
    )


async def broadcast_global_impl(
    manager: Any, event: dict[str, Any], exclude_player: str | None = None
) -> dict[str, Any]:
    """Broadcast a message to all connected players."""
    from .connection_delegates import delegate_message_broadcaster

    return await delegate_message_broadcaster(
        manager.message_broadcaster,
        "broadcast_global",
        {"total_players": 0},
        manager.player_websockets,
        event,
        exclude_player,
    )


async def broadcast_room_event_impl(
    manager: Any, event_type: str, room_id: str, data: dict[str, Any]
) -> dict[str, Any]:
    """Broadcast a room-specific event to all players in the room."""
    try:
        from ..exceptions import DatabaseError
        from .envelope import build_event

        event = build_event(event_type, data)
        result = await broadcast_to_room_impl(manager, room_id, event)
        return result
    except (DatabaseError, AttributeError) as e:
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


async def broadcast_global_event_impl(manager: Any, event_type: str, data: dict[str, Any]) -> dict[str, Any]:
    """Broadcast a global event to all connected players."""
    try:
        from ..exceptions import DatabaseError
        from .envelope import build_event

        event = build_event(event_type, data)
        return await broadcast_global_impl(manager, event, exclude_player=None)
    except (DatabaseError, AttributeError) as e:
        logger.error("Error broadcasting global event", error=str(e), event_type=event_type)
        return {
            "total_players": 0,
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
            "error": str(e),
        }


# ============================================================================
# Disconnection Methods
# ============================================================================


async def force_disconnect_player_impl(manager: Any, player_id: UUID) -> None:
    """Force disconnect a player from all connections (WebSocket only)."""
    from ..exceptions import DatabaseError

    try:
        logger.info("Force disconnecting player from all connections", player_id=player_id)
        if player_id in manager.player_websockets:
            await manager.disconnect_websocket(player_id, is_force_disconnect=True)
        logger.info("Player force disconnected from all connections", player_id=player_id)
    except (DatabaseError, AttributeError) as e:
        logger.error("Error force disconnecting player", player_id=player_id, error=str(e), exc_info=True)


async def disconnect_websocket_connection_impl(manager: Any, player_id: UUID, connection_id: str) -> bool:
    """Disconnect a specific WebSocket connection for a player."""
    from ..exceptions import DatabaseError

    try:
        if connection_id not in manager.connection_metadata:
            logger.warning("Connection not found in metadata", connection_id=connection_id)
            return False
        metadata = manager.connection_metadata[connection_id]
        if metadata.player_id != player_id or metadata.connection_type != "websocket":
            logger.warning(
                "Connection does not belong to player or is not a WebSocket",
                connection_id=connection_id,
                player_id=player_id,
            )
            return False
        return await manager.disconnect_connection_by_id(connection_id)
    except (DatabaseError, AttributeError) as e:
        logger.error(
            "Error disconnecting WebSocket connection",
            connection_id=connection_id,
            player_id=player_id,
            error=str(e),
            exc_info=True,
        )
        return False


# ============================================================================
# Health Check Methods
# ============================================================================


async def check_connection_health_impl(manager: Any, player_id: UUID) -> dict[str, Any]:
    """Check the health of all connections for a player."""
    if manager.health_monitor is None:
        logger.error("Health monitor not initialized")
        return {"player_id": player_id, "overall_health": "error"}
    method = manager.health_monitor.check_player_connection_health
    return await method(
        player_id=player_id,
        player_websockets=manager.player_websockets,
        active_websockets=manager.active_websockets,
    )


async def _check_connection_health_impl(manager: Any) -> None:
    """Check health of all connections and clean up stale/dead ones."""
    from .connection_delegates import delegate_health_monitor

    await delegate_health_monitor(
        manager.health_monitor,
        "check_all_connections_health",
        manager.active_websockets,
        manager.connection_metadata,
        manager.player_websockets,
    )


async def _periodic_health_check_impl(manager: Any) -> None:
    """Periodic health check task that runs continuously."""
    from .connection_delegates import delegate_health_monitor

    await delegate_health_monitor(
        manager.health_monitor,
        "periodic_health_check_task",
        manager.active_websockets,
        manager.connection_metadata,
        manager.player_websockets,
    )


def start_health_checks_impl(manager: Any) -> None:
    """Start the periodic health check task."""
    from .connection_delegates import delegate_health_monitor_sync

    delegate_health_monitor_sync(
        manager.health_monitor,
        "start_periodic_checks",
        manager.active_websockets,
        manager.connection_metadata,
        manager.player_websockets,
    )


def stop_health_checks_impl(manager: Any) -> None:
    """Stop the periodic health check task."""
    if manager.health_monitor is None:
        logger.error("Health monitor not initialized")
        return
    manager.health_monitor.stop_periodic_checks()


# ============================================================================
# Error Handling Methods
# ============================================================================


async def detect_and_handle_error_state_impl(
    manager: Any, player_id: UUID, error_type: str, error_details: str, connection_id: str | None = None
) -> dict[str, Any]:
    """Detect when a client is in an error state and handle it appropriately."""
    from .connection_delegates import delegate_error_handler

    return await delegate_error_handler(
        manager.error_handler,
        "detect_and_handle_error_state",
        {
            "player_id": player_id,
            "error_type": error_type,
            "success": False,
            "errors": ["Error handler not initialized"],
        },
        player_id,
        error_type,
        error_details,
        connection_id,
    )


async def handle_websocket_error_impl(
    manager: Any, player_id: UUID, connection_id: str, error_type: str, error_details: str
) -> dict[str, Any]:
    """Handle WebSocket-specific errors."""
    from .connection_delegates import delegate_error_handler

    return await delegate_error_handler(
        manager.error_handler,
        "handle_websocket_error",
        {"player_id": player_id, "success": False, "errors": ["Error handler not initialized"]},
        player_id,
        connection_id,
        error_type,
        error_details,
    )


async def handle_authentication_error_impl(
    manager: Any, player_id: UUID, error_type: str, error_details: str
) -> dict[str, Any]:
    """Handle authentication-related errors."""
    from .connection_delegates import delegate_error_handler

    return await delegate_error_handler(
        manager.error_handler,
        "handle_authentication_error",
        {"player_id": player_id, "success": False, "errors": ["Error handler not initialized"]},
        player_id,
        error_type,
        error_details,
    )


async def handle_security_violation_impl(
    manager: Any, player_id: UUID, violation_type: str, violation_details: str
) -> dict[str, Any]:
    """Handle security violations."""
    from .connection_delegates import delegate_error_handler

    return await delegate_error_handler(
        manager.error_handler,
        "handle_security_violation",
        {"player_id": player_id, "success": False, "errors": ["Error handler not initialized"]},
        player_id,
        violation_type,
        violation_details,
    )


async def recover_from_error_impl(manager: Any, player_id: UUID, recovery_type: str = "FULL") -> dict[str, Any]:
    """Attempt to recover from an error state for a player."""
    from .connection_delegates import delegate_error_handler

    return await delegate_error_handler(
        manager.error_handler,
        "recover_from_error",
        {"player_id": player_id, "success": False, "errors": ["Error handler not initialized"]},
        player_id,
        recovery_type,
    )


# ============================================================================
# Game State Provider Methods
# ============================================================================


async def get_player_impl(manager: Any, player_id: UUID) -> Any:
    """Get a player from the persistence layer (async version)."""
    from .connection_delegates import delegate_game_state_provider

    return await delegate_game_state_provider(manager.game_state_provider, "get_player", None, player_id)


async def get_players_batch_impl(manager: Any, player_ids: list[UUID]) -> dict[UUID, Any]:
    """Get multiple players from the persistence layer in a single batch operation."""
    from .connection_delegates import delegate_game_state_provider

    return await delegate_game_state_provider(manager.game_state_provider, "get_players_batch", {}, player_ids)


async def convert_room_players_uuids_to_names_impl(manager: Any, room_data: dict[str, Any]) -> dict[str, Any]:
    """Convert player UUIDs and NPC IDs in room_data to names."""
    from .connection_delegates import delegate_game_state_provider

    return await delegate_game_state_provider(
        manager.game_state_provider, "convert_room_uuids_to_names", room_data, room_data
    )


def get_npcs_batch_impl(manager: Any, npc_ids: list[str]) -> dict[str, str]:
    """Get NPC names for multiple NPCs in a batch operation."""
    from .connection_delegates import delegate_game_state_provider_sync

    return delegate_game_state_provider_sync(manager.game_state_provider, "get_npcs_batch", {}, npc_ids)


async def get_room_occupants_impl(manager: Any, room_id: str) -> list[dict[str, Any]]:
    """Get list of occupants in a room."""
    from .connection_delegates import delegate_game_state_provider

    return await delegate_game_state_provider(
        manager.game_state_provider, "get_room_occupants", [], room_id=room_id, online_players=manager.online_players
    )


async def send_initial_game_state_impl(manager: Any, player_id: UUID, player: Any, room_id: str) -> None:
    """Send initial game_state event to a newly connected player."""
    from .connection_delegates import delegate_game_state_provider

    await delegate_game_state_provider(
        manager.game_state_provider,
        "send_initial_game_state",
        None,
        player_id=player_id,
        player=player,
        room_id=room_id,
        online_players=manager.online_players,
    )


# ============================================================================
# Cleanup Methods
# ============================================================================


async def cleanup_dead_connections_impl(manager: Any, player_id: UUID | None = None) -> dict[str, Any]:
    """Clean up dead connections for a specific player or all players."""
    from .connection_delegates import delegate_connection_cleaner

    return await delegate_connection_cleaner(
        manager.connection_cleaner,
        "cleanup_dead_connections",
        {"players_checked": 0, "connections_cleaned": 0, "errors": ["Connection cleaner not initialized"]},
        player_websockets=manager.player_websockets,
        active_websockets=manager.active_websockets,
        player_id=player_id,
    )


async def check_and_cleanup_impl(manager: Any) -> None:
    """Periodically check for cleanup conditions and perform cleanup if needed."""
    from .connection_delegates import delegate_connection_cleaner

    await delegate_connection_cleaner(
        manager.connection_cleaner,
        "check_and_cleanup",
        {},
        online_players=manager.online_players,
        last_seen=manager.last_seen,
        player_websockets=manager.player_websockets,
        active_websockets=manager.active_websockets,
        connection_timestamps=manager.connection_timestamps,
        cleanup_stats=manager.cleanup_stats,
        last_active_update_times=manager.last_active_update_times,
    )


async def force_cleanup_impl(manager: Any) -> None:
    """Force immediate cleanup of all orphaned data."""
    from .connection_delegates import delegate_connection_cleaner

    await delegate_connection_cleaner(
        manager.connection_cleaner,
        "force_cleanup",
        {},
        cleanup_stats=manager.cleanup_stats,
        cleanup_orphaned_data_callback=manager.cleanup_orphaned_data,
        prune_stale_players_callback=manager.prune_stale_players,
    )


def cleanup_ghost_players_impl(manager: Any) -> None:
    """Clean up ghost players from all rooms."""
    from .connection_delegates import delegate_connection_cleaner_sync

    delegate_connection_cleaner_sync(
        manager.connection_cleaner, "cleanup_ghost_players", online_players=manager.online_players
    )


def prune_stale_players_impl(manager: Any, max_age_seconds: int = 90) -> None:
    """Remove players whose presence is stale beyond the threshold."""
    from .connection_delegates import delegate_connection_cleaner_sync

    delegate_connection_cleaner_sync(
        manager.connection_cleaner,
        "prune_stale_players",
        last_seen=manager.last_seen,
        online_players=manager.online_players,
        player_websockets=manager.player_websockets,
        active_websockets=manager.active_websockets,
        last_active_update_times=manager.last_active_update_times,
        max_age_seconds=max_age_seconds,
    )


async def cleanup_orphaned_data_impl(manager: Any) -> None:
    """Clean up orphaned data that might accumulate over time."""
    from .connection_delegates import delegate_connection_cleaner

    await delegate_connection_cleaner(
        manager.connection_cleaner,
        "cleanup_orphaned_data",
        {},
        connection_timestamps=manager.connection_timestamps,
        active_websockets=manager.active_websockets,
        cleanup_stats=manager.cleanup_stats,
    )


async def send_personal_message_impl(manager: Any, player_id: UUID, event: dict[str, Any]) -> dict[str, Any]:
    """Send a personal message to a player via WebSocket."""
    from .connection_delegates import delegate_personal_message_sender

    return await delegate_personal_message_sender(
        manager.personal_message_sender,
        "send_message",
        {"success": False},
        manager.player_websockets,
        manager.active_websockets,
        player_id=player_id,
        event=event,
    )


async def handle_player_entered_room_impl(manager: Any, event_data: dict[str, Any]) -> None:
    """Handle PlayerEnteredRoom events by broadcasting updated occupant count."""
    from .connection_delegates import delegate_room_event_handler

    await delegate_room_event_handler(manager.room_event_handler, "handle_player_entered_room", event_data)


async def handle_player_left_room_impl(manager: Any, event_data: dict[str, Any]) -> None:
    """Handle PlayerLeftRoom events by broadcasting updated occupant count."""
    from .connection_delegates import delegate_room_event_handler

    await delegate_room_event_handler(manager.room_event_handler, "handle_player_left_room", event_data)


# ============================================================================
# Utility Methods
# ============================================================================


def is_websocket_open_impl(_manager: Any, websocket: WebSocket) -> bool:
    """Check if a WebSocket is open."""
    try:
        from starlette.websockets import WebSocketState

        state = getattr(websocket, "application_state", None)
        return state != WebSocketState.DISCONNECTED
    except (AttributeError, ValueError, TypeError):
        return True


async def safe_close_websocket_impl(
    manager: Any, websocket: WebSocket, code: int = 1000, reason: str = "Connection closed"
) -> None:
    """Safely close a WebSocket connection."""
    import asyncio

    ws_id = id(websocket)
    if manager.is_websocket_closed(ws_id):
        return
    if not is_websocket_open_impl(manager, websocket):
        manager.mark_websocket_closed(ws_id)
        return
    try:
        await asyncio.wait_for(websocket.close(code=code, reason=reason), timeout=2.0)
    except (AttributeError, ValueError, TypeError, RuntimeError):
        pass
    finally:
        manager.mark_websocket_closed(ws_id)


# ============================================================================
# Compatibility and Room Methods
# ============================================================================


async def subscribe_to_room_impl(manager: Any, player_id: UUID, room_id: str) -> None:
    """Subscribe a player to a room (compatibility method)."""
    canonical_id = manager.canonical_room_id(room_id) or room_id
    return manager.room_manager.subscribe_to_room(str(player_id), canonical_id)


async def unsubscribe_from_room_impl(manager: Any, player_id: UUID, room_id: str) -> None:
    """Unsubscribe a player from a room (compatibility method)."""
    canonical_id = manager.canonical_room_id(room_id) or room_id
    return manager.room_manager.unsubscribe_from_room(str(player_id), canonical_id)


def canonical_room_id_public_impl(manager: Any, room_id: str | None) -> str | None:
    """Resolve a room id to the canonical Room.id value (public method)."""
    from .connection_room_utils import canonical_room_id_impl

    return canonical_room_id_impl(room_id, manager)


# ============================================================================
# Simple Getter/Setter Methods
# ============================================================================


def get_pending_messages_impl(manager: Any, player_id: UUID) -> list[dict[str, Any]]:
    """Get pending messages for a player."""
    return manager.message_queue.get_messages(str(player_id))


def convert_uuids_to_strings_impl(_manager: Any, obj: Any) -> Any:
    """Recursively convert UUID objects to strings for JSON serialization."""
    from .connection_helpers import convert_uuids_to_strings

    return convert_uuids_to_strings(obj)


def get_next_sequence_impl(manager: Any) -> int:
    """Get the next sequence number for events."""
    manager.sequence_counter += 1
    return manager.sequence_counter


# ============================================================================
# Event Subscription Methods
# ============================================================================


async def subscribe_to_room_events_impl(manager: Any) -> None:
    """Subscribe to room movement events for occupant broadcasting."""
    from .connection_event_helpers import subscribe_to_room_events_impl as subscribe_impl

    await subscribe_impl(manager)


async def unsubscribe_from_room_events_impl(manager: Any) -> None:
    """Unsubscribe from room movement events."""
    from .connection_event_helpers import unsubscribe_from_room_events_impl as unsubscribe_impl

    await unsubscribe_impl(manager)
