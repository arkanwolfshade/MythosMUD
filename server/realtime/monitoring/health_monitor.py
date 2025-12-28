"""
Health monitoring for connection management.

This module provides comprehensive connection health checking including
WebSocket state verification, token validation, and proactive cleanup of
stale connections.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Health monitoring is now a focused, independently testable component.
"""

import asyncio
import time
import uuid
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from ...structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from collections.abc import Awaitable

    from fastapi import WebSocket

    from ..connection_manager import ConnectionMetadata
    from .performance_tracker import PerformanceTracker

logger = get_logger(__name__)


class HealthMonitor:
    """
    Monitors connection health and manages periodic health checks.

    This class provides:
    - Periodic connection health verification
    - WebSocket state checking
    - Token revalidation
    - Stale connection detection
    - Automatic cleanup of dead connections
    - Background health check task management

    AI Agent: Single Responsibility - Connection health monitoring only.
    """

    def __init__(
        self,
        is_websocket_open_callback: Callable[["WebSocket"], bool],
        validate_token_callback: Callable[[str, uuid.UUID], "Awaitable[bool]"],
        cleanup_dead_websocket_callback: Callable[[uuid.UUID, str], "Awaitable[None]"],
        performance_tracker: "PerformanceTracker",
        health_check_interval: float = 30.0,
        connection_timeout: float = 300.0,
        token_revalidation_interval: float = 300.0,
    ) -> None:
        """
        Initialize the health monitor.

        Args:
            is_websocket_open_callback: Callback to check if WebSocket is open
            validate_token_callback: Callback to validate JWT token
            cleanup_dead_websocket_callback: Callback to cleanup dead WebSocket
            performance_tracker: PerformanceTracker instance for metrics
            health_check_interval: Interval between health checks in seconds
            connection_timeout: Connection timeout threshold in seconds
            token_revalidation_interval: Token revalidation interval in seconds
        """
        self.is_websocket_open = is_websocket_open_callback
        self.validate_token = validate_token_callback
        self.cleanup_dead_websocket = cleanup_dead_websocket_callback
        self.performance_tracker = performance_tracker

        self.health_check_interval = health_check_interval
        self.connection_timeout = connection_timeout
        self.token_revalidation_interval = token_revalidation_interval

        self._health_check_task: Any | None = None

    async def check_player_connection_health(
        self,
        player_id: uuid.UUID,
        player_websockets: dict[uuid.UUID, list[str]],
        active_websockets: dict[str, "WebSocket"],
    ) -> dict[str, Any]:
        """
        Check the health of all connections for a player.

        Args:
            player_id: The player's ID
            player_websockets: Player to WebSocket connection mapping
            active_websockets: Active WebSocket connections

        Returns:
            dict: Connection health information
        """
        health_status: dict[str, Any] = {
            "player_id": player_id,
            "websocket_healthy": 0,
            "websocket_unhealthy": 0,
            "overall_health": "unknown",
        }

        try:
            # Check WebSocket connections
            if player_id in player_websockets:
                connection_ids = player_websockets[player_id].copy()
                for connection_id in connection_ids:
                    if connection_id in active_websockets:
                        websocket = active_websockets[connection_id]
                        # Guard against None websocket (can happen during cleanup)
                        # JUSTIFICATION: Type annotation says dict[str, WebSocket], but runtime can have None
                        # values during cleanup/race conditions. This is defensive programming.
                        if websocket is None:
                            continue  # type: ignore[unreachable]
                        try:
                            # Check WebSocket health by checking its state
                            if websocket.client_state.name == "CONNECTED":
                                health_status["websocket_healthy"] += 1
                            else:
                                raise ConnectionError("WebSocket not connected")
                        except (RuntimeError, ConnectionError, AttributeError) as e:
                            logger.error(
                                "WebSocket health check failed",
                                player_id=player_id,
                                connection_id=connection_id,
                                error=str(e),
                                error_type=type(e).__name__,
                            )
                            health_status["websocket_unhealthy"] += 1
                            # Clean up unhealthy connection
                            await self.cleanup_dead_websocket(player_id, connection_id)

            # Determine overall health
            total_healthy = health_status["websocket_healthy"]
            total_connections = total_healthy + health_status["websocket_unhealthy"]

            if total_connections == 0:
                health_status["overall_health"] = "no_connections"
            elif health_status["websocket_unhealthy"] == 0:
                health_status["overall_health"] = "healthy"
            elif total_healthy > 0:
                health_status["overall_health"] = "degraded"
            else:
                health_status["overall_health"] = "unhealthy"

            return health_status

        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors in health monitoring
            logger.error("Error checking connection health", player_id=player_id, error=str(e))
            health_status["overall_health"] = "error"
            return health_status

    async def check_all_connections_health(
        self,
        active_websockets: dict[str, "WebSocket"],
        connection_metadata: dict[str, "ConnectionMetadata"],
        player_websockets: dict[uuid.UUID, list[str]],
    ) -> None:
        """
        Check health of all connections and clean up stale/dead ones.

        This method:
        - Verifies WebSocket state for all active connections
        - Detects stale connections based on last_seen timestamps
        - Cleans up dead connections proactively
        - Updates connection metadata health status

        Args:
            active_websockets: Active WebSocket connections
            connection_metadata: Connection metadata
            player_websockets: Player to WebSocket connection mapping

        AI: Periodic health checks prevent memory leaks from dead connections.
        """
        start_time = time.time()
        try:
            now = time.time()
            stale_connections: list[tuple[uuid.UUID, str]] = []  # (player_id, connection_id)

            # Check WebSocket connections
            for connection_id, websocket in list(active_websockets.items()):
                try:
                    # Get connection metadata
                    metadata = connection_metadata.get(connection_id)
                    if not metadata:
                        # Missing metadata - mark for cleanup
                        # Try to find player_id from player_websockets mapping
                        player_id_for_cleanup: uuid.UUID | None = None
                        for pid, conn_ids in player_websockets.items():
                            if connection_id in conn_ids:
                                player_id_for_cleanup = pid
                                break
                        if player_id_for_cleanup is not None:
                            stale_connections.append((player_id_for_cleanup, connection_id))
                        continue

                    # Check if connection is stale (no activity for timeout period)
                    time_since_last_seen = now - metadata.last_seen
                    if time_since_last_seen > self.connection_timeout:
                        logger.debug(
                            "Connection marked as stale",
                            connection_id=connection_id,
                            player_id=metadata.player_id,
                            seconds_idle=time_since_last_seen,
                        )
                        stale_connections.append((metadata.player_id, connection_id))
                        metadata.is_healthy = False
                        continue

                    # Verify WebSocket is actually open
                    if not self.is_websocket_open(websocket):
                        logger.debug(
                            "WebSocket not open, marking for cleanup",
                            connection_id=connection_id,
                            player_id=metadata.player_id,
                        )
                        stale_connections.append((metadata.player_id, connection_id))
                        metadata.is_healthy = False
                        continue

                    # Check token validity if token exists and revalidation interval has passed
                    if metadata.token and metadata.last_token_validation:
                        time_since_validation = now - metadata.last_token_validation
                        if time_since_validation >= self.token_revalidation_interval:
                            if not await self.validate_token(metadata.token, metadata.player_id):
                                logger.warning(
                                    "Token validation failed during health check",
                                    connection_id=connection_id,
                                    player_id=metadata.player_id,
                                )
                                stale_connections.append((metadata.player_id, connection_id))
                                metadata.is_healthy = False
                                continue
                            else:
                                # Update last validation time
                                metadata.last_token_validation = now
                                logger.debug(
                                    "Token revalidated successfully",
                                    connection_id=connection_id,
                                    player_id=metadata.player_id,
                                )

                    # Connection is healthy
                    metadata.is_healthy = True

                except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors in health monitoring
                    logger.warning(
                        "Error checking connection health",
                        connection_id=connection_id,
                        error=str(e),
                    )
                    # Mark for cleanup on error
                    metadata = connection_metadata.get(connection_id)
                    if metadata:
                        stale_connections.append((metadata.player_id, connection_id))
                        metadata.is_healthy = False

            # Clean up stale connections
            if stale_connections:
                logger.info(
                    "Cleaning up stale connections from health check",
                    stale_count=len(stale_connections),
                )
                for player_id, connection_id in stale_connections:
                    try:
                        await self.cleanup_dead_websocket(player_id, connection_id)
                    except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors during cleanup
                        logger.error(
                            "Error cleaning up stale connection",
                            player_id=player_id,
                            connection_id=connection_id,
                            error=str(e),
                        )

            # Update performance stats
            duration_ms = (time.time() - start_time) * 1000
            self.performance_tracker.record_health_check(duration_ms)

            logger.debug(
                "Connection health check completed",
                duration_ms=duration_ms,
                stale_connections_cleaned=len(stale_connections),
            )

        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors in health monitoring
            logger.error("Error in connection health check", error=str(e), exc_info=True)

    async def periodic_health_check_task(
        self,
        active_websockets: dict[str, "WebSocket"],
        connection_metadata: dict[str, "ConnectionMetadata"],
        player_websockets: dict[uuid.UUID, list[str]],
    ) -> None:
        """
        Periodic health check task that runs continuously.

        This task:
        - Runs health checks at configured intervals
        - Handles cancellation gracefully
        - Logs health check statistics

        Args:
            active_websockets: Active WebSocket connections (shared reference)
            connection_metadata: Connection metadata (shared reference)
            player_websockets: Player to WebSocket connection mapping (shared reference)

        AI: Background task for proactive connection health monitoring.
        """
        logger.info(
            "Starting periodic connection health checks",
            interval_seconds=self.health_check_interval,
            connection_timeout_seconds=self.connection_timeout,
        )

        try:
            while True:
                await asyncio.sleep(self.health_check_interval)
                await self.check_all_connections_health(active_websockets, connection_metadata, player_websockets)
        except asyncio.CancelledError:
            logger.info("Periodic health check task cancelled")
            raise
        except Exception as e:
            logger.error("Error in periodic health check task", error=str(e), exc_info=True)
            raise

    def start_periodic_checks(
        self,
        active_websockets: dict[str, "WebSocket"],
        connection_metadata: dict[str, "ConnectionMetadata"],
        player_websockets: dict[uuid.UUID, list[str]],
    ) -> None:
        """
        Start the periodic health check task.

        This should be called during application startup to begin
        proactive connection health monitoring.

        Args:
            active_websockets: Active WebSocket connections (shared reference)
            connection_metadata: Connection metadata (shared reference)
            player_websockets: Player to WebSocket connection mapping (shared reference)

        AI: Creates and tracks the health check task to prevent memory leaks.
        """
        if self._health_check_task is not None and not self._health_check_task.done():
            logger.warning("Health check task already running")
            return

        try:
            from ...app.tracked_task_manager import get_global_tracked_manager

            tracked_manager = get_global_tracked_manager()
            self._health_check_task = tracked_manager.create_tracked_task(
                self.periodic_health_check_task(active_websockets, connection_metadata, player_websockets),
                task_name="health_monitor/periodic_health_check",
                task_type="health_monitor",
            )
            logger.info("Periodic health check task started")
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors starting health check task
            logger.error("Error starting health check task", error=str(e), exc_info=True)

    def stop_periodic_checks(self) -> None:
        """
        Stop the periodic health check task.

        This should be called during application shutdown.
        """
        if self._health_check_task is not None and not self._health_check_task.done():
            logger.info("Stopping periodic health check task")
            self._health_check_task.cancel()
            try:
                # Wait briefly for task to cancel
                try:
                    _ = asyncio.get_running_loop()  # Verify loop exists
                    # Schedule wait in background with proper tracking
                    # AnyIO Pattern: Track background tasks for proper cleanup
                    # Note: This is a short-lived task that completes quickly
                    asyncio.create_task(self._wait_for_task_cancellation(self._health_check_task))
                    # Don't track this specific task as it's very short-lived and self-cleaning
                    # The health check task itself is already tracked separately
                except RuntimeError:
                    # No running loop - task will be cleaned up on next event loop
                    logger.debug("No running loop for health check task cancellation")
            except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors during task cancellation
                logger.warning("Error waiting for health check task cancellation", error=str(e))
            self._health_check_task = None

    async def _wait_for_task_cancellation(self, task: Any) -> None:
        """Wait for a task to be cancelled, with timeout."""
        try:
            await asyncio.wait_for(task, timeout=5.0)
        except (TimeoutError, asyncio.CancelledError):
            pass
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors during task wait
            logger.debug("Task cancellation wait completed", error=str(e))
