"""
Integration tests for complete auto-progression combat flow.

This module tests the integration of all auto-progression features:
- Complete auto-progression combat flow
- Auto-progression event system integration
- Auto-progression messaging system integration
- End-to-end auto-progression combat scenarios
"""

from datetime import datetime
from uuid import uuid4

import pytest

from server.models.combat import CombatParticipantType, CombatStatus
from server.services.combat_service import CombatService


class TestAutoProgressionIntegration:
    """Test the complete auto-progression combat system integration."""

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
    async def test_complete_auto_progression_combat_flow(self, combat_service):
        """Test complete auto-progression combat flow from start to end."""
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
            target_hp=8,
            target_max_hp=8,
            target_dex=10,
        )

        # Verify combat started with auto-progression enabled
        assert combat.status == CombatStatus.ACTIVE
        assert combat.auto_progression_enabled is True
        assert combat.turn_interval_seconds == 6

        # Player attacks NPC
        result = await combat_service.process_attack(player_id, npc_id, damage=2)

        # Verify attack succeeded and auto-progression handled NPC turn
        assert result.success is True
        assert result.target_died is False
        assert result.combat_ended is False

        # Verify it's back to player's turn after auto-progression
        current_participant = combat.get_current_turn_participant()
        assert current_participant.participant_type == CombatParticipantType.PLAYER
        assert current_participant.participant_id == player_id

        # Verify health was tracked correctly
        npc_participant = combat.participants[npc_id]
        assert npc_participant.current_hp == 6  # 8 - 2 = 6

    @pytest.mark.asyncio
    async def test_auto_progression_event_system_integration(self, combat_service):
        """Test auto-progression event system integration."""
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

        # Player attacks NPC
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify auto-progression events are processed correctly
        assert result.success is True
        assert result.combat_id == combat.combat_id

        # Verify combat state is maintained through auto-progression
        assert combat.status == CombatStatus.ACTIVE
        assert combat.auto_progression_enabled is True

    @pytest.mark.asyncio
    async def test_auto_progression_messaging_system_integration(self, combat_service):
        """Test auto-progression messaging system integration."""
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

        # Player attacks NPC
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify messaging system integration
        assert result.success is True
        assert result.message is not None

        # Verify combat messaging continues through auto-progression
        assert combat.status == CombatStatus.ACTIVE

    @pytest.mark.asyncio
    async def test_end_to_end_auto_progression_combat_scenario(self, combat_service):
        """Test end-to-end auto-progression combat scenario."""
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
            target_hp=5,
            target_max_hp=8,
            target_dex=10,
        )

        # Multiple rounds of combat with auto-progression
        for _round_num in range(3):
            # Player attacks NPC
            result = await combat_service.process_attack(player_id, npc_id, damage=1)

            # Verify auto-progression handled the round
            assert result.success is True

            # Verify it's back to player's turn
            current_participant = combat.get_current_turn_participant()
            assert current_participant.participant_type == CombatParticipantType.PLAYER

            # Check if combat ended
            if result.combat_ended:
                break

        # Verify NPC health was reduced by attacks
        npc_participant = combat.participants[npc_id]
        assert npc_participant.current_hp < 5  # Started with 5, should be reduced

    @pytest.mark.asyncio
    async def test_auto_progression_with_multiple_combat_rounds(self, combat_service):
        """Test auto-progression across multiple combat rounds."""
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

        # Process multiple rounds
        for _round_num in range(5):
            # Player attacks NPC
            result = await combat_service.process_attack(player_id, npc_id, damage=1)

            # Verify auto-progression handled the round
            assert result.success is True

            # Verify it's back to player's turn
            current_participant = combat.get_current_turn_participant()
            assert current_participant.participant_type == CombatParticipantType.PLAYER

            # Check if combat ended
            if result.combat_ended:
                break

        # Verify NPC health was reduced by attacks (NPCs don't die in passive mode)
        npc_participant = combat.participants[npc_id]
        assert npc_participant.current_hp < 10  # Started with 10, should be reduced

    @pytest.mark.asyncio
    async def test_auto_progression_timing_integration(self, combat_service):
        """Test auto-progression timing integration."""
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

        # Verify timing is set correctly
        assert combat.turn_interval_seconds == 6
        assert combat.next_turn_time is not None

        # Player attacks NPC
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify timing is maintained through auto-progression
        assert result.success is True
        assert combat.next_turn_time is not None

    @pytest.mark.asyncio
    async def test_auto_progression_error_handling_integration(self, combat_service):
        """Test auto-progression error handling integration."""
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

        # Simulate error by corrupting combat state
        combat.turn_order = []

        # Attempt to process attack - should handle error gracefully
        try:
            result = await combat_service.process_attack(player_id, npc_id, damage=1)
            # If no exception is raised, verify the result
            assert result.success is False
        except ValueError as e:
            # Expected error due to corrupted turn order
            assert "not the attacker's turn" in str(e)

    @pytest.mark.asyncio
    async def test_auto_progression_performance_integration(self, combat_service):
        """Test auto-progression performance integration."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        await combat_service.start_combat(
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

        # Measure time for complete auto-progression flow
        start_time = datetime.utcnow()

        # Process multiple rounds with auto-progression
        for _ in range(5):
            result = await combat_service.process_attack(player_id, npc_id, damage=1)
            if result.combat_ended:
                break

        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds()

        # Should complete quickly (under 2 seconds for 5 rounds)
        assert duration < 2.0

    @pytest.mark.asyncio
    async def test_auto_progression_configuration_integration(self, combat_service):
        """Test auto-progression configuration integration."""
        # Test default configuration
        assert combat_service.auto_progression_enabled is True
        assert combat_service.turn_interval_seconds == 6

        # Test configuration changes
        combat_service.turn_interval_seconds = 10
        assert combat_service.turn_interval_seconds == 10

        combat_service.auto_progression_enabled = False
        assert combat_service.auto_progression_enabled is False

        # Test that configuration affects combat
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat with modified configuration
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

        # Verify configuration is applied
        assert combat.auto_progression_enabled is False
        assert combat.turn_interval_seconds == 10
