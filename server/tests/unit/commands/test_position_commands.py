"""
Unit tests for position command handlers.

Tests handlers for posture adjustment commands (sit, stand, lie).
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


def test_format_room_posture_message_sitting():
    """Test _format_room_posture_message formats sitting message."""
    result = _format_room_posture_message("TestPlayer", None, "sitting")
    
    assert "settles into a seated position" in result
    assert "TestPlayer" in result


def test_format_room_posture_message_lying():
    """Test _format_room_posture_message formats lying message."""
    result = _format_room_posture_message("TestPlayer", None, "lying")
    
    assert "stretches out and lies prone" in result
    assert "TestPlayer" in result


def test_format_room_posture_message_standing_from_lying():
    """Test _format_room_posture_message formats standing from lying."""
    result = _format_room_posture_message("TestPlayer", "lying", "standing")
    
    assert "pushes up from the floor" in result
    assert "TestPlayer" in result


def test_format_room_posture_message_standing_from_sitting():
    """Test _format_room_posture_message formats standing from sitting."""
    result = _format_room_posture_message("TestPlayer", "sitting", "standing")
    
    assert "rises from their seat" in result
    assert "TestPlayer" in result


def test_format_room_posture_message_standing_no_previous():
    """Test _format_room_posture_message formats standing with no previous position."""
    result = _format_room_posture_message("TestPlayer", None, "standing")
    
    assert "straightens and stands tall" in result
    assert "TestPlayer" in result


def test_format_room_posture_message_unknown_position():
    """Test _format_room_posture_message handles unknown position."""
    result = _format_room_posture_message("TestPlayer", None, "unknown")
    
    assert "shifts their posture uneasily" in result
    assert "TestPlayer" in result


@pytest.mark.asyncio
async def test_handle_position_change_no_persistence():
    """Test _handle_position_change handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None
    
    result = await _handle_position_change({}, mock_request, None, "testplayer", "sitting", "sit")
    
    assert "result" in result
    assert result["changed"] is False


@pytest.mark.asyncio
async def test_handle_position_change_success():
    """Test _handle_position_change successfully changes position."""
    mock_player_id = uuid.uuid4()
    mock_room_id = "test-room"
    mock_persistence = MagicMock()
    mock_position_service = MagicMock()
    mock_position_service.change_position = AsyncMock(return_value={
        "success": True,
        "position": "sitting",
        "previous_position": "standing",
        "player_display_name": "TestPlayer",
        "player_id": mock_player_id,
        "room_id": mock_room_id,
        "message": "You sit down.",
    })
    
    mock_connection_manager = MagicMock()
    mock_connection_manager.broadcast_to_room = AsyncMock()
    
    mock_state = MagicMock()
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    with patch("server.commands.position_commands.PlayerPositionService", return_value=mock_position_service):
        with patch("server.commands.position_commands.build_event", return_value={"type": "player_posture_change"}):
            result = await _handle_position_change(
                {"username": "testuser"}, mock_request, None, "testplayer", "sitting", "sit"
            )
    
    assert result["changed"] is True
    assert result["position"] == "sitting"


@pytest.mark.asyncio
async def test_handle_position_change_broadcast_error():
    """Test _handle_position_change handles broadcast errors gracefully."""
    mock_player_id = uuid.uuid4()
    mock_room_id = "test-room"
    mock_position_service = MagicMock()
    mock_position_service.change_position = AsyncMock(return_value={
        "success": True,
        "position": "sitting",
        "previous_position": "standing",
        "player_display_name": "TestPlayer",
        "player_id": mock_player_id,
        "room_id": mock_room_id,
        "message": "You sit down.",
    })
    
    mock_connection_manager = MagicMock()
    mock_connection_manager.broadcast_to_room = AsyncMock(side_effect=ValueError("Test error"))
    
    mock_persistence = MagicMock()
    mock_state = MagicMock()
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    with patch("server.commands.position_commands.PlayerPositionService", return_value=mock_position_service):
        with patch("server.commands.position_commands.build_event", return_value={"type": "player_posture_change"}):
            result = await _handle_position_change(
                {"username": "testuser"}, mock_request, None, "testplayer", "sitting", "sit"
            )
    
    # Should still succeed even if broadcast fails
    assert result["changed"] is True


@pytest.mark.asyncio
async def test_handle_sit_command():
    """Test handle_sit_command calls _handle_position_change with correct parameters."""
    with patch("server.commands.position_commands._handle_position_change", new_callable=AsyncMock) as mock_handle:
        mock_handle.return_value = {"result": "You sit down.", "changed": True, "position": "sitting"}
        
        result = await handle_sit_command({}, {}, MagicMock(), None, "testplayer")
        
        assert result["changed"] is True
        mock_handle.assert_awaited_once()
        # Verify the desired_position and command_name parameters
        call_kwargs = mock_handle.call_args[1] if mock_handle.call_args[1] else {}
        call_args = mock_handle.call_args[0] if mock_handle.call_args[0] else ()
        # Check positional args: current_user, request, alias_storage, player_name, desired_position, command_name
        if len(call_args) >= 6:
            assert call_args[4] == "sitting"  # desired_position
            assert call_args[5] == "sit"  # command_name


@pytest.mark.asyncio
async def test_handle_stand_command():
    """Test handle_stand_command calls _handle_position_change with correct parameters."""
    with patch("server.commands.position_commands._handle_position_change", new_callable=AsyncMock) as mock_handle:
        mock_handle.return_value = {"result": "You stand up.", "changed": True, "position": "standing"}
        
        result = await handle_stand_command({}, {}, MagicMock(), None, "testplayer")
        
        assert result["changed"] is True
        mock_handle.assert_awaited_once()
        # Verify the desired_position and command_name parameters
        call_args = mock_handle.call_args[0] if mock_handle.call_args[0] else ()
        if len(call_args) >= 6:
            assert call_args[4] == "standing"  # desired_position
            assert call_args[5] == "stand"  # command_name


@pytest.mark.asyncio
async def test_handle_lie_command():
    """Test handle_lie_command calls _handle_position_change with correct parameters."""
    with patch("server.commands.position_commands._handle_position_change", new_callable=AsyncMock) as mock_handle:
        mock_handle.return_value = {"result": "You lie down.", "changed": True, "position": "lying"}
        
        result = await handle_lie_command({}, {}, MagicMock(), None, "testplayer")
        
        assert result["changed"] is True
        mock_handle.assert_awaited_once()
        # Verify the desired_position and command_name parameters
        call_args = mock_handle.call_args[0] if mock_handle.call_args[0] else ()
        if len(call_args) >= 6:
            assert call_args[4] == "lying"  # desired_position
            assert call_args[5] == "lie"  # command_name
