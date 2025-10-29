"""Tests for player respawn service."""

from unittest.mock import AsyncMock, Mock

import pytest

from server.models.player import Player
from server.services.player_respawn_service import PlayerRespawnService

DEFAULT_RESPAWN_ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"


@pytest.fixture
def player_respawn_service():
    """Create a player respawn service instance for testing."""
    return PlayerRespawnService()


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = Mock(spec=Player)
    player.player_id = "test-player-id"
    player.name = "TestPlayer"
    player.current_room_id = "test-room-id"
    player.respawn_room_id = DEFAULT_RESPAWN_ROOM
    return player


class TestPlayerRespawnService:
    """Test suite for PlayerRespawnService."""

    @pytest.mark.asyncio
    async def test_move_player_to_limbo_success(self, player_respawn_service, mock_player):
        """Test moving a player to limbo room."""
        death_location = "dangerous-room"

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await player_respawn_service.move_player_to_limbo("test-player-id", death_location, mock_session)

        assert result is True
        # Verify player was moved to limbo room
        assert mock_player.current_room_id == "limbo_death_void"
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_move_player_to_limbo_player_not_found(self, player_respawn_service):
        """Test limbo movement when player doesn't exist."""
        mock_session = AsyncMock()
        mock_session.get.return_value = None

        result = await player_respawn_service.move_player_to_limbo("nonexistent-player", "test-room", mock_session)

        assert result is False

    @pytest.mark.asyncio
    async def test_get_respawn_room_custom_room(self, player_respawn_service, mock_player):
        """Test getting custom respawn room from player."""
        mock_player.respawn_room_id = "custom-respawn-room"

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await player_respawn_service.get_respawn_room("test-player-id", mock_session)

        assert result == "custom-respawn-room"

    @pytest.mark.asyncio
    async def test_get_respawn_room_default(self, player_respawn_service, mock_player):
        """Test getting default respawn room when player has None."""
        mock_player.respawn_room_id = None

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await player_respawn_service.get_respawn_room("test-player-id", mock_session)

        assert result == DEFAULT_RESPAWN_ROOM

    @pytest.mark.asyncio
    async def test_get_respawn_room_player_not_found(self, player_respawn_service):
        """Test getting respawn room when player doesn't exist."""
        mock_session = AsyncMock()
        mock_session.get.return_value = None

        result = await player_respawn_service.get_respawn_room("nonexistent-player", mock_session)

        assert result == DEFAULT_RESPAWN_ROOM

    @pytest.mark.asyncio
    async def test_respawn_player_success(self, player_respawn_service, mock_player):
        """Test successful player respawn."""
        # Set player to dead state
        stats = {"current_health": -10}
        mock_player.get_stats.return_value = stats
        mock_player.respawn_room_id = DEFAULT_RESPAWN_ROOM
        mock_player.current_room_id = "limbo_death_void"

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await player_respawn_service.respawn_player("test-player-id", mock_session)

        assert result is True
        # Verify HP was restored to 100
        mock_player.set_stats.assert_called_once()
        updated_stats = mock_player.set_stats.call_args[0][0]
        assert updated_stats["current_health"] == 100
        # Verify player was moved to respawn room
        assert mock_player.current_room_id == DEFAULT_RESPAWN_ROOM
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_respawn_player_custom_respawn_room(self, player_respawn_service, mock_player):
        """Test respawn with custom respawn room."""
        stats = {"current_health": -10}
        mock_player.get_stats.return_value = stats
        mock_player.respawn_room_id = "custom-respawn-room"
        mock_player.current_room_id = "limbo_death_void"

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await player_respawn_service.respawn_player("test-player-id", mock_session)

        assert result is True
        assert mock_player.current_room_id == "custom-respawn-room"

    @pytest.mark.asyncio
    async def test_respawn_player_not_found(self, player_respawn_service):
        """Test respawn when player doesn't exist."""
        mock_session = AsyncMock()
        mock_session.get.return_value = None

        result = await player_respawn_service.respawn_player("nonexistent-player", mock_session)

        assert result is False

    @pytest.mark.asyncio
    async def test_respawn_player_restores_full_hp(self, player_respawn_service, mock_player):
        """Test that respawn always restores to 100 HP."""
        # Test with different negative HP values
        for hp in [-10, -5, -1, 0]:
            stats = {"current_health": hp, "sanity": 50}
            mock_player.get_stats.return_value = stats.copy()
            mock_player.current_room_id = "limbo_death_void"

            mock_session = AsyncMock()
            mock_session.get.return_value = mock_player

            await player_respawn_service.respawn_player("test-player-id", mock_session)

            # Verify HP was set to exactly 100
            updated_stats = mock_player.set_stats.call_args[0][0]
            assert updated_stats["current_health"] == 100
            # Verify other stats were preserved
            assert updated_stats["sanity"] == 50

            mock_player.reset_mock()

    @pytest.mark.asyncio
    async def test_move_player_to_limbo_database_exception(self, player_respawn_service, mock_player):
        """Test limbo movement handles database exceptions gracefully."""
        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player
        mock_session.commit.side_effect = Exception("Database error")

        result = await player_respawn_service.move_player_to_limbo("test-player-id", "death-room", mock_session)

        assert result is False
        mock_session.rollback.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_respawn_room_database_exception(self, player_respawn_service):
        """Test get_respawn_room handles database exceptions gracefully."""
        mock_session = AsyncMock()
        mock_session.get.side_effect = Exception("Database error")

        result = await player_respawn_service.get_respawn_room("test-player-id", mock_session)

        # Should return default room on error
        assert result == DEFAULT_RESPAWN_ROOM

    @pytest.mark.asyncio
    async def test_respawn_player_with_event_bus(self, mock_player):
        """Test player respawn with event bus integration."""
        # Create service with event bus
        mock_event_bus = Mock()
        service = PlayerRespawnService(event_bus=mock_event_bus)

        stats = {"current_health": -10}
        mock_player.get_stats.return_value = stats
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "limbo_death_void"
        mock_player.respawn_room_id = DEFAULT_RESPAWN_ROOM

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await service.respawn_player("test-player-id", mock_session)

        assert result is True
        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        event = mock_event_bus.publish.call_args[0][0]
        assert event.event_type == "PlayerRespawnedEvent"
        assert event.player_id == "test-player-id"
        assert event.old_hp == -10
        assert event.new_hp == 100
        assert event.respawn_room_id == DEFAULT_RESPAWN_ROOM

    @pytest.mark.asyncio
    async def test_respawn_player_database_exception(self, player_respawn_service, mock_player):
        """Test respawn handles database exceptions gracefully."""
        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player
        mock_session.commit.side_effect = Exception("Database error")

        mock_player.get_stats.return_value = {"current_health": -10}

        result = await player_respawn_service.respawn_player("test-player-id", mock_session)

        assert result is False
        mock_session.rollback.assert_called_once()
