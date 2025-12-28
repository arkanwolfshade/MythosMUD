"""
Unit tests for exploration command handlers.

Tests the exploration command functionality.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.exploration_commands import handle_explore_command


@pytest.mark.asyncio
async def test_handle_explore_command():
    """Test handle_explore_command() explores area."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_explore_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert isinstance(result["result"], str)


@pytest.mark.asyncio
async def test_handle_explore_command_no_persistence():
    """Test handle_explore_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_explore_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()
