"""
Unit tests for look_player helper functions.

Tests the helper functions in look_player.py module.
"""

from unittest.mock import MagicMock

from server.commands.look_player import _format_player_look_display, _select_target_player


def test_select_target_player_single_match():
    """Test _select_target_player() returns single matching player."""
    player1 = MagicMock()
    player1.name = "Player1"
    matching_players = [player1]

    target_player, error_result = _select_target_player(matching_players, "player1", None, "CurrentPlayer")

    assert target_player == player1
    assert error_result is None


def test_select_target_player_no_match():
    """Test _select_target_player() returns error when no match."""
    matching_players = []

    target_player, error_result = _select_target_player(matching_players, "player1", None, "CurrentPlayer")

    assert target_player is None
    assert error_result is not None
    assert "don't see anyone" in error_result["result"]


def test_select_target_player_with_instance_number():
    """Test _select_target_player() uses instance_number."""
    player1 = MagicMock()
    player1.name = "Player1"
    player2 = MagicMock()
    player2.name = "Player2"
    matching_players = [player1, player2]

    target_player, error_result = _select_target_player(matching_players, "player", 2, "CurrentPlayer")

    assert target_player == player2
    assert error_result is None


def test_select_target_player_instance_number_out_of_range():
    """Test _select_target_player() returns error for invalid instance number."""
    player1 = MagicMock()
    player1.name = "Player1"
    matching_players = [player1]

    target_player, error_result = _select_target_player(matching_players, "player", 5, "CurrentPlayer")

    assert target_player is None
    assert error_result is not None
    assert "aren't that many" in error_result["result"]


def test_select_target_player_multiple_matches():
    """Test _select_target_player() returns error for multiple matches."""
    player1 = MagicMock()
    player1.name = "Player1"
    player2 = MagicMock()
    player2.name = "Player2"
    matching_players = [player1, player2]

    target_player, error_result = _select_target_player(matching_players, "player", None, "CurrentPlayer")

    assert target_player is None
    assert error_result is not None
    assert "multiple players" in error_result["result"]


def test_format_player_look_display():
    """Test _format_player_look_display() formats player display."""
    target_player = MagicMock()
    target_player.name = "TestPlayer"
    target_player.get_stats.return_value = {
        "position": "standing",
        "current_dp": 20,
        "max_dp": 20,
        "lucidity": 100,
    }
    target_player.get_equipped_items.return_value = {
        "weapon": {"item_name": "Sword"},
    }

    result = _format_player_look_display(target_player)

    assert "TestPlayer" in result
    assert "Position:" in result
    assert "Health:" in result
    assert "lucidity:" in result


def test_format_player_look_display_no_equipment():
    """Test _format_player_look_display() handles player with no equipment."""
    target_player = MagicMock()
    target_player.name = "TestPlayer"
    target_player.get_stats.return_value = {
        "position": "standing",
        "current_dp": 20,
        "max_dp": 20,
        "lucidity": 100,
    }
    target_player.get_equipped_items.return_value = {}

    result = _format_player_look_display(target_player)

    assert "TestPlayer" in result
    assert "Visible Equipment" not in result


def test_format_player_look_display_unknown_name():
    """Test _format_player_look_display() handles player without name."""
    target_player = MagicMock()
    del target_player.name
    target_player.get_stats.return_value = {"position": "standing"}
    target_player.get_equipped_items.return_value = {}

    result = _format_player_look_display(target_player)

    assert "Unknown" in result
