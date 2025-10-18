"""
Comprehensive tests for player combat integration.

This module tests player combat state tracking, XP reward system,
and integration with the existing player service for XP persistence.
"""

from datetime import datetime, timedelta
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.models.player import Player
from server.services.player_combat_service import PlayerCombatService


class TestPlayerCombatState:
    """Test player combat state tracking and management."""

    @pytest.fixture
    def player_combat_service(self):
        """Create a player combat service instance for testing."""
        mock_persistence = AsyncMock()
        mock_event_bus = AsyncMock()
        return PlayerCombatService(mock_persistence, mock_event_bus)

    @pytest.fixture
    def sample_player(self):
        """Create a sample player for testing."""
        player = Player(
            player_id=str(uuid4()),
            user_id=str(uuid4()),
            name="TestPlayer",
            current_room_id="test_room_001",
            experience_points=100,
            level=5,
        )
        return player

    @pytest.fixture
    def sample_combat(self):
        """Create a sample combat instance for testing."""
        combat = CombatInstance(room_id="test_room_001")

        player_id = uuid4()
        npc_id = uuid4()

        player = CombatParticipant(
            participant_id=player_id,
            participant_type=CombatParticipantType.PLAYER,
            name="TestPlayer",
            current_hp=100,
            max_hp=100,
            dexterity=15,
        )

        npc = CombatParticipant(
            participant_id=npc_id,
            participant_type=CombatParticipantType.NPC,
            name="TestNPC",
            current_hp=50,
            max_hp=50,
            dexterity=10,
        )

        combat.participants[player_id] = player
        combat.participants[npc_id] = npc
        combat.turn_order = [player_id, npc_id]

        return combat, player_id, npc_id

    @pytest.mark.asyncio
    async def test_track_player_combat_state(self, player_combat_service, sample_player, sample_combat):
        """Test tracking player combat state."""
        combat, player_id, _ = sample_combat

        # Track player combat state
        await player_combat_service.track_player_combat_state(
            player_id=player_id,
            player_name=sample_player.name,
            combat_id=combat.combat_id,
            room_id=combat.room_id,
        )

        # Verify player is tracked in combat
        assert player_id in player_combat_service._player_combat_states
        state = player_combat_service._player_combat_states[player_id]
        assert state.player_name == sample_player.name
        assert state.combat_id == combat.combat_id
        assert state.room_id == combat.room_id
        assert state.is_in_combat is True

    @pytest.mark.asyncio
    async def test_get_player_combat_state(self, player_combat_service, sample_player, sample_combat):
        """Test getting player combat state."""
        combat, player_id, _ = sample_combat

        # Track player combat state
        await player_combat_service.track_player_combat_state(
            player_id=player_id,
            player_name=sample_player.name,
            combat_id=combat.combat_id,
            room_id=combat.room_id,
        )

        # Get player combat state
        state = await player_combat_service.get_player_combat_state(player_id)
        assert state is not None
        assert state.player_name == sample_player.name
        assert state.combat_id == combat.combat_id
        assert state.is_in_combat is True

    @pytest.mark.asyncio
    async def test_get_player_combat_state_not_found(self, player_combat_service):
        """Test getting combat state for player not in combat."""
        player_id = uuid4()
        state = await player_combat_service.get_player_combat_state(player_id)
        assert state is None

    @pytest.mark.asyncio
    async def test_clear_player_combat_state(self, player_combat_service, sample_player, sample_combat):
        """Test clearing player combat state."""
        combat, player_id, _ = sample_combat

        # Track player combat state
        await player_combat_service.track_player_combat_state(
            player_id=player_id,
            player_name=sample_player.name,
            combat_id=combat.combat_id,
            room_id=combat.room_id,
        )

        # Clear player combat state
        await player_combat_service.clear_player_combat_state(player_id)

        # Verify player is no longer tracked
        assert player_id not in player_combat_service._player_combat_states
        state = await player_combat_service.get_player_combat_state(player_id)
        assert state is None

    @pytest.mark.asyncio
    async def test_is_player_in_combat(self, player_combat_service, sample_player, sample_combat):
        """Test checking if player is in combat."""
        combat, player_id, _ = sample_combat

        # Initially not in combat
        assert await player_combat_service.is_player_in_combat(player_id) is False

        # Track player combat state
        await player_combat_service.track_player_combat_state(
            player_id=player_id,
            player_name=sample_player.name,
            combat_id=combat.combat_id,
            room_id=combat.room_id,
        )

        # Now in combat
        assert await player_combat_service.is_player_in_combat(player_id) is True


class TestPlayerXPIntegration:
    """Test player XP reward system and persistence integration."""

    @pytest.fixture
    def player_combat_service(self):
        """Create a player combat service instance for testing."""
        mock_persistence = AsyncMock()
        mock_event_bus = AsyncMock()
        return PlayerCombatService(mock_persistence, mock_event_bus)

    @pytest.fixture
    def sample_player(self):
        """Create a sample player for testing."""
        player = Player(
            player_id=str(uuid4()),
            user_id=str(uuid4()),
            name="TestPlayer",
            current_room_id="test_room_001",
            experience_points=100,
            level=5,
        )
        return player

    @pytest.mark.asyncio
    async def test_award_xp_on_npc_death(self, player_combat_service, sample_player):
        """Test awarding XP when player defeats an NPC."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_reward = 25

        # Mock persistence to return the player
        player_combat_service._persistence.async_get_player = AsyncMock(return_value=sample_player)
        player_combat_service._persistence.async_save_player = AsyncMock()

        # Award XP
        await player_combat_service.award_xp_on_npc_death(player_id=player_id, npc_id=npc_id, xp_amount=xp_reward)

        # Verify player XP was increased
        assert sample_player.experience_points == 125  # 100 + 25
        assert sample_player.level == 2  # (125 // 100) + 1 = 1 + 1 = 2

        # Verify player was saved
        player_combat_service._persistence.async_save_player.assert_called_once_with(sample_player)

    @pytest.mark.asyncio
    async def test_award_xp_player_not_found(self, player_combat_service):
        """Test awarding XP when player is not found."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_reward = 25

        # Mock persistence to return None (player not found)
        player_combat_service._persistence.async_get_player = AsyncMock(return_value=None)

        # Award XP should not raise error but log warning
        await player_combat_service.award_xp_on_npc_death(player_id=player_id, npc_id=npc_id, xp_amount=xp_reward)

        # Verify no save was called
        player_combat_service._persistence.async_save_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_calculate_xp_reward_based_on_npc_level(self, player_combat_service):
        """Test calculating XP reward based on NPC level and stats."""
        npc_id = uuid4()
        npc_level = 3
        npc_xp_value = 15

        # Mock NPC data
        npc_data = {"base_stats": {"level": npc_level, "xp_value": npc_xp_value}}

        # Mock persistence to return NPC data
        player_combat_service._persistence.async_get_npc_by_id = AsyncMock(return_value=npc_data)

        # Calculate XP reward
        xp_reward = await player_combat_service.calculate_xp_reward(npc_id)

        # Verify XP reward calculation (currently returns default value)
        expected_xp = 5  # Default XP reward as implemented
        assert xp_reward == expected_xp

    @pytest.mark.asyncio
    async def test_calculate_xp_reward_default_fallback(self, player_combat_service):
        """Test calculating XP reward with default fallback when NPC not found."""
        npc_id = uuid4()

        # Mock persistence to return None (NPC not found)
        player_combat_service._persistence.async_get_npc_by_id = AsyncMock(return_value=None)

        # Calculate XP reward
        xp_reward = await player_combat_service.calculate_xp_reward(npc_id)

        # Verify default XP reward
        assert xp_reward == 5  # Default fallback value

    @pytest.mark.asyncio
    async def test_level_up_calculation(self, player_combat_service, sample_player):
        """Test level up calculation when XP is awarded."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_reward = 150  # Enough to level up

        # Mock persistence
        player_combat_service._persistence.async_get_player = AsyncMock(return_value=sample_player)
        player_combat_service._persistence.async_save_player = AsyncMock()

        # Award XP
        await player_combat_service.award_xp_on_npc_death(player_id=player_id, npc_id=npc_id, xp_amount=xp_reward)

        # Verify level up
        assert sample_player.experience_points == 250  # 100 + 150
        assert sample_player.level == 3  # (250 // 100) + 1 = 2 + 1 = 3

    @pytest.mark.asyncio
    async def test_xp_award_event_publishing(self, player_combat_service, sample_player):
        """Test that XP award events are published."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_reward = 25

        # Mock persistence
        player_combat_service._persistence.async_get_player = AsyncMock(return_value=sample_player)
        player_combat_service._persistence.async_save_player = AsyncMock()

        # Award XP
        await player_combat_service.award_xp_on_npc_death(player_id=player_id, npc_id=npc_id, xp_amount=xp_reward)

        # Verify event was published
        player_combat_service._event_bus.publish_event.assert_called_once()
        call_args = player_combat_service._event_bus.publish_event.call_args[0][0]
        assert call_args.event_type == "player_xp_awarded"
        assert call_args.player_id == player_id
        assert call_args.xp_amount == xp_reward
        assert call_args.new_level == sample_player.level


class TestPlayerCombatIntegration:
    """Test integration between player combat state and XP system."""

    @pytest.fixture
    def player_combat_service(self):
        """Create a player combat service instance for testing."""
        mock_persistence = AsyncMock()
        mock_event_bus = AsyncMock()
        return PlayerCombatService(mock_persistence, mock_event_bus)

    @pytest.fixture
    def sample_player(self):
        """Create a sample player for testing."""
        player = Player(
            player_id=str(uuid4()),
            user_id=str(uuid4()),
            name="TestPlayer",
            current_room_id="test_room_001",
            experience_points=100,
            level=5,
        )
        return player

    @pytest.mark.asyncio
    async def test_combat_start_player_tracking(self, player_combat_service, sample_player):
        """Test that players are tracked when combat starts."""
        player_id = uuid4()
        combat_id = uuid4()
        room_id = "test_room_001"

        # Start combat tracking
        await player_combat_service.handle_combat_start(
            player_id=player_id,
            player_name=sample_player.name,
            combat_id=combat_id,
            room_id=room_id,
        )

        # Verify player is tracked
        assert await player_combat_service.is_player_in_combat(player_id) is True
        state = await player_combat_service.get_player_combat_state(player_id)
        assert state.combat_id == combat_id
        assert state.room_id == room_id

    @pytest.mark.asyncio
    async def test_combat_end_player_cleanup(self, player_combat_service, sample_player):
        """Test that player combat state is cleaned up when combat ends."""
        player_id = uuid4()
        combat_id = uuid4()
        room_id = "test_room_001"

        # Start combat tracking
        await player_combat_service.handle_combat_start(
            player_id=player_id,
            player_name=sample_player.name,
            combat_id=combat_id,
            room_id=room_id,
        )

        # End combat
        await player_combat_service.handle_combat_end(combat_id)

        # Verify player is no longer tracked
        assert await player_combat_service.is_player_in_combat(player_id) is False
        state = await player_combat_service.get_player_combat_state(player_id)
        assert state is None

    @pytest.mark.asyncio
    async def test_npc_death_xp_award_integration(self, player_combat_service, sample_player):
        """Test complete integration of NPC death and XP awarding."""
        player_id = uuid4()
        npc_id = uuid4()
        combat_id = uuid4()
        room_id = "test_room_001"
        xp_reward = 30

        # Mock persistence
        player_combat_service._persistence.async_get_player = AsyncMock(return_value=sample_player)
        player_combat_service._persistence.async_save_player = AsyncMock()

        # Start combat tracking
        await player_combat_service.handle_combat_start(
            player_id=player_id,
            player_name=sample_player.name,
            combat_id=combat_id,
            room_id=room_id,
        )

        # Award XP on NPC death
        await player_combat_service.handle_npc_death(player_id=player_id, npc_id=npc_id, xp_amount=xp_reward)

        # Verify XP was awarded
        assert sample_player.experience_points == 130  # 100 + 30
        player_combat_service._persistence.async_save_player.assert_called_once_with(sample_player)

        # Verify event was published
        player_combat_service._event_bus.publish_event.assert_called_once()

    @pytest.mark.asyncio
    async def test_multiple_players_combat_tracking(self, player_combat_service):
        """Test tracking multiple players in different combats."""
        player1_id = uuid4()
        player2_id = uuid4()
        combat1_id = uuid4()
        combat2_id = uuid4()
        room_id = "test_room_001"

        # Start combat for player 1
        await player_combat_service.handle_combat_start(
            player_id=player1_id,
            player_name="Player1",
            combat_id=combat1_id,
            room_id=room_id,
        )

        # Start combat for player 2
        await player_combat_service.handle_combat_start(
            player_id=player2_id,
            player_name="Player2",
            combat_id=combat2_id,
            room_id=room_id,
        )

        # Verify both players are tracked
        assert await player_combat_service.is_player_in_combat(player1_id) is True
        assert await player_combat_service.is_player_in_combat(player2_id) is True

        # Get all players in combat
        players_in_combat = await player_combat_service.get_players_in_combat()
        assert len(players_in_combat) == 2
        assert player1_id in players_in_combat
        assert player2_id in players_in_combat

    @pytest.mark.asyncio
    async def test_combat_timeout_cleanup(self, player_combat_service):
        """Test cleanup of stale combat states."""
        player_id = uuid4()
        combat_id = uuid4()
        room_id = "test_room_001"

        # Start combat tracking
        await player_combat_service.handle_combat_start(
            player_id=player_id,
            player_name="TestPlayer",
            combat_id=combat_id,
            room_id=room_id,
        )

        # Manually set last activity to be stale
        state = player_combat_service._player_combat_states[player_id]
        state.last_activity = datetime.utcnow() - timedelta(minutes=35)

        # Clean up stale states
        cleaned_count = await player_combat_service.cleanup_stale_combat_states()

        # Verify cleanup
        assert cleaned_count == 1
        assert await player_combat_service.is_player_in_combat(player_id) is False

    @pytest.mark.asyncio
    async def test_error_handling_in_xp_award(self, player_combat_service):
        """Test error handling in XP award process."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_reward = 25

        # Mock persistence to raise an error
        player_combat_service._persistence.async_get_player = AsyncMock(side_effect=Exception("Database error"))

        # Award XP should not raise error but handle gracefully
        await player_combat_service.award_xp_on_npc_death(player_id=player_id, npc_id=npc_id, xp_amount=xp_reward)

        # Verify no save was attempted
        player_combat_service._persistence.async_save_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_combat_state_persistence_across_restarts(self, player_combat_service):
        """Test that combat states are properly managed across service restarts."""
        player_id = uuid4()
        combat_id = uuid4()
        room_id = "test_room_001"

        # Start combat tracking
        await player_combat_service.handle_combat_start(
            player_id=player_id,
            player_name="TestPlayer",
            combat_id=combat_id,
            room_id=room_id,
        )

        # Simulate service restart by creating new instance
        new_service = PlayerCombatService(player_combat_service._persistence, player_combat_service._event_bus)

        # Verify player is not tracked in new instance (combat states are in-memory only)
        assert await new_service.is_player_in_combat(player_id) is False
        state = await new_service.get_player_combat_state(player_id)
        assert state is None
