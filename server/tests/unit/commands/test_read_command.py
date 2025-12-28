"""
Unit tests for read command handlers.

Tests the read command functionality.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.read_command import handle_read_command


@pytest.mark.asyncio
async def test_handle_read_command():
    """Test handle_read_command() reads item."""
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

    result = await handle_read_command({"target": "book"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert isinstance(result["result"], str)


@pytest.mark.asyncio
async def test_handle_read_command_no_target():
    """Test handle_read_command() handles missing target."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_no_persistence():
    """Test handle_read_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_read_command({"target": "book"}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()
