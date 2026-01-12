"""
Connection cleanup and maintenance for connection management.

This module provides comprehensive cleanup operations including stale
connection removal, orphaned data cleanup, and ghost player removal.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Cleanup and maintenance is now a focused, independently testable component.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Connection cleanup requires many parameters for context and cleanup operations

import time
import uuid
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError

from ...structured_logging.enhanced_logging_config import get_logger

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
                logger.info("Pruned stale players", stale_ids=[str(pid) for pid in stale_ids])
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error pruning stale players", error=str(e))

    async def cleanup_orphaned_data(
        self,
        connection_timestamps: dict[str, float],
        active_websockets: dict[str, "WebSocket"],
        cleanup_stats: dict[str, Any],
    ) -> None:
        """Clean up orphaned data that might accumulate over time.

        Args:
            connection_timestamps: Connection timestamp tracking
            active_websockets: Active WebSocket connections
            cleanup_stats: Cleanup statistics dictionary
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
            stale_connections = []
            for connection_id, timestamp in list(connection_timestamps.items()):
                connection_age = now_ts - timestamp
                if connection_age > self.memory_monitor.max_connection_age:
                    logger.info(
                        "DEBUG: Connection is stale",
                        connection_id=connection_id,
                        connection_age=connection_age,
                        max_connection_age=self.memory_monitor.max_connection_age,
                    )
                    stale_connections.append(connection_id)

            for connection_id in stale_connections:
                if connection_id in active_websockets:
                    try:
                        websocket = active_websockets[connection_id]
                        # Guard against None websocket (can happen during cleanup)
                        # JUSTIFICATION: Type annotation says dict[str, WebSocket], but runtime can have None
                        # values during cleanup/race conditions. This is defensive programming.
                        if websocket is None:
                            del active_websockets[connection_id]  # type: ignore[unreachable]
                            continue
                        logger.info("DEBUG: Closing stale WebSocket due to timeout", connection_id=connection_id)
                        await websocket.close(code=1000, reason="Connection timeout")
                        logger.info("Successfully closed stale WebSocket", connection_id=connection_id)
                    except (DatabaseError, SQLAlchemyError) as e:
                        logger.warning("Error closing stale connection", connection_id=connection_id, error=str(e))
                    del active_websockets[connection_id]
                del connection_timestamps[connection_id]
                cleanup_stats_local["stale_connections"] += 1

            # Update cleanup stats
            cleanup_stats["cleanups_performed"] += 1
            self.memory_monitor.update_cleanup_time()

            if any(cleanup_stats_local.values()):
                logger.info("Memory cleanup completed", stale_connections=cleanup_stats_local["stale_connections"])

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error cleaning up orphaned data", error=str(e), exc_info=True)

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

        try:  # pylint: disable=too-many-nested-blocks  # Reason: Connection cleanup requires complex nested logic for player iteration, connection validation, and error handling
            if player_id:
                # Clean up specific player
                players_to_check = [player_id]
            else:
                # Clean up all players
                players_to_check = list(player_websockets.keys())

            cleanup_results["players_checked"] = len(players_to_check)

            for pid in players_to_check:
                try:
                    # Check WebSocket connections
                    if pid in player_websockets:
                        connection_ids = player_websockets[pid].copy()
                        for connection_id in connection_ids:
                            if connection_id in active_websockets:
                                websocket = active_websockets[connection_id]
                                try:
                                    # Check WebSocket health by checking its state
                                    if websocket.client_state.name != "CONNECTED":
                                        raise ConnectionError("WebSocket not connected")
                                except (RuntimeError, ConnectionError, AttributeError) as e:
                                    logger.debug(
                                        "WebSocket cleanup check failed",
                                        player_id=pid,
                                        connection_id=connection_id,
                                        error=str(e),
                                        error_type=type(e).__name__,
                                    )
                                    # Connection is dead, clean it up
                                    await self.cleanup_dead_websocket(pid, connection_id)
                                    cleanup_results["connections_cleaned"] += 1
                except (DatabaseError, SQLAlchemyError) as e:
                    cleanup_results["errors"].append(f"Error cleaning player {pid}: {e}")

            logger.info("Connection cleanup completed", cleanup_results=cleanup_results)
            return cleanup_results

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error during connection cleanup", error=str(e))
            cleanup_results["errors"].append(str(e))
            return cleanup_results

    def cleanup_ghost_players(self, online_players: dict[uuid.UUID, dict[str, Any]]) -> None:
        """
        Clean up ghost players from all rooms.

        This method removes players from room's internal _players set
        if they are no longer in the online_players set.

        Args:
            online_players: Online players dictionary
        """
        try:  # pylint: disable=too-many-nested-blocks  # Reason: Room cleanup requires complex nested logic for persistence validation, room iteration, and player tracking
            async_persistence = self.get_async_persistence()
            if not async_persistence or not hasattr(async_persistence, "list_rooms"):
                return

            # Get all online player IDs (convert to strings for comparison with room._players)
            # CRITICAL FIX: room._players uses string UUIDs, online_players.keys() uses UUID objects
            # We must convert to the same type for set comparison to work correctly
            online_player_ids = {str(pid) for pid in online_players.keys()}

            # Get all rooms from the room cache
            for room in async_persistence.list_rooms():
                if not hasattr(room, "get_players"):
                    continue

                _room_id = room.id

                # Get players in this room (already strings)
                room_player_ids = set(room.get_players())

                # Find ghost players (players in room but not online)
                # Both sets are now strings, so comparison will work correctly
                potential_ghost_players = room_player_ids - online_player_ids

                if potential_ghost_players:
                    # CRITICAL FIX: Before removing players, verify they actually have NO connections
                    # A player might be in room._players but not in online_players during a race condition
                    # (e.g., during movement, or between connection setup steps)
                    # Only remove players who have ZERO WebSocket connections
                    actual_ghost_players = set()
                    for ghost_player_id_str in potential_ghost_players:
                        try:
                            ghost_player_uuid = uuid.UUID(ghost_player_id_str)
                            # Check if player has ANY WebSocket connections
                            has_connections = self.has_websocket_connection(ghost_player_uuid)
                            if not has_connections:
                                actual_ghost_players.add(ghost_player_id_str)
                            else:
                                logger.debug(
                                    "Player in room but not in online_players - keeping due to active connection",
                                    player_id=ghost_player_id_str,
                                    room_id=room.id,
                                    has_websocket=has_connections,
                                )
                        except (ValueError, AttributeError) as e:
                            # If we can't parse the UUID, it's definitely a ghost
                            logger.warning(
                                "Invalid player ID format in room - removing",
                                player_id=ghost_player_id_str,
                                room_id=room.id,
                                error=str(e),
                            )
                            actual_ghost_players.add(ghost_player_id_str)

                    if actual_ghost_players:
                        logger.debug(
                            "DEBUG: Found actual ghost players in room",
                            room_id=room.id,
                            ghost_players=actual_ghost_players,
                        )
                        for ghost_player_id in actual_ghost_players:
                            room.remove_player_silently(ghost_player_id)
                            logger.debug(
                                "DEBUG: Removed actual ghost player from room",
                                ghost_player_id=ghost_player_id,
                                room_id=room.id,
                            )

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
            prune_stale_players_callback(90)  # Default 90 seconds
            self.memory_monitor.force_garbage_collection()
            cleanup_stats["cleanups_performed"] += 1
            self.memory_monitor.update_cleanup_time()
            logger.info("Force cleanup completed")
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error during force cleanup", error=str(e), exc_info=True)

    async def check_and_cleanup(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Cleanup checking requires many parameters for context and cleanup operations
        self,
        online_players: dict[uuid.UUID, dict[str, Any]],
        last_seen: dict[uuid.UUID, float],
        player_websockets: dict[uuid.UUID, list[str]],
        active_websockets: dict[str, "WebSocket"],
        connection_timestamps: dict[str, float],
        cleanup_stats: dict[str, Any],
        last_active_update_times: dict[uuid.UUID, float],
    ) -> None:
        """
        Periodically check for cleanup conditions and perform cleanup if needed.

        Args:
            online_players: Online players dictionary
            last_seen: Last seen timestamps
            player_websockets: Player to WebSocket connection mapping
            active_websockets: Active WebSocket connections
            connection_timestamps: Connection timestamp tracking
            cleanup_stats: Cleanup statistics dictionary
            last_active_update_times: Last active update times
        """
        if self.memory_monitor.should_cleanup():
            logger.info("MemoryMonitor triggered cleanup.")
            cleanup_stats["memory_cleanups"] += 1
            cleanup_stats["last_cleanup"] = time.time()
            await self.cleanup_orphaned_data(connection_timestamps, active_websockets, cleanup_stats)
            self.prune_stale_players(
                last_seen,
                online_players,
                player_websockets,
                active_websockets,
                last_active_update_times,
            )
            self.memory_monitor.force_garbage_collection()
            logger.info("Cleanup complete.")
