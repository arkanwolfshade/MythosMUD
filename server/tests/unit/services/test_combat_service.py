"""
Unit tests for the CombatService class.

This module tests the core combat logic, state management, and turn order
calculations in isolation from other systems.
"""

from datetime import datetime, timedelta
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from server.models.combat import CombatInstance, CombatStatus
from server.services.combat_service import CombatService
from server.services.player_combat_service import PlayerCombatService


class TestCombatServiceUnit:
    """Unit tests for CombatService core functionality."""

    @pytest.fixture
    def combat_service(self):
        """Create a combat service instance for testing."""
        return CombatService()

    @pytest.fixture
    def mock_player_combat_service(self):
        """Create a mock player combat service."""
        return AsyncMock(spec=PlayerCombatService)

    @pytest.fixture
    def combat_service_with_player_service(self, mock_player_combat_service):
        """Create a combat service with player combat service injected."""
        return CombatService(player_combat_service=mock_player_combat_service)

    @pytest.mark.asyncio
    async def test_start_combat_creates_combat_instance(self, combat_service):
        """Test that starting combat creates a proper combat instance."""
        player_id = uuid4()
        npc_id = uuid4()

        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        assert isinstance(combat, CombatInstance)
        assert combat.room_id == "test_room"
        assert combat.status == CombatStatus.ACTIVE
        assert len(combat.participants) == 2
        assert player_id in combat.participants
        assert npc_id in combat.participants

    @pytest.mark.asyncio
    async def test_start_combat_sets_turn_order_by_dexterity(self, combat_service):
        """Test that turn order is set correctly based on dexterity."""
        player_id = uuid4()
        npc_id = uuid4()

        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,  # Higher dex
            target_hp=50,
            target_max_hp=50,
            target_dex=10,  # Lower dex
        )

        # Player should go first due to higher dexterity
        assert combat.turn_order[0] == player_id
        assert combat.turn_order[1] == npc_id

    @pytest.mark.asyncio
    async def test_start_combat_tracks_participants(self, combat_service):
        """Test that combat participants are properly tracked."""
        player_id = uuid4()
        npc_id = uuid4()

        await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Check that participants are tracked
        assert player_id in combat_service._player_combats
        assert npc_id in combat_service._npc_combats
        assert len(combat_service._active_combats) == 1

    @pytest.mark.asyncio
    async def test_start_combat_with_player_service_integration(
        self, combat_service_with_player_service, mock_player_combat_service
    ):
        """Test that starting combat integrates with player combat service."""
        player_id = uuid4()
        npc_id = uuid4()

        await combat_service_with_player_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Verify player combat service was called
        mock_player_combat_service.track_player_combat_state.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_combat_by_participant_finds_combat(self, combat_service):
        """Test getting combat by participant ID."""
        player_id = uuid4()
        npc_id = uuid4()

        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Test finding combat by participant
        found_combat = await combat_service.get_combat_by_participant(player_id)
        assert found_combat == combat

        found_combat = await combat_service.get_combat_by_participant(npc_id)
        assert found_combat == combat

    @pytest.mark.asyncio
    async def test_get_combat_by_participant_returns_none_for_unknown(self, combat_service):
        """Test getting combat for unknown participant returns None."""
        unknown_id = uuid4()
        found_combat = await combat_service.get_combat_by_participant(unknown_id)
        assert found_combat is None

    @pytest.mark.asyncio
    async def test_process_attack_success(self, combat_service):
        """Test successful attack processing."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Process attack
        result = await combat_service.process_attack(player_id, npc_id, damage=5)

        assert result.success is True
        assert result.damage == 5
        assert result.target_died is False
        assert result.combat_ended is False

    @pytest.mark.asyncio
    async def test_process_attack_kills_target(self, combat_service):
        """Test attack that kills the target."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat with low target HP
        await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=5,  # Low HP
            target_max_hp=50,
            target_dex=10,
        )

        # Process attack that kills target
        result = await combat_service.process_attack(player_id, npc_id, damage=10)

        assert result.success is True
        assert result.damage == 10
        assert result.target_died is True
        assert result.combat_ended is True
        assert result.xp_awarded > 0

    @pytest.mark.asyncio
    async def test_process_attack_with_player_service_xp_award(
        self, combat_service_with_player_service, mock_player_combat_service
    ):
        """Test that XP is awarded through player combat service when target dies."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat with low target HP
        await combat_service_with_player_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=5,  # Low HP
            target_max_hp=50,
            target_dex=10,
        )

        # Process attack that kills target
        result = await combat_service_with_player_service.process_attack(player_id, npc_id, damage=10)

        assert result.success is True
        assert result.target_died is True
        assert result.combat_ended is True

        # Verify player combat service was called for XP award
        mock_player_combat_service.award_xp_on_npc_death.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_attack_not_in_combat_raises_error(self, combat_service):
        """Test that attacking when not in combat raises an error."""
        player_id = uuid4()
        npc_id = uuid4()

        with pytest.raises(ValueError, match="Attacker is not in combat"):
            await combat_service.process_attack(player_id, npc_id, damage=5)

    @pytest.mark.asyncio
    async def test_process_attack_wrong_turn_raises_error(self, combat_service):
        """Test that attacking when it's not the attacker's turn raises an error."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat with NPC having higher dexterity
        await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=10,  # Lower dex
            target_hp=50,
            target_max_hp=50,
            target_dex=15,  # Higher dex - goes first
        )

        # Try to attack when it's not player's turn
        with pytest.raises(ValueError, match="It is not the attacker's turn"):
            await combat_service.process_attack(player_id, npc_id, damage=5)

    @pytest.mark.asyncio
    async def test_end_combat_cleans_up_state(self, combat_service):
        """Test that ending combat cleans up all state."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        combat_id = combat.combat_id

        # End combat
        await combat_service.end_combat(combat_id, "Test end")

        # Verify cleanup
        assert combat.status == CombatStatus.ENDED
        assert combat_id not in combat_service._active_combats
        assert player_id not in combat_service._player_combats
        assert npc_id not in combat_service._npc_combats

    @pytest.mark.asyncio
    async def test_end_combat_with_player_service_cleanup(
        self, combat_service_with_player_service, mock_player_combat_service
    ):
        """Test that ending combat cleans up player combat state."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service_with_player_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        combat_id = combat.combat_id

        # End combat
        await combat_service_with_player_service.end_combat(combat_id, "Test end")

        # Verify player combat service cleanup was called
        mock_player_combat_service.handle_combat_end.assert_called_once_with(combat_id)

    @pytest.mark.asyncio
    async def test_cleanup_stale_combats(self, combat_service):
        """Test cleaning up stale combats."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Manually set last activity to be stale
        combat.last_activity = datetime.utcnow() - timedelta(minutes=35)

        # Clean up stale combats
        cleaned_count = await combat_service.cleanup_stale_combats()

        assert cleaned_count == 1
        assert combat.status == CombatStatus.ENDED
        assert combat.combat_id not in combat_service._active_combats

    @pytest.mark.asyncio
    async def test_cleanup_stale_combats_with_player_service(
        self, combat_service_with_player_service, mock_player_combat_service
    ):
        """Test that cleaning up stale combats also cleans up player combat state."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service_with_player_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Manually set last activity to be stale
        combat.last_activity = datetime.utcnow() - timedelta(minutes=35)

        # Clean up stale combats
        cleaned_count = await combat_service_with_player_service.cleanup_stale_combats()

        assert cleaned_count == 1
        # Verify player combat service cleanup was called
        mock_player_combat_service.handle_combat_end.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_combat_stats(self, combat_service):
        """Test getting combat statistics."""
        # Initially no combats
        stats = await combat_service.get_combat_stats()
        assert stats["active_combats"] == 0
        assert stats["player_combats"] == 0
        assert stats["npc_combats"] == 0

        # Start a combat
        player_id = uuid4()
        npc_id = uuid4()

        await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Check stats after starting combat
        stats = await combat_service.get_combat_stats()
        assert stats["active_combats"] == 1
        assert stats["player_combats"] == 1
        assert stats["npc_combats"] == 1

    @pytest.mark.asyncio
    async def test_calculate_xp_reward_default(self, combat_service):
        """Test default XP reward calculation."""
        npc_id = uuid4()
        xp_reward = await combat_service._calculate_xp_reward(npc_id)

        # Should return a positive integer
        assert isinstance(xp_reward, int)
        assert xp_reward > 0

    @pytest.mark.asyncio
    async def test_calculate_xp_reward_with_player_service(
        self, combat_service_with_player_service, mock_player_combat_service
    ):
        """Test XP reward calculation with player combat service."""
        npc_id = uuid4()
        expected_xp = 10
        mock_player_combat_service.calculate_xp_reward.return_value = expected_xp

        xp_reward = await combat_service_with_player_service._calculate_xp_reward(npc_id)

        assert xp_reward == expected_xp
        mock_player_combat_service.calculate_xp_reward.assert_called_once_with(npc_id)

    def test_combat_service_initialization(self):
        """Test combat service initialization."""
        service = CombatService()

        assert service._active_combats == {}
        assert service._player_combats == {}
        assert service._npc_combats == {}
        assert service._combat_timeout_minutes == 30
        assert service._player_combat_service is None

    def test_combat_service_initialization_with_player_service(self, mock_player_combat_service):
        """Test combat service initialization with player combat service."""
        service = CombatService(player_combat_service=mock_player_combat_service)

        assert service._active_combats == {}
        assert service._player_combats == {}
        assert service._npc_combats == {}
        assert service._combat_timeout_minutes == 30
        assert service._player_combat_service == mock_player_combat_service
