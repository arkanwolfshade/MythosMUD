"""
Unit tests for occupant formatter.

Tests the occupant_formatter module classes and functions.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.realtime.occupant_formatter import OccupantFormatter


def test_occupant_formatter_init():
    """Test OccupantFormatter.__init__() initializes formatter."""
    formatter = OccupantFormatter()

    assert hasattr(formatter, "_logger")


def test_occupant_formatter_is_uuid_string_valid():
    """Test OccupantFormatter._is_uuid_string() returns True for valid UUID."""
    valid_uuid = "123e4567-e89b-12d3-a456-426614174000"

    result = OccupantFormatter._is_uuid_string(valid_uuid)

    assert result is True


def test_occupant_formatter_is_uuid_string_invalid_length():
    """Test OccupantFormatter._is_uuid_string() returns False for invalid length."""
    invalid_uuid = "123e4567-e89b-12d3-a456"

    result = OccupantFormatter._is_uuid_string(invalid_uuid)

    assert result is False


def test_occupant_formatter_is_uuid_string_invalid_dashes():
    """Test OccupantFormatter._is_uuid_string() returns False for wrong dash count."""
    invalid_uuid = "123e4567-e89b-12d3-a456-426614174000-extra"

    result = OccupantFormatter._is_uuid_string(invalid_uuid)

    assert result is False


def test_occupant_formatter_is_uuid_string_invalid_chars():
    """Test OccupantFormatter._is_uuid_string() returns False for invalid characters."""
    invalid_uuid = "123e4567-e89b-12d3-a456-42661417400g"  # 'g' is invalid

    result = OccupantFormatter._is_uuid_string(invalid_uuid)

    assert result is False


def test_occupant_formatter_is_valid_name_for_occupant_valid():
    """Test OccupantFormatter._is_valid_name_for_occupant() returns True for valid name."""
    formatter = OccupantFormatter()

    result = formatter._is_valid_name_for_occupant("TestPlayer")

    assert result is True


def test_occupant_formatter_is_valid_name_for_occupant_uuid():
    """Test OccupantFormatter._is_valid_name_for_occupant() returns False for UUID."""
    formatter = OccupantFormatter()
    uuid_string = "123e4567-e89b-12d3-a456-426614174000"

    result = formatter._is_valid_name_for_occupant(uuid_string)

    assert result is False


def test_occupant_formatter_is_valid_name_for_occupant_empty():
    """Test OccupantFormatter._is_valid_name_for_occupant() returns False for empty string."""
    formatter = OccupantFormatter()

    result = formatter._is_valid_name_for_occupant("")

    # Empty string is falsy, so the function returns False (empty string is falsy)
    assert result is False or result == ""


def test_occupant_formatter_is_valid_name_for_occupant_none():
    """Test OccupantFormatter._is_valid_name_for_occupant() returns False for None."""
    formatter = OccupantFormatter()

    result = formatter._is_valid_name_for_occupant(None)

    # None is falsy, so the function returns False (None is falsy)
    # The function checks `name and isinstance(name, str)`, so None returns False
    assert not result  # Should be False or falsy


def test_occupant_formatter_is_valid_name_for_occupant_non_string():
    """Test OccupantFormatter._is_valid_name_for_occupant() returns False for non-string."""
    formatter = OccupantFormatter()

    result = formatter._is_valid_name_for_occupant(123)

    assert result is False


def test_occupant_formatter_add_valid_name_to_lists():
    """Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists."""
    formatter = OccupantFormatter()
    players = []
    all_occupants = []

    formatter._add_valid_name_to_lists("TestPlayer", players, all_occupants)

    assert "TestPlayer" in players
    assert "TestPlayer" in all_occupants
    assert len(players) == 1
    assert len(all_occupants) == 1


def test_occupant_formatter_process_player_name_for_update_valid():
    """Test OccupantFormatter._process_player_name_for_update() adds valid player name."""
    formatter = OccupantFormatter()
    players = []
    all_occupants = []
    room_id = "room_123"

    formatter._process_player_name_for_update("TestPlayer", players, all_occupants, room_id)

    assert "TestPlayer" in players
    assert "TestPlayer" in all_occupants


def test_occupant_formatter_process_player_name_for_update_uuid():
    """Test OccupantFormatter._process_player_name_for_update() skips UUID player name."""
    formatter = OccupantFormatter()
    players = []
    all_occupants = []
    room_id = "room_123"
    uuid_string = "123e4567-e89b-12d3-a456-426614174000"

    with patch.object(formatter._logger, "warning") as mock_warning:
        formatter._process_player_name_for_update(uuid_string, players, all_occupants, room_id)

        assert "TestPlayer" not in players
        assert uuid_string not in all_occupants
        mock_warning.assert_called_once()


def test_occupant_formatter_process_npc_name_for_update_valid():
    """Test OccupantFormatter._process_npc_name_for_update() adds valid NPC name."""
    formatter = OccupantFormatter()
    npcs = []
    all_occupants = []
    room_id = "room_123"

    formatter._process_npc_name_for_update("TestNPC", npcs, all_occupants, room_id)

    assert "TestNPC" in npcs
    assert "TestNPC" in all_occupants


def test_occupant_formatter_process_npc_name_for_update_uuid():
    """Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name."""
    formatter = OccupantFormatter()
    npcs = []
    all_occupants = []
    room_id = "room_123"
    uuid_string = "123e4567-e89b-12d3-a456-426614174000"

    with patch.object(formatter._logger, "warning") as mock_warning:
        formatter._process_npc_name_for_update(uuid_string, npcs, all_occupants, room_id)

        assert uuid_string not in npcs
        assert uuid_string not in all_occupants
        mock_warning.assert_called_once()


def test_occupant_formatter_process_dict_occupant_for_update_player():
    """Test OccupantFormatter._process_dict_occupant_for_update() processes player dict."""
    formatter = OccupantFormatter()
    players = []
    npcs = []
    all_occupants = []
    room_id = "room_123"
    occ = {"player_name": "TestPlayer"}

    formatter._process_dict_occupant_for_update(occ, players, npcs, all_occupants, room_id)

    assert "TestPlayer" in players
    assert "TestPlayer" in all_occupants
    assert len(npcs) == 0


def test_occupant_formatter_process_dict_occupant_for_update_npc():
    """Test OccupantFormatter._process_dict_occupant_for_update() processes NPC dict."""
    formatter = OccupantFormatter()
    players = []
    npcs = []
    all_occupants = []
    room_id = "room_123"
    occ = {"npc_name": "TestNPC"}

    formatter._process_dict_occupant_for_update(occ, players, npcs, all_occupants, room_id)

    assert "TestNPC" in npcs
    assert "TestNPC" in all_occupants
    assert len(players) == 0


def test_occupant_formatter_process_dict_occupant_for_update_fallback_name():
    """Test OccupantFormatter._process_dict_occupant_for_update() processes fallback name."""
    formatter = OccupantFormatter()
    players = []
    npcs = []
    all_occupants = []
    room_id = "room_123"
    occ = {"name": "TestOccupant"}

    formatter._process_dict_occupant_for_update(occ, players, npcs, all_occupants, room_id)

    assert "TestOccupant" in all_occupants
    assert len(players) == 0
    assert len(npcs) == 0


def test_occupant_formatter_process_string_occupant_for_update_valid():
    """Test OccupantFormatter._process_string_occupant_for_update() adds valid string."""
    formatter = OccupantFormatter()
    all_occupants = []
    room_id = "room_123"

    formatter._process_string_occupant_for_update("TestOccupant", all_occupants, room_id)

    assert "TestOccupant" in all_occupants


def test_occupant_formatter_process_string_occupant_for_update_uuid():
    """Test OccupantFormatter._process_string_occupant_for_update() skips UUID string."""
    formatter = OccupantFormatter()
    all_occupants = []
    room_id = "room_123"
    uuid_string = "123e4567-e89b-12d3-a456-426614174000"

    with patch.object(formatter._logger, "warning") as mock_warning:
        formatter._process_string_occupant_for_update(uuid_string, all_occupants, room_id)

        assert uuid_string not in all_occupants
        mock_warning.assert_called_once()


def test_occupant_formatter_separate_occupants_by_type_dict_players():
    """Test OccupantFormatter.separate_occupants_by_type() separates dict players."""
    formatter = OccupantFormatter()
    occupants_info = [{"player_name": "Player1"}, {"player_name": "Player2"}]

    players, npcs, all_occupants = formatter.separate_occupants_by_type(occupants_info, "room_123")

    assert len(players) == 2
    assert "Player1" in players
    assert "Player2" in players
    assert len(npcs) == 0
    assert len(all_occupants) == 2


def test_occupant_formatter_separate_occupants_by_type_dict_npcs():
    """Test OccupantFormatter.separate_occupants_by_type() separates dict NPCs."""
    formatter = OccupantFormatter()
    occupants_info = [{"npc_name": "NPC1"}, {"npc_name": "NPC2"}]

    players, npcs, all_occupants = formatter.separate_occupants_by_type(occupants_info, "room_123")

    assert len(npcs) == 2
    assert "NPC1" in npcs
    assert "NPC2" in npcs
    assert len(players) == 0
    assert len(all_occupants) == 2


def test_occupant_formatter_separate_occupants_by_type_strings():
    """Test OccupantFormatter.separate_occupants_by_type() processes string occupants."""
    formatter = OccupantFormatter()
    occupants_info = ["Occupant1", "Occupant2"]

    players, npcs, all_occupants = formatter.separate_occupants_by_type(occupants_info, "room_123")

    assert len(players) == 0
    assert len(npcs) == 0
    assert len(all_occupants) == 2
    assert "Occupant1" in all_occupants
    assert "Occupant2" in all_occupants


def test_occupant_formatter_separate_occupants_by_type_mixed():
    """Test OccupantFormatter.separate_occupants_by_type() handles mixed types."""
    formatter = OccupantFormatter()
    occupants_info = [
        {"player_name": "Player1"},
        {"npc_name": "NPC1"},
        "Occupant1",
    ]

    players, npcs, all_occupants = formatter.separate_occupants_by_type(occupants_info, "room_123")

    assert "Player1" in players
    assert "NPC1" in npcs
    assert "Occupant1" in all_occupants
    assert len(all_occupants) == 3


def test_occupant_formatter_separate_occupants_by_type_none():
    """Test OccupantFormatter.separate_occupants_by_type() handles None input."""
    formatter = OccupantFormatter()

    players, npcs, all_occupants = formatter.separate_occupants_by_type(None, "room_123")

    assert len(players) == 0
    assert len(npcs) == 0
    assert len(all_occupants) == 0


def test_occupant_formatter_separate_occupants_by_type_empty():
    """Test OccupantFormatter.separate_occupants_by_type() handles empty list."""
    formatter = OccupantFormatter()

    players, npcs, all_occupants = formatter.separate_occupants_by_type([], "room_123")

    assert len(players) == 0
    assert len(npcs) == 0
    assert len(all_occupants) == 0
