"""
Unit tests for logout_commands helper functions.

Tests helper functions in logout_commands.py module.
"""

from unittest.mock import MagicMock

from server.commands.logout_commands import (
    _clear_corrupted_cache_entry,
)


def test_clear_corrupted_cache_entry():
    """Test _clear_corrupted_cache_entry() clears cache entry."""
    request = MagicMock()
    request.state = MagicMock()
    request.state._command_player_cache = {"TestPlayer": "cached_data"}

    _clear_corrupted_cache_entry(request, "TestPlayer")

    assert "TestPlayer" not in request.state._command_player_cache


def test_clear_corrupted_cache_entry_no_request():
    """Test _clear_corrupted_cache_entry() handles None request."""
    _clear_corrupted_cache_entry(None, "TestPlayer")
    # Should not raise


def test_clear_corrupted_cache_entry_no_state():
    """Test _clear_corrupted_cache_entry() handles request without state."""
    request = MagicMock()
    del request.state

    _clear_corrupted_cache_entry(request, "TestPlayer")
    # Should not raise
