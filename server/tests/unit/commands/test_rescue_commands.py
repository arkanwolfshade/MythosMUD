"""
Unit tests for rescue commands.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.rescue_commands import handle_ground_command


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    app = MagicMock()
    state = MagicMock()
    persistence = MagicMock()
    state.persistence = persistence
    app.state = state
    request = MagicMock()
    request.app = app
    return request


@pytest.fixture
def mock_rescuer():
    """Create a mock rescuer player."""
    rescuer = MagicMock()
    rescuer.player_id = uuid.uuid4()
    rescuer.name = "rescuer"
    rescuer.current_room_id = "earth_arkhamcity_intersection_derby_high"
    return rescuer


@pytest.fixture
def mock_target():
    """Create a mock target player."""
    target = MagicMock()
    target.player_id = uuid.uuid4()
    target.name = "victim"
    target.current_room_id = "earth_arkhamcity_intersection_derby_high"
    return target


@pytest.mark.asyncio
async def test_ground_command_no_persistence():
    """Test ground command without persistence."""
    # Create request without app/state/persistence
    request = MagicMock()
    request.app = None
    
    result = await handle_ground_command(
        command_data={"target_player": "victim"},
        current_user={"username": "rescuer"},
        request=request,
        alias_storage=None,
        player_name="rescuer",
    )
    
    assert "no anchor to reality" in result["result"].lower()


@pytest.mark.asyncio
async def test_ground_command_no_rescuer(mock_request):
    """Test ground command when rescuer not found."""
    mock_request.app.state.persistence.get_player_by_name.return_value = None
    
    result = await handle_ground_command(
        command_data={"target_player": "victim"},
        current_user={"username": "rescuer"},
        request=mock_request,
        alias_storage=None,
        player_name="rescuer",
    )
    
    assert "identity drifts" in result["result"].lower()


@pytest.mark.asyncio
async def test_ground_command_no_target(mock_request, mock_rescuer):
    """Test ground command with no target specified."""
    mock_request.app.state.persistence.get_player_by_name.return_value = mock_rescuer
    
    result = await handle_ground_command(
        command_data={},
        current_user={"username": "rescuer"},
        request=mock_request,
        alias_storage=None,
        player_name="rescuer",
    )
    
    assert "ground whom" in result["result"].lower()


@pytest.mark.asyncio
async def test_ground_command_target_not_found(mock_request, mock_rescuer):
    """Test ground command when target not found."""
    mock_request.app.state.persistence.get_player_by_name.side_effect = [mock_rescuer, None]
    
    result = await handle_ground_command(
        command_data={"target_player": "nonexistent"},
        current_user={"username": "rescuer"},
        request=mock_request,
        alias_storage=None,
        player_name="rescuer",
    )
    
    assert "no echoes" in result["result"].lower()


@pytest.mark.asyncio
async def test_ground_command_different_rooms(mock_request, mock_rescuer):
    """Test ground command when rescuer and target are in different rooms."""
    target = MagicMock()
    target.player_id = uuid.uuid4()
    target.name = "victim"
    target.current_room_id = "different_room"
    
    mock_request.app.state.persistence.get_player_by_name.side_effect = [mock_rescuer, target]
    
    result = await handle_ground_command(
        command_data={"target_player": "victim"},
        current_user={"username": "rescuer"},
        request=mock_request,
        alias_storage=None,
        player_name="rescuer",
    )
    
    assert "not within reach" in result["result"].lower()
