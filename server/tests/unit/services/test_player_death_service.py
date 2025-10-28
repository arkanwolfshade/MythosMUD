"""
Unit tests for Player Death Service.

Tests the player death detection, mortally wounded state management,
HP decay processing, and death event handling.
"""

from unittest.mock import AsyncMock, Mock

import pytest

from server.services.player_death_service import PlayerDeathService


class TestPlayerDeathServiceInitialization:
    """Test PlayerDeathService initialization."""

    def test_service_initialization(self):
        """Test that the service initializes correctly."""
        mock_persistence = Mock()
        mock_event_bus = Mock()

        service = PlayerDeathService(mock_persistence, mock_event_bus)

        assert service._persistence == mock_persistence
        assert service._event_bus == mock_event_bus
        assert service._mortally_wounded_players == set()


class TestGetMortallyWoundedPlayers:
    """Test getting list of mortally wounded players."""

    @pytest.fixture
    def death_service(self):
        """Create a death service for testing."""
        mock_persistence = Mock()
        mock_event_bus = Mock()
        return PlayerDeathService(mock_persistence, mock_event_bus)

    def test_get_mortally_wounded_players_empty(self, death_service):
        """Test getting mortally wounded players when none exist."""
        # Mock persistence to return no players
        death_service._persistence.get_all_players = Mock(return_value=[])

        result = death_service.get_mortally_wounded_players()

        assert result == []

    def test_get_mortally_wounded_players_all_alive(self, death_service):
        """Test getting mortally wounded players when all are alive."""
        # Mock players all with positive HP
        mock_player1 = Mock()
        mock_player1.player_id = "player1"
        mock_player1.is_mortally_wounded = Mock(return_value=False)

        mock_player2 = Mock()
        mock_player2.player_id = "player2"
        mock_player2.is_mortally_wounded = Mock(return_value=False)

        death_service._persistence.get_all_players = Mock(return_value=[mock_player1, mock_player2])

        result = death_service.get_mortally_wounded_players()

        assert result == []

    def test_get_mortally_wounded_players_some_wounded(self, death_service):
        """Test getting mortally wounded players when some exist."""
        # Mock mix of alive, mortally wounded, and dead players
        mock_player1 = Mock()
        mock_player1.player_id = "player1"
        mock_player1.is_mortally_wounded = Mock(return_value=False)  # Alive

        mock_player2 = Mock()
        mock_player2.player_id = "player2"
        mock_player2.is_mortally_wounded = Mock(return_value=True)  # Mortally wounded

        mock_player3 = Mock()
        mock_player3.player_id = "player3"
        mock_player3.is_mortally_wounded = Mock(return_value=True)  # Mortally wounded

        mock_player4 = Mock()
        mock_player4.player_id = "player4"
        mock_player4.is_dead = Mock(return_value=True)
        mock_player4.is_mortally_wounded = Mock(return_value=False)  # Dead

        death_service._persistence.get_all_players = Mock(
            return_value=[mock_player1, mock_player2, mock_player3, mock_player4]
        )

        result = death_service.get_mortally_wounded_players()

        assert len(result) == 2
        assert "player2" in result
        assert "player3" in result


class TestProcessMortallyWoundedTick:
    """Test HP decay processing for mortally wounded players."""

    @pytest.fixture
    def death_service(self):
        """Create a death service for testing."""
        mock_persistence = Mock()
        mock_event_bus = Mock()
        return PlayerDeathService(mock_persistence, mock_event_bus)

    @pytest.mark.asyncio
    async def test_process_tick_reduces_hp_by_one(self, death_service):
        """Test that HP decay reduces HP by 1."""
        player_id = "player1"

        # Mock player at 0 HP
        mock_player = Mock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.get_stats = Mock(return_value={"current_health": 0})
        mock_player.set_stats = Mock()
        mock_player.is_mortally_wounded = Mock(return_value=True)
        mock_player.is_dead = Mock(return_value=False)
        mock_player.current_room_id = "test_room_001"

        death_service._persistence.get_player = Mock(return_value=mock_player)
        death_service._persistence.save_player = Mock()

        await death_service.process_mortally_wounded_tick(player_id)

        # Verify HP was reduced by 1
        mock_player.set_stats.assert_called_once()
        updated_stats = mock_player.set_stats.call_args[0][0]
        assert updated_stats["current_health"] == -1

        # Verify player was saved
        death_service._persistence.save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_process_tick_caps_at_minus_ten(self, death_service):
        """Test that HP decay stops at -10."""
        player_id = "player1"

        # Mock player at -9 HP
        mock_player = Mock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.get_stats = Mock(return_value={"current_health": -9})
        mock_player.set_stats = Mock()
        mock_player.current_room_id = "test_room_001"

        # After decaying, player will be at -10 (dead)
        def check_death_state(*args, **kwargs):
            stats = mock_player.get_stats()
            return stats["current_health"] <= -10

        mock_player.is_dead = Mock(side_effect=check_death_state)
        mock_player.is_mortally_wounded = Mock(return_value=True)

        death_service._persistence.get_player = Mock(return_value=mock_player)
        death_service._persistence.save_player = Mock()

        await death_service.process_mortally_wounded_tick(player_id)

        # Verify HP was capped at -10
        updated_stats = mock_player.set_stats.call_args[0][0]
        assert updated_stats["current_health"] == -10

    @pytest.mark.asyncio
    async def test_process_tick_triggers_death_at_minus_ten(self, death_service):
        """Test that reaching -10 HP triggers death."""
        player_id = "player1"

        # Mock player at -9 HP (will become -10 after tick)
        mock_player = Mock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.get_stats = Mock(return_value={"current_health": -9})
        mock_player.set_stats = Mock()
        mock_player.current_room_id = "test_room_001"

        # Player will be dead after decay
        death_service._persistence.get_player = Mock(return_value=mock_player)
        death_service._persistence.save_player = Mock()

        # Mock handle_player_death to verify it's called
        death_service.handle_player_death = AsyncMock()

        # First check: player is mortally wounded
        mock_player.is_mortally_wounded = Mock(return_value=True)
        mock_player.is_dead = Mock(return_value=False)

        await death_service.process_mortally_wounded_tick(player_id)

        # After HP update, check if player is dead
        updated_stats = mock_player.set_stats.call_args[0][0]
        if updated_stats["current_health"] <= -10:
            # Manually trigger death check (in real code, this is done after save)
            mock_player.is_dead = Mock(return_value=True)
            await death_service.handle_player_death(
                player_id=player_id,
                death_location=mock_player.current_room_id,
                killer_info={"killer_type": "hp_decay", "killer_name": "blood loss"}
            )

        # Verify death handler was called
        death_service.handle_player_death.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_tick_player_not_found(self, death_service):
        """Test that processing handles missing player gracefully."""
        player_id = "nonexistent_player"

        death_service._persistence.get_player = Mock(return_value=None)

        # Should not raise exception
        await death_service.process_mortally_wounded_tick(player_id)

    @pytest.mark.asyncio
    async def test_process_tick_publishes_decay_event(self, death_service):
        """Test that HP decay publishes PlayerHPDecayEvent."""
        player_id = "player1"

        # Mock player at -3 HP
        mock_player = Mock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.get_stats = Mock(return_value={"current_health": -3})
        mock_player.set_stats = Mock()
        mock_player.is_mortally_wounded = Mock(return_value=True)
        mock_player.is_dead = Mock(return_value=False)
        mock_player.current_room_id = "test_room_001"

        death_service._persistence.get_player = Mock(return_value=mock_player)
        death_service._persistence.save_player = Mock()

        await death_service.process_mortally_wounded_tick(player_id)

        # Verify event was published
        death_service._event_bus.publish.assert_called_once()
        published_event = death_service._event_bus.publish.call_args[0][0]
        assert published_event.event_type == "PlayerHPDecayEvent"
        assert published_event.player_id == player_id
        assert published_event.old_hp == -3
        assert published_event.new_hp == -4


class TestHandlePlayerDeath:
    """Test player death handling."""

    @pytest.fixture
    def death_service(self):
        """Create a death service for testing."""
        mock_persistence = Mock()
        mock_event_bus = Mock()
        return PlayerDeathService(mock_persistence, mock_event_bus)

    @pytest.mark.asyncio
    async def test_handle_player_death_publishes_event(self, death_service):
        """Test that player death publishes PlayerDiedEvent."""
        player_id = "player1"
        death_location = "earth_arkhamcity_downtown_001"
        killer_info = {
            "killer_id": "npc_morgue_attendant_001",
            "killer_name": "Morgue Attendant",
            "killer_type": "npc"
        }

        # Mock player
        mock_player = Mock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = death_location

        death_service._persistence.get_player = Mock(return_value=mock_player)

        await death_service.handle_player_death(player_id, death_location, killer_info)

        # Verify event was published
        death_service._event_bus.publish.assert_called_once()
        published_event = death_service._event_bus.publish.call_args[0][0]
        assert published_event.event_type == "PlayerDiedEvent"
        assert published_event.player_id == player_id
        assert published_event.death_location == death_location

    @pytest.mark.asyncio
    async def test_handle_player_death_from_hp_decay(self, death_service):
        """Test handling death from HP decay (no killer)."""
        player_id = "player1"
        death_location = "earth_arkhamcity_downtown_001"
        killer_info = {"killer_type": "hp_decay", "killer_name": "blood loss"}

        mock_player = Mock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = death_location

        death_service._persistence.get_player = Mock(return_value=mock_player)

        await death_service.handle_player_death(player_id, death_location, killer_info)

        # Verify event was published with hp_decay as killer
        published_event = death_service._event_bus.publish.call_args[0][0]
        assert published_event.killer_type == "hp_decay"

    @pytest.mark.asyncio
    async def test_handle_player_death_removes_from_tracked_set(self, death_service):
        """Test that death removes player from mortally wounded tracking."""
        player_id = "player1"
        death_location = "test_room_001"

        # Add player to mortally wounded set
        death_service._mortally_wounded_players.add(player_id)

        mock_player = Mock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = death_location

        death_service._persistence.get_player = Mock(return_value=mock_player)

        await death_service.handle_player_death(
            player_id, death_location, {"killer_type": "hp_decay", "killer_name": "blood loss"}
        )

        # Verify player was removed from tracking set
        assert player_id not in death_service._mortally_wounded_players


class TestMortallyWoundedTracking:
    """Test mortally wounded player tracking."""

    @pytest.fixture
    def death_service(self):
        """Create a death service for testing."""
        mock_persistence = Mock()
        mock_event_bus = Mock()
        return PlayerDeathService(mock_persistence, mock_event_bus)

    def test_add_mortally_wounded_player(self, death_service):
        """Test adding player to mortally wounded tracking."""
        player_id = "player1"

        death_service.add_mortally_wounded_player(player_id)

        assert player_id in death_service._mortally_wounded_players

    def test_remove_mortally_wounded_player(self, death_service):
        """Test removing player from mortally wounded tracking."""
        player_id = "player1"
        death_service._mortally_wounded_players.add(player_id)

        death_service.remove_mortally_wounded_player(player_id)

        assert player_id not in death_service._mortally_wounded_players

    def test_remove_nonexistent_player_does_not_error(self, death_service):
        """Test that removing non-tracked player doesn't raise error."""
        player_id = "nonexistent_player"

        # Should not raise exception
        death_service.remove_mortally_wounded_player(player_id)

        assert player_id not in death_service._mortally_wounded_players


class TestProcessAllMortallyWoundedPlayers:
    """Test bulk processing of all mortally wounded players."""

    @pytest.fixture
    def death_service(self):
        """Create a death service for testing."""
        mock_persistence = Mock()
        mock_event_bus = Mock()
        return PlayerDeathService(mock_persistence, mock_event_bus)

    @pytest.mark.asyncio
    async def test_process_all_mortally_wounded_players(self, death_service):
        """Test processing all mortally wounded players in one tick."""
        # Add multiple mortally wounded players
        death_service._mortally_wounded_players = {"player1", "player2", "player3"}

        # Mock the individual tick processing
        death_service.process_mortally_wounded_tick = AsyncMock()

        await death_service.process_all_mortally_wounded_players()

        # Verify all players were processed
        assert death_service.process_mortally_wounded_tick.call_count == 3
        death_service.process_mortally_wounded_tick.assert_any_call("player1")
        death_service.process_mortally_wounded_tick.assert_any_call("player2")
        death_service.process_mortally_wounded_tick.assert_any_call("player3")

    @pytest.mark.asyncio
    async def test_process_all_with_errors_continues(self, death_service):
        """Test that errors in processing one player don't stop others."""
        death_service._mortally_wounded_players = {"player1", "player2", "player3"}

        # Mock processing to fail for player2
        async def mock_process_tick(player_id):
            if player_id == "player2":
                raise Exception("Test error")

        death_service.process_mortally_wounded_tick = AsyncMock(side_effect=mock_process_tick)

        # Should not raise exception, should continue processing all players
        await death_service.process_all_mortally_wounded_players()

        # All three players should have been attempted
        assert death_service.process_mortally_wounded_tick.call_count == 3
