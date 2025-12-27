"""
Unit tests for status command handlers.

Tests handlers for status and whoami commands.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.status_commands import (
    _add_additional_stats_lines,
    _add_profession_lines,
    _build_base_status_lines,
    _get_combat_status,
    _get_profession_info,
    handle_status_command,
    handle_whoami_command,
)


@pytest.mark.asyncio
async def test_get_profession_info_no_profession_id():
    """Test _get_profession_info returns None values when profession_id is 0."""
    mock_player = MagicMock()
    mock_player.profession_id = 0
    mock_persistence = MagicMock()
    
    result = await _get_profession_info(mock_player, mock_persistence)
    
    assert result["name"] is None
    assert result["description"] is None
    assert result["flavor_text"] is None
    mock_persistence.get_profession_by_id.assert_not_called()


@pytest.mark.asyncio
async def test_get_profession_info_player_dict_no_profession_id():
    """Test _get_profession_info handles player as dict with no profession_id."""
    mock_player = {}
    mock_persistence = MagicMock()
    
    result = await _get_profession_info(mock_player, mock_persistence)
    
    assert result["name"] is None
    assert result["description"] is None
    assert result["flavor_text"] is None


@pytest.mark.asyncio
async def test_get_profession_info_with_profession():
    """Test _get_profession_info returns profession info when profession exists."""
    mock_player = MagicMock()
    mock_player.profession_id = 1
    mock_profession = MagicMock()
    mock_profession.name = "Investigator"
    mock_profession.description = "A seeker of truth"
    mock_profession.flavor_text = "In the shadows of Arkham"
    mock_persistence = MagicMock()
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
    
    result = await _get_profession_info(mock_player, mock_persistence)
    
    assert result["name"] == "Investigator"
    assert result["description"] == "A seeker of truth"
    assert result["flavor_text"] == "In the shadows of Arkham"
    mock_persistence.get_profession_by_id.assert_awaited_once_with(1)


@pytest.mark.asyncio
async def test_get_profession_info_profession_not_found():
    """Test _get_profession_info returns None values when profession not found."""
    mock_player = MagicMock()
    mock_player.profession_id = 999
    mock_persistence = MagicMock()
    mock_persistence.get_profession_by_id = AsyncMock(return_value=None)
    
    result = await _get_profession_info(mock_player, mock_persistence)
    
    assert result["name"] is None
    assert result["description"] is None
    assert result["flavor_text"] is None


@pytest.mark.asyncio
async def test_get_profession_info_error_handling():
    """Test _get_profession_info handles errors gracefully."""
    mock_player = MagicMock()
    mock_player.profession_id = 1
    mock_persistence = MagicMock()
    mock_persistence.get_profession_by_id = AsyncMock(side_effect=AttributeError("Test error"))
    
    result = await _get_profession_info(mock_player, mock_persistence)
    
    assert result["name"] is None
    assert result["description"] is None
    assert result["flavor_text"] is None


@pytest.mark.asyncio
async def test_get_combat_status_no_combat_service():
    """Test _get_combat_status returns False when no combat service."""
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    # Use hasattr check - if combat_service doesn't exist, accessing it returns None
    # The code does: app.state.combat_service if app else None
    # So we need to ensure app.state.combat_service is None/doesn't exist
    type(mock_app.state).combat_service = None  # Set to None
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    
    result = await _get_combat_status(mock_app, mock_player)
    
    assert result is False


@pytest.mark.asyncio
async def test_get_combat_status_no_app():
    """Test _get_combat_status returns False when no app."""
    mock_player = MagicMock()
    
    result = await _get_combat_status(None, mock_player)
    
    assert result is False


@pytest.mark.asyncio
async def test_get_combat_status_player_in_combat():
    """Test _get_combat_status returns True when player is in combat."""
    mock_combat = MagicMock()
    mock_combat_service = MagicMock()
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.combat_service = mock_combat_service
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    
    result = await _get_combat_status(mock_app, mock_player)
    
    assert result is True
    mock_combat_service.get_combat_by_participant.assert_awaited_once_with("test-player-id")


@pytest.mark.asyncio
async def test_get_combat_status_player_not_in_combat():
    """Test _get_combat_status returns False when player is not in combat."""
    mock_combat_service = MagicMock()
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.combat_service = mock_combat_service
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    
    result = await _get_combat_status(mock_app, mock_player)
    
    assert result is False


def test_build_base_status_lines():
    """Test _build_base_status_lines builds correct status lines."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.experience_points = 100
    stats = {
        "position": "sitting",
        "current_dp": 80,
        "max_dp": 100,
        "lucidity": 75,
        "max_lucidity": 100,
    }
    
    result = _build_base_status_lines(mock_player, "Test Room", stats, False)
    
    assert "Name: TestPlayer" in result
    assert "Location: Test Room" in result
    assert "Position: Sitting" in result
    assert "Health: 80/100" in result
    assert "lucidity: 75/100" in result
    assert "XP: 100" in result
    assert "In Combat: No" in result


def test_build_base_status_lines_in_combat():
    """Test _build_base_status_lines shows combat status correctly."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.experience_points = 100
    stats = {"position": "standing", "current_dp": 100, "max_dp": 100, "lucidity": 100, "max_lucidity": 100}
    
    result = _build_base_status_lines(mock_player, "Test Room", stats, True)
    
    assert "In Combat: Yes" in result


def test_add_profession_lines_with_profession():
    """Test _add_profession_lines adds profession info when available."""
    status_lines = []
    profession_info = {
        "name": "Investigator",
        "description": "A seeker of truth",
        "flavor_text": "In the shadows of Arkham",
    }
    
    _add_profession_lines(status_lines, profession_info)
    
    assert len(status_lines) == 3
    assert "Profession: Investigator" in status_lines
    assert "Description: A seeker of truth" in status_lines
    assert "Background: In the shadows of Arkham" in status_lines


def test_add_profession_lines_no_name():
    """Test _add_profession_lines does nothing when no profession name."""
    status_lines = []
    profession_info = {"name": None, "description": "Some description", "flavor_text": "Some text"}
    
    _add_profession_lines(status_lines, profession_info)
    
    assert len(status_lines) == 0


def test_add_profession_lines_partial_info():
    """Test _add_profession_lines handles partial profession info."""
    status_lines = []
    profession_info = {"name": "Investigator", "description": None, "flavor_text": None}
    
    _add_profession_lines(status_lines, profession_info)
    
    assert len(status_lines) == 1
    assert "Profession: Investigator" in status_lines


def test_add_additional_stats_lines_with_stats():
    """Test _add_additional_stats_lines adds stats when non-zero."""
    status_lines = []
    stats = {"fear": 10, "corruption": 5, "occult_knowledge": 20}
    
    _add_additional_stats_lines(status_lines, stats)
    
    assert len(status_lines) == 3
    assert "Fear: 10" in status_lines
    assert "Corruption: 5" in status_lines
    assert "Occult Knowledge: 20" in status_lines


def test_add_additional_stats_lines_zero_stats():
    """Test _add_additional_stats_lines does nothing when stats are zero."""
    status_lines = []
    stats = {"fear": 0, "corruption": 0, "occult_knowledge": 0}
    
    _add_additional_stats_lines(status_lines, stats)
    
    assert len(status_lines) == 0


def test_add_additional_stats_lines_missing_stats():
    """Test _add_additional_stats_lines handles missing stats."""
    status_lines = []
    stats = {}
    
    _add_additional_stats_lines(status_lines, stats)
    
    assert len(status_lines) == 0


@pytest.mark.asyncio
async def test_handle_status_command_no_persistence():
    """Test handle_status_command returns error when no persistence."""
    mock_request = MagicMock()
    mock_request.app = None
    
    result = await handle_status_command({}, {}, mock_request, None, "testplayer")
    
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_status_command_player_not_found():
    """Test handle_status_command returns error when player not found."""
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_status_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "not found" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_status_command_success():
    """Test handle_status_command returns status information successfully."""
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.current_room_id = "test_room"
    mock_player.experience_points = 100
    mock_player.get_stats = MagicMock(return_value={
        "position": "standing",
        "current_dp": 100,
        "max_dp": 100,
        "lucidity": 100,
        "max_lucidity": 100,
    })
    mock_room = MagicMock()
    mock_room.name = "Test Room"
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_profession_by_id = AsyncMock(return_value=None)
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    mock_combat_service = MagicMock()
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.combat_service = mock_combat_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_status_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "result" in result
    assert "Name: TestPlayer" in result["result"]
    assert "Location: Test Room" in result["result"]


@pytest.mark.asyncio
async def test_handle_status_command_error_handling():
    """Test handle_status_command handles errors gracefully."""
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(side_effect=AttributeError("Test error"))
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_status_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "Error" in result["result"]


@pytest.mark.asyncio
async def test_handle_whoami_command():
    """Test handle_whoami_command calls handle_status_command."""
    mock_request = MagicMock()
    mock_request.app = None
    
    result = await handle_whoami_command({}, {}, mock_request, None, "testplayer")
    
    # Should return same result as status command
    assert "result" in result
