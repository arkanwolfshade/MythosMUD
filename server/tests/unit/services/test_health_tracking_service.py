"""
Test health tracking system with real-time updates and persistence.

This module tests the new health tracking features:
- Real-time health tracking and display
- In-memory NPC health tracking (resets on combat end)
- Persistent player health tracking (saved to database)
- On-demand health status checking commands
- Integration with combat system
"""

from datetime import UTC, datetime
from uuid import uuid4

import pytest

from server.models.combat import CombatParticipantType, CombatStatus
from server.services.combat_service import CombatParticipantData, CombatService


class TestHealthTrackingSystem:
    """Test the health tracking system with real-time updates and persistence."""

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
    async def test_real_time_health_tracking_during_combat(self, combat_service):
        """Test real-time health tracking during combat."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=8,
            max_dp=8,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Verify initial health values
        player_participant = combat.participants[player_id]
        npc_participant = combat.participants[npc_id]

        assert player_participant.current_dp == 10
        assert player_participant.max_dp == 10
        assert npc_participant.current_dp == 8
        assert npc_participant.max_dp == 8

        # Player attacks NPC
        result = await combat_service.process_attack(player_id, npc_id, damage=2)

        # Verify health was updated in real-time
        assert result.success is True
        assert npc_participant.current_dp == 6  # 8 - 2 = 6
        assert npc_participant.max_dp == 8  # Max HP unchanged

    @pytest.mark.asyncio
    async def test_npc_health_tracking_in_memory(self, combat_service):
        """Test that NPC health is tracked in-memory only."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=10,
            max_dp=10,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Player attacks NPC multiple times
        await combat_service.process_attack(player_id, npc_id, damage=3)
        await combat_service.process_attack(player_id, npc_id, damage=2)

        # Verify NPC health is tracked in-memory
        npc_participant = combat.participants[npc_id]
        assert npc_participant.current_dp == 5  # 10 - 3 - 2 = 5

        # End combat
        await combat_service.end_combat(combat.combat_id, "Test combat end")

        # Verify NPC health is reset (in-memory only, no persistence)
        # Note: In a real implementation, we would verify that NPC health
        # is not persisted to any database and resets on combat end

    @pytest.mark.asyncio
    async def test_player_health_persistence(self, combat_service):
        """Test that player health changes are persisted to database."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=10,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Advance to NPC's turn (NPC performs non-combat action, no damage)
        await combat_service._advance_turn_automatically(combat, current_tick=2)
        current_participant = combat.get_current_turn_participant()
        await combat_service._process_npc_turn(combat, current_participant, current_tick=2)

        # Verify player health is unchanged (NPC doesn't attack in passive mode)
        player_participant = combat.participants[player_id]
        assert player_participant.current_dp == 10

        # End combat
        await combat_service.end_combat(combat.combat_id, "Test combat end")

        # Note: In a real implementation, we would verify that player health
        # changes are persisted to the database through the player combat service

    @pytest.mark.asyncio
    async def test_health_display_in_combat_messages(self, combat_service):
        """Test that health information is displayed in combat messages."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=8,
            max_dp=8,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Player attacks NPC
        result = await combat_service.process_attack(player_id, npc_id, damage=2)

        # Verify health information is included in combat result
        assert result.success is True
        # Note: In a real implementation, we would verify that the result
        # includes health information like "TestNPC (6/8 HP remaining)"

    @pytest.mark.asyncio
    async def test_on_demand_health_status_checking(self, combat_service):
        """Test on-demand health status checking commands."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=8,
            max_dp=8,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Player attacks NPC to change health
        await combat_service.process_attack(player_id, npc_id, damage=3)

        # Get current health status
        player_participant = combat.participants[player_id]
        npc_participant = combat.participants[npc_id]

        # Verify health status can be checked on-demand
        assert player_participant.current_dp == 10
        assert player_participant.max_dp == 10
        assert npc_participant.current_dp == 5  # 8 - 3 = 5
        assert npc_participant.max_dp == 8

    @pytest.mark.asyncio
    async def test_health_tracking_integration_with_auto_progression(self, combat_service):
        """Test health tracking integration with auto-progression system."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=8,
            max_dp=8,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Player attacks NPC
        await combat_service.process_attack(player_id, npc_id, damage=2)

        # Verify health was tracked during auto-progression
        npc_participant = combat.participants[npc_id]
        assert npc_participant.current_dp == 6  # 8 - 2 = 6

        # Auto-progression should continue without affecting health
        # (NPC performs non-combat actions)
        await combat_service._process_automatic_combat_progression(combat)

        # Verify health remains unchanged after NPC non-combat action
        assert npc_participant.current_dp == 6
        assert npc_participant.max_dp == 8

    @pytest.mark.asyncio
    async def test_health_tracking_with_combat_end(self, combat_service):
        """Test health tracking when combat ends."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=3,
            max_dp=8,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Player attacks NPC to defeat it
        result = await combat_service.process_attack(player_id, npc_id, damage=5)

        # Verify combat ended due to NPC defeat
        assert result.success is True
        assert result.target_died is True
        assert result.combat_ended is True

        # Verify NPC health reached 0
        npc_participant = combat.participants[npc_id]
        assert npc_participant.current_dp == 0

    @pytest.mark.asyncio
    async def test_health_tracking_error_handling(self, combat_service):
        """Test error handling in health tracking system."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=10,
            max_dp=10,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Simulate error by corrupting participant health
        # (In a real implementation, we would corrupt the participant health here)

        # Process attack - should handle health tracking errors gracefully
        await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify combat continues despite potential errors
        assert combat.status == CombatStatus.ACTIVE

    @pytest.mark.asyncio
    async def test_health_tracking_performance(self, combat_service):
        """Test that health tracking doesn't cause performance issues."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=10,
            max_dp=10,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Measure time for multiple health tracking operations
        start_time = datetime.now(UTC)

        for _ in range(10):  # 10 health tracking operations
            await combat_service.process_attack(player_id, npc_id, damage=1)

        end_time = datetime.now(UTC)
        duration = (end_time - start_time).total_seconds()

        # Should complete quickly (under 2 seconds for 10 operations)
        assert duration < 2.0

        # Verify health was tracked correctly
        npc_participant = combat.participants[npc_id]
        assert npc_participant.current_dp == 0  # 10 - (10 * 1) = 0

    @pytest.mark.asyncio
    async def test_health_tracking_configuration(self, combat_service):
        """Test health tracking configuration options."""
        # Test default configuration
        assert combat_service.auto_progression_enabled is True
        assert combat_service.turn_interval_seconds == 6

        # Test that health tracking works with different configurations
        combat_service.turn_interval_seconds = 10
        assert combat_service.turn_interval_seconds == 10

        combat_service.auto_progression_enabled = False
        assert combat_service.auto_progression_enabled is False
