"""
Unit tests for grace period command blocking in unified command handler.

Tests that commands are blocked for players in grace period.
"""

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.command_handler.command_execution_request import CommandExecutionRequest
from server.command_handler.command_guards import check_grace_period_block


@pytest.fixture
def mock_request() -> MagicMock:
    """Create a mock request with app.state for command guards."""
    request: MagicMock = MagicMock()
    app: MagicMock = MagicMock()
    state: MagicMock = MagicMock()
    request.app = app
    app.state = state
    return request


def _request_state(mock_request: MagicMock) -> MagicMock:
    """Typed access to mock_request.app.state for guard tests."""
    app: MagicMock = cast(MagicMock, mock_request.app)
    return cast(MagicMock, app.state)


def _as_command_request(mock_request: MagicMock) -> CommandExecutionRequest:
    """Narrow MagicMock request fixtures for check_grace_period_block."""
    return cast(CommandExecutionRequest, mock_request)


@pytest.mark.asyncio
async def test_check_grace_period_block_blocks_commands(
    mock_request: MagicMock,
) -> None:  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test check_grace_period_block() blocks commands for grace period players."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    state = _request_state(mock_request)

    mock_connection_manager: MagicMock = MagicMock()
    mock_connection_manager.grace_period_players = {player_id: MagicMock()}
    state.connection_manager = mock_connection_manager

    mock_player: MagicMock = MagicMock()
    mock_player.player_id = str(player_id)
    mock_player_service: MagicMock = MagicMock()
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    state.player_service = mock_player_service

    with patch("server.command_handler.command_guards.is_player_in_grace_period", return_value=True):
        result = await check_grace_period_block(player_name, _as_command_request(mock_request))

        assert result is not None
        assert "result" in result
        message = result["result"]
        assert isinstance(message, str)
        assert "disconnected" in message.lower() or "cannot perform" in message.lower()


@pytest.mark.asyncio
async def test_check_grace_period_block_allows_commands_when_not_in_grace_period(
    mock_request: MagicMock,
) -> None:  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test check_grace_period_block() allows commands when player not in grace period."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    state = _request_state(mock_request)

    mock_connection_manager: MagicMock = MagicMock()
    mock_connection_manager.grace_period_players = {}
    state.connection_manager = mock_connection_manager

    mock_player: MagicMock = MagicMock()
    mock_player.player_id = str(player_id)
    mock_player_service: MagicMock = MagicMock()
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    state.player_service = mock_player_service

    with patch("server.command_handler.command_guards.is_player_in_grace_period", return_value=False):
        result = await check_grace_period_block(player_name, _as_command_request(mock_request))

        assert result is None


@pytest.mark.asyncio
async def test_check_grace_period_block_handles_missing_services(
    mock_request: MagicMock,
) -> None:  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test check_grace_period_block() handles missing services gracefully."""
    player_name = "TestPlayer"
    _request_state(mock_request).connection_manager = None

    result = await check_grace_period_block(player_name, _as_command_request(mock_request))

    assert result is None


@pytest.mark.asyncio
async def test_check_grace_period_block_handles_player_not_found(
    mock_request: MagicMock,
) -> None:  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test check_grace_period_block() handles player not found gracefully."""
    player_name = "TestPlayer"
    state = _request_state(mock_request)

    mock_connection_manager: MagicMock = MagicMock()
    mock_connection_manager.grace_period_players = {}
    state.connection_manager = mock_connection_manager

    mock_player_service: MagicMock = MagicMock()
    mock_player_service.get_player_by_name = AsyncMock(return_value=None)
    state.player_service = mock_player_service

    result = await check_grace_period_block(player_name, _as_command_request(mock_request))

    assert result is None
