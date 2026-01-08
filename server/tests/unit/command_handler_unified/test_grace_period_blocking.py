"""
Unit tests for grace period command blocking in unified command handler.

Tests that commands are blocked for players in grace period.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.command_handler_unified import _check_grace_period_block


@pytest.fixture
def mock_request():
    """Create a mock request."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.mark.asyncio
async def test_check_grace_period_block_blocks_commands(mock_request):  # pylint: disable=redefined-outer-name
    """Test _check_grace_period_block() blocks commands for grace period players."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"

    # Mock connection manager with player in grace period
    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {player_id: MagicMock()}
    mock_request.app.state.connection_manager = mock_connection_manager

    # Mock player service
    mock_player_service = MagicMock()
    mock_player = MagicMock()
    mock_player.player_id = str(player_id)
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.player_service = mock_player_service

    with patch("server.command_handler_unified.is_player_in_grace_period", return_value=True):
        result = await _check_grace_period_block(player_name, mock_request)

        assert result is not None
        assert "result" in result
        assert "disconnected" in result["result"].lower() or "cannot perform" in result["result"].lower()


@pytest.mark.asyncio
async def test_check_grace_period_block_allows_commands_when_not_in_grace_period(mock_request):  # pylint: disable=redefined-outer-name
    """Test _check_grace_period_block() allows commands when player not in grace period."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"

    # Mock connection manager with player NOT in grace period
    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {}
    mock_request.app.state.connection_manager = mock_connection_manager

    # Mock player service
    mock_player_service = MagicMock()
    mock_player = MagicMock()
    mock_player.player_id = str(player_id)
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.player_service = mock_player_service

    with patch("server.command_handler_unified.is_player_in_grace_period", return_value=False):
        result = await _check_grace_period_block(player_name, mock_request)

        assert result is None  # No blocking


@pytest.mark.asyncio
async def test_check_grace_period_block_handles_missing_services(mock_request):  # pylint: disable=redefined-outer-name
    """Test _check_grace_period_block() handles missing services gracefully."""
    player_name = "TestPlayer"
    mock_request.app.state.connection_manager = None

    result = await _check_grace_period_block(player_name, mock_request)

    assert result is None  # No blocking when services unavailable


@pytest.mark.asyncio
async def test_check_grace_period_block_handles_player_not_found(mock_request):  # pylint: disable=redefined-outer-name
    """Test _check_grace_period_block() handles player not found gracefully."""
    player_name = "TestPlayer"

    # Mock connection manager
    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {}
    mock_request.app.state.connection_manager = mock_connection_manager

    # Mock player service returns None
    mock_player_service = MagicMock()
    mock_player_service.get_player_by_name = AsyncMock(return_value=None)
    mock_request.app.state.player_service = mock_player_service

    result = await _check_grace_period_block(player_name, mock_request)

    assert result is None  # No blocking when player not found
