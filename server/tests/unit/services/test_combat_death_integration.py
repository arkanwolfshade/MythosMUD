"""Tests for combat service death mechanics integration."""

from uuid import uuid4

import pytest

from server.models.combat import CombatParticipantType, CombatStatus
from server.services.combat_service import CombatService


@pytest.fixture
def combat_service():
    """Create a combat service for testing."""
    return CombatService()


class TestCombatDeathIntegration:
    """Test suite for combat service death mechanics integration."""

    @pytest.mark.asyncio
    async def test_player_hp_capped_at_minus_ten(self, combat_service):
        """Test that player HP is capped at -10 when taking damage."""
        attacker_id = uuid4()
        target_id = uuid4()

        # Start combat with player as target
        combat = await combat_service.start_combat(
            room_id="test-room",
            attacker_id=attacker_id,
            target_id=target_id,
            attacker_name="Beast",
            target_name="Player",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=10,
            target_hp=5,  # Low HP - will go negative
            target_max_hp=100,
            target_dex=10,
            current_tick=0,
            attacker_type=CombatParticipantType.NPC,
            target_type=CombatParticipantType.PLAYER,
        )

        # Process attack that would drop player to -20 HP
        result = await combat_service.process_attack(attacker_id, target_id, damage=25, is_initial_attack=True)

        # Verify HP is capped at -10
        target = combat.participants[target_id]
        assert target.current_hp == -10
        assert result.success is True

    @pytest.mark.asyncio
    async def test_npc_hp_capped_at_zero(self, combat_service):
        """Test that NPC HP is capped at 0 (not negative)."""
        attacker_id = uuid4()
        target_id = uuid4()

        # Start combat with NPC as target
        combat = await combat_service.start_combat(
            room_id="test-room",
            attacker_id=attacker_id,
            target_id=target_id,
            attacker_name="Player",
            target_name="Beast",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=10,
            target_hp=5,  # Low HP
            target_max_hp=100,
            target_dex=10,
            current_tick=0,
            attacker_type=CombatParticipantType.PLAYER,
            target_type=CombatParticipantType.NPC,
        )

        # Process attack that would drop NPC to negative HP
        result = await combat_service.process_attack(attacker_id, target_id, damage=20, is_initial_attack=True)

        # Verify NPC HP is capped at 0
        target = combat.participants[target_id]
        assert target.current_hp == 0
        assert result.target_died is True

    @pytest.mark.asyncio
    async def test_detect_player_mortally_wounded_at_zero_hp(self, combat_service):
        """Test detection of mortally wounded state when player HP reaches 0."""
        attacker_id = uuid4()
        target_id = uuid4()

        # Start combat with player at low HP
        combat = await combat_service.start_combat(
            room_id="test-room",
            attacker_id=attacker_id,
            target_id=target_id,
            attacker_name="Beast",
            target_name="Player",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=10,
            target_hp=10,  # Will reach exactly 0 HP
            target_max_hp=100,
            target_dex=10,
            current_tick=0,
            attacker_type=CombatParticipantType.NPC,
            target_type=CombatParticipantType.PLAYER,
        )

        # Process attack that brings player to exactly 0 HP
        result = await combat_service.process_attack(attacker_id, target_id, damage=10, is_initial_attack=True)

        # Verify player is mortally wounded (HP = 0)
        target = combat.participants[target_id]
        assert target.current_hp == 0
        # Combat should NOT end for mortally wounded (only at -10)
        assert result.combat_ended is False

    @pytest.mark.asyncio
    async def test_detect_player_death_at_minus_ten_hp(self, combat_service):
        """Test detection of death state when player HP reaches -10."""
        attacker_id = uuid4()
        target_id = uuid4()

        # Start combat with player at critical HP
        combat = await combat_service.start_combat(
            room_id="test-room",
            attacker_id=attacker_id,
            target_id=target_id,
            attacker_name="Beast",
            target_name="Player",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=10,
            target_hp=5,  # Will go to -10 HP
            target_max_hp=100,
            target_dex=10,
            current_tick=0,
            attacker_type=CombatParticipantType.NPC,
            target_type=CombatParticipantType.PLAYER,
        )

        # Process attack that brings player to -10 HP
        result = await combat_service.process_attack(attacker_id, target_id, damage=15, is_initial_attack=True)

        # Verify player is dead (HP = -10)
        target = combat.participants[target_id]
        assert target.current_hp == -10
        # Combat SHOULD end when player dies
        assert result.combat_ended is True
        assert result.target_died is True

    @pytest.mark.asyncio
    async def test_multiple_players_one_dies_combat_continues(self, combat_service):
        """Test that combat continues when one player dies but others remain."""
        # This test will be implemented when multi-player combat is supported
        # For now, we're testing single player vs NPC combat
        # In future: NPC has threat queue, one player dies (removed), others continue
        pytest.skip("Multi-player threat queue not yet implemented")

    @pytest.mark.asyncio
    async def test_dead_player_removed_from_combat(self, combat_service):
        """Test that dead players are properly removed from combat."""
        attacker_id = uuid4()
        target_id = uuid4()

        # Start combat
        combat = await combat_service.start_combat(
            room_id="test-room",
            attacker_id=attacker_id,
            target_id=target_id,
            attacker_name="Beast",
            target_name="Player",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=10,
            target_hp=5,
            target_max_hp=100,
            target_dex=10,
            current_tick=0,
            attacker_type=CombatParticipantType.NPC,
            target_type=CombatParticipantType.PLAYER,
        )

        # Kill the player
        await combat_service.process_attack(attacker_id, target_id, damage=15, is_initial_attack=True)

        # Verify combat ended and player was removed
        assert combat.status == CombatStatus.ENDED
        # Verify player is no longer tracked in combat
        assert target_id not in combat_service._player_combats
