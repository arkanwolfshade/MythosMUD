"""
Connection cleanup and maintenance for connection management.

This module provides comprehensive cleanup operations including stale
connection removal, orphaned data cleanup, and ghost player removal.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Cleanup and maintenance is now a focused, independently testable component.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Connection cleanup requires many parameters for context and cleanup operations

import os
import time
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError

from ...structured_logging.enhanced_logging_config import get_logger


def _stale_prune_max_age_seconds() -> int:
    """Stale-prune threshold (seconds). Higher in e2e/local to avoid mid-run drops."""
    env = os.environ.get("LOGGING_ENVIRONMENT") or ""
    return 300 if env in ("e2e_test", "local") else 90


@dataclass
class CleanupContext:
    """Context for periodic cleanup checks. Groups parameters to stay under param-count limit."""

    online_players: dict[uuid.UUID, dict[str, Any]]
    last_seen: dict[uuid.UUID, float]
    player_websockets: dict[uuid.UUID, list[str]]
    active_websockets: dict[str, Any]
    connection_timestamps: dict[str, float]
    cleanup_stats: dict[str, Any]
    last_active_update_times: dict[uuid.UUID, float]
    connection_metadata: dict[str, Any] | None = None


if TYPE_CHECKING:
    from collections.abc import Awaitable

    from fastapi import WebSocket

    from ..memory_monitor import MemoryMonitor
    from ..message_queue import MessageQueue
    from ..rate_limiter import RateLimiter
    from ..room_subscription_manager import RoomSubscriptionManager

logger = get_logger(__name__)


class ConnectionCleaner:
    """
    Manages connection cleanup and maintenance operations.

    This class provides:
    - Stale player pruning
    - Orphaned data cleanup
    - Dead connection removal
    - Ghost player cleanup from rooms
    - Forced cleanup operations

    AI Agent: Single Responsibility - Connection cleanup and maintenance only.
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Connection cleaner initialization requires many service dependencies
        self,
        memory_monitor: "MemoryMonitor",
        rate_limiter: "RateLimiter",
        message_queue: "MessageQueue",
        room_manager: "RoomSubscriptionManager",
        cleanup_dead_websocket_callback: Callable[[uuid.UUID, str], "Awaitable[None]"],
        has_websocket_connection_callback: Callable[[uuid.UUID], bool],
        get_async_persistence: Callable[[], Any],
    ) -> None:
        """
        Initialize the connection cleaner.

        Args:
            memory_monitor: MemoryMonitor instance
            rate_limiter: RateLimiter instance
            message_queue: MessageQueue instance
            room_manager: RoomSubscriptionManager instance
            cleanup_dead_websocket_callback: Callback to cleanup dead WebSocket
            has_websocket_connection_callback: Callback to check if player has WebSocket connection
            get_async_persistence: Callback to get async persistence layer
        """
        self.memory_monitor = memory_monitor
        self.rate_limiter = rate_limiter
        self.message_queue = message_queue
        self.room_manager = room_manager
        self.cleanup_dead_websocket = cleanup_dead_websocket_callback
        self.has_websocket_connection = has_websocket_connection_callback
        self.get_async_persistence = get_async_persistence

    def _identify_stale_players(
        self, last_seen: dict[uuid.UUID, float], max_age_seconds: int, now_ts: float
    ) -> list[uuid.UUID]:
        """
        Identify players whose last_seen timestamp exceeds the max age.

        Args:
            last_seen: Last seen timestamps
            max_age_seconds: Maximum age in seconds
            now_ts: Current timestamp

        Returns:
            List of stale player IDs
        """
        stale_ids: list[uuid.UUID] = []
        for pid, last in list(last_seen.items()):
            if now_ts - last > max_age_seconds:
                stale_ids.append(pid)
        return stale_ids

    def _remove_stale_player_data(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Player data cleanup requires many parameters for context and cleanup operations
        self,
        pid: uuid.UUID,
        online_players: dict[uuid.UUID, dict[str, Any]],
        player_websockets: dict[uuid.UUID, list[str]],
        active_websockets: dict[str, "WebSocket"],
        last_seen: dict[uuid.UUID, float],
        last_active_update_times: dict[uuid.UUID, float],
    ) -> None:
        """
        Remove all data for a stale player.

        Args:
            pid: Player ID to remove
            online_players: Online players dictionary
            player_websockets: Player to WebSocket connection mapping
            active_websockets: Active WebSocket connections
            last_seen: Last seen timestamps
            last_active_update_times: Last active update times
        """
        if pid in online_players:
            del online_players[pid]
        if pid in player_websockets:
            conn_ids = player_websockets.pop(pid, None)
            if conn_ids:
                for conn_id in conn_ids:
                    if conn_id in active_websockets:
                        del active_websockets[conn_id]
        self.room_manager.remove_player_from_all_rooms(str(pid))
        if pid in last_seen:
            del last_seen[pid]
        last_active_update_times.pop(pid, None)
        self.rate_limiter.remove_player_data(str(pid))
        self.message_queue.remove_player_messages(str(pid))

    def prune_stale_players(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Player pruning requires many parameters for context and pruning operations
        self,
        last_seen: dict[uuid.UUID, float],
        online_players: dict[uuid.UUID, dict[str, Any]],
        player_websockets: dict[uuid.UUID, list[str]],
        active_websockets: dict[str, "WebSocket"],
        last_active_update_times: dict[uuid.UUID, float],
        max_age_seconds: int = 90,
    ) -> None:
        """
        Remove players whose presence is stale beyond the threshold.

        Args:
            last_seen: Last seen timestamps
            online_players: Online players dictionary
            player_websockets: Player to WebSocket connection mapping
            active_websockets: Active WebSocket connections
            last_active_update_times: Last active update times
            max_age_seconds: Maximum age in seconds before considering a player stale
        """
        try:
            now_ts = time.time()
            stale_ids = self._identify_stale_players(last_seen, max_age_seconds, now_ts)

            for pid in stale_ids:
                self._remove_stale_player_data(
                    pid, online_players, player_websockets, active_websockets, last_seen, last_active_update_times
                )

            if stale_ids:
                logger.info(
                    "Pruned stale players (debug: mid-run drops)",
                    disconnect_reason="stale_prune",
                    stale_ids=[str(pid) for pid in stale_ids],
                )
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error pruning stale players", error=str(e))

    def _identify_stale_connections(
        self,
        connection_timestamps: dict[str, float],
        now_ts: float,
    ) -> list[str]:
        """Return connection IDs that exceed max_connection_age."""
        stale: list[str] = []
        for connection_id, timestamp in list(connection_timestamps.items()):
            if now_ts - timestamp > self.memory_monitor.max_connection_age:
                stale.append(connection_id)
        return stale

    def _get_player_id_from_metadata(
        self,
        connection_metadata: dict[str, Any] | None,
        connection_id: str,
    ) -> Any:
        """Extract player_id from connection metadata if present."""
        if not connection_metadata or connection_id not in connection_metadata:
            return None
        meta = connection_metadata.get(connection_id)
        if meta is None or not hasattr(meta, "player_id"):
            return None
        return getattr(meta, "player_id", None)

    async def _close_and_remove_stale_websocket(
        self,
        connection_id: str,
        active_websockets: dict[str, "WebSocket"],
        connection_timestamps: dict[str, float],
        connection_metadata: dict[str, Any] | None,
    ) -> None:
        """Close stale WebSocket and remove from tracking. Handles None websocket defensively."""
        websocket = active_websockets.get(connection_id)
        if websocket is None:
            active_websockets.pop(connection_id, None)
            connection_timestamps.pop(connection_id, None)
            return
        player_id = self._get_player_id_from_metadata(connection_metadata, connection_id)
        logger.info(
            "Closing WebSocket due to connection timeout (debug: mid-run drops)",
            disconnect_reason="connection_timeout",
            connection_id=connection_id,
            player_id=str(player_id) if player_id is not None else None,
        )
        try:
            await websocket.close(code=1000, reason="Connection timeout")
            logger.info("Successfully closed stale WebSocket", connection_id=connection_id)
        except (DatabaseError, SQLAlchemyError) as e:
            logger.warning("Error closing stale connection", connection_id=connection_id, error=str(e))
        finally:
            active_websockets.pop(connection_id, None)
            connection_timestamps.pop(connection_id, None)

    async def cleanup_orphaned_data(
        self,
        connection_timestamps: dict[str, float],
        active_websockets: dict[str, "WebSocket"],
        cleanup_stats: dict[str, Any],
        connection_metadata: dict[str, Any] | None = None,
    ) -> None:
        """Clean up orphaned data that might accumulate over time.

        Args:
            connection_timestamps: Connection timestamp tracking
            active_websockets: Active WebSocket connections
            cleanup_stats: Cleanup statistics dictionary
            connection_metadata: Optional connection_id -> metadata (for disconnect_reason logging).
        """
        try:
            now_ts = time.time()
            cleanup_stats_local = {
                "orphaned_attempts": 0,
                "orphaned_messages": 0,
                "stale_connections": 0,
                "large_message_queues": 0,
                "large_rate_limits": 0,
            }

            # Clean up rate limiting data
            self.rate_limiter.cleanup_old_attempts()
            self.rate_limiter.cleanup_large_structures(self.memory_monitor.max_rate_limit_entries)

            # Clean up message queue data
            self.message_queue.cleanup_old_messages()
            self.message_queue.cleanup_large_structures(self.memory_monitor.max_pending_messages)

            # Clean up stale connections
            stale_connections = self._identify_stale_connections(connection_timestamps, now_ts)
            for connection_id in stale_connections:
                if connection_id not in active_websockets:
                    connection_timestamps.pop(connection_id, None)
                else:
                    await self._close_and_remove_stale_websocket(
                        connection_id, active_websockets, connection_timestamps, connection_metadata
                    )
                cleanup_stats_local["stale_connections"] += 1

            # Update cleanup stats
            cleanup_stats["cleanups_performed"] += 1
            self.memory_monitor.update_cleanup_time()

            if any(cleanup_stats_local.values()):
                logger.info("Memory cleanup completed", stale_connections=cleanup_stats_local["stale_connections"])

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error cleaning up orphaned data", error=str(e), exc_info=True)

    def _is_websocket_dead(self, websocket: "WebSocket") -> bool:
        """Return True if websocket appears dead (should be cleaned up)."""
        try:
            return websocket.client_state.name != "CONNECTED"
        except (RuntimeError, ConnectionError, AttributeError):
            return True

    def _get_players_to_check(
        self,
        player_id: uuid.UUID | None,
        player_websockets: dict[uuid.UUID, list[str]],
    ) -> list[uuid.UUID]:
        """Return list of player IDs to check (single player or all)."""
        if player_id:
            return [player_id]
        return list(player_websockets.keys())

    async def _cleanup_dead_connections_for_player(
        self,
        pid: uuid.UUID,
        player_websockets: dict[uuid.UUID, list[str]],
        active_websockets: dict[str, "WebSocket"],
        cleanup_results: dict[str, Any],
    ) -> None:
        """Clean up dead connections for a single player."""
        if pid not in player_websockets:
            return
        for connection_id in player_websockets[pid].copy():
            if connection_id not in active_websockets:
                continue
            websocket = active_websockets[connection_id]
            if not self._is_websocket_dead(websocket):
                continue
            logger.debug(
                "WebSocket cleanup check failed",
                player_id=pid,
                connection_id=connection_id,
                error="WebSocket not connected",
                error_type="ConnectionError",
            )
            await self.cleanup_dead_websocket(pid, connection_id)
            cleanup_results["connections_cleaned"] += 1

    async def cleanup_dead_connections(
        self,
        player_websockets: dict[uuid.UUID, list[str]],
        active_websockets: dict[str, "WebSocket"],
        player_id: uuid.UUID | None = None,
    ) -> dict[str, Any]:
        """
        Clean up dead connections for a specific player or all players.

        Args:
            player_websockets: Player to WebSocket connection mapping
            active_websockets: Active WebSocket connections
            player_id: Optional player ID to clean up. If None, cleans up all players.

        Returns:
            dict: Cleanup results
        """
        cleanup_results: dict[str, Any] = {"players_checked": 0, "connections_cleaned": 0, "errors": []}

        try:
            players_to_check = self._get_players_to_check(player_id, player_websockets)
            cleanup_results["players_checked"] = len(players_to_check)

            for pid in players_to_check:
                try:
                    await self._cleanup_dead_connections_for_player(
                        pid, player_websockets, active_websockets, cleanup_results
                    )
                except (DatabaseError, SQLAlchemyError) as e:
                    cleanup_results["errors"].append(f"Error cleaning player {pid}: {e}")

            logger.info("Connection cleanup completed", cleanup_results=cleanup_results)
            return cleanup_results

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error during connection cleanup", error=str(e))
            cleanup_results["errors"].append(str(e))
            return cleanup_results

    def _get_online_player_ids(self, online_players: dict[uuid.UUID, dict[str, Any]]) -> set[str]:
        """Return set of online player IDs as strings (room._players uses string UUIDs)."""
        return {str(pid) for pid in online_players.keys()}

    def _get_potential_ghost_players(self, room: Any, online_player_ids: set[str]) -> set[str]:
        """Return players in room but not online. Empty if room has no get_players."""
        if not hasattr(room, "get_players"):
            return set()
        room_player_ids = set(room.get_players())
        return room_player_ids - online_player_ids

    def _filter_actual_ghost_players(self, potential_ghost_players: set[str], room: Any) -> set[str]:
        """Filter to players with zero WebSocket connections (or invalid UUIDs)."""
        actual: set[str] = set()
        for ghost_player_id_str in potential_ghost_players:
            try:
                ghost_player_uuid = uuid.UUID(ghost_player_id_str)
                has_connections = self.has_websocket_connection(ghost_player_uuid)
                if not has_connections:
                    actual.add(ghost_player_id_str)
                else:
                    logger.debug(
                        "Player in room but not in online_players - keeping due to active connection",
                        player_id=ghost_player_id_str,
                        room_id=room.id,
                        has_websocket=has_connections,
                    )
            except (ValueError, AttributeError) as e:
                logger.warning(
                    "Invalid player ID format in room - removing",
                    player_id=ghost_player_id_str,
                    room_id=room.id,
                    error=str(e),
                )
                actual.add(ghost_player_id_str)
        return actual

    def _remove_ghost_players_from_room(self, room: Any, ghost_player_ids: set[str]) -> None:
        """Remove ghost players from room and log."""
        for ghost_player_id in ghost_player_ids:
            room.remove_player_silently(ghost_player_id)
            logger.debug(
                "DEBUG: Removed actual ghost player from room",
                ghost_player_id=ghost_player_id,
                room_id=room.id,
            )

    def cleanup_ghost_players(self, online_players: dict[uuid.UUID, dict[str, Any]]) -> None:
        """
        Clean up ghost players from all rooms.

        This method removes players from room's internal _players set
        if they are no longer in the online_players set.

        Args:
            online_players: Online players dictionary
        """
        try:
            async_persistence = self.get_async_persistence()
            if not async_persistence or not hasattr(async_persistence, "list_rooms"):
                return

            online_player_ids = self._get_online_player_ids(online_players)

            for room in async_persistence.list_rooms():
                potential = self._get_potential_ghost_players(room, online_player_ids)
                if not potential:
                    continue
                actual = self._filter_actual_ghost_players(potential, room)
                if not actual:
                    continue
                logger.debug(
                    "DEBUG: Found actual ghost players in room",
                    room_id=room.id,
                    ghost_players=actual,
                )
                self._remove_ghost_players_from_room(room, actual)

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error cleaning up ghost players", error=str(e), exc_info=True)

    async def force_cleanup(
        self,
        cleanup_stats: dict[str, Any],
        cleanup_orphaned_data_callback: Callable[[], "Awaitable[None]"],
        prune_stale_players_callback: Callable[[int], None],
    ) -> None:
        """
        Force immediate cleanup of all orphaned data.

        Args:
            cleanup_stats: Cleanup statistics dictionary
            cleanup_orphaned_data_callback: Callback to cleanup orphaned data
            prune_stale_players_callback: Callback to prune stale players
        """
        try:
            logger.info("Forcing immediate cleanup")

            # Cancel any running cleanup tasks - handled by caller if needed

            await cleanup_orphaned_data_callback()
            prune_stale_players_callback(_stale_prune_max_age_seconds())
            self.memory_monitor.force_garbage_collection()
            cleanup_stats["cleanups_performed"] += 1
            self.memory_monitor.update_cleanup_time()
            logger.info("Force cleanup completed")
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error during force cleanup", error=str(e), exc_info=True)

    async def check_and_cleanup(self, ctx: CleanupContext) -> None:
        """
        Periodically check for cleanup conditions and perform cleanup if needed.

        Args:
            ctx: Cleanup context (online_players, last_seen, player_websockets,
                 active_websockets, connection_timestamps, cleanup_stats,
                 last_active_update_times, connection_metadata).
        """
        if self.memory_monitor.should_cleanup():
            logger.info("MemoryMonitor triggered cleanup.")
            ctx.cleanup_stats["memory_cleanups"] += 1
            ctx.cleanup_stats["last_cleanup"] = time.time()
            await self.cleanup_orphaned_data(
                ctx.connection_timestamps,
                ctx.active_websockets,
                ctx.cleanup_stats,
                ctx.connection_metadata,
            )
            self.prune_stale_players(
                ctx.last_seen,
                ctx.online_players,
                ctx.player_websockets,
                ctx.active_websockets,
                ctx.last_active_update_times,
                max_age_seconds=_stale_prune_max_age_seconds(),
            )
            self.memory_monitor.force_garbage_collection()
            logger.info("Cleanup complete.")
