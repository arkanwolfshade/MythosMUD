"""
Tests for statistics aggregation for connection management.

This module tests the StatisticsAggregator class which aggregates statistics
from various connection management components.
"""

import time
from unittest.mock import MagicMock, patch
from uuid import uuid4

from server.realtime.monitoring.statistics_aggregator import StatisticsAggregator


class TestStatisticsAggregatorInit:
    """Test StatisticsAggregator initialization."""

    def test_init(self) -> None:
        """Test StatisticsAggregator initialization."""
        mock_memory_monitor = MagicMock()
        mock_rate_limiter = MagicMock()
        mock_message_queue = MagicMock()
        mock_room_manager = MagicMock()
        mock_performance_tracker = MagicMock()

        aggregator = StatisticsAggregator(
            mock_memory_monitor,
            mock_rate_limiter,
            mock_message_queue,
            mock_room_manager,
            mock_performance_tracker,
        )

        assert aggregator.memory_monitor == mock_memory_monitor
        assert aggregator.rate_limiter == mock_rate_limiter
        assert aggregator.message_queue == mock_message_queue
        assert aggregator.room_manager == mock_room_manager
        assert aggregator.performance_tracker == mock_performance_tracker


class TestGetMemoryStats:
    """Test get_memory_stats method."""

    def test_get_memory_stats_success(self) -> None:
        """Test successfully getting memory stats."""
        mock_memory_monitor = MagicMock()
        mock_memory_monitor.get_memory_stats.return_value = {"memory_usage": 100}
        mock_memory_monitor.last_cleanup_time = 1000.0
        mock_memory_monitor.cleanup_interval = 60.0
        mock_memory_monitor.memory_threshold = 0.8
        mock_memory_monitor.max_connection_age = 3600.0
        mock_memory_monitor.max_pending_messages = 1000
        mock_memory_monitor.max_rate_limit_entries = 500

        mock_rate_limiter = MagicMock()
        mock_rate_limiter.get_stats.return_value = {"rate_limit_stats": 50}
        mock_rate_limiter.connection_attempts = {"conn1": time.time()}

        mock_message_queue = MagicMock()
        mock_message_queue.get_stats.return_value = {"queue_stats": 25}
        mock_message_queue.pending_messages = {"msg1": "data"}

        mock_room_manager = MagicMock()
        mock_room_manager.get_stats.return_value = {"room_stats": 10}
        mock_room_manager.room_occupants = {"room1": ["player1"]}

        mock_performance_tracker = MagicMock()

        aggregator = StatisticsAggregator(
            mock_memory_monitor,
            mock_rate_limiter,
            mock_message_queue,
            mock_room_manager,
            mock_performance_tracker,
        )

        player_id1 = uuid4()
        player_id2 = uuid4()
        active_websockets = {"conn1": MagicMock(), "conn2": MagicMock()}
        player_websockets = {player_id1: ["conn1"], player_id2: ["conn2", "conn3"]}
        connection_timestamps = {"conn1": time.time(), "conn2": time.time()}
        cleanup_stats = {"cleaned": 5}
        player_sessions = {player_id1: "session1", player_id2: "session2"}
        session_connections = {"session1": ["conn1"], "session2": ["conn2", "conn3"]}
        online_players = {player_id1: {"name": "Player1"}, player_id2: {"name": "Player2"}}
        last_seen = {player_id1: time.time(), player_id2: time.time()}

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_memory_stats(
                active_websockets,
                player_websockets,
                connection_timestamps,
                cleanup_stats,
                player_sessions,
                session_connections,
                online_players,
                last_seen,
            )

            assert "memory" in result
            assert "connections" in result
            assert result["connections"]["active_websockets"] == 2
            assert result["connections"]["total_websocket_connections"] == 3
            assert result["connections"]["players_with_multiple_connections"] == 1
            assert result["sessions"]["total_sessions"] == 2
            assert result["data_structures"]["online_players"] == 2

    def test_get_memory_stats_empty(self) -> None:
        """Test getting memory stats with empty data structures."""
        mock_memory_monitor = MagicMock()
        mock_memory_monitor.get_memory_stats.return_value = {}
        mock_memory_monitor.last_cleanup_time = None
        mock_memory_monitor.cleanup_interval = 60.0
        mock_memory_monitor.memory_threshold = 0.8
        mock_memory_monitor.max_connection_age = 3600.0
        mock_memory_monitor.max_pending_messages = 1000
        mock_memory_monitor.max_rate_limit_entries = 500

        mock_rate_limiter = MagicMock()
        mock_rate_limiter.get_stats.return_value = {}
        mock_rate_limiter.connection_attempts = {}

        mock_message_queue = MagicMock()
        mock_message_queue.get_stats.return_value = {}
        mock_message_queue.pending_messages = {}

        mock_room_manager = MagicMock()
        mock_room_manager.get_stats.return_value = {}
        mock_room_manager.room_occupants = {}

        mock_performance_tracker = MagicMock()

        aggregator = StatisticsAggregator(
            mock_memory_monitor,
            mock_rate_limiter,
            mock_message_queue,
            mock_room_manager,
            mock_performance_tracker,
        )

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_memory_stats(
                {},
                {},
                {},
                {},
                {},
                {},
                {},
                {},
            )

            assert result["connections"]["avg_connections_per_player"] == 0
            assert result["sessions"]["avg_connections_per_session"] == 0

    def test_get_memory_stats_error(self) -> None:
        """Test getting memory stats when error occurs."""
        mock_memory_monitor = MagicMock()
        mock_memory_monitor.get_memory_stats.side_effect = Exception("Error")

        aggregator = StatisticsAggregator(
            mock_memory_monitor,
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_memory_stats({}, {}, {}, {}, {}, {}, {}, {})

            assert result == {}


class TestGetConnectionStats:
    """Test get_connection_stats method."""

    def test_get_connection_stats_success(self) -> None:
        """Test successfully getting connection stats."""
        aggregator = StatisticsAggregator(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )

        player_id1 = uuid4()
        player_id2 = uuid4()
        player_websockets = {player_id1: ["conn1"], player_id2: ["conn2", "conn3"]}

        # Create mock metadata objects
        class MockMetadata:
            def __init__(self, is_healthy, established_at):
                self.is_healthy = is_healthy
                self.established_at = established_at

        now = time.time()
        connection_metadata = {
            "conn1": MockMetadata(True, now - 100),
            "conn2": MockMetadata(False, now - 200),
            "conn3": MockMetadata(True, now - 3700),  # Older than 1 hour
        }

        session_connections = {"session1": ["conn1"], "session2": ["conn2", "conn3"]}
        player_sessions = {player_id1: "session1", player_id2: "session2"}

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_connection_stats(
                player_websockets,
                connection_metadata,
                session_connections,
                player_sessions,
            )

            assert "connection_distribution" in result
            assert result["connection_distribution"]["total_players"] == 2
            assert result["connection_distribution"]["websocket_only_players"] == 2
            assert result["connection_health"]["healthy_connections"] == 2
            assert result["connection_health"]["unhealthy_connections"] == 1
            assert result["connection_lifecycle"]["connections_older_than_1h"] == 1

    def test_get_connection_stats_empty(self) -> None:
        """Test getting connection stats with empty data."""
        aggregator = StatisticsAggregator(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_connection_stats({}, {}, {}, {})

            assert result["connection_distribution"]["total_players"] == 0
            assert result["connection_health"]["health_percentage"] == 0
            assert result["session_metrics"]["avg_connections_per_session"] == 0

    def test_get_connection_stats_error(self) -> None:
        """Test getting connection stats when error occurs."""
        aggregator = StatisticsAggregator(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            # Cause an error by passing invalid data
            result = aggregator.get_connection_stats(None, {}, {}, {})  # type: ignore[arg-type]

            assert "error" in result
            assert "timestamp" in result


class TestGetConnectionHealthStats:
    """Test get_connection_health_stats method."""

    def test_get_connection_health_stats_success(self) -> None:
        """Test successfully getting connection health stats."""
        aggregator = StatisticsAggregator(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )

        # Create mock metadata objects
        class MockMetadata:
            def __init__(self, is_healthy, established_at, connection_type, session_id=None):
                self.is_healthy = is_healthy
                self.established_at = established_at
                self.connection_type = connection_type
                self.session_id = session_id

        now = time.time()
        connection_metadata = {
            "conn1": MockMetadata(True, now - 100, "websocket", "session1"),
            "conn2": MockMetadata(False, now - 200, "websocket", "session1"),
            "conn3": MockMetadata(True, now - 3700, "websocket", "session2"),  # Older than 1 hour
            "conn4": MockMetadata(True, now - 90000, "websocket", "session2"),  # Older than 24 hours
        }

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_connection_health_stats(connection_metadata)

            assert "overall_health" in result
            assert result["overall_health"]["healthy_connections"] == 3
            assert result["overall_health"]["unhealthy_connections"] == 1
            assert result["connection_lifecycle"]["stale_connections"] == 2
            assert result["health_trends"]["connections_older_than_1h"] == 2
            assert result["health_trends"]["connections_older_than_24h"] == 1

    def test_get_connection_health_stats_empty(self) -> None:
        """Test getting connection health stats with empty data."""
        aggregator = StatisticsAggregator(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_connection_health_stats({})

            assert result["overall_health"]["total_connections"] == 0
            assert result["overall_health"]["health_percentage"] == 0
            assert result["session_health"]["total_sessions"] == 0

    def test_get_connection_health_stats_error(self) -> None:
        """Test getting connection health stats when error occurs."""
        aggregator = StatisticsAggregator(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            # Cause an error by passing invalid data
            result = aggregator.get_connection_health_stats(None)  # type: ignore[arg-type]

            assert "error" in result
            assert "timestamp" in result


class TestGetMemoryAlerts:
    """Test get_memory_alerts method."""

    def test_get_memory_alerts_success(self) -> None:
        """Test successfully getting memory alerts."""
        mock_memory_monitor = MagicMock()
        mock_memory_monitor.get_memory_alerts.return_value = ["Alert 1", "Alert 2"]

        mock_rate_limiter = MagicMock()
        mock_rate_limiter.connection_attempts = {"conn1": time.time()}

        mock_message_queue = MagicMock()
        mock_message_queue.pending_messages = {"msg1": "data"}

        aggregator = StatisticsAggregator(
            mock_memory_monitor,
            mock_rate_limiter,
            mock_message_queue,
            MagicMock(),
            MagicMock(),
        )

        now = time.time()
        connection_timestamps = {
            "conn1": now - 100,
            "conn2": now - 4000,  # Stale connection
        }
        max_connection_age = 3600.0

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_memory_alerts(connection_timestamps, max_connection_age)

            assert isinstance(result, list)
            assert len(result) == 2
            mock_memory_monitor.get_memory_alerts.assert_called_once()

    def test_get_memory_alerts_no_stale_connections(self) -> None:
        """Test getting memory alerts when no stale connections exist."""
        mock_memory_monitor = MagicMock()
        mock_memory_monitor.get_memory_alerts.return_value = []

        mock_rate_limiter = MagicMock()
        mock_rate_limiter.connection_attempts = {}

        mock_message_queue = MagicMock()
        mock_message_queue.pending_messages = {}

        aggregator = StatisticsAggregator(
            mock_memory_monitor,
            mock_rate_limiter,
            mock_message_queue,
            MagicMock(),
            MagicMock(),
        )

        now = time.time()
        connection_timestamps = {
            "conn1": now - 100,  # Not stale
        }
        max_connection_age = 3600.0

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_memory_alerts(connection_timestamps, max_connection_age)

            assert isinstance(result, list)
            # Should still call get_memory_alerts with stale_connections=0
            mock_memory_monitor.get_memory_alerts.assert_called_once()

    def test_get_memory_alerts_error(self) -> None:
        """Test getting memory alerts when error occurs."""
        mock_memory_monitor = MagicMock()
        mock_memory_monitor.get_memory_alerts.side_effect = Exception("Error")

        aggregator = StatisticsAggregator(
            mock_memory_monitor,
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )

        with patch("server.realtime.monitoring.statistics_aggregator.logger"):
            result = aggregator.get_memory_alerts({}, 3600.0)

            assert isinstance(result, list)
            assert len(result) == 1
            assert "ERROR" in result[0]
