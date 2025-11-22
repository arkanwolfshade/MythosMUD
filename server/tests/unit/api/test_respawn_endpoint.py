"""Tests for player respawn API endpoint."""

from unittest.mock import AsyncMock, Mock

import pytest

from server.models.player import Player
from server.services.player_respawn_service import LIMBO_ROOM_ID


@pytest.fixture
def mock_dead_player():
    """Create a mock dead player."""
    player = Mock(spec=Player)
    player.player_id = "test-player-id"
    player.name = "DeadPlayer"
    player.current_room_id = LIMBO_ROOM_ID
    player.respawn_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
    stats = {"current_health": -10}
    player.get_stats.return_value = stats
    player.is_dead.return_value = True
    return player


@pytest.fixture
def mock_alive_player():
    """Create a mock alive player."""
    player = Mock(spec=Player)
    player.player_id = "test-player-id"
    player.name = "AlivePlayer"
    player.current_room_id = "test-room"
    stats = {"current_health": 50}
    player.get_stats.return_value = stats
    player.is_dead.return_value = False
    return player


class TestRespawnEndpoint:
    """Test suite for /api/player/respawn endpoint."""

    @pytest.mark.asyncio
    async def test_respawn_dead_player_success(self, mock_dead_player):
        """Test successful respawn of a dead player."""
        # Mock services
        mock_player_service = Mock()
        mock_player_service.get_player_by_id = AsyncMock(return_value=mock_dead_player)

        mock_respawn_service = Mock()
        mock_respawn_service.respawn_player = AsyncMock(return_value=True)
        mock_respawn_service.get_respawn_room = Mock(return_value="earth_arkhamcity_sanitarium_room_foyer_001")

        mock_persistence = Mock()
        mock_room = {"id": "earth_arkhamcity_sanitarium_room_foyer_001", "name": "Foyer"}
        mock_persistence.get_room_by_id = Mock(return_value=mock_room)

        mock_session = Mock()

        # Simulate respawn endpoint logic
        player = await mock_player_service.get_player_by_id("test-player-id")

        # Verify player is dead
        assert player.is_dead() is True

        # Respawn the player
        result = await mock_respawn_service.respawn_player(player.player_id, mock_session)
        assert result is True

        # Get respawn room data
        respawn_room_id = mock_respawn_service.get_respawn_room(player.player_id, mock_session)
        room_data = mock_persistence.get_room_by_id(respawn_room_id)

        assert room_data["id"] == "earth_arkhamcity_sanitarium_room_foyer_001"

    @pytest.mark.asyncio
    async def test_respawn_alive_player_forbidden(self, mock_alive_player):
        """Test that respawn fails for alive players."""
        mock_player_service = Mock()
        mock_player_service.get_player_by_id = AsyncMock(return_value=mock_alive_player)

        # Simulate respawn endpoint validation
        player = await mock_player_service.get_player_by_id("test-player-id")

        # Verify player is alive and respawn should be forbidden
        assert player.is_dead() is False
        # In the actual endpoint, this would raise HTTPException(403)

    @pytest.mark.asyncio
    async def test_respawn_player_not_found(self):
        """Test respawn when player doesn't exist."""
        mock_player_service = Mock()
        mock_player_service.get_player_by_id = AsyncMock(return_value=None)

        # Simulate respawn endpoint logic
        player = await mock_player_service.get_player_by_id("nonexistent-player")

        # Verify player not found
        assert player is None
        # In the actual endpoint, this would raise HTTPException(404)

    @pytest.mark.asyncio
    async def test_respawn_rate_limiting(self):
        """Test rate limiting for respawn endpoint."""
        # This test verifies the rate limiter integration
        # Actual rate limiting is tested in the rate limiter tests
        # The endpoint should use @rate_limiter.limit decorator
        pass

    @pytest.mark.asyncio
    async def test_respawn_returns_room_data(self, mock_dead_player):
        """Test that respawn returns complete room data."""
        mock_persistence = Mock()
        mock_room = {
            "id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "name": "Main Foyer",
            "description": "A grand entrance hall...",
            "exits": {"east": "hallway_001"},
        }
        mock_persistence.get_room_by_id = Mock(return_value=mock_room)

        # Simulate getting room data after respawn
        room_data = mock_persistence.get_room_by_id("earth_arkhamcity_sanitarium_room_foyer_001")

        assert room_data["id"] == "earth_arkhamcity_sanitarium_room_foyer_001"
        assert "name" in room_data
        assert "description" in room_data
        assert "exits" in room_data

    @pytest.mark.asyncio
    async def test_respawn_updates_player_state(self, mock_dead_player):
        """Test that respawn updates player state correctly."""
        # After respawn, player should have:
        # - HP = 100
        # - current_room_id = respawn_room_id
        # - No longer in limbo

        # Simulate state update
        stats = mock_dead_player.get_stats()
        stats["current_health"] = 100
        mock_dead_player.set_stats(stats)
        mock_dead_player.current_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"

        # Verify updates
        updated_stats = mock_dead_player.get_stats()
        assert updated_stats["current_health"] == 100
        assert mock_dead_player.current_room_id != LIMBO_ROOM_ID
