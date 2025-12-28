"""
Unit tests for game state provider.

Tests the GameStateProvider class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.integration.game_state_provider import GameStateProvider


@pytest.fixture
def mock_room_manager():
    """Create a mock room manager."""
    return MagicMock()


@pytest.fixture
def mock_get_async_persistence():
    """Create a mock get_async_persistence callback."""
    return MagicMock(return_value=MagicMock())


@pytest.fixture
def mock_send_personal_message():
    """Create a mock send_personal_message callback."""
    return AsyncMock(return_value={"success": True})


@pytest.fixture
def mock_get_app():
    """Create a mock get_app callback."""
    return MagicMock(return_value=MagicMock())


@pytest.fixture
def game_state_provider(mock_room_manager, mock_get_async_persistence, mock_send_personal_message, mock_get_app):
    """Create a GameStateProvider instance."""
    return GameStateProvider(
        room_manager=mock_room_manager,
        get_async_persistence=mock_get_async_persistence,
        send_personal_message_callback=mock_send_personal_message,
        get_app=mock_get_app,
    )


@pytest.mark.asyncio
async def test_get_player(game_state_provider):
    """Test get_player() retrieves player from persistence."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    # get_player uses get_async_persistence() directly from async_persistence module
    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_get_persistence.return_value = mock_persistence
        result = await game_state_provider.get_player(player_id)
        assert result == mock_player
        mock_persistence.get_player_by_id.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_get_players_batch(game_state_provider, mock_get_async_persistence):
    """Test get_players_batch() retrieves multiple players."""
    player_id1 = uuid.uuid4()
    player_id2 = uuid.uuid4()
    mock_player1 = MagicMock()
    mock_player2 = MagicMock()
    mock_persistence = MagicMock()
    # get_players_batch calls get_player_by_id for each player_id, not get_players_batch
    mock_persistence.get_player_by_id = AsyncMock(side_effect=[mock_player1, mock_player2])
    mock_get_async_persistence.return_value = mock_persistence
    result = await game_state_provider.get_players_batch([player_id1, player_id2])
    assert player_id1 in result
    assert player_id2 in result
    assert result[player_id1] == mock_player1
    assert result[player_id2] == mock_player2


@pytest.mark.asyncio
async def test_get_players_batch_empty(game_state_provider, mock_get_async_persistence):
    """Test get_players_batch() returns empty dict for empty input."""
    result = await game_state_provider.get_players_batch([])
    assert result == {}


@pytest.mark.asyncio
async def test_get_players_batch_no_persistence(game_state_provider, mock_get_async_persistence):
    """Test get_players_batch() returns empty dict when persistence is None."""
    mock_get_async_persistence.return_value = None
    result = await game_state_provider.get_players_batch([uuid.uuid4()])
    assert result == {}
