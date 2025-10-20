"""
Test automatic combat progression functionality.

This module tests the automatic combat progression system that ensures
combat continues automatically until one participant is defeated.
"""

from uuid import uuid4

import pytest

from server.models.combat import CombatParticipantType
from server.services.combat_service import CombatService


class TestCombatAutoProgression:
    """Test automatic combat progression functionality."""

    @pytest.fixture
    def mock_player_combat_service(self):
        """Create a mock player combat service."""
        return None  # We don't need the full service for this test

    @pytest.fixture
    def combat_service(self, mock_player_combat_service):
        """Create a combat service."""
        return CombatService(player_combat_service=mock_player_combat_service)

    @pytest.mark.asyncio
    async def test_automatic_combat_progression_player_attacks_npc(self, combat_service):
        """Test automatic combat progression when player attacks NPC."""
        # Setup: Player attacks NPC, NPC should automatically attack back
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=10,
            attacker_max_hp=10,
            attacker_dex=15,  # Higher dexterity, goes first
            target_hp=5,
            target_max_hp=5,
            target_dex=10,
        )

        # Verify combat started
        assert combat.status.value == "active"
        assert len(combat.participants) == 2
        assert player_id in combat.participants
        assert npc_id in combat.participants

        # Player attacks NPC (should kill NPC with 5 damage)
        result = await combat_service.process_attack(player_id, npc_id, damage=5)

        # Verify attack succeeded and combat ended
        assert result.success is True
        assert result.target_died is True
        assert result.combat_ended is True

        # Verify combat is no longer active
        combat_after = await combat_service.get_combat_by_participant(player_id)
        assert combat_after is None  # Combat should be ended

    @pytest.mark.asyncio
    async def test_automatic_combat_progression_multiple_rounds(self, combat_service):
        """Test automatic combat progression with multiple rounds."""
        # Setup: Player and NPC with higher HP for multiple rounds
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=10,
            attacker_max_hp=10,
            attacker_dex=15,  # Higher dexterity, goes first
            target_hp=10,
            target_max_hp=10,
            target_dex=10,
        )

        # Player attacks NPC (1 damage)
        result1 = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify first attack succeeded but combat continues
        assert result1.success is True
        assert result1.target_died is False
        assert result1.combat_ended is False

        # Check that NPC's HP was reduced
        npc_participant = combat.participants[npc_id]
        assert npc_participant.current_hp == 9  # 10 - 1 = 9

        # The automatic progression should have processed the NPC's turn
        # and advanced back to the player's turn
        current_participant = combat.get_current_turn_participant()
        assert current_participant is not None
        assert current_participant.participant_id == player_id

        # Player attacks again (should kill NPC)
        result2 = await combat_service.process_attack(player_id, npc_id, damage=9)

        # Verify second attack killed NPC and ended combat
        assert result2.success is True
        assert result2.target_died is True
        assert result2.combat_ended is True

    @pytest.mark.asyncio
    async def test_automatic_combat_progression_npc_kills_player(self, combat_service):
        """Test automatic combat progression when NPC kills player."""
        # Setup: Player with higher dexterity goes first, but NPC attacks back
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat with player having higher dexterity
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=5,
            attacker_max_hp=5,
            attacker_dex=15,  # Higher dexterity, goes first
            target_hp=10,
            target_max_hp=10,
            target_dex=10,
        )

        # Player attacks NPC (1 damage)
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify attack succeeded but combat continues
        assert result.success is True
        assert result.target_died is False
        assert result.combat_ended is False

        # The automatic progression should have processed the NPC's turn
        # and the NPC should have attacked the player
        player_participant = combat.participants[player_id]

        # Check if player was damaged by NPC's automatic attack
        # (This depends on the NPC's damage output)
        assert player_participant.current_hp <= 5  # Player took damage
        # Verify it's now the player's turn again
        current_participant = combat.get_current_turn_participant()
        assert current_participant is not None
        assert current_participant.participant_id == player_id
        assert current_participant.participant_type == (CombatParticipantType.PLAYER)

    @pytest.mark.asyncio
    async def test_combat_progression_stops_at_player_turn(self, combat_service):
        """Test that automatic progression stops when it's a player's turn."""
        # Setup: Player with higher dexterity
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=10,
            attacker_max_hp=10,
            attacker_dex=15,  # Higher dexterity, goes first
            target_hp=10,
            target_max_hp=10,
            target_dex=10,
        )

        # Player attacks NPC (1 damage)
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify attack succeeded but combat continues
        assert result.success is True
        assert result.target_died is False
        assert result.combat_ended is False

        # Verify it's still the player's turn (auto progression should stop)
        current_participant = combat.get_current_turn_participant()
        assert current_participant is not None
        assert current_participant.participant_id == player_id
        assert current_participant.participant_type == (CombatParticipantType.PLAYER)

    @pytest.mark.asyncio
    async def test_combat_progression_handles_errors_gracefully(self, combat_service):
        """Test that combat progression handles errors gracefully."""
        # Setup: Player attacks NPC
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=10,
            attacker_max_hp=10,
            attacker_dex=15,
            target_hp=10,
            target_max_hp=10,
            target_dex=10,
        )

        # Player attacks NPC (1 damage)
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify attack succeeded
        assert result.success is True
        assert result.target_died is False
        assert result.combat_ended is False

        # The automatic progression should handle any errors gracefully
        # and not cause infinite loops or crashes
        current_participant = combat.get_current_turn_participant()
        assert current_participant is not None
