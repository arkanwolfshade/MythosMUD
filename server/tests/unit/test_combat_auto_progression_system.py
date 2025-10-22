"""
Test automatic combat progression system with 6-second intervals.

This module tests the new auto-progression features:
- Automatic combat round progression every 6 seconds
- Turn timing and scheduling system
- Combat round management with automatic advancement
- Integration with existing combat system
"""

from datetime import datetime, timedelta
from uuid import uuid4

import pytest

from server.models.combat import CombatParticipantType, CombatStatus
from server.services.combat_service import CombatService


class TestCombatAutoProgressionSystem:
    """Test the automatic combat progression system with timing."""

    @pytest.fixture
    def mock_player_combat_service(self):
        """Create a mock player combat service."""
        return None  # We don't need the full service for this test

    @pytest.fixture
    def combat_service(self, mock_player_combat_service):
        """Create a combat service with auto-progression enabled."""
        service = CombatService(player_combat_service=mock_player_combat_service)
        # Enable auto-progression with 6-second intervals
        service._auto_progression_enabled = True
        service._turn_interval_seconds = 6
        return service

    @pytest.mark.asyncio
    async def test_combat_starts_with_auto_progression_enabled(self, combat_service):
        """Test that combat starts with auto-progression enabled."""
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
            current_tick=1,
        )

        # Verify combat started with auto-progression enabled
        assert combat.status == CombatStatus.ACTIVE
        assert hasattr(combat, "auto_progression_enabled")
        assert combat.auto_progression_enabled is True
        assert hasattr(combat, "turn_interval_ticks")
        assert combat.turn_interval_ticks == 6
        assert hasattr(combat, "next_turn_tick")

    @pytest.mark.asyncio
    async def test_automatic_turn_progression_with_timing(self, combat_service):
        """Test automatic turn progression with 6-second intervals."""
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
            current_tick=1,
        )

        # Verify initial state
        assert combat.current_turn == 0
        assert combat.combat_round == 0
        current_participant = combat.get_current_turn_participant()
        assert current_participant.participant_id == player_id

        # Simulate automatic turn progression after 6 seconds
        await combat_service._advance_turn_automatically(combat, current_tick=2)

        # Verify turn advanced
        assert combat.current_turn == 1
        assert combat.combat_round == 0
        current_participant = combat.get_current_turn_participant()
        assert current_participant.participant_id == npc_id

    @pytest.mark.asyncio
    async def test_combat_round_advancement_after_full_round(self, combat_service):
        """Test that combat rounds advance after all participants have acted."""
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
            current_tick=1,
        )

        # Verify initial state
        assert combat.current_turn == 0
        assert combat.combat_round == 0

        # Advance through all turns (2 participants = 2 turns per round)
        await combat_service._advance_turn_automatically(combat, current_tick=2)  # Turn 1 (NPC)
        assert combat.current_turn == 1
        assert combat.combat_round == 0

        await combat_service._advance_turn_automatically(combat, current_tick=2)  # Turn 0 (Player) - next round
        assert combat.current_turn == 0
        assert combat.combat_round == 1

    @pytest.mark.asyncio
    async def test_turn_timing_and_scheduling(self, combat_service):
        """Test turn timing and scheduling system."""
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
            current_tick=1,
        )

        # Verify initial timing
        assert hasattr(combat, "next_turn_tick")
        assert combat.next_turn_tick is not None

        # Verify next turn tick is set to 6 ticks from now
        expected_tick = 1 + 6  # current_tick (1) + turn_interval_ticks (6)
        assert combat.next_turn_tick == expected_tick

    @pytest.mark.asyncio
    async def test_automatic_combat_progression_stops_at_player_turn(self, combat_service):
        """Test that automatic progression stops when it's a player's turn."""
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
            current_tick=1,
        )

        # Player's turn - automatic progression should stop
        current_participant = combat.get_current_turn_participant()
        assert current_participant.participant_type == CombatParticipantType.PLAYER

        # Attempt automatic progression - should not advance past player turn
        await combat_service._process_automatic_combat_progression(combat)

        # Verify it's still the player's turn
        current_participant = combat.get_current_turn_participant()
        assert current_participant.participant_type == CombatParticipantType.PLAYER
        assert current_participant.participant_id == player_id

    @pytest.mark.asyncio
    async def test_automatic_combat_progression_processes_npc_turns(self, combat_service):
        """Test that automatic progression processes NPC turns."""
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
            current_tick=1,
        )

        # Advance to NPC's turn
        await combat_service._advance_turn_automatically(combat, current_tick=2)

        # Verify it's now the NPC's turn
        current_participant = combat.get_current_turn_participant()
        assert current_participant.participant_type == CombatParticipantType.NPC
        assert current_participant.participant_id == npc_id

        # Process automatic progression - should handle NPC turn
        await combat_service._process_automatic_combat_progression(combat)

        # Verify turn advanced back to player
        current_participant = combat.get_current_turn_participant()
        assert current_participant.participant_type == CombatParticipantType.PLAYER
        assert current_participant.participant_id == player_id

    @pytest.mark.asyncio
    async def test_combat_timeout_with_auto_progression(self, combat_service):
        """Test combat timeout handling with auto-progression."""
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
            current_tick=1,
        )

        # Simulate timeout by setting last activity to past
        combat.last_activity = datetime.utcnow() - timedelta(minutes=31)

        # Cleanup should end the combat
        cleaned_up = await combat_service.cleanup_stale_combats()
        assert cleaned_up == 1

        # Verify combat is ended
        combat_after = await combat_service.get_combat_by_participant(player_id)
        assert combat_after is None

    @pytest.mark.asyncio
    async def test_auto_progression_integration_with_existing_system(self, combat_service):
        """Test that auto-progression integrates with existing combat system."""
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
            current_tick=1,
        )

        # Player attacks
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify attack succeeded
        assert result.success is True
        assert result.target_died is False
        assert result.combat_ended is False

        # Verify auto-progression handled NPC turn and advanced back to player
        current_participant = combat.get_current_turn_participant()
        assert current_participant.participant_type == CombatParticipantType.PLAYER
        assert current_participant.participant_id == player_id

    @pytest.mark.asyncio
    async def test_combat_auto_progression_error_handling(self, combat_service):
        """Test error handling in auto-progression system."""
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
            current_tick=1,
        )

        # Simulate error by corrupting combat state
        combat.turn_order = []  # This should cause an error

        # Auto-progression should handle error gracefully
        await combat_service._process_automatic_combat_progression(combat)

        # Combat should be ended due to error
        combat_after = await combat_service.get_combat_by_participant(player_id)
        assert combat_after is None

    @pytest.mark.asyncio
    async def test_auto_progression_configuration(self, combat_service):
        """Test auto-progression configuration options."""
        # Test default configuration
        assert combat_service._auto_progression_enabled is True
        assert combat_service._turn_interval_seconds == 6

        # Test configuration changes
        combat_service._turn_interval_seconds = 10
        assert combat_service._turn_interval_seconds == 10

        combat_service._auto_progression_enabled = False
        assert combat_service._auto_progression_enabled is False

    @pytest.mark.asyncio
    async def test_combat_progression_performance(self, combat_service):
        """Test that auto-progression doesn't cause performance issues."""
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
            current_tick=1,
        )

        # Measure time for multiple turn progressions
        start_time = datetime.utcnow()

        for _ in range(10):  # 10 turn progressions
            await combat_service._advance_turn_automatically(combat, current_tick=2)

        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds()

        # Should complete quickly (under 1 second for 10 progressions)
        assert duration < 1.0
