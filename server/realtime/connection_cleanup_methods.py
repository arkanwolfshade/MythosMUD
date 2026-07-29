"""
Cleanup method implementations for ConnectionManager.

Thin wrappers that delegate to ConnectionCleaner via connection_delegates.
"""

from typing import Any
from uuid import UUID

from ..structured_logging.enhanced_logging_config import get_logger
from .connection_delegates import delegate_connection_cleaner, delegate_connection_cleaner_sync
from .maintenance.connection_cleaner import CleanupContext
from .player_disconnect_handlers import age_off_disconnected_sessions

logger = get_logger(__name__)


async def cleanup_dead_connections_impl(manager: Any, player_id: UUID | None = None) -> dict[str, Any]:
    """Clean up dead connections for a specific player or all players."""
    return await delegate_connection_cleaner(
        manager.connection_cleaner,
        "cleanup_dead_connections",
        {
            "players_checked": 0,
            "connections_cleaned": 0,
            "errors": ["Connection cleaner not initialized"],
        },
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
        manager.connection_cleaner,
        "cleanup_ghost_players",
        online_players=manager.online_players,
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
