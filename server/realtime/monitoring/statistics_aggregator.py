"""
Statistics aggregation for connection management.

This module aggregates statistics from various connection management components
and provides comprehensive reporting for monitoring and diagnostics.

AI Agent: Extracted from ConnectionManager to centralize statistics reporting logic.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Statistics aggregation requires many parameters and intermediate variables for complex statistics processing logic

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

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Statistics aggregator initialization requires many service dependencies
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

    def get_memory_stats(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Memory stats retrieval requires many parameters and intermediate variables for complex statistics processing
        self,
        active_websockets: dict[str, Any],
        player_websockets: dict[uuid.UUID, list[str]],
        connection_timestamps: dict[str, float],
        cleanup_stats: dict[str, object],
        player_sessions: dict[uuid.UUID, str],
        session_connections: dict[str, list[str]],
        online_players: dict[uuid.UUID, dict[str, Any]],
        last_seen: dict[uuid.UUID, float],
        closed_websockets_count: int,
        connection_metadata: dict[str, Any],
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
            closed_websockets_count: Count of closed WebSocket IDs being tracked
            connection_metadata: Connection metadata dictionary

        Returns:
            dict: Comprehensive memory and connection statistics
        """
        try:
            return self._build_memory_stats_payload(
                active_websockets=active_websockets,
                player_websockets=player_websockets,
                connection_timestamps=connection_timestamps,
                cleanup_stats=cleanup_stats,
                player_sessions=player_sessions,
                session_connections=session_connections,
                online_players=online_players,
                last_seen=last_seen,
                closed_websockets_count=closed_websockets_count,
                connection_metadata=connection_metadata,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory stats retrieval errors unpredictable, must return empty dict
            logger.error("Error getting memory stats", error=str(e), exc_info=True)
            return {}

    @staticmethod
    def _count_orphaned_connections(
        active_websockets: dict[str, Any],
        player_websockets: dict[uuid.UUID, list[str]],
        online_players: dict[uuid.UUID, dict[str, Any]],
    ) -> int:
        """Count active connections not tied to any online player."""
        orphaned = 0
        for conn_id in active_websockets:
            tied = any(
                conn_id in conn_ids and player_id in online_players for player_id, conn_ids in player_websockets.items()
            )
            if not tied:
                orphaned += 1
        return orphaned

    def _memory_connections_section(
        self,
        active_websockets: dict[str, Any],
        player_websockets: dict[uuid.UUID, list[str]],
        connection_timestamps: dict[str, float],
        online_players: dict[uuid.UUID, dict[str, Any]],
        closed_websockets_count: int,
        connection_metadata: dict[str, Any],
    ) -> dict[str, Any]:
        """Build the connections subsection of memory stats."""
        total_ws = sum(len(conn_ids) for conn_ids in player_websockets.values())
        active_count = len(active_websockets)
        return {
            "active_websockets": active_count,
            "active_websockets_count": active_count,
            "total_connections": active_count,
            "player_websockets": len(player_websockets),
            "player_websockets_count": len(player_websockets),
            "connection_timestamps": len(connection_timestamps),
            "connection_metadata_count": len(connection_metadata),
            "closed_websockets_count": closed_websockets_count,
            "total_websocket_connections": total_ws,
            "players_with_multiple_connections": sum(1 for c in player_websockets.values() if len(c) > 1),
            "avg_connections_per_player": self._safe_ratio(total_ws, len(player_websockets)),
            "active_to_player_ratio": self._safe_ratio(active_count, len(online_players)),
            "orphaned_connections": self._count_orphaned_connections(
                active_websockets, player_websockets, online_players
            ),
        }

    def _memory_sessions_section(
        self,
        player_sessions: dict[uuid.UUID, str],
        session_connections: dict[str, list[str]],
        total_websocket_connections: int,
    ) -> dict[str, Any]:
        """Build the sessions subsection of memory stats."""
        total_sessions = len(player_sessions)
        total_session_connections = sum(len(conn_ids) for conn_ids in session_connections.values())
        return {
            "total_sessions": total_sessions,
            "total_session_connections": total_session_connections,
            "avg_connections_per_session": self._safe_ratio(total_session_connections, total_sessions),
            "session_connection_ratio": self._safe_ratio(total_session_connections, total_websocket_connections),
        }

    def _memory_monitor_config_section(self) -> dict[str, Any]:
        """Expose memory monitor configuration knobs for stats payload."""
        monitor = self.memory_monitor
        return {
            "last_cleanup": monitor.last_cleanup_time,
            "cleanup_interval": monitor.cleanup_interval,
            "memory_threshold": monitor.memory_threshold,
            "max_connection_age": monitor.max_connection_age,
            "max_pending_messages": monitor.max_pending_messages,
            "max_rate_limit_entries": monitor.max_rate_limit_entries,
        }

    def _build_memory_stats_payload(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Assembles multi-section memory stats from several subsystems
        self,
        active_websockets: dict[str, Any],
        player_websockets: dict[uuid.UUID, list[str]],
        connection_timestamps: dict[str, float],
        cleanup_stats: dict[str, object],
        player_sessions: dict[uuid.UUID, str],
        session_connections: dict[str, list[str]],
        online_players: dict[uuid.UUID, dict[str, Any]],
        last_seen: dict[uuid.UUID, float],
        closed_websockets_count: int,
        connection_metadata: dict[str, Any],
    ) -> dict[str, Any]:
        """Compose memory statistics payload (extracted to keep get_memory_stats CCN low)."""
        connections = self._memory_connections_section(
            active_websockets,
            player_websockets,
            connection_timestamps,
            online_players,
            closed_websockets_count,
            connection_metadata,
        )
        return {
            "memory": self.memory_monitor.get_memory_stats(),
            "connections": connections,
            "sessions": self._memory_sessions_section(
                player_sessions, session_connections, connections["total_websocket_connections"]
            ),
            "data_structures": {
                "online_players": len(online_players),
                "last_seen": len(last_seen),
                "room_occupants": len(self.room_manager.room_occupants),
                "connection_attempts": len(self.rate_limiter.connection_attempts),
                "pending_messages": len(self.message_queue.pending_messages),
            },
            "cleanup_stats": cleanup_stats,
            "memory_monitor": self._memory_monitor_config_section(),
            "rate_limiter": self.rate_limiter.get_stats(),
            "message_queue": self.message_queue.get_stats(),
            "room_manager": self.room_manager.get_stats(),
        }

    @staticmethod
    def _safe_ratio(numerator: float, denominator: float) -> float:
        """Return numerator/denominator, or 0 when denominator is empty."""
        if not denominator:
            return 0.0
        return numerator / denominator

    @staticmethod
    def _session_connection_distribution(session_connections: dict[str, list[str]]) -> dict[int, int]:
        """Count how many sessions have each connection-count size."""
        session_connection_counts: dict[int, int] = {}
        for conn_ids in session_connections.values():
            count = len(conn_ids)
            session_connection_counts[count] = session_connection_counts.get(count, 0) + 1
        return session_connection_counts

    @staticmethod
    def _connection_age_extrema(connection_ages: list[float]) -> tuple[float, float, float]:
        """Return (avg, max, min) connection ages; zeros when the list is empty."""
        if not connection_ages:
            return 0.0, 0.0, 0.0
        return sum(connection_ages) / len(connection_ages), max(connection_ages), min(connection_ages)

    def _build_connection_stats(  # pylint: disable=too-many-locals  # Reason: Assembles multi-section stats payload from several subsystems
        self,
        player_websockets: dict[uuid.UUID, list[str]],
        connection_metadata: dict[str, Any],
        session_connections: dict[str, list[str]],
        player_sessions: dict[uuid.UUID, str],
    ) -> dict[str, Any]:
        """Compose connection statistics payload (extracted to keep get_connection_stats CCN low)."""
        now = time.time()
        total_players = len(player_websockets)
        websocket_only_players = sum(1 for conn_ids in player_websockets.values() if conn_ids)
        healthy_connections, unhealthy_connections = self._analyze_connection_health(connection_metadata)
        total_connection_metadata = len(connection_metadata)
        session_connection_counts = self._session_connection_distribution(session_connections)
        connection_ages, _ = self._analyze_connection_ages(connection_metadata, now)
        avg_age, max_age, min_age = self._connection_age_extrema(connection_ages)
        age_trends = self._build_health_trends(connection_ages)
        total_sess = sum(len(c) for c in session_connections.values())
        total_ws = sum(len(c) for c in player_websockets.values())
        return {
            "connection_distribution": {
                "total_players": total_players,
                "websocket_only_players": websocket_only_players,
            },
            "connection_health": {
                "total_connections": total_connection_metadata,
                "healthy_connections": healthy_connections,
                "unhealthy_connections": unhealthy_connections,
                "health_percentage": self._safe_ratio(healthy_connections * 100, total_connection_metadata),
            },
            "session_metrics": {
                "total_sessions": len(player_sessions),
                "total_session_connections": total_sess,
                "session_connection_distribution": session_connection_counts,
                "avg_connections_per_session": self._safe_ratio(total_sess, len(session_connections)),
            },
            "connection_lifecycle": {
                "avg_connection_age_seconds": avg_age,
                "max_connection_age_seconds": max_age,
                "min_connection_age_seconds": min_age,
                "connections_older_than_1h": age_trends["connections_older_than_1h"],
                "connections_older_than_24h": age_trends["connections_older_than_24h"],
            },
            "performance_metrics": {
                "total_websocket_connections": total_ws,
                "avg_connections_per_player": self._safe_ratio(total_ws, total_players),
            },
            "timestamp": now,
        }

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
            return self._build_connection_stats(
                player_websockets, connection_metadata, session_connections, player_sessions
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Connection stats retrieval errors unpredictable, must return error response
            logger.error("Error getting connection stats", error=str(e), exc_info=True)
            return {"error": f"Failed to get connection stats: {e}", "timestamp": time.time()}

    def _analyze_connection_health(self, connection_metadata: dict[str, Any]) -> tuple[int, int]:
        """
        Analyze connection health distribution.

        Args:
            connection_metadata: Connection metadata

        Returns:
            Tuple of (healthy_connections, unhealthy_connections)
        """
        healthy_connections = 0
        unhealthy_connections = 0

        for _connection_id, metadata in connection_metadata.items():
            if metadata.is_healthy:
                healthy_connections += 1
            else:
                unhealthy_connections += 1

        return healthy_connections, unhealthy_connections

    def _analyze_connection_types(self, connection_metadata: dict[str, Any]) -> int:
        """
        Analyze connection types.

        Args:
            connection_metadata: Connection metadata

        Returns:
            Number of websocket connections
        """
        websocket_connections = 0

        for _connection_id, metadata in connection_metadata.items():
            if metadata.connection_type == "websocket":
                websocket_connections += 1

        return websocket_connections

    def _analyze_connection_ages(self, connection_metadata: dict[str, Any], now: float) -> tuple[list[float], int]:
        """
        Analyze connection ages.

        Args:
            connection_metadata: Connection metadata
            now: Current timestamp

        Returns:
            Tuple of (connection_ages list, stale_connections count)
        """
        connection_ages = []
        stale_connections = 0

        for _connection_id, metadata in connection_metadata.items():
            age = now - metadata.established_at
            connection_ages.append(age)
            if age > 3600:  # 1 hour
                stale_connections += 1

        return connection_ages, stale_connections

    def _analyze_session_health(self, connection_metadata: dict[str, Any]) -> dict[str, dict[str, int]]:
        """
        Analyze session health.

        Args:
            connection_metadata: Connection metadata

        Returns:
            Dictionary mapping session_id to health stats
        """
        session_health = {}

        for _connection_id, metadata in connection_metadata.items():
            if metadata.session_id:
                if metadata.session_id not in session_health:
                    session_health[metadata.session_id] = {"healthy": 0, "unhealthy": 0, "total": 0}
                session_health[metadata.session_id]["total"] += 1
                if metadata.is_healthy:
                    session_health[metadata.session_id]["healthy"] += 1
                else:
                    session_health[metadata.session_id]["unhealthy"] += 1

        return session_health

    def _calculate_session_health_percentages(self, session_health: dict[str, dict[str, int]]) -> tuple[int, int]:
        """
        Calculate session health percentages.

        Args:
            session_health: Session health dictionary

        Returns:
            Tuple of (healthy_sessions, unhealthy_sessions)
        """
        healthy_sessions = 0
        unhealthy_sessions = 0

        for _session_id, health in session_health.items():
            if health["total"] > 0:
                health_percentage = health["healthy"] / health["total"] * 100
                if health_percentage >= 80:  # 80% threshold for healthy session
                    healthy_sessions += 1
                else:
                    unhealthy_sessions += 1

        return healthy_sessions, unhealthy_sessions

    def _build_health_trends(self, connection_ages: list[float]) -> dict[str, int]:
        """
        Build health trends statistics.

        Args:
            connection_ages: List of connection ages

        Returns:
            Dictionary with health trends
        """
        return {
            "connections_older_than_1h": sum(1 for age in connection_ages if age > 3600),
            "connections_older_than_24h": sum(1 for age in connection_ages if age > 86400),
            "connections_older_than_7d": sum(1 for age in connection_ages if age > 604800),
        }

    def _build_health_stats_response(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Health stats building requires many parameters for complete health context
        self,
        total_connections: int,
        healthy_connections: int,
        unhealthy_connections: int,
        websocket_connections: int,
        connection_ages: list[float],
        stale_connections: int,
        total_sessions: int,
        healthy_sessions: int,
        unhealthy_sessions: int,
        now: float,
    ) -> dict[str, Any]:
        """
        Build connection health statistics response.

        Args:
            total_connections: Total number of connections
            healthy_connections: Number of healthy connections
            unhealthy_connections: Number of unhealthy connections
            websocket_connections: Number of websocket connections
            connection_ages: List of connection ages
            stale_connections: Number of stale connections
            total_sessions: Total number of sessions
            healthy_sessions: Number of healthy sessions
            unhealthy_sessions: Number of unhealthy sessions
            now: Current timestamp

        Returns:
            Dictionary with health statistics
        """
        return {
            "overall_health": {
                "total_connections": total_connections,
                "healthy_connections": healthy_connections,
                "unhealthy_connections": unhealthy_connections,
                "health_percentage": (healthy_connections / total_connections * 100) if total_connections > 0 else 0,
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
            "health_trends": self._build_health_trends(connection_ages),
            "timestamp": now,
        }

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

            healthy_connections, unhealthy_connections = self._analyze_connection_health(connection_metadata)
            websocket_connections = self._analyze_connection_types(connection_metadata)
            connection_ages, stale_connections = self._analyze_connection_ages(connection_metadata, now)
            session_health = self._analyze_session_health(connection_metadata)
            healthy_sessions, unhealthy_sessions = self._calculate_session_health_percentages(session_health)

            total_connections = len(connection_metadata)
            total_sessions = len(session_health)

            return self._build_health_stats_response(
                total_connections,
                healthy_connections,
                unhealthy_connections,
                websocket_connections,
                connection_ages,
                stale_connections,
                total_sessions,
                healthy_sessions,
                unhealthy_sessions,
                now,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Connection health stats retrieval errors unpredictable, must return error response
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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory alerts retrieval errors unpredictable, must return error message
            logger.error("Error getting memory alerts", error=str(e), exc_info=True)
            return [f"ERROR: Failed to get memory alerts: {e}"]
