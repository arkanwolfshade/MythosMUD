"""
Unit tests for the PlayerCombatService class.

This module tests player combat state tracking, XP rewards, and integration
with the persistence layer in isolation from other systems.
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from server.models.player import Player
from server.services.player_combat_service import PlayerCombatService, PlayerCombatState

# from server.events.combat_events import PlayerXPAwardedEvent  # Event doesn't exist yet


class TestPlayerCombatServiceUnit:
    """Unit tests for PlayerCombatService core functionality."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return AsyncMock()

    @pytest.fixture
    def mock_event_bus(self):
        """Create a mock event bus.

        Note: EventBus.publish() is synchronous, so use Mock() not AsyncMock().
        """
        from unittest.mock import Mock

        mock_bus = Mock()
        mock_bus.publish = Mock(return_value=None)
        return mock_bus

    @pytest.fixture
    def player_combat_service(self, mock_persistence, mock_event_bus):
        """Create a player combat service instance for testing."""
        return PlayerCombatService(mock_persistence, mock_event_bus)

    @pytest.fixture
    def sample_player(self):
        """Create a sample player for testing."""
        return Player(
            player_id=str(uuid4()),
            user_id=str(uuid4()),
            name="TestPlayer",
            experience_points=100,
            level=5,
        )

    @pytest.mark.asyncio
    async def test_track_player_combat_state(self, player_combat_service):
        """Test tracking player combat state."""
        player_id = uuid4()
        player_name = "TestPlayer"
        combat_id = uuid4()
        room_id = "test_room_001"

        await player_combat_service.track_player_combat_state(
            player_id=player_id,
            player_name=player_name,
            combat_id=combat_id,
            room_id=room_id,
        )

        # Verify state was tracked
        assert player_id in player_combat_service._player_combat_states
        state = player_combat_service._player_combat_states[player_id]
        assert state.player_name == player_name
        assert state.combat_id == combat_id
        assert state.room_id == room_id
        assert state.is_in_combat is True

    @pytest.mark.asyncio
    async def test_get_player_combat_state(self, player_combat_service):
        """Test getting player combat state."""
        player_id = uuid4()
        combat_id = uuid4()

        # Track state
        await player_combat_service.track_player_combat_state(
            player_id=player_id,
            player_name="TestPlayer",
            combat_id=combat_id,
            room_id="test_room",
        )

        # Get state
        state = await player_combat_service.get_player_combat_state(player_id)
        assert state is not None
        assert state.player_id == player_id
        assert state.combat_id == combat_id

        # Test non-existent player
        non_existent_id = uuid4()
        state = await player_combat_service.get_player_combat_state(non_existent_id)
        assert state is None

    @pytest.mark.asyncio
    async def test_clear_player_combat_state(self, player_combat_service):
        """Test clearing player combat state."""
        player_id = uuid4()

        # Track state
        await player_combat_service.track_player_combat_state(
            player_id=player_id,
            player_name="TestPlayer",
            combat_id=uuid4(),
            room_id="test_room",
        )

        # Verify state exists
        assert player_id in player_combat_service._player_combat_states

        # Clear state
        await player_combat_service.clear_player_combat_state(player_id)

        # Verify state is cleared
        assert player_id not in player_combat_service._player_combat_states

    @pytest.mark.asyncio
    async def test_handle_combat_end(self, player_combat_service):
        """Test handling combat end for multiple players."""
        player1_id = uuid4()
        player2_id = uuid4()
        combat_id = uuid4()

        # Track states for two players in same combat
        await player_combat_service.track_player_combat_state(
            player_id=player1_id,
            player_name="Player1",
            combat_id=combat_id,
            room_id="test_room",
        )

        await player_combat_service.track_player_combat_state(
            player_id=player2_id,
            player_name="Player2",
            combat_id=combat_id,
            room_id="test_room",
        )

        # Track state for different combat
        different_combat_id = uuid4()
        player3_id = uuid4()
        await player_combat_service.track_player_combat_state(
            player_id=player3_id,
            player_name="Player3",
            combat_id=different_combat_id,
            room_id="test_room",
        )

        # Handle combat end
        await player_combat_service.handle_combat_end(combat_id)

        # Verify only players from the ended combat are cleared
        assert player1_id not in player_combat_service._player_combat_states
        assert player2_id not in player_combat_service._player_combat_states
        assert player3_id in player_combat_service._player_combat_states

    @pytest.mark.asyncio
    async def test_award_xp_on_npc_death_success(self, player_combat_service, mock_persistence, sample_player):
        """Test successful XP award on NPC death."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_amount = 10

        # Mock persistence to return sample player
        mock_persistence.async_get_player.return_value = sample_player
        mock_persistence.save_player = AsyncMock()

        # Award XP
        await player_combat_service.award_xp_on_npc_death(
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
        )

        # Verify player was retrieved and saved
        mock_persistence.async_get_player.assert_called_once_with(player_id)
        mock_persistence.save_player.assert_called_once()

        # Verify XP was added
        assert sample_player.experience_points == 110  # 100 + 10

    @pytest.mark.asyncio
    async def test_award_xp_on_npc_death_player_not_found(self, player_combat_service, mock_persistence):
        """Test XP award when player is not found."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_amount = 10

        # Mock persistence to return None (player not found)
        mock_persistence.async_get_player.return_value = None
        mock_persistence.save_player = AsyncMock()

        # Award XP
        await player_combat_service.award_xp_on_npc_death(
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
        )

        # Verify player was retrieved but not saved
        mock_persistence.async_get_player.assert_called_once_with(player_id)
        mock_persistence.save_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_award_xp_on_npc_death_publishes_event(
        self, player_combat_service, mock_persistence, mock_event_bus, sample_player
    ):
        """Test that XP award publishes an event."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_amount = 10

        # Mock persistence to return sample player
        mock_persistence.async_get_player.return_value = sample_player
        mock_persistence.save_player = AsyncMock()

        # Award XP
        await player_combat_service.award_xp_on_npc_death(
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
        )

        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        # Note: PlayerXPAwardedEvent doesn't exist yet, so we just verify the event was published
        published_event = mock_event_bus.publish.call_args[0][0]
        assert published_event is not None

    @pytest.mark.asyncio
    async def test_calculate_xp_reward(self, player_combat_service):
        """Test XP reward calculation."""
        npc_id = uuid4()

        # Mock lifecycle manager with empty records to trigger fallback
        mock_lifecycle_manager = AsyncMock()
        mock_lifecycle_manager.lifecycle_records = {}
        player_combat_service._persistence.get_npc_lifecycle_manager = AsyncMock(return_value=mock_lifecycle_manager)

        xp_reward = await player_combat_service.calculate_xp_reward(npc_id)

        # Should return an integer (0 when no lifecycle record found)
        assert isinstance(xp_reward, int)
        assert xp_reward == 0  # Default is 0 when NPC not in lifecycle manager

    @pytest.mark.asyncio
    async def test_cleanup_stale_combat_states(self, player_combat_service):
        """Test cleaning up stale combat states."""
        player_id = uuid4()

        # Track state
        await player_combat_service.track_player_combat_state(
            player_id=player_id,
            player_name="TestPlayer",
            combat_id=uuid4(),
            room_id="test_room",
        )

        # Manually set last activity to be stale
        player_combat_service._player_combat_states[player_id].last_activity = datetime.now(UTC) - timedelta(minutes=35)

        # Clean up stale states
        cleaned_count = await player_combat_service.cleanup_stale_combat_states()

        assert cleaned_count == 1
        assert player_id not in player_combat_service._player_combat_states

    @pytest.mark.asyncio
    async def test_cleanup_stale_combat_states_no_stale(self, player_combat_service):
        """Test cleanup when no stale states exist."""
        player_id = uuid4()

        # Track state
        await player_combat_service.track_player_combat_state(
            player_id=player_id,
            player_name="TestPlayer",
            combat_id=uuid4(),
            room_id="test_room",
        )

        # Clean up stale states (should not clean up recent state)
        cleaned_count = await player_combat_service.cleanup_stale_combat_states()

        assert cleaned_count == 0
        assert player_id in player_combat_service._player_combat_states

    @pytest.mark.asyncio
    async def test_get_combat_stats(self, player_combat_service):
        """Test getting combat statistics."""
        # Initially no players in combat
        stats = await player_combat_service.get_combat_stats()
        assert stats["players_in_combat"] == 0
        assert stats["active_combats"] == 0

        # Track states for two players in same combat
        combat_id = uuid4()
        player1_id = uuid4()
        player2_id = uuid4()

        await player_combat_service.track_player_combat_state(
            player_id=player1_id,
            player_name="Player1",
            combat_id=combat_id,
            room_id="test_room",
        )

        await player_combat_service.track_player_combat_state(
            player_id=player2_id,
            player_name="Player2",
            combat_id=combat_id,
            room_id="test_room",
        )

        # Check stats
        stats = await player_combat_service.get_combat_stats()
        assert stats["players_in_combat"] == 2
        assert stats["active_combats"] == 1  # Same combat

    def test_player_combat_state_creation(self):
        """Test PlayerCombatState creation."""
        player_id = uuid4()
        player_name = "TestPlayer"
        combat_id = uuid4()
        room_id = "test_room"

        state = PlayerCombatState(
            player_id=player_id,
            player_name=player_name,
            combat_id=combat_id,
            room_id=room_id,
        )

        assert state.player_id == player_id
        assert state.player_name == player_name
        assert state.combat_id == combat_id
        assert state.room_id == room_id
        assert state.is_in_combat is True
        assert isinstance(state.last_activity, datetime)

    def test_player_combat_state_defaults(self):
        """Test PlayerCombatState default values."""
        state = PlayerCombatState(
            player_id=uuid4(),
            player_name="TestPlayer",
            combat_id=uuid4(),
            room_id="test_room",
        )

        assert state.is_in_combat is True
        assert isinstance(state.last_activity, datetime)

    def test_player_combat_service_initialization(self, mock_persistence, mock_event_bus):
        """Test PlayerCombatService initialization."""
        service = PlayerCombatService(mock_persistence, mock_event_bus)

        assert service._player_combat_states == {}
        assert service._persistence == mock_persistence
        assert service._event_bus == mock_event_bus
        assert service._combat_timeout_minutes == 30

    @pytest.mark.asyncio
    async def test_handle_npc_death_delegates_to_award_xp(self, player_combat_service, mock_persistence, sample_player):
        """Test that handle_npc_death delegates to award_xp_on_npc_death."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_amount = 10

        # Mock persistence
        mock_persistence.async_get_player.return_value = sample_player
        mock_persistence.save_player = AsyncMock()

        # Call handle_npc_death
        await player_combat_service.handle_npc_death(
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
        )

        # Verify award_xp_on_npc_death was called
        mock_persistence.async_get_player.assert_called_once_with(player_id)
        mock_persistence.save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_award_xp_handles_exception(self, player_combat_service, mock_persistence):
        """Test that XP award handles exceptions gracefully."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_amount = 10

        # Mock persistence to raise an exception
        mock_persistence.async_get_player.side_effect = Exception("Database error")

        # Award XP should not raise exception
        await player_combat_service.award_xp_on_npc_death(
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
        )

        # Should have attempted to get player
        mock_persistence.async_get_player.assert_called_once_with(player_id)
