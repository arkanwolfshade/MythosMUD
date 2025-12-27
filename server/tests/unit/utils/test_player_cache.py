"""
Unit tests for player caching utilities.

Tests helpers for caching player objects during a single command request.
"""

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from server.utils.player_cache import cache_player, get_cached_player


def test_get_cached_player_no_request():
    """Test get_cached_player returns None when request is None."""
    result = get_cached_player(None, "testplayer")
    
    assert result is None


def test_get_cached_player_no_state():
    """Test get_cached_player returns None when request has no state."""
    request = MagicMock()
    del request.state  # Remove state attribute
    
    result = get_cached_player(request, "testplayer")
    
    assert result is None


def test_get_cached_player_no_cache():
    """Test get_cached_player returns None when state has no cache."""
    request = MagicMock()
    request.state = SimpleNamespace()
    
    result = get_cached_player(request, "testplayer")
    
    assert result is None


def test_get_cached_player_cache_not_dict():
    """Test get_cached_player returns None when cache is not a dict."""
    request = MagicMock()
    request.state = SimpleNamespace(_command_player_cache="not_a_dict")
    
    result = get_cached_player(request, "testplayer")
    
    assert result is None


def test_get_cached_player_player_not_in_cache():
    """Test get_cached_player returns None when player not in cache."""
    request = MagicMock()
    request.state = SimpleNamespace(_command_player_cache={"otherplayer": MagicMock()})
    
    result = get_cached_player(request, "testplayer")
    
    assert result is None


def test_get_cached_player_player_in_cache():
    """Test get_cached_player returns cached player."""
    mock_player = MagicMock()
    request = MagicMock()
    request.state = SimpleNamespace(_command_player_cache={"testplayer": mock_player})
    
    result = get_cached_player(request, "testplayer")
    
    assert result == mock_player


def test_cache_player_no_request():
    """Test cache_player does nothing when request is None."""
    # Should not raise
    cache_player(None, "testplayer", MagicMock())


def test_cache_player_no_state():
    """Test cache_player does nothing when request has no state."""
    request = MagicMock()
    del request.state  # Remove state attribute
    
    # Should not raise
    cache_player(request, "testplayer", MagicMock())


def test_cache_player_creates_cache():
    """Test cache_player creates cache if it doesn't exist."""
    request = MagicMock()
    request.state = SimpleNamespace()
    mock_player = MagicMock()
    
    cache_player(request, "testplayer", mock_player)
    
    assert hasattr(request.state, "_command_player_cache")
    assert isinstance(request.state._command_player_cache, dict)
    assert request.state._command_player_cache["testplayer"] == mock_player


def test_cache_player_uses_existing_cache():
    """Test cache_player uses existing cache if it exists."""
    existing_cache = {"otherplayer": MagicMock()}
    request = MagicMock()
    request.state = SimpleNamespace(_command_player_cache=existing_cache)
    mock_player = MagicMock()
    
    cache_player(request, "testplayer", mock_player)
    
    assert request.state._command_player_cache == existing_cache
    assert existing_cache["testplayer"] == mock_player
    assert existing_cache["otherplayer"] is not None


def test_cache_player_overwrites_existing():
    """Test cache_player overwrites existing player in cache."""
    mock_player1 = MagicMock()
    mock_player2 = MagicMock()
    request = MagicMock()
    request.state = SimpleNamespace(_command_player_cache={"testplayer": mock_player1})
    
    cache_player(request, "testplayer", mock_player2)
    
    assert request.state._command_player_cache["testplayer"] == mock_player2


def test_cache_player_cache_not_dict():
    """Test cache_player replaces cache if it's not a dict."""
    request = MagicMock()
    request.state = SimpleNamespace(_command_player_cache="not_a_dict")
    mock_player = MagicMock()
    
    cache_player(request, "testplayer", mock_player)
    
    assert isinstance(request.state._command_player_cache, dict)
    assert request.state._command_player_cache["testplayer"] == mock_player


def test_get_and_cache_player_round_trip():
    """Test get_cached_player and cache_player work together."""
    request = MagicMock()
    request.state = SimpleNamespace()
    mock_player = MagicMock()
    
    # Cache player
    cache_player(request, "testplayer", mock_player)
    
    # Retrieve cached player
    result = get_cached_player(request, "testplayer")
    
    assert result == mock_player
