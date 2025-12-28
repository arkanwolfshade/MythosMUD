"""
Unit tests for statistics aggregator.

Tests the StatisticsAggregator class.
"""

import uuid
from unittest.mock import MagicMock

import pytest

from server.realtime.monitoring.statistics_aggregator import StatisticsAggregator


@pytest.fixture
def mock_memory_monitor():
    """Create a mock memory monitor."""
    monitor = MagicMock()
    monitor.get_memory_stats = MagicMock(return_value={"total_memory": 1000, "used_memory": 500})
    return monitor


@pytest.fixture
def mock_rate_limiter():
    """Create a mock rate limiter."""
    limiter = MagicMock()
    limiter.get_stats = MagicMock(return_value={"total_requests": 100, "rate_limited": 5})
    return limiter


@pytest.fixture
def mock_message_queue():
    """Create a mock message queue."""
    queue = MagicMock()
    queue.get_stats = MagicMock(return_value={"pending_messages": 10, "processed_messages": 1000})
    return queue


@pytest.fixture
def mock_room_manager():
    """Create a mock room manager."""
    manager = MagicMock()
    manager.get_stats = MagicMock(return_value={"total_rooms": 50, "total_subscriptions": 200})
    return manager


@pytest.fixture
def mock_performance_tracker():
    """Create a mock performance tracker."""
    return MagicMock()


@pytest.fixture
def statistics_aggregator(
    mock_memory_monitor, mock_rate_limiter, mock_message_queue, mock_room_manager, mock_performance_tracker
):
    """Create a StatisticsAggregator instance."""
    return StatisticsAggregator(
        memory_monitor=mock_memory_monitor,
        rate_limiter=mock_rate_limiter,
        message_queue=mock_message_queue,
        room_manager=mock_room_manager,
        performance_tracker=mock_performance_tracker,
    )


def test_statistics_aggregator_init(statistics_aggregator, mock_memory_monitor, mock_rate_limiter):
    """Test StatisticsAggregator initialization."""
    assert statistics_aggregator.memory_monitor == mock_memory_monitor
    assert statistics_aggregator.rate_limiter == mock_rate_limiter


def test_get_memory_stats(statistics_aggregator, mock_memory_monitor):
    """Test get_memory_stats() returns comprehensive statistics."""
    active_websockets = {"ws_001": MagicMock(), "ws_002": MagicMock()}
    player_websockets = {uuid.uuid4(): ["ws_001"], uuid.uuid4(): ["ws_002"]}
    connection_timestamps = {"ws_001": 1000.0, "ws_002": 2000.0}
    cleanup_stats = {"cleaned_connections": 5}
    player_sessions = {uuid.uuid4(): "session_001"}
    session_connections = {"session_001": ["ws_001"]}
    online_players = {uuid.uuid4(): {"name": "Player1"}}
    last_seen = {uuid.uuid4(): 3000.0}
    result = statistics_aggregator.get_memory_stats(
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
    assert "cleanup_stats" in result
