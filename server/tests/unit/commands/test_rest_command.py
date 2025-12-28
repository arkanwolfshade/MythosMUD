"""
Unit tests for rest command handlers.

Tests the rest command functionality.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.rest_command import handle_rest_command


@pytest.mark.asyncio
async def test_handle_rest_command():
    """Test handle_rest_command() allows player to rest."""
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

    result = await handle_rest_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert isinstance(result["result"], str)


@pytest.mark.asyncio
async def test_handle_rest_command_no_persistence():
    """Test handle_rest_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()
