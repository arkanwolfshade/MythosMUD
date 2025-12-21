"""Tests for player death service."""

from unittest.mock import AsyncMock, Mock
from uuid import uuid4

import pytest

from server.models.player import Player
from server.services.player_death_service import PlayerDeathService


@pytest.fixture
def player_death_service():
    """Create a player death service instance for testing."""
    return PlayerDeathService()


# Test UUID constant for consistent testing
TEST_PLAYER_ID = uuid4()


@pytest.fixture
def mock_player():  # pylint: disable=redefined-outer-name
    """Create a mock player with configurable HP."""
    player = Mock(spec=Player)
    player.player_id = TEST_PLAYER_ID
    player.name = "TestPlayer"
    player.current_room_id = "test-room-id"
    return player


class TestPlayerDeathService:  # pylint: disable=redefined-outer-name
    """Test suite for PlayerDeathService."""

    @pytest.mark.asyncio
    async def test_get_mortally_wounded_players_empty(self, player_death_service):
        """Test getting mortally wounded players when none exist."""
        # Mock database session to return no players (using async SQLAlchemy 2.0 API)
        mock_session = AsyncMock()
        mock_scalars = Mock()
        mock_scalars.all.return_value = []
        mock_result = Mock()
        mock_result.scalars.return_value = mock_scalars
        mock_session.execute.return_value = mock_result

        result = await player_death_service.get_mortally_wounded_players(mock_session)

        assert result == []

    @pytest.mark.asyncio
    async def test_get_mortally_wounded_players_with_valid_players(self, player_death_service):
        """Test getting mortally wounded players when some exist."""
        # Create mock players with different HP values
        player1 = Mock(spec=Player)
        player1.player_id = "player-1"
        player1.get_stats.return_value = {"current_dp": 0}  # Mortally wounded

        player2 = Mock(spec=Player)
        player2.player_id = "player-2"
        player2.get_stats.return_value = {"current_dp": -5}  # Mortally wounded

        player3 = Mock(spec=Player)
        player3.player_id = "player-3"
        player3.get_stats.return_value = {"current_dp": 50}  # Alive

        player4 = Mock(spec=Player)
        player4.player_id = "player-4"
        player4.get_stats.return_value = {"current_dp": -10}  # Dead

        # Mock database session to return all players (using async SQLAlchemy 2.0 API)
        mock_session = AsyncMock()
        mock_scalars = Mock()
        mock_scalars.all.return_value = [player1, player2, player3, player4]
        mock_result = Mock()
        mock_result.scalars.return_value = mock_scalars
        mock_session.execute.return_value = mock_result

        result = await player_death_service.get_mortally_wounded_players(mock_session)

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
        stats = {"current_dp": -3}
        mock_player.get_stats.return_value = stats
        mock_player.is_dead.return_value = False

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await player_death_service.process_mortally_wounded_tick(TEST_PLAYER_ID, mock_session)

        # Verify HP was decreased by 1
        assert result is True
        mock_player.set_stats.assert_called_once()
        updated_stats = mock_player.set_stats.call_args[0][0]
        assert updated_stats["current_dp"] == -4
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_cap_at_minus_ten(self, player_death_service, mock_player):
        """Test HP decay caps at -10."""
        # Set player to -9 HP (one away from death)
        stats = {"current_dp": -9}
        mock_player.get_stats.return_value = stats
        mock_player.is_dead.return_value = False

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await player_death_service.process_mortally_wounded_tick(TEST_PLAYER_ID, mock_session)

        # Verify HP was decreased to exactly -10 (capped)
        assert result is True
        updated_stats = mock_player.set_stats.call_args[0][0]
        assert updated_stats["current_dp"] == -10
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_already_at_cap(self, player_death_service, mock_player):
        """Test HP decay when already at -10."""
        # Set player to exactly -10 HP
        stats = {"current_dp": -10}
        mock_player.get_stats.return_value = stats
        mock_player.is_dead.return_value = True

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await player_death_service.process_mortally_wounded_tick(TEST_PLAYER_ID, mock_session)

        # Should not process decay for dead player
        assert result is False
        mock_player.set_stats.assert_not_called()
        mock_session.commit.assert_not_called()

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_player_not_found(self, player_death_service):
        """Test HP decay when player doesn't exist."""
        mock_session = AsyncMock()
        mock_session.get.return_value = None

        result = await player_death_service.process_mortally_wounded_tick("nonexistent-player", mock_session)

        assert result is False

    @pytest.mark.asyncio
    async def test_handle_player_death_basic(self, player_death_service, mock_player):
        """Test basic player death handling."""
        mock_player.current_room_id = "death-room"
        mock_player.name = "DeadPlayer"
        # get_stats() must return a mutable dict, not a Mock
        mock_player.get_stats.return_value = {"current_dp": -10, "position": "standing"}
        mock_player.set_stats = Mock()

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        killer_info = {"killer_id": "npc-123", "killer_name": "Terrible Beast"}

        result = await player_death_service.handle_player_death(TEST_PLAYER_ID, "death-room", killer_info, mock_session)

        assert result is True
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_death_no_killer(self, player_death_service, mock_player):
        """Test player death without a killer."""
        mock_player.current_room_id = "death-room"
        mock_player.name = "DeadPlayer"
        # get_stats() must return a mutable dict, not a Mock
        mock_player.get_stats.return_value = {"current_dp": -10, "position": "standing"}
        mock_player.set_stats = Mock()

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await player_death_service.handle_player_death(TEST_PLAYER_ID, "death-room", None, mock_session)

        assert result is True
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_death_player_not_found(self, player_death_service):
        """Test death handling when player doesn't exist."""
        mock_session = AsyncMock()
        mock_session.get.return_value = None

        result = await player_death_service.handle_player_death("nonexistent-player", "test-room", None, mock_session)

        assert result is False

    @pytest.mark.asyncio
    async def test_get_mortally_wounded_players_database_exception(self, player_death_service):
        """Test get_mortally_wounded_players handles database exceptions gracefully."""
        # Mock session that raises an exception (using async SQLAlchemy 2.0 API)
        mock_session = AsyncMock()
        mock_session.execute.side_effect = Exception("Database connection error")

        result = await player_death_service.get_mortally_wounded_players(mock_session)

        # Should return empty list on error
        assert result == []

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_with_event_bus(self, mock_player):
        """Test HP decay with event bus integration."""
        # Create service with event bus
        mock_event_bus = Mock()
        service = PlayerDeathService(event_bus=mock_event_bus)

        stats = {"current_dp": -5}
        mock_player.get_stats.return_value = stats
        mock_player.is_dead.return_value = False
        mock_player.name = "TestPlayer"

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        result = await service.process_mortally_wounded_tick(uuid4(), mock_session)

        assert result is True
        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        event = mock_event_bus.publish.call_args[0][0]
        assert event.event_type == "PlayerDPDecayEvent"
        assert event.old_dp == -5
        assert event.new_dp == -6

    @pytest.mark.asyncio
    async def test_process_mortally_wounded_tick_database_exception(self, player_death_service, mock_player):
        """Test HP decay handles database exceptions gracefully."""
        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player
        mock_session.commit.side_effect = Exception("Database error")

        mock_player.get_stats.return_value = {"current_dp": -5}
        mock_player.is_dead.return_value = False

        result = await player_death_service.process_mortally_wounded_tick(TEST_PLAYER_ID, mock_session)

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
        # get_stats() must return a mutable dict, not a Mock
        mock_player.get_stats.return_value = {"current_dp": -10, "position": "standing"}
        mock_player.set_stats = Mock()

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        killer_info = {"killer_id": "npc-123", "killer_name": "Beast"}

        result = await service.handle_player_death(TEST_PLAYER_ID, "death-room", killer_info, mock_session)

        assert result is True
        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        event = mock_event_bus.publish.call_args[0][0]
        assert event.event_type == "PlayerDiedEvent"
        assert event.player_id == TEST_PLAYER_ID
        assert event.killer_id == "npc-123"

    @pytest.mark.asyncio
    async def test_handle_player_death_database_exception(self, player_death_service, mock_player):
        """Test death handling handles database exceptions gracefully."""
        mock_player.current_room_id = "death-room"
        mock_player.name = "DeadPlayer"
        # get_stats() must return a mutable dict, not a Mock
        mock_player.get_stats.return_value = {"current_dp": -10, "position": "standing"}
        mock_player.set_stats = Mock()

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player
        mock_session.commit.side_effect = Exception("Database error")

        result = await player_death_service.handle_player_death(TEST_PLAYER_ID, "death-room", None, mock_session)

        assert result is False
        mock_session.rollback.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_death_clears_combat_state(self, mock_player):
        """Test that player death clears combat state (GitHub issue #244)."""
        # Create service with both event bus and player combat service
        mock_event_bus = Mock()
        mock_player_combat_service = AsyncMock()
        service = PlayerDeathService(event_bus=mock_event_bus, player_combat_service=mock_player_combat_service)

        # Setup player
        player_id = uuid4()
        mock_player.player_id = str(player_id)
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "death-room"
        # get_stats() must return a mutable dict, not a Mock
        mock_player.get_stats.return_value = {"current_dp": -10, "position": "standing"}
        mock_player.set_stats = Mock()

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        killer_info = {"killer_id": "npc-123", "killer_name": "Beast"}

        # Call handle_player_death with the same player_id
        result = await service.handle_player_death(player_id, "death-room", killer_info, mock_session)

        # Verify death was handled successfully
        assert result is True
        mock_session.commit.assert_called_once()

        # CRITICAL: Verify combat state was cleared
        mock_player_combat_service.clear_player_combat_state.assert_called_once()
        # Verify the correct player UUID was passed
        call_args = mock_player_combat_service.clear_player_combat_state.call_args
        assert call_args[0][0] == player_id

    @pytest.mark.asyncio
    async def test_handle_player_death_without_combat_service(self, mock_player):
        """Test that player death works even without player combat service."""
        # Create service without player combat service
        mock_event_bus = Mock()
        service = PlayerDeathService(event_bus=mock_event_bus, player_combat_service=None)

        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "death-room"
        # get_stats() must return a mutable dict, not a Mock
        mock_player.get_stats.return_value = {"current_dp": -10, "position": "standing"}
        mock_player.set_stats = Mock()

        mock_session = AsyncMock()
        mock_session.get.return_value = mock_player

        # Should not raise exception even without combat service
        result = await service.handle_player_death(uuid4(), "death-room", None, mock_session)

        assert result is True
        mock_session.commit.assert_called_once()
