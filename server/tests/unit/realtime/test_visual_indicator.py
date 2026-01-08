"""
Unit tests for visual indicator (linkdead) display.

Tests that "(linkdead)" indicator is properly displayed for players in grace period
in room occupant lists and /look command output.
"""

import uuid
from unittest.mock import MagicMock, patch

import pytest

from server.commands.look_player import _format_player_look_display
from server.commands.look_room import _filter_other_players
from server.realtime.player_occupant_processor import PlayerOccupantProcessor


@pytest.mark.asyncio
async def test_filter_other_players_adds_linkdead_indicator():
    """Test _filter_other_players() adds (linkdead) indicator for grace period players."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = str(player_id)
    players_in_room = [mock_player]
    player_name = "OtherPlayer"

    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {player_id: MagicMock()}  # Player in grace period

    with patch("server.commands.look_room.is_player_in_grace_period", return_value=True):
        result = await _filter_other_players(players_in_room, player_name, mock_connection_manager)

        assert len(result) == 1
        assert "(linkdead)" in result[0]
        assert "TestPlayer" in result[0]


@pytest.mark.asyncio
async def test_filter_other_players_no_linkdead_when_not_in_grace_period():
    """Test _filter_other_players() does not add (linkdead) when player not in grace period."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = str(player_id)
    players_in_room = [mock_player]
    player_name = "OtherPlayer"

    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {}  # Player not in grace period

    with patch("server.commands.look_room.is_player_in_grace_period", return_value=False):
        result = await _filter_other_players(players_in_room, player_name, mock_connection_manager)

        assert len(result) == 1
        assert "(linkdead)" not in result[0]
        assert result[0] == "TestPlayer"


def test_format_player_look_display_adds_linkdead_indicator():
    """Test _format_player_look_display() adds (linkdead) indicator for grace period players."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = str(player_id)
    mock_player.get_stats = MagicMock(return_value={"position": "standing"})

    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {player_id: MagicMock()}  # Player in grace period

    with patch("server.commands.look_player.is_player_in_grace_period", return_value=True):
        with patch("server.commands.look_player._get_health_label", return_value="Healthy"):
            with patch("server.commands.look_player._get_lucidity_label", return_value="Sane"):
                with patch("server.commands.look_player._get_visible_equipment", return_value={}):
                    result = _format_player_look_display(mock_player, mock_connection_manager)

                    assert "(linkdead)" in result
                    assert "TestPlayer" in result


def test_format_player_look_display_no_linkdead_when_not_in_grace_period():
    """Test _format_player_look_display() does not add (linkdead) when player not in grace period."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = str(player_id)
    mock_player.get_stats = MagicMock(return_value={"position": "standing"})

    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {}  # Player not in grace period

    with patch("server.commands.look_player.is_player_in_grace_period", return_value=False):
        with patch("server.commands.look_player._get_health_label", return_value="Healthy"):
            with patch("server.commands.look_player._get_lucidity_label", return_value="Sane"):
                with patch("server.commands.look_player._get_visible_equipment", return_value={}):
                    result = _format_player_look_display(mock_player, mock_connection_manager)

                    assert "(linkdead)" not in result
                    assert "TestPlayer" in result


def test_player_occupant_processor_adds_linkdead_indicator():
    """Test PlayerOccupantProcessor adds (linkdead) indicator for grace period players."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {player_id: MagicMock()}  # Player in grace period
    mock_name_extractor = MagicMock()
    mock_name_extractor.extract_and_validate_player_name = MagicMock(return_value="TestPlayer")

    processor = PlayerOccupantProcessor(mock_connection_manager, mock_name_extractor)

    with patch("server.realtime.player_occupant_processor.is_player_in_grace_period", return_value=True):
        # Accessing protected member is necessary to test the method used by PlayerOccupantProcessor implementation
        result = processor._create_player_occupant_info(player_id, str(player_id), mock_player)  # pylint: disable=protected-access

        assert result is not None
        assert "(linkdead)" in result["player_name"]
        assert "TestPlayer" in result["player_name"]


def test_player_occupant_processor_no_linkdead_when_not_in_grace_period():
    """Test PlayerOccupantProcessor does not add (linkdead) when player not in grace period."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {}  # Player not in grace period
    mock_connection_manager.player_websockets = {}
    mock_name_extractor = MagicMock()
    mock_name_extractor.extract_and_validate_player_name = MagicMock(return_value="TestPlayer")

    processor = PlayerOccupantProcessor(mock_connection_manager, mock_name_extractor)

    with patch("server.realtime.player_occupant_processor.is_player_in_grace_period", return_value=False):
        # Accessing protected member is necessary to test the method used by PlayerOccupantProcessor implementation
        result = processor._create_player_occupant_info(player_id, str(player_id), mock_player)  # pylint: disable=protected-access

        assert result is not None
        assert "(linkdead)" not in result["player_name"]
        assert result["player_name"] == "TestPlayer"
