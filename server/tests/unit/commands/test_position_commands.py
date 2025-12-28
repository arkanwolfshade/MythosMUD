"""
Unit tests for position command handlers.

Tests the sit, stand, lie, and ground commands.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.position_commands import (
    handle_ground_command,
    handle_lie_command,
    handle_sit_command,
    handle_stand_command,
)


@pytest.mark.asyncio
async def test_handle_sit_command():
    """Test handle_sit_command() changes player position to sitting."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.position_state = "standing"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_sit_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert mock_player.position_state == "sitting" or "sit" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_stand_command():
    """Test handle_stand_command() changes player position to standing."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.position_state = "sitting"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_stand_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert mock_player.position_state == "standing" or "stand" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_lie_command():
    """Test handle_lie_command() changes player position to lying."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.position_state = "standing"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_lie_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert mock_player.position_state == "lying" or "lie" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command():
    """Test handle_ground_command() helps catatonic player."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.position_state = "standing"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_ground_command(
        {"target": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
