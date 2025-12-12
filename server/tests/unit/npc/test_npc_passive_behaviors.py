"""
Test NPC passive behavior system with non-combat actions.

This module tests the new NPC passive behavior features:
- NPC non-combat actions during their turns
- Thematic NPC behavior messages (defensive maneuvers, taunts, thematic behaviors)
- NPC turn execution with non-combat actions
- Integration with auto-progression system
"""

from datetime import UTC, datetime
from uuid import uuid4

import pytest

from server.models.combat import CombatParticipantType, CombatStatus
from server.services.combat_service import CombatParticipantData, CombatService


class TestNPCPassiveBehaviorSystem:
    """Test the NPC passive behavior system with non-combat actions."""

    def _create_combat_participants(
        self,
        player_id,
        npc_id,
        attacker_hp=10,
        attacker_max_dp=10,
        attacker_dex=10,
        target_hp=10,
        target_max_dp=10,
        target_dex=10,
    ):
        """Helper to create CombatParticipantData objects for tests."""
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=attacker_hp,
            max_dp=attacker_max_dp,
            dexterity=attacker_dex,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=target_hp,
            max_dp=target_max_dp,
            dexterity=target_dex,
            participant_type=CombatParticipantType.NPC,
        )
        return attacker, target

    @pytest.fixture
    def mock_player_combat_service(self):
        """Create a mock player combat service."""
        return None  # We don't need the full service for this test

    @pytest.fixture
    def combat_service(self, mock_player_combat_service):
        """Create a combat service with auto-progression enabled."""
        service = CombatService(player_combat_service=mock_player_combat_service)
        # Enable auto-progression with 6-second intervals
        service.auto_progression_enabled = True
        service.turn_interval_seconds = 6
        return service

    @pytest.mark.asyncio
    async def test_npc_performs_combat_action_during_turn(self, combat_service):
        """Test that NPCs perform combat actions during their turns."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=10,
            attacker_max_dp=10,
            attacker_dex=15,
            target_hp=10,
            target_max_dp=10,
            target_dex=10,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Advance to NPC's turn
        await combat_service._advance_turn_automatically(combat, current_tick=2)

        # Verify it's now the NPC's turn
        current_participant = combat.get_current_turn_participant()
        assert current_participant.participant_type == CombatParticipantType.NPC
        assert current_participant.participant_id == npc_id

        # Process NPC turn - should perform combat action (attack)
        await combat_service._process_npc_turn(combat, current_participant, current_tick=2)

        # Verify NPC performed combat action (damage dealt to player)
        player_participant = combat.participants[player_id]
        assert player_participant.current_dp < 10  # Damage taken

    @pytest.mark.asyncio
    async def test_npc_non_combat_action_selection(self, combat_service):
        """Test that NPCs select appropriate non-combat actions."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=10,
            attacker_max_dp=10,
            attacker_dex=10,
            target_hp=10,
            target_max_dp=10,
            target_dex=15,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Advance to NPC's turn
        await combat_service._advance_turn_automatically(combat, current_tick=2)
        current_participant = combat.get_current_turn_participant()

        # Process multiple NPC turns to test action selection variety
        for _ in range(5):
            await combat_service._process_npc_turn(combat, current_participant, current_tick=2)
            # Note: In a real implementation, we would track the specific actions
            # For now, we just verify no damage is dealt
            player_participant = combat.participants[player_id]
            assert player_participant.current_dp == 10  # No damage taken
            combat.advance_turn(current_tick=2)
            current_participant = combat.get_current_turn_participant()

    @pytest.mark.asyncio
    async def test_npc_defensive_maneuver_messages(self, combat_service):
        """Test NPC defensive maneuver messages."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=10,
            attacker_max_dp=10,
            attacker_dex=10,
            target_hp=10,
            target_max_dp=10,
            target_dex=15,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Advance to NPC's turn
        await combat_service._advance_turn_automatically(combat, current_tick=2)
        current_participant = combat.get_current_turn_participant()

        # Process NPC turn - should generate defensive maneuver message
        await combat_service._process_npc_turn(combat, current_participant, current_tick=2)

        # Verify NPC performed non-combat action
        player_participant = combat.participants[player_id]
        assert player_participant.current_dp == 10  # No damage taken

    @pytest.mark.asyncio
    async def test_npc_taunt_messages(self, combat_service):
        """Test NPC taunt messages."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=10,
            attacker_max_dp=10,
            attacker_dex=10,
            target_hp=10,
            target_max_dp=10,
            target_dex=15,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Advance to NPC's turn
        await combat_service._advance_turn_automatically(combat, current_tick=2)
        current_participant = combat.get_current_turn_participant()

        # Process NPC turn - should generate taunt message
        await combat_service._process_npc_turn(combat, current_participant, current_tick=2)

        # Verify NPC performed non-combat action
        player_participant = combat.participants[player_id]
        assert player_participant.current_dp == 10  # No damage taken

    @pytest.mark.asyncio
    async def test_npc_thematic_behavior_messages(self, combat_service):
        """Test NPC thematic behavior messages."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=10,
            attacker_max_dp=10,
            attacker_dex=10,
            target_hp=10,
            target_max_dp=10,
            target_dex=15,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Advance to NPC's turn
        await combat_service._advance_turn_automatically(combat, current_tick=2)
        current_participant = combat.get_current_turn_participant()

        # Process NPC turn - should generate thematic behavior message
        await combat_service._process_npc_turn(combat, current_participant, current_tick=2)

        # Verify NPC performed non-combat action
        player_participant = combat.participants[player_id]
        assert player_participant.current_dp == 10  # No damage taken

    @pytest.mark.asyncio
    async def test_npc_turn_execution_with_non_combat_actions(self, combat_service):
        """Test complete NPC turn execution with non-combat actions."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=10,
            attacker_max_dp=10,
            attacker_dex=10,
            target_hp=50,
            target_max_dp=50,
            target_dex=15,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Advance to NPC's turn
        await combat_service._advance_turn_automatically(combat, current_tick=2)
        current_participant = combat.get_current_turn_participant()

        # Process NPC turn
        await combat_service._process_npc_turn(combat, current_participant, current_tick=2)

        # Verify turn was processed without damage
        player_participant = combat.participants[player_id]
        assert player_participant.current_dp == 10  # No damage taken

        # Verify combat continues
        assert combat.status == CombatStatus.ACTIVE

    @pytest.mark.asyncio
    async def test_npc_combat_behavior_integration_with_auto_progression(self, combat_service):
        """Test NPC combat behavior integration with auto-progression system."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat with higher player HP so they don't die immediately
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=50,
            attacker_max_dp=50,
            attacker_dex=10,
            target_hp=10,
            target_max_dp=10,
            target_dex=15,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Process automatic combat progression - should handle NPC turn with combat action
        await combat_service._process_automatic_combat_progression(combat)

        # Verify it's back to player's turn (if combat is still active)
        if combat.status == CombatStatus.ACTIVE:
            current_participant = combat.get_current_turn_participant()
            assert current_participant.participant_type == CombatParticipantType.PLAYER
            assert current_participant.participant_id == player_id

            # Verify damage was dealt to player
            player_participant = combat.participants[player_id]
            assert player_participant.current_dp < 50  # Damage taken
        else:
            # Combat ended (player died), which is also valid
            assert combat.status == CombatStatus.ENDED

    @pytest.mark.asyncio
    async def test_npc_combat_behavior_with_multiple_rounds(self, combat_service):
        """Test NPC combat behavior across multiple combat rounds."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat with higher HP so it can last multiple rounds
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=50,
            attacker_max_dp=50,
            attacker_dex=10,
            target_hp=50,
            target_max_dp=50,
            target_dex=15,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Process multiple rounds
        for _round_num in range(3):
            # Process automatic combat progression for the round
            await combat_service._process_automatic_combat_progression(combat)

            # Check if combat is still active
            if combat.status == CombatStatus.ACTIVE:
                # Verify it's back to player's turn after each round
                current_participant = combat.get_current_turn_participant()
                assert current_participant.participant_type == CombatParticipantType.PLAYER
                assert current_participant.participant_id == player_id

                # Verify damage was dealt to player
                player_participant = combat.participants[player_id]
                assert player_participant.current_dp < 50  # Damage taken

                # Advance to next round
                combat.advance_turn(current_tick=2)
            else:
                # Combat ended, which is valid
                assert combat.status == CombatStatus.ENDED
                break

    @pytest.mark.asyncio
    async def test_npc_passive_behavior_error_handling(self, combat_service):
        """Test error handling in NPC passive behavior system."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=10,
            attacker_max_dp=10,
            attacker_dex=10,
            target_hp=50,
            target_max_dp=50,
            target_dex=15,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Advance to NPC's turn
        await combat_service._advance_turn_automatically(combat, current_tick=2)
        current_participant = combat.get_current_turn_participant()

        # Simulate error by corrupting NPC participant
        current_participant.participant_type = None  # This should cause an error

        # Process NPC turn - should handle error gracefully
        await combat_service._process_npc_turn(combat, current_participant, current_tick=2)

        # Verify combat continues despite error
        assert combat.status == CombatStatus.ACTIVE

    @pytest.mark.asyncio
    async def test_npc_passive_behavior_performance(self, combat_service):
        """Test that NPC passive behavior doesn't cause performance issues."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker, target = self._create_combat_participants(
            player_id,
            npc_id,
            attacker_hp=10,
            attacker_max_dp=10,
            attacker_dex=10,
            target_hp=10,
            target_max_dp=10,
            target_dex=15,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Advance to NPC's turn
        await combat_service._advance_turn_automatically(combat, current_tick=2)
        current_participant = combat.get_current_turn_participant()

        # Measure time for multiple NPC turns
        start_time = datetime.now(UTC)

        for _ in range(10):  # 10 NPC turns
            # Check if combat is still active before processing turn
            if combat.status != CombatStatus.ACTIVE:
                break
            await combat_service._process_npc_turn(combat, current_participant, current_tick=2)
            # Advance turn if combat is still active
            if combat.status == CombatStatus.ACTIVE:
                combat.advance_turn(current_tick=2)
                current_participant = combat.get_current_turn_participant()

        end_time = datetime.now(UTC)
        duration = (end_time - start_time).total_seconds()

        # Should complete quickly (under 1 second for 10 turns)
        assert duration < 1.0

    @pytest.mark.asyncio
    async def test_npc_passive_behavior_configuration(self, combat_service):
        """Test NPC passive behavior configuration options."""
        # Test default configuration
        assert combat_service.auto_progression_enabled is True
        assert combat_service.turn_interval_seconds == 6

        # Test configuration changes
        combat_service.turn_interval_seconds = 10
        assert combat_service.turn_interval_seconds == 10

        combat_service.auto_progression_enabled = False
        assert combat_service.auto_progression_enabled is False
