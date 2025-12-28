"""
Unit tests for player_cache utilities.

Tests the player caching functions for request-scoped caching.
"""

from unittest.mock import MagicMock

from server.utils.player_cache import cache_player, get_cached_player


def test_get_cached_player_none():
    """Test get_cached_player() returns None when no cache exists."""
    mock_request = MagicMock()
    mock_request.state = None
    result = get_cached_player(mock_request, "player1")
    assert result is None


def test_cache_and_get_player():
    """Test cache_player() and get_cached_player() operations."""
    mock_request = MagicMock()
    mock_state = MagicMock()
    mock_state._command_player_cache = None
    mock_request.state = mock_state

    mock_player = {"name": "TestPlayer", "id": "player1"}
    cache_player(mock_request, "player1", mock_player)
    result = get_cached_player(mock_request, "player1")
    assert result == mock_player


def test_get_cached_player_nonexistent():
    """Test get_cached_player() returns None for nonexistent key."""
    mock_request = MagicMock()
    mock_state = MagicMock()
    mock_state._command_player_cache = {}
    mock_request.state = mock_state

    result = get_cached_player(mock_request, "nonexistent")
    assert result is None


def test_cache_player_multiple():
    """Test cache_player() can cache multiple players."""
    mock_request = MagicMock()
    mock_state = MagicMock()
    mock_state._command_player_cache = None
    mock_request.state = mock_state

    player1 = {"name": "Player1", "id": "player1"}
    player2 = {"name": "Player2", "id": "player2"}

    cache_player(mock_request, "player1", player1)
    cache_player(mock_request, "player2", player2)

    assert get_cached_player(mock_request, "player1") == player1
    assert get_cached_player(mock_request, "player2") == player2


def test_cache_player_overwrite():
    """Test cache_player() overwrites existing entries."""
    mock_request = MagicMock()
    mock_state = MagicMock()
    mock_state._command_player_cache = None
    mock_request.state = mock_state

    player1_old = {"name": "Player1Old", "id": "player1"}
    player1_new = {"name": "Player1New", "id": "player1"}

    cache_player(mock_request, "player1", player1_old)
    cache_player(mock_request, "player1", player1_new)

    result = get_cached_player(mock_request, "player1")
    assert result == player1_new


def test_get_cached_player_no_state():
    """Test get_cached_player() handles missing state."""
    mock_request = MagicMock()
    mock_request.state = None
    result = get_cached_player(mock_request, "player1")
    assert result is None


def test_cache_player_no_state():
    """Test cache_player() handles missing state gracefully."""
    mock_request = MagicMock()
    mock_request.state = None
    # Should not raise
    cache_player(mock_request, "player1", {"name": "TestPlayer"})
