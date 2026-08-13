"""
Extracted methods from ConnectionManager for better code organization.

This module contains methods that were extracted from ConnectionManager
to reduce file complexity and improve maintainability.
"""

# pylint: disable=too-many-lines  # Reason: Connection manager methods require extensive method implementations for comprehensive connection management operations

from typing import Any, cast
from uuid import UUID

from fastapi import WebSocket

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


# ============================================================================
# Statistics Methods
# ============================================================================


def get_memory_stats_impl(manager: Any) -> dict[str, Any]:
    """Get comprehensive memory and connection statistics."""
    result: dict[str, Any] = cast(
        dict[str, Any],
        manager.statistics_aggregator.get_memory_stats(
            active_websockets=manager.active_websockets,
            player_websockets=manager.player_websockets,
            connection_timestamps=manager.connection_timestamps,
            cleanup_stats=manager.cleanup_stats,
            player_sessions=manager.player_sessions,
            session_connections=manager.session_connections,
            online_players=manager.online_players,
            last_seen=manager.last_seen,
            closed_websockets_count=manager.get_closed_websockets_count(),
            connection_metadata=manager.connection_metadata,
        ),
    )
    return result


def get_dual_connection_stats_impl(manager: Any) -> dict[str, Any]:
    """Get comprehensive connection statistics."""
    result: dict[str, Any] = cast(
        dict[str, Any],
        manager.statistics_aggregator.get_connection_stats(
            player_websockets=manager.player_websockets,
            connection_metadata=manager.connection_metadata,
            session_connections=manager.session_connections,
            player_sessions=manager.player_sessions,
        ),
    )
    return result


def get_connection_health_stats_impl(manager: Any) -> dict[str, Any]:
    """Get comprehensive connection health statistics."""
    result: dict[str, Any] = cast(
        dict[str, Any],
        manager.statistics_aggregator.get_connection_health_stats(connection_metadata=manager.connection_metadata),
    )
    return result


def get_memory_alerts_impl(manager: Any) -> list[str]:
    """Get memory-related alerts."""
    result: list[str] = cast(
        list[str],
        manager.statistics_aggregator.get_memory_alerts(
            connection_timestamps=manager.connection_timestamps,
            max_connection_age=manager.memory_monitor.max_connection_age,
        ),
    )
    return result


def get_error_statistics_impl(manager: Any) -> dict[str, Any]:
    """Get error handling statistics."""
    if manager.error_handler is None:
        logger.error("Error handler not initialized")
        return {}
    result: dict[str, Any] = cast(
        dict[str, Any],
        manager.error_handler.get_error_statistics(
            online_players=manager.online_players, player_websockets=manager.player_websockets
        ),
    )
    return result


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


# ============================================================================
# Presence and Player Info Methods
# ============================================================================


def get_player_websocket_connection_id_impl(manager: Any, player_id: UUID) -> str | None:
    """Get the first WebSocket connection ID for a player (backward compatibility)."""
    if player_id in manager.player_websockets and manager.player_websockets[player_id]:
        result: str = cast(str, manager.player_websockets[player_id][0])
        return result
    return None


def get_connection_id_from_websocket_impl(manager: Any, websocket: WebSocket) -> str | None:
    """Get connection ID from a WebSocket instance."""
    for conn_id, ws in manager.active_websockets.items():
        if ws is websocket:
            result: str = cast(str, conn_id)
            return result
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
    manager: Any, event_type: str, room_id: str, data: dict[str, object]
) -> dict[str, Any]:
    """Broadcast a room-specific event to all players in the room."""
    try:
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


async def broadcast_global_event_impl(manager: Any, event_type: str, data: dict[str, object]) -> dict[str, Any]:
    """Broadcast a global event to all connected players."""
    try:
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
    try:
        logger.info("Force disconnecting player from all connections", player_id=player_id)
        if player_id in manager.player_websockets:
            await manager.disconnect_websocket(player_id, is_force_disconnect=True)
        logger.info("Player force disconnected from all connections", player_id=player_id)
    except (DatabaseError, AttributeError) as e:
        logger.error("Error force disconnecting player", player_id=player_id, error=str(e), exc_info=True)
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: peer-closed WebSocket errors must not abort force disconnect API
        logger.error(
            "Error force disconnecting player",
            player_id=player_id,
            error=str(e),
            error_type=type(e).__name__,
            exc_info=True,
        )


async def disconnect_websocket_connection_impl(manager: Any, player_id: UUID, connection_id: str) -> bool:
    """Disconnect a specific WebSocket connection for a player."""
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
        result: bool = cast(bool, await manager.disconnect_connection_by_id(connection_id))
        return result
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
# Game State Provider Methods
# ============================================================================


async def get_player_impl(manager: Any, player_id: UUID) -> Any:
    """Get a player from the persistence layer (async version)."""
    from .connection_delegates import delegate_game_state_provider

    return await delegate_game_state_provider(manager.game_state_provider, "get_player", None, player_id)


async def get_players_batch_impl(manager: Any, player_ids: list[UUID]) -> dict[UUID, Any]:
    """Get multiple players from the persistence layer in a single batch operation."""
    from .connection_delegates import delegate_game_state_provider

    result: dict[UUID, Any] = cast(
        dict[UUID, Any],
        await delegate_game_state_provider(manager.game_state_provider, "get_players_batch", {}, player_ids),
    )
    return result


async def convert_room_players_uuids_to_names_impl(manager: Any, room_data: dict[str, Any]) -> dict[str, Any]:
    """Convert player UUIDs and NPC IDs in room_data to names."""
    from .connection_delegates import delegate_game_state_provider

    result: dict[str, Any] = cast(
        dict[str, Any],
        await delegate_game_state_provider(
            manager.game_state_provider, "convert_room_uuids_to_names", room_data, room_data
        ),
    )
    return result


def get_npcs_batch_impl(manager: Any, npc_ids: list[str]) -> dict[str, str]:
    """Get NPC names for multiple NPCs in a batch operation."""
    from .connection_delegates import delegate_game_state_provider_sync

    result: dict[str, str] = cast(
        dict[str, str],
        delegate_game_state_provider_sync(manager.game_state_provider, "get_npcs_batch", {}, npc_ids),
    )
    return result


async def get_room_occupants_impl(manager: Any, room_id: str) -> list[dict[str, Any]]:
    """Get list of occupants in a room."""
    from .connection_delegates import delegate_game_state_provider

    result: list[dict[str, Any]] = cast(
        list[dict[str, Any]],
        await delegate_game_state_provider(
            manager.game_state_provider,
            "get_room_occupants",
            [],
            room_id=room_id,
            online_players=manager.online_players,
        ),
    )
    return result


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
    """Safely close a WebSocket connection.

    Must never raise: logout force-disconnect continues room cleanup and
    player_left_game after close; re-raises leave players linkdead without
    leave announcements (seen in e2e disconnect specs).
    """
    import asyncio

    from .websocket_helpers import is_client_disconnected_exception

    ws_id = id(websocket)
    if manager.is_websocket_closed(ws_id):
        return
    if not is_websocket_open_impl(manager, websocket):
        manager.mark_websocket_closed(ws_id)
        return
    try:
        await asyncio.wait_for(websocket.close(code=code, reason=reason), timeout=2.0)
    except Exception as exc:  # pylint: disable=broad-exception-caught  # Reason: close of a dead peer must not abort disconnect cleanup; any failure means socket is already gone
        if not is_client_disconnected_exception(exc) and not isinstance(
            exc, (AttributeError, ValueError, TypeError, RuntimeError, TimeoutError)
        ):
            logger.debug(
                "WebSocket close failed; treating as closed",
                error=str(exc),
                error_type=type(exc).__name__,
            )
    finally:
        manager.mark_websocket_closed(ws_id)


# ============================================================================
# Compatibility and Room Methods
# ============================================================================


async def subscribe_to_room_impl(manager: Any, player_id: UUID, room_id: str) -> None:
    """Subscribe a player to a room (compatibility method)."""
    canonical_id = manager.canonical_room_id(room_id) or room_id
    result: None = cast(None, manager.room_manager.subscribe_to_room(str(player_id), canonical_id))
    return result


async def unsubscribe_from_room_impl(manager: Any, player_id: UUID, room_id: str) -> None:
    """Unsubscribe a player from a room (compatibility method)."""
    canonical_id = manager.canonical_room_id(room_id) or room_id
    result: None = cast(None, manager.room_manager.unsubscribe_from_room(str(player_id), canonical_id))
    return result


def canonical_room_id_public_impl(manager: Any, room_id: str | None) -> str | None:
    """Resolve a room id to the canonical Room.id value (public method)."""
    from .connection_room_utils import canonical_room_id_impl

    return canonical_room_id_impl(room_id, manager)


# ============================================================================
# Simple Getter/Setter Methods
# ============================================================================


def convert_uuids_to_strings_impl(_manager: Any, obj: Any) -> Any:
    """Recursively convert UUID objects to strings for JSON serialization."""
    from .connection_helpers import convert_uuids_to_strings

    return convert_uuids_to_strings(obj)


def get_next_sequence_impl(manager: Any) -> int:
    """Get the next sequence number for events."""
    manager.sequence_counter += 1
    result: int = cast(int, manager.sequence_counter)
    return result


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
