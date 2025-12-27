"""
Unit tests for rest command handler.

Tests the /rest command for MP regeneration.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.rest_command import handle_rest_command


@pytest.mark.asyncio
async def test_handle_rest_command_no_app():
    """Test handle_rest_command returns error when no app."""
    mock_request = MagicMock()
    mock_request.app = None
    
    result = await handle_rest_command({}, {}, mock_request, None, "testplayer")
    
    assert "application not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_no_persistence():
    """Test handle_rest_command returns error when no persistence."""
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    del mock_app.state.persistence
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_rest_command({}, {}, mock_request, None, "testplayer")
    
    assert "persistence layer not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_no_mp_service():
    """Test handle_rest_command returns error when no MP regeneration service."""
    mock_persistence = MagicMock()
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    del mock_app.state.mp_regeneration_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_rest_command({}, {}, mock_request, None, "testplayer")
    
    assert "not initialized" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_player_not_found():
    """Test handle_rest_command returns error when player not found."""
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.mp_regeneration_service = MagicMock()
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_rest_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "not recognized" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_not_sitting_or_lying():
    """Test handle_rest_command returns error when player is standing."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_player.get_stats = MagicMock(return_value={"position": "standing"})
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.mp_regeneration_service = MagicMock()
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_rest_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "sitting or lying" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_success_sitting():
    """Test handle_rest_command successfully rests when sitting."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_player.get_stats = MagicMock(return_value={"position": "sitting"})
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_mp_service = MagicMock()
    mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={
        "success": True,
        "message": "You rest and recover 10 MP.",
    })
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.mp_regeneration_service = mock_mp_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_rest_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "rest and recover" in result["result"].lower()
    mock_mp_service.restore_mp_from_rest.assert_awaited_once_with("test-player-id", 60)


@pytest.mark.asyncio
async def test_handle_rest_command_success_lying():
    """Test handle_rest_command successfully rests when lying."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_player.get_stats = MagicMock(return_value={"position": "lying"})
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_mp_service = MagicMock()
    mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={
        "success": True,
        "message": "You rest deeply and recover 15 MP.",
    })
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.mp_regeneration_service = mock_mp_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_rest_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "rest" in result["result"].lower()
    mock_mp_service.restore_mp_from_rest.assert_awaited_once_with("test-player-id", 60)


@pytest.mark.asyncio
async def test_handle_rest_command_with_duration():
    """Test handle_rest_command uses specified duration."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_player.get_stats = MagicMock(return_value={"position": "sitting"})
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_mp_service = MagicMock()
    mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={
        "success": True,
        "message": "You rest for 120 seconds.",
    })
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.mp_regeneration_service = mock_mp_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"duration": 120}
    result = await handle_rest_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "rest" in result["result"].lower()
    mock_mp_service.restore_mp_from_rest.assert_awaited_once_with("test-player-id", 120)


@pytest.mark.asyncio
async def test_handle_rest_command_duration_too_low():
    """Test handle_rest_command caps duration at minimum 1."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_player.get_stats = MagicMock(return_value={"position": "sitting"})
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_mp_service = MagicMock()
    mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={
        "success": True,
        "message": "You rest.",
    })
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.mp_regeneration_service = mock_mp_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"duration": -10}
    result = await handle_rest_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    # Should default to 60 when duration < 1
    mock_mp_service.restore_mp_from_rest.assert_awaited_once_with("test-player-id", 60)


@pytest.mark.asyncio
async def test_handle_rest_command_duration_too_high():
    """Test handle_rest_command caps duration at maximum 300."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_player.get_stats = MagicMock(return_value={"position": "sitting"})
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_mp_service = MagicMock()
    mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={
        "success": True,
        "message": "You rest.",
    })
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.mp_regeneration_service = mock_mp_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"duration": 500}
    result = await handle_rest_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    # Should cap at 300 when duration > 300
    mock_mp_service.restore_mp_from_rest.assert_awaited_once_with("test-player-id", 300)


@pytest.mark.asyncio
async def test_handle_rest_command_invalid_duration():
    """Test handle_rest_command handles invalid duration gracefully."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_player.get_stats = MagicMock(return_value={"position": "sitting"})
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_mp_service = MagicMock()
    mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={
        "success": True,
        "message": "You rest.",
    })
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.mp_regeneration_service = mock_mp_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"duration": "invalid"}
    result = await handle_rest_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    # Should default to 60 when duration is invalid
    mock_mp_service.restore_mp_from_rest.assert_awaited_once_with("test-player-id", 60)


@pytest.mark.asyncio
async def test_handle_rest_command_service_failure():
    """Test handle_rest_command handles service failure."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_player.get_stats = MagicMock(return_value={"position": "sitting"})
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_mp_service = MagicMock()
    mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={
        "success": False,
        "message": "You are too exhausted to rest.",
    })
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.mp_regeneration_service = mock_mp_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_rest_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "too exhausted" in result["result"].lower()
