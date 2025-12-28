"""
Unit tests for connection cleaner.

Tests the ConnectionCleaner class.
"""

import time
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.maintenance.connection_cleaner import ConnectionCleaner


@pytest.fixture
def mock_memory_monitor():
    """Create a mock memory monitor."""
    return MagicMock()


@pytest.fixture
def mock_rate_limiter():
    """Create a mock rate limiter."""
    return MagicMock()


@pytest.fixture
def mock_message_queue():
    """Create a mock message queue."""
    return MagicMock()


@pytest.fixture
def mock_room_manager():
    """Create a mock room manager."""
    return MagicMock()


@pytest.fixture
def mock_cleanup_dead_websocket():
    """Create a mock cleanup_dead_websocket callback."""
    return AsyncMock()


@pytest.fixture
def mock_has_websocket_connection():
    """Create a mock has_websocket_connection callback."""
    return MagicMock(return_value=False)


@pytest.fixture
def mock_get_async_persistence():
    """Create a mock get_async_persistence callback."""
    return MagicMock(return_value=None)


@pytest.fixture
def connection_cleaner(
    mock_memory_monitor,
    mock_rate_limiter,
    mock_message_queue,
    mock_room_manager,
    mock_cleanup_dead_websocket,
    mock_has_websocket_connection,
    mock_get_async_persistence,
):
    """Create a ConnectionCleaner instance."""
    return ConnectionCleaner(
        memory_monitor=mock_memory_monitor,
        rate_limiter=mock_rate_limiter,
        message_queue=mock_message_queue,
        room_manager=mock_room_manager,
        cleanup_dead_websocket_callback=mock_cleanup_dead_websocket,
        has_websocket_connection_callback=mock_has_websocket_connection,
        get_async_persistence=mock_get_async_persistence,
    )


def test_connection_cleaner_init(connection_cleaner, mock_memory_monitor, mock_rate_limiter):
    """Test ConnectionCleaner initialization."""
    assert connection_cleaner.memory_monitor == mock_memory_monitor
    assert connection_cleaner.rate_limiter == mock_rate_limiter


def test_prune_stale_players(connection_cleaner, mock_room_manager):
    """Test prune_stale_players() removes stale players."""
    now = time.time()
    player_id = uuid.uuid4()
    last_seen = {player_id: now - 200}  # 200 seconds ago
    online_players = {player_id: {"name": "Player1"}}
    player_websockets = {player_id: []}
    active_websockets = {}
    last_active_update_times = {}
    connection_cleaner.prune_stale_players(
        last_seen, online_players, player_websockets, active_websockets, last_active_update_times, max_age_seconds=90
    )
    # Player should be removed from online_players
    assert player_id not in online_players


def test_prune_stale_players_not_stale(connection_cleaner, mock_room_manager):
    """Test prune_stale_players() does not remove recent players."""
    now = time.time()
    player_id = uuid.uuid4()
    last_seen = {player_id: now - 30}  # 30 seconds ago (within threshold)
    online_players = {player_id: {"name": "Player1"}}
    player_websockets = {player_id: []}
    active_websockets = {}
    last_active_update_times = {}
    connection_cleaner.prune_stale_players(
        last_seen, online_players, player_websockets, active_websockets, last_active_update_times, max_age_seconds=90
    )
    # Player should still be in online_players
    assert player_id in online_players
