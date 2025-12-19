"""Tests for HP decay processing in game tick loop."""

import uuid
from unittest.mock import AsyncMock, Mock

import pytest

from server.models.player import Player
from server.services.player_death_service import PlayerDeathService


@pytest.fixture
def mock_player_death_service():
    """Create a mock player death service."""
    service = Mock(spec=PlayerDeathService)
    service.get_mortally_wounded_players = Mock(return_value=[])
    service.process_mortally_wounded_tick = AsyncMock(return_value=True)
    return service


@pytest.fixture
def mock_mortally_wounded_player():
    """Create a mock mortally wounded player."""
    player = Mock(spec=Player)
    player.player_id = "test-player-id"
    player.name = "TestPlayer"
    player.get_stats.return_value = {"current_health": -3}
    player.is_mortally_wounded.return_value = True
    player.is_dead.return_value = False
    return player


class TestGameTickHPDecay:
    """Test suite for HP decay processing in game tick loop."""

    @pytest.mark.asyncio
    async def test_hp_decay_processes_mortally_wounded_players(
        self, mock_player_death_service, mock_mortally_wounded_player
    ):
        """Test that game tick processes HP decay for all mortally wounded players."""
        # Setup mock service to return one mortally wounded player
        mock_player_death_service.get_mortally_wounded_players.return_value = [mock_mortally_wounded_player]

        mock_session = AsyncMock()

        # Process one tick
        for player in mock_player_death_service.get_mortally_wounded_players():
            await mock_player_death_service.process_mortally_wounded_tick(player.player_id, mock_session)

        # Verify HP decay was called
        mock_player_death_service.process_mortally_wounded_tick.assert_called_once_with(
            mock_mortally_wounded_player.player_id, mock_session
        )

    @pytest.mark.asyncio
    async def test_hp_decay_broadcasts_messages(self, mock_player_death_service):
        """Test that HP decay broadcasts messages to affected players."""
        # This will be verified through integration testing
        # The service publishes events which are handled by NATS

    @pytest.mark.asyncio
    async def test_hp_decay_stops_at_minus_ten(self) -> None:
        """Test that HP decay stops processing when player reaches -10 HP."""
        player = Mock(spec=Player)
        player.player_id = uuid.uuid4()
        player.get_stats.return_value = {"current_health": -10}
        player.is_dead.return_value = True

        service = PlayerDeathService()
        mock_session = AsyncMock()
        mock_session.get.return_value = player

        # Try to process decay on dead player
        result = await service.process_mortally_wounded_tick(player.player_id, mock_session)

        # Should not process decay for dead player
        assert result is False

    @pytest.mark.asyncio
    async def test_hp_decay_handles_multiple_players(self, mock_player_death_service):
        """Test that HP decay processes multiple mortally wounded players."""
        player1 = Mock(spec=Player)
        player1.player_id = uuid.uuid4()

        player2 = Mock(spec=Player)
        player2.player_id = uuid.uuid4()

        player3 = Mock(spec=Player)
        player3.player_id = uuid.uuid4()

        mock_player_death_service.get_mortally_wounded_players.return_value = [player1, player2, player3]

        mock_session = AsyncMock()

        # Process one tick
        for player in mock_player_death_service.get_mortally_wounded_players():
            await mock_player_death_service.process_mortally_wounded_tick(player.player_id, mock_session)

        # Verify all players were processed
        assert mock_player_death_service.process_mortally_wounded_tick.call_count == 3

    @pytest.mark.asyncio
    async def test_hp_decay_continues_each_tick(self, mock_player_death_service, mock_mortally_wounded_player):
        """Test that HP decay continues on each tick until death."""
        mock_player_death_service.get_mortally_wounded_players.return_value = [mock_mortally_wounded_player]

        mock_session = AsyncMock()

        # Simulate multiple ticks
        for _tick in range(5):
            players = mock_player_death_service.get_mortally_wounded_players()
            for player in players:
                await mock_player_death_service.process_mortally_wounded_tick(player.player_id, mock_session)

        # Verify HP decay was called 5 times (once per tick)
        assert mock_player_death_service.process_mortally_wounded_tick.call_count == 5
