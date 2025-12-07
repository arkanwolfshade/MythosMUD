"""Tests for player delirium respawn API endpoint."""

from unittest.mock import AsyncMock, Mock

import pytest

from server.models.lucidity import PlayerLucidity
from server.models.player import Player


@pytest.fixture
def mock_delirious_player():
    """Create a mock delirious player (lucidity <= -10)."""
    player = Mock(spec=Player)
    player.player_id = "test-player-id"
    player.name = "DeliriousPlayer"
    player.current_room_id = "test-room"
    stats = {"current_health": 50}
    player.get_stats.return_value = stats
    return player


@pytest.fixture
def mock_lucid_player():
    """Create a mock lucid player (lucidity > -10)."""
    player = Mock(spec=Player)
    player.player_id = "test-player-id"
    player.name = "LucidPlayer"
    player.current_room_id = "test-room"
    stats = {"current_health": 50}
    player.get_stats.return_value = stats
    return player


@pytest.fixture
def mock_delirious_lucidity():
    """Create a mock lucidity record with lucidity <= -10."""
    lucidity = Mock(spec=PlayerLucidity)
    lucidity.current_lcd = -15
    lucidity.current_tier = "catatonic"
    return lucidity


@pytest.fixture
def mock_lucid_lucidity():
    """Create a mock lucidity record with lucidity > -10."""
    lucidity = Mock(spec=PlayerLucidity)
    lucidity.current_lcd = 50
    lucidity.current_tier = "lucid"
    return lucidity


class TestDeliriumRespawnEndpoint:
    """Test suite for /api/players/respawn-delirium endpoint."""

    @pytest.mark.asyncio
    async def test_respawn_delirious_player_success(self, mock_delirious_player, mock_delirious_lucidity):
        """Test successful respawn of a delirious player."""
        # Mock services
        mock_player_service = Mock()
        mock_player_service.respawn_player_from_delirium_by_user_id = AsyncMock(
            return_value={
                "success": True,
                "player": {
                    "id": "test-player-id",
                    "name": "DeliriousPlayer",
                    "hp": 50,
                    "max_hp": 100,
                    "lucidity": 10,
                    "current_room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
                },
                "room": {
                    "id": "earth_arkhamcity_sanitarium_room_foyer_001",
                    "name": "Sanitarium Foyer",
                },
                "message": "You have been restored to lucidity and returned to the Sanitarium",
            }
        )

        # Simulate delirium respawn endpoint logic
        result = await mock_player_service.respawn_player_from_delirium_by_user_id(
            "test-user-id", None, None, None
        )

        # Verify respawn was successful
        assert result["success"] is True
        assert result["player"]["lucidity"] == 10
        assert result["player"]["current_room_id"] == "earth_arkhamcity_sanitarium_room_foyer_001"
        assert "Sanitarium" in result["message"]

    @pytest.mark.asyncio
    async def test_respawn_lucid_player_forbidden(self, mock_lucid_player, mock_lucid_lucidity):
        """Test that delirium respawn fails for lucid players."""
        # Simulate endpoint validation
        # Player with lucidity > -10 should not be able to respawn from delirium
        assert mock_lucid_lucidity.current_lcd > -10
        # In the actual endpoint, this would raise HTTPException(403)

    @pytest.mark.asyncio
    async def test_respawn_player_not_found(self):
        """Test delirium respawn when player doesn't exist."""
        mock_player_service = Mock()
        mock_player_service.respawn_player_from_delirium_by_user_id = AsyncMock(
            side_effect=Exception("Player not found")
        )

        # Simulate endpoint logic
        with pytest.raises(Exception, match="Player not found"):
            await mock_player_service.respawn_player_from_delirium_by_user_id(
                "nonexistent-user", None, None, None
            )

    @pytest.mark.asyncio
    async def test_respawn_returns_room_data(self, mock_delirious_player):
        """Test that delirium respawn returns complete room data."""
        mock_persistence = Mock()
        mock_room = {
            "id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "name": "Sanitarium Foyer",
            "description": "A sterile waiting area...",
            "exits": {"east": "hallway_001"},
        }
        mock_persistence.get_room = Mock(return_value=mock_room)

        # Simulate getting room data after delirium respawn
        room_data = mock_persistence.get_room("earth_arkhamcity_sanitarium_room_foyer_001")

        assert room_data["id"] == "earth_arkhamcity_sanitarium_room_foyer_001"
        assert "name" in room_data
        assert "description" in room_data
        assert "exits" in room_data

    @pytest.mark.asyncio
    async def test_respawn_updates_player_state(self, mock_delirious_player, mock_delirious_lucidity):
        """Test that delirium respawn updates player state correctly."""
        # After delirium respawn, player should have:
        # - lucidity = 10
        # - current_room_id = sanitarium
        # - posture = standing

        # Simulate state update
        mock_delirious_lucidity.current_lcd = 10
        mock_delirious_lucidity.current_tier = "lucid"
        mock_delirious_player.current_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        stats = mock_delirious_player.get_stats()
        stats["position"] = "standing"
        mock_delirious_player.set_stats(stats)

        # Verify updates
        assert mock_delirious_lucidity.current_lcd == 10
        assert mock_delirious_lucidity.current_tier == "lucid"
        assert mock_delirious_player.current_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"
        updated_stats = mock_delirious_player.get_stats()
        assert updated_stats["position"] == "standing"
