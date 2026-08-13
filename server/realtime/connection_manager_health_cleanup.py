"""
Health checks, error handling, and cleanup helpers for ConnectionManager.

Extracted from connection_manager_methods to keep file NLOC under lizard limits.
"""

from typing import Any, cast
from uuid import UUID

from ..structured_logging.enhanced_logging_config import get_logger
from .connection_delegates import (
    delegate_connection_cleaner,
    delegate_connection_cleaner_sync,
    delegate_error_handler,
    delegate_health_monitor,
    delegate_health_monitor_sync,
)
from .maintenance.connection_cleaner import CleanupContext
from .player_disconnect_handlers import age_off_disconnected_sessions

logger = get_logger(__name__)

# ============================================================================
# Health Check Methods
# ============================================================================


async def check_connection_health_impl(manager: Any, player_id: UUID) -> dict[str, Any]:
    """Check the health of all connections for a player."""
    if manager.health_monitor is None:
        logger.error("Health monitor not initialized")
        return {"player_id": player_id, "overall_health": "error"}
    method = manager.health_monitor.check_player_connection_health
    result: dict[str, Any] = cast(
        dict[str, Any],
        await method(
            player_id=player_id,
            player_websockets=manager.player_websockets,
            active_websockets=manager.active_websockets,
        ),
    )
    return result


async def _check_connection_health_impl(manager: Any) -> None:
    """Check health of all connections and clean up stale/dead ones."""
    await delegate_health_monitor(
        manager.health_monitor,
        "check_all_connections_health",
        manager.active_websockets,
        manager.connection_metadata,
        manager.player_websockets,
    )


async def _periodic_health_check_impl(manager: Any) -> None:
    """Periodic health check task that runs continuously."""
    await delegate_health_monitor(
        manager.health_monitor,
        "periodic_health_check_task",
        manager.active_websockets,
        manager.connection_metadata,
        manager.player_websockets,
    )


def start_health_checks_impl(manager: Any) -> None:
    """Start the periodic health check task."""
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
    return await delegate_error_handler(
        manager.error_handler,
        "recover_from_error",
        {"player_id": player_id, "success": False, "errors": ["Error handler not initialized"]},
        player_id,
        recovery_type,
    )


# ============================================================================
# Cleanup Methods
# ============================================================================


async def cleanup_dead_connections_impl(manager: Any, player_id: UUID | None = None) -> dict[str, Any]:
    """Clean up dead connections for a specific player or all players."""
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
    ctx = CleanupContext(
        online_players=manager.online_players,
        last_seen=manager.last_seen,
        player_websockets=manager.player_websockets,
        active_websockets=manager.active_websockets,
        connection_timestamps=manager.connection_timestamps,
        cleanup_stats=manager.cleanup_stats,
        last_active_update_times=manager.last_active_update_times,
        connection_metadata=manager.connection_metadata,
    )
    await delegate_connection_cleaner(manager.connection_cleaner, "check_and_cleanup", {}, ctx=ctx)


async def force_cleanup_impl(manager: Any) -> None:
    """Force immediate cleanup of all orphaned data."""
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
    delegate_connection_cleaner_sync(
        manager.connection_cleaner, "cleanup_ghost_players", online_players=manager.online_players
    )


def prune_stale_players_impl(manager: Any, max_age_seconds: int = 90) -> None:
    """Remove players whose presence is stale beyond the threshold."""
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
    aged = age_off_disconnected_sessions(manager)
    if aged:
        logger.debug("Aged off disconnected sessions", count=aged)

    await delegate_connection_cleaner(
        manager.connection_cleaner,
        "cleanup_orphaned_data",
        {},
        connection_timestamps=manager.connection_timestamps,
        active_websockets=manager.active_websockets,
        cleanup_stats=manager.cleanup_stats,
        connection_metadata=manager.connection_metadata,
    )
