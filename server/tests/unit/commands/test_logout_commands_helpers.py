"""
Unit tests for logout_commands helper functions.

Tests helper functions in logout_commands.py module.
"""

from unittest.mock import MagicMock

from server.commands.logout_commands import (
    _clear_corrupted_cache_entry,
    _get_player_position_from_connection_manager,
    _sync_player_position,
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


def test_get_player_position_from_connection_manager():
    """Test _get_player_position_from_connection_manager() returns position."""
    connection_manager = MagicMock()
    connection_manager.online_players = {"player_001": {"position": "sitting"}}
    player = MagicMock()
    player.player_id = "player_001"

    result = _get_player_position_from_connection_manager(connection_manager, player, "TestPlayer")

    assert result == "sitting"


def test_get_player_position_from_connection_manager_by_name():
    """Test _get_player_position_from_connection_manager() finds by display name."""
    connection_manager = MagicMock()
    connection_manager.online_players = {}
    connection_manager.get_online_player_by_display_name.return_value = {"position": "standing"}
    player = MagicMock()
    player.player_id = None

    result = _get_player_position_from_connection_manager(connection_manager, player, "TestPlayer")

    assert result == "standing"


def test_get_player_position_from_connection_manager_no_manager():
    """Test _get_player_position_from_connection_manager() returns None when no manager."""
    result = _get_player_position_from_connection_manager(None, MagicMock(), "TestPlayer")

    assert result is None


def test_get_player_position_from_connection_manager_not_found():
    """Test _get_player_position_from_connection_manager() returns None when player not found."""
    connection_manager = MagicMock()
    connection_manager.online_players = {}
    connection_manager.get_online_player_by_display_name.return_value = None
    player = MagicMock()
    player.player_id = None

    result = _get_player_position_from_connection_manager(connection_manager, player, "TestPlayer")

    assert result is None


def test_sync_player_position():
    """Test _sync_player_position() updates player stats."""
    player = MagicMock()
    player.get_stats.return_value = {"position": "standing"}
    player.set_stats = MagicMock()

    _sync_player_position(player, "sitting")

    player.set_stats.assert_called_once()
    call_args = player.set_stats.call_args[0][0]
    assert call_args["position"] == "sitting"


def test_sync_player_position_none():
    """Test _sync_player_position() does nothing when position is None."""
    player = MagicMock()
    player.get_stats.return_value = {"position": "standing"}

    _sync_player_position(player, None)

    player.set_stats.assert_not_called()


def test_sync_player_position_no_change():
    """Test _sync_player_position() does nothing when position matches."""
    player = MagicMock()
    player.get_stats.return_value = {"position": "standing"}

    _sync_player_position(player, "standing")

    player.set_stats.assert_not_called()
