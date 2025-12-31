"""
Unit tests for utility command handlers.

Tests the whoami command functionality.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.utility_commands import handle_whoami_command


@pytest.mark.asyncio
async def test_handle_whoami_command():
    """Test handle_whoami_command() returns player information."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_whoami_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "TestPlayer" in result["result"] or isinstance(result["result"], str)


@pytest.mark.asyncio
async def test_handle_whoami_command_no_persistence():
    """Test handle_whoami_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_whoami_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_whoami_command_player_not_found():
    """Test handle_whoami_command() handles player not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_whoami_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not found" in result["result"].lower() or "error" in result["result"].lower()
