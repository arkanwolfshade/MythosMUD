"""Tests for player death service."""

from unittest.mock import Mock

import pytest

from server.models.player import Player
from server.services.player_death_service import PlayerDeathService


@pytest.fixture
def player_death_service():
    """Create a player death service instance for testing."""
    return PlayerDeathService()


@pytest.fixture
def mock_player():
    """Create a mock player with configurable HP."""
    player = Mock(spec=Player)
    player.player_id = "test-player-id"
    player.name = "TestPlayer"
    player.current_room_id = "test-room-id"
    return player


class TestPlayerDeathService:
    """Test suite for PlayerDeathService."""

    def test_get_mortally_wounded_players_empty(self, player_death_service):
        """Test getting mortally wounded players when none exist."""
        # Mock database session to return no players
        mock_session = Mock()
        mock_session.query().all.return_value = []

        result = player_death_service.get_mortally_wounded_players(mock_session)

        assert result == []

    def test_get_mortally_wounded_players_with_valid_players(self, player_death_service):
        """Test getting mortally wounded players when some exist."""
        # Create mock players with different HP values
        player1 = Mock(spec=Player)
        player1.player_id = "player-1"
        player1.get_stats.return_value = {"current_health": 0}  # Mortally wounded

        player2 = Mock(spec=Player)
        player2.player_id = "player-2"
        player2.get_stats.return_value = {"current_health": -5}  # Mortally wounded

        player3 = Mock(spec=Player)
        player3.player_id = "player-3"
        player3.get_stats.return_value = {"current_health": 50}  # Alive

        player4 = Mock(spec=Player)
        player4.player_id = "player-4"
        player4.get_stats.return_value = {"current_health": -10}  # Dead

        mock_session = Mock()
        mock_session.query().all.return_value = [player1, player2, player3, player4]

        result = player_death_service.get_mortally_wounded_players(mock_session)

        # Should only return player1 and player2 (mortally wounded)
        assert len(result) == 2
        assert player1 in result
        assert player2 in result
        assert player3 not in result
        assert player4 not in result

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_normal_decay(self, player_death_service, mock_player):
        """Test HP decay processing for a mortally wounded player."""
        # Set player to mortally wounded state
        stats = {"current_health": -3}
        mock_player.get_stats.return_value = stats
        mock_player.is_dead.return_value = False

        mock_session = Mock()
        mock_session.get.return_value = mock_player

        result = await player_death_service.process_mortally_wounded_tick("test-player-id", mock_session)

        # Verify HP was decreased by 1
        assert result is True
        mock_player.set_stats.assert_called_once()
        updated_stats = mock_player.set_stats.call_args[0][0]
        assert updated_stats["current_health"] == -4
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_cap_at_minus_ten(self, player_death_service, mock_player):
        """Test HP decay caps at -10."""
        # Set player to -9 HP (one away from death)
        stats = {"current_health": -9}
        mock_player.get_stats.return_value = stats
        mock_player.is_dead.return_value = False

        mock_session = Mock()
        mock_session.get.return_value = mock_player

        result = await player_death_service.process_mortally_wounded_tick("test-player-id", mock_session)

        # Verify HP was decreased to exactly -10 (capped)
        assert result is True
        updated_stats = mock_player.set_stats.call_args[0][0]
        assert updated_stats["current_health"] == -10
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_already_at_cap(self, player_death_service, mock_player):
        """Test HP decay when already at -10."""
        # Set player to exactly -10 HP
        stats = {"current_health": -10}
        mock_player.get_stats.return_value = stats
        mock_player.is_dead.return_value = True

        mock_session = Mock()
        mock_session.get.return_value = mock_player

        result = await player_death_service.process_mortally_wounded_tick("test-player-id", mock_session)

        # Should not process decay for dead player
        assert result is False
        mock_player.set_stats.assert_not_called()
        mock_session.commit.assert_not_called()

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_player_not_found(self, player_death_service):
        """Test HP decay when player doesn't exist."""
        mock_session = Mock()
        mock_session.get.return_value = None

        result = await player_death_service.process_mortally_wounded_tick("nonexistent-player", mock_session)

        assert result is False

    @pytest.mark.asyncio
    async def test_handle_player_death_basic(self, player_death_service, mock_player):
        """Test basic player death handling."""
        mock_player.current_room_id = "death-room"
        mock_player.name = "DeadPlayer"

        mock_session = Mock()
        mock_session.get.return_value = mock_player

        killer_info = {"killer_id": "npc-123", "killer_name": "Terrible Beast"}

        result = await player_death_service.handle_player_death(
            "test-player-id", "death-room", killer_info, mock_session
        )

        assert result is True
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_death_no_killer(self, player_death_service, mock_player):
        """Test player death without a killer."""
        mock_player.current_room_id = "death-room"
        mock_player.name = "DeadPlayer"

        mock_session = Mock()
        mock_session.get.return_value = mock_player

        result = await player_death_service.handle_player_death("test-player-id", "death-room", None, mock_session)

        assert result is True
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_death_player_not_found(self, player_death_service):
        """Test death handling when player doesn't exist."""
        mock_session = Mock()
        mock_session.get.return_value = None

        result = await player_death_service.handle_player_death("nonexistent-player", "test-room", None, mock_session)

        assert result is False

    def test_get_mortally_wounded_players_database_exception(self, player_death_service):
        """Test get_mortally_wounded_players handles database exceptions gracefully."""
        # Mock session that raises an exception
        mock_session = Mock()
        mock_session.query.side_effect = Exception("Database connection error")

        result = player_death_service.get_mortally_wounded_players(mock_session)

        # Should return empty list on error
        assert result == []

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_with_event_bus(self, mock_player):
        """Test HP decay with event bus integration."""
        # Create service with event bus
        mock_event_bus = Mock()
        service = PlayerDeathService(event_bus=mock_event_bus)

        stats = {"current_health": -5}
        mock_player.get_stats.return_value = stats
        mock_player.is_dead.return_value = False
        mock_player.name = "TestPlayer"

        mock_session = Mock()
        mock_session.get.return_value = mock_player

        result = await service.process_mortally_wounded_tick("test-player-id", mock_session)

        assert result is True
        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        event = mock_event_bus.publish.call_args[0][0]
        assert event.event_type == "PlayerHPDecayEvent"
        assert event.old_hp == -5
        assert event.new_hp == -6

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_database_exception(self, player_death_service, mock_player):
        """Test HP decay handles database exceptions gracefully."""
        mock_session = Mock()
        mock_session.get.return_value = mock_player
        mock_session.commit.side_effect = Exception("Database error")

        mock_player.get_stats.return_value = {"current_health": -5}
        mock_player.is_dead.return_value = False

        result = await player_death_service.process_mortally_wounded_tick("test-player-id", mock_session)

        assert result is False
        mock_session.rollback.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_death_with_event_bus(self, mock_player):
        """Test player death handling with event bus integration."""
        # Create service with event bus
        mock_event_bus = Mock()
        service = PlayerDeathService(event_bus=mock_event_bus)

        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "death-room"

        mock_session = Mock()
        mock_session.get.return_value = mock_player

        killer_info = {"killer_id": "npc-123", "killer_name": "Beast"}

        result = await service.handle_player_death("test-player-id", "death-room", killer_info, mock_session)

        assert result is True
        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        event = mock_event_bus.publish.call_args[0][0]
        assert event.event_type == "PlayerDiedEvent"
        assert event.player_id == "test-player-id"
        assert event.killer_id == "npc-123"

    @pytest.mark.asyncio
    async def test_handle_player_death_database_exception(self, player_death_service, mock_player):
        """Test death handling handles database exceptions gracefully."""
        mock_session = Mock()
        mock_session.get.return_value = mock_player
        mock_session.commit.side_effect = Exception("Database error")

        result = await player_death_service.handle_player_death("test-player-id", "death-room", None, mock_session)

        assert result is False
        mock_session.rollback.assert_called_once()
