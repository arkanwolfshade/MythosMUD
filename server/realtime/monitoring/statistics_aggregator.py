"""
Statistics aggregation for connection management.

This module aggregates statistics from various connection management components
and provides comprehensive reporting for monitoring and diagnostics.

AI Agent: Extracted from ConnectionManager to centralize statistics reporting logic.
"""

import time
import uuid
from typing import TYPE_CHECKING, Any

from ...structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..memory_monitor import MemoryMonitor
    from ..message_queue import MessageQueue
    from ..rate_limiter import RateLimiter
    from ..room_subscription_manager import RoomSubscriptionManager
    from .performance_tracker import PerformanceTracker

logger = get_logger(__name__)


class StatisticsAggregator:
    """
    Aggregates statistics from connection management components.

    This class provides comprehensive reporting by collecting and combining
    statistics from all connection management subsystems.

    AI Agent: Single Responsibility - Statistics aggregation and reporting only.
    """

    def __init__(
        self,
        memory_monitor: "MemoryMonitor",
        rate_limiter: "RateLimiter",
        message_queue: "MessageQueue",
        room_manager: "RoomSubscriptionManager",
        performance_tracker: "PerformanceTracker",
    ) -> None:
        """
        Initialize the statistics aggregator.

        Args:
            memory_monitor: MemoryMonitor instance
            rate_limiter: RateLimiter instance
            message_queue: MessageQueue instance
            room_manager: RoomSubscriptionManager instance
            performance_tracker: PerformanceTracker instance
        """
        self.memory_monitor = memory_monitor
        self.rate_limiter = rate_limiter
        self.message_queue = message_queue
        self.room_manager = room_manager
        self.performance_tracker = performance_tracker

    def get_memory_stats(
        self,
        active_websockets: dict[str, Any],
        player_websockets: dict[uuid.UUID, list[str]],
        connection_timestamps: dict[str, float],
        cleanup_stats: dict[str, Any],
        player_sessions: dict[uuid.UUID, str],
        session_connections: dict[str, list[str]],
        online_players: dict[uuid.UUID, dict[str, Any]],
        last_seen: dict[uuid.UUID, float],
    ) -> dict[str, Any]:
        """
        Get comprehensive memory and connection statistics.

        Args:
            active_websockets: Active WebSocket connections
            player_websockets: Player to WebSocket connection mapping
            connection_timestamps: Connection timestamp tracking
            cleanup_stats: Cleanup statistics
            player_sessions: Player to session mapping
            session_connections: Session to connection mapping
            online_players: Online player tracking
            last_seen: Last seen timestamps

        Returns:
            dict: Comprehensive memory and connection statistics
        """
        try:
            memory_stats = self.memory_monitor.get_memory_stats()
            rate_limiter_stats = self.rate_limiter.get_stats()
            message_queue_stats = self.message_queue.get_stats()
            room_stats = self.room_manager.get_stats()

            # Calculate connection metrics
            total_websocket_connections = sum(len(conn_ids) for conn_ids in player_websockets.values())
            players_with_multiple_connections = sum(1 for conn_ids in player_websockets.values() if len(conn_ids) > 1)

            # Session metrics
            total_sessions = len(player_sessions)
            total_session_connections = sum(len(conn_ids) for conn_ids in session_connections.values())

            return {
                "memory": memory_stats,
                "connections": {
                    "active_websockets": len(active_websockets),
                    "total_connections": len(active_websockets),
                    "player_websockets": len(player_websockets),
                    "connection_timestamps": len(connection_timestamps),
                    # Connection metrics
                    "total_websocket_connections": total_websocket_connections,
                    "players_with_multiple_connections": players_with_multiple_connections,
                    "avg_connections_per_player": total_websocket_connections / len(player_websockets)
                    if player_websockets
                    else 0,
                },
                "sessions": {
                    "total_sessions": total_sessions,
                    "total_session_connections": total_session_connections,
                    "avg_connections_per_session": total_session_connections / total_sessions
                    if total_sessions > 0
                    else 0,
                    "session_connection_ratio": total_session_connections / total_websocket_connections
                    if total_websocket_connections > 0
                    else 0,
                },
                "data_structures": {
                    "online_players": len(online_players),
                    "last_seen": len(last_seen),
                    "room_occupants": len(self.room_manager.room_occupants),
                    "connection_attempts": len(self.rate_limiter.connection_attempts),
                    "pending_messages": len(self.message_queue.pending_messages),
                },
                "cleanup_stats": cleanup_stats,
                "memory_monitor": {
                    "last_cleanup": self.memory_monitor.last_cleanup_time,
                    "cleanup_interval": self.memory_monitor.cleanup_interval,
                    "memory_threshold": self.memory_monitor.memory_threshold,
                    "max_connection_age": self.memory_monitor.max_connection_age,
                    "max_pending_messages": self.memory_monitor.max_pending_messages,
                    "max_rate_limit_entries": self.memory_monitor.max_rate_limit_entries,
                },
                "rate_limiter": rate_limiter_stats,
                "message_queue": message_queue_stats,
                "room_manager": room_stats,
            }
        except Exception as e:
            logger.error("Error getting memory stats", error=str(e), exc_info=True)
            return {}

    def get_connection_stats(
        self,
        player_websockets: dict[uuid.UUID, list[str]],
        connection_metadata: dict[str, Any],
        session_connections: dict[str, list[str]],
        player_sessions: dict[uuid.UUID, str],
    ) -> dict[str, Any]:
        """
        Get comprehensive connection statistics.

        Args:
            player_websockets: Player to WebSocket connection mapping
            connection_metadata: Connection metadata
            session_connections: Session to connection mapping
            player_sessions: Player to session mapping

        Returns:
            dict: Connection statistics including metrics, health, and performance data
        """
        try:
            now = time.time()

            # Calculate connection type distribution
            websocket_only_players = 0
            total_players = len(player_websockets)

            for player_id in player_websockets.keys():
                has_websocket = len(player_websockets[player_id]) > 0

                if has_websocket:
                    websocket_only_players += 1

            # Calculate connection health metrics
            healthy_connections = 0
            unhealthy_connections = 0
            total_connection_metadata = len(connection_metadata)

            for metadata in connection_metadata.values():
                if metadata.is_healthy:
                    healthy_connections += 1
                else:
                    unhealthy_connections += 1

            # Calculate session distribution
            session_connection_counts: dict[int, int] = {}
            for _session_id, conn_ids in session_connections.items():
                count = len(conn_ids)
                session_connection_counts[count] = session_connection_counts.get(count, 0) + 1

            # Calculate connection age distribution
            connection_ages = []
            for metadata in connection_metadata.values():
                age = now - metadata.established_at
                connection_ages.append(age)

            avg_connection_age = sum(connection_ages) / len(connection_ages) if connection_ages else 0
            max_connection_age = max(connection_ages) if connection_ages else 0
            min_connection_age = min(connection_ages) if connection_ages else 0

            return {
                "connection_distribution": {
                    "total_players": total_players,
                    "websocket_only_players": websocket_only_players,
                },
                "connection_health": {
                    "total_connections": total_connection_metadata,
                    "healthy_connections": healthy_connections,
                    "unhealthy_connections": unhealthy_connections,
                    "health_percentage": (healthy_connections / total_connection_metadata * 100)
                    if total_connection_metadata > 0
                    else 0,
                },
                "session_metrics": {
                    "total_sessions": len(player_sessions),
                    "total_session_connections": sum(len(conn_ids) for conn_ids in session_connections.values()),
                    "session_connection_distribution": session_connection_counts,
                    "avg_connections_per_session": sum(len(conn_ids) for conn_ids in session_connections.values())
                    / len(session_connections)
                    if session_connections
                    else 0,
                },
                "connection_lifecycle": {
                    "avg_connection_age_seconds": avg_connection_age,
                    "max_connection_age_seconds": max_connection_age,
                    "min_connection_age_seconds": min_connection_age,
                    "connections_older_than_1h": sum(1 for age in connection_ages if age > 3600),
                    "connections_older_than_24h": sum(1 for age in connection_ages if age > 86400),
                },
                "performance_metrics": {
                    "total_websocket_connections": sum(len(conn_ids) for conn_ids in player_websockets.values()),
                    "avg_connections_per_player": (sum(len(conn_ids) for conn_ids in player_websockets.values()))
                    / total_players
                    if total_players > 0
                    else 0,
                },
                "timestamp": now,
            }
        except Exception as e:
            logger.error("Error getting connection stats", error=str(e), exc_info=True)
            return {"error": f"Failed to get connection stats: {e}", "timestamp": time.time()}

    def get_connection_health_stats(self, connection_metadata: dict[str, Any]) -> dict[str, Any]:
        """
        Get comprehensive connection health statistics.

        Args:
            connection_metadata: Connection metadata

        Returns:
            dict: Connection health statistics including health distribution and trends
        """
        try:
            now = time.time()

            # Analyze connection health distribution
            healthy_connections = 0
            unhealthy_connections = 0

            # Analyze connection types
            websocket_connections = 0

            # Analyze connection ages
            connection_ages = []
            stale_connections = 0

            # Analyze session health
            session_health = {}

            for _connection_id, metadata in connection_metadata.items():
                # Health analysis
                if metadata.is_healthy:
                    healthy_connections += 1
                else:
                    unhealthy_connections += 1

                # Type analysis
                if metadata.connection_type == "websocket":
                    websocket_connections += 1

                # Age analysis
                age = now - metadata.established_at
                connection_ages.append(age)
                if age > 3600:  # 1 hour
                    stale_connections += 1

                # Session health analysis
                if metadata.session_id:
                    if metadata.session_id not in session_health:
                        session_health[metadata.session_id] = {"healthy": 0, "unhealthy": 0, "total": 0}
                    session_health[metadata.session_id]["total"] += 1
                    if metadata.is_healthy:
                        session_health[metadata.session_id]["healthy"] += 1
                    else:
                        session_health[metadata.session_id]["unhealthy"] += 1

            # Calculate session health percentages
            healthy_sessions = 0
            unhealthy_sessions = 0
            for _session_id, health in session_health.items():
                if health["total"] > 0:
                    health_percentage = health["healthy"] / health["total"] * 100
                    if health_percentage >= 80:  # 80% threshold for healthy session
                        healthy_sessions += 1
                    else:
                        unhealthy_sessions += 1

            total_connections = len(connection_metadata)
            total_sessions = len(session_health)

            return {
                "overall_health": {
                    "total_connections": total_connections,
                    "healthy_connections": healthy_connections,
                    "unhealthy_connections": unhealthy_connections,
                    "health_percentage": (healthy_connections / total_connections * 100)
                    if total_connections > 0
                    else 0,
                },
                "connection_type_health": {
                    "websocket_connections": websocket_connections,
                    "websocket_health_percentage": 0,  # Would need separate tracking
                },
                "connection_lifecycle": {
                    "avg_connection_age_seconds": sum(connection_ages) / len(connection_ages) if connection_ages else 0,
                    "max_connection_age_seconds": max(connection_ages) if connection_ages else 0,
                    "min_connection_age_seconds": min(connection_ages) if connection_ages else 0,
                    "stale_connections": stale_connections,
                    "stale_connection_percentage": (stale_connections / total_connections * 100)
                    if total_connections > 0
                    else 0,
                },
                "session_health": {
                    "total_sessions": total_sessions,
                    "healthy_sessions": healthy_sessions,
                    "unhealthy_sessions": unhealthy_sessions,
                    "session_health_percentage": (healthy_sessions / total_sessions * 100) if total_sessions > 0 else 0,
                    "avg_connections_per_session": total_connections / total_sessions if total_sessions > 0 else 0,
                },
                "health_trends": {
                    "connections_older_than_1h": sum(1 for age in connection_ages if age > 3600),
                    "connections_older_than_24h": sum(1 for age in connection_ages if age > 86400),
                    "connections_older_than_7d": sum(1 for age in connection_ages if age > 604800),
                },
                "timestamp": now,
            }
        except Exception as e:
            logger.error("Error getting connection health stats", error=str(e), exc_info=True)
            return {"error": f"Failed to get connection health stats: {e}", "timestamp": time.time()}

    def get_memory_alerts(self, connection_timestamps: dict[str, float], max_connection_age: float) -> list[str]:
        """
        Get memory-related alerts.

        Args:
            connection_timestamps: Connection timestamp tracking
            max_connection_age: Maximum connection age threshold

        Returns:
            list: List of memory alert messages
        """
        try:
            # Calculate stale connections
            now_ts = time.time()
            stale_connections = 0
            for timestamp in connection_timestamps.values():
                if now_ts - timestamp > max_connection_age:
                    stale_connections += 1

            connection_stats = {
                "connection_attempts": len(self.rate_limiter.connection_attempts),
                "pending_messages": len(self.message_queue.pending_messages),
                "stale_connections": stale_connections,
            }
            return self.memory_monitor.get_memory_alerts(connection_stats)
        except Exception as e:
            logger.error("Error getting memory alerts", error=str(e), exc_info=True)
            return [f"ERROR: Failed to get memory alerts: {e}"]
