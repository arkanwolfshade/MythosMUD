"""
Unit tests for position commands.

Tests the posture-changing commands (sit, stand, lie).
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.position_commands import (
    _format_room_posture_message,
    _handle_position_change,
    handle_lie_command,
    handle_sit_command,
    handle_stand_command,
)


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    app = MagicMock()
    app.state = MagicMock()
    request = MagicMock()
    request.app = app
    return request


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.broadcast_to_room = AsyncMock()
    return manager


def test_format_room_posture_message_sitting():
    """Test formatting room message for sitting."""
    result = _format_room_posture_message("TestPlayer", None, "sitting")
    assert "settles into a seated position" in result


def test_format_room_posture_message_lying():
    """Test formatting room message for lying."""
    result = _format_room_posture_message("TestPlayer", None, "lying")
    assert "stretches out and lies prone" in result


def test_format_room_posture_message_standing_from_lying():
    """Test formatting room message for standing from lying."""
    result = _format_room_posture_message("TestPlayer", "lying", "standing")
    assert "pushes up from the floor" in result


def test_format_room_posture_message_standing_from_sitting():
    """Test formatting room message for standing from sitting."""
    result = _format_room_posture_message("TestPlayer", "sitting", "standing")
    assert "rises from their seat" in result


def test_format_room_posture_message_standing_no_previous():
    """Test formatting room message for standing with no previous position."""
    result = _format_room_posture_message("TestPlayer", None, "standing")
    assert "straightens and stands tall" in result


def test_format_room_posture_message_unknown():
    """Test formatting room message for unknown position."""
    result = _format_room_posture_message("TestPlayer", None, "unknown")
    assert "shifts their posture uneasily" in result


@pytest.mark.asyncio
async def test_handle_position_change_success(mock_request, mock_persistence, mock_connection_manager):
    """Test handling position change successfully."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager

    mock_position_service = MagicMock()
    mock_position_service.change_position = AsyncMock(
        return_value={
            "success": True,
            "position": "sitting",
            "previous_position": "standing",
            "player_display_name": "TestPlayer",
            "player_id": uuid.uuid4(),
            "room_id": "room_001",
            "message": "You sit down.",
        }
    )

    with patch("server.commands.position_commands.PlayerPositionService", return_value=mock_position_service):
        result = await _handle_position_change(
            {"username": "testuser"}, mock_request, None, "TestPlayer", "sitting", "sit"
        )

        assert result["changed"] is True
        assert result["position"] == "sitting"
        assert "room_message" in result
        mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_position_change_failure(mock_request, mock_persistence):
    """Test handling position change when it fails."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = None

    mock_position_service = MagicMock()
    mock_position_service.change_position = AsyncMock(
        return_value={
            "success": False,
            "position": "standing",
            "message": "You cannot sit right now.",
        }
    )

    with patch("server.commands.position_commands.PlayerPositionService", return_value=mock_position_service):
        result = await _handle_position_change(
            {"username": "testuser"}, mock_request, None, "TestPlayer", "sitting", "sit"
        )

        assert result["changed"] is False
        assert "You cannot sit right now" in result["result"]


@pytest.mark.asyncio
async def test_handle_position_change_no_connection_manager(mock_request, mock_persistence):
    """Test handling position change without connection manager."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = None

    mock_position_service = MagicMock()
    mock_position_service.change_position = AsyncMock(
        return_value={
            "success": True,
            "position": "sitting",
            "previous_position": "standing",
            "player_display_name": "TestPlayer",
            "player_id": uuid.uuid4(),
            "room_id": "room_001",
            "message": "You sit down.",
        }
    )

    with patch("server.commands.position_commands.PlayerPositionService", return_value=mock_position_service):
        result = await _handle_position_change(
            {"username": "testuser"}, mock_request, None, "TestPlayer", "sitting", "sit"
        )

        assert result["changed"] is True


@pytest.mark.asyncio
async def test_handle_position_change_broadcast_error(mock_request, mock_persistence, mock_connection_manager):
    """Test handling position change when broadcast fails."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_connection_manager.broadcast_to_room.side_effect = ValueError("Broadcast error")

    mock_position_service = MagicMock()
    mock_position_service.change_position = AsyncMock(
        return_value={
            "success": True,
            "position": "sitting",
            "previous_position": "standing",
            "player_display_name": "TestPlayer",
            "player_id": uuid.uuid4(),
            "room_id": "room_001",
            "message": "You sit down.",
        }
    )

    with patch("server.commands.position_commands.PlayerPositionService", return_value=mock_position_service):
        result = await _handle_position_change(
            {"username": "testuser"}, mock_request, None, "TestPlayer", "sitting", "sit"
        )

        # Should still succeed even if broadcast fails
        assert result["changed"] is True


@pytest.mark.asyncio
async def test_handle_sit_command(mock_request):
    """Test handle_sit_command delegates correctly."""
    with patch("server.commands.position_commands._handle_position_change", new_callable=AsyncMock) as mock_handle:
        mock_handle.return_value = {"result": "You sit down.", "changed": True}
        result = await handle_sit_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")
        mock_handle.assert_awaited_once_with(
            {"username": "testuser"},
            mock_request,
            None,
            "TestPlayer",
            desired_position="sitting",
            command_name="sit",
        )
        assert result["changed"] is True


@pytest.mark.asyncio
async def test_handle_stand_command(mock_request):
    """Test handle_stand_command delegates correctly."""
    with patch("server.commands.position_commands._handle_position_change", new_callable=AsyncMock) as mock_handle:
        mock_handle.return_value = {"result": "You stand up.", "changed": True}
        result = await handle_stand_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")
        mock_handle.assert_awaited_once_with(
            {"username": "testuser"},
            mock_request,
            None,
            "TestPlayer",
            desired_position="standing",
            command_name="stand",
        )
        assert result["changed"] is True


@pytest.mark.asyncio
async def test_handle_lie_command(mock_request):
    """Test handle_lie_command delegates correctly."""
    with patch("server.commands.position_commands._handle_position_change", new_callable=AsyncMock) as mock_handle:
        mock_handle.return_value = {"result": "You lie down.", "changed": True}
        result = await handle_lie_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")
        mock_handle.assert_awaited_once_with(
            {"username": "testuser"},
            mock_request,
            None,
            "TestPlayer",
            desired_position="lying",
            command_name="lie",
        )
        assert result["changed"] is True
