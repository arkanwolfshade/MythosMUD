"""
Unit tests for combat initialization.

Tests the CombatInitializer class for creating and initializing combat instances.
"""

import uuid

import pytest

from server.models.combat import CombatParticipantType
from server.services.combat_initialization import CombatInitializer
from server.services.combat_types import CombatParticipantData


class TestCombatInitializer:
    """Test suite for CombatInitializer class."""

    @pytest.fixture
    def attacker_data(self):
        """Create attacker participant data."""
        return CombatParticipantData(
            participant_id=uuid.uuid4(),
            name="Player1",
            current_dp=100,
            max_dp=100,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )

    @pytest.fixture
    def target_data(self):
        """Create target participant data."""
        return CombatParticipantData(
            participant_id=uuid.uuid4(),
            name="NPC1",
            current_dp=50,
            max_dp=50,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )

    def test_create_combat_instance_basic(self, attacker_data, target_data):
        """Test create_combat_instance creates basic combat instance."""
        room_id = "room_001"
        current_tick = 100
        combat = CombatInitializer.create_combat_instance(
            room_id=room_id,
            attacker=attacker_data,
            target=target_data,
            current_tick=current_tick,
            auto_progression_enabled=True,
            turn_interval_seconds=6,
        )

        assert combat.room_id == room_id
        assert combat.auto_progression_enabled is True
        assert combat.start_tick == current_tick
        assert combat.last_activity_tick == current_tick
        assert combat.next_turn_tick == current_tick + 6

    def test_create_combat_instance_participants(self, attacker_data, target_data):
        """Test create_combat_instance adds participants correctly."""
        combat = CombatInitializer.create_combat_instance(
            room_id="room_001",
            attacker=attacker_data,
            target=target_data,
            current_tick=100,
            auto_progression_enabled=True,
            turn_interval_seconds=6,
        )

        assert len(combat.participants) == 2
        assert attacker_data.participant_id in combat.participants
        assert target_data.participant_id in combat.participants

        attacker_participant = combat.participants[attacker_data.participant_id]
        assert attacker_participant.name == "Player1"
        assert attacker_participant.current_dp == 100
        assert attacker_participant.max_dp == 100
        assert attacker_participant.dexterity == 15
        assert attacker_participant.participant_type == CombatParticipantType.PLAYER

        target_participant = combat.participants[target_data.participant_id]
        assert target_participant.name == "NPC1"
        assert target_participant.current_dp == 50
        assert target_participant.max_dp == 50
        assert target_participant.dexterity == 10
        assert target_participant.participant_type == CombatParticipantType.NPC

    def test_create_combat_instance_turn_order_higher_dexterity_first(self, attacker_data, target_data):
        """Test create_combat_instance orders turns by dexterity (highest first)."""
        # Attacker has higher dexterity
        attacker_data.dexterity = 20
        target_data.dexterity = 10

        combat = CombatInitializer.create_combat_instance(
            room_id="room_001",
            attacker=attacker_data,
            target=target_data,
            current_tick=100,
            auto_progression_enabled=True,
            turn_interval_seconds=6,
        )

        assert len(combat.turn_order) == 2
        assert combat.turn_order[0] == attacker_data.participant_id
        assert combat.turn_order[1] == target_data.participant_id

    def test_create_combat_instance_turn_order_lower_dexterity_first(self, attacker_data, target_data):
        """Test create_combat_instance orders turns when target has higher dexterity."""
        # Target has higher dexterity
        attacker_data.dexterity = 10
        target_data.dexterity = 20

        combat = CombatInitializer.create_combat_instance(
            room_id="room_001",
            attacker=attacker_data,
            target=target_data,
            current_tick=100,
            auto_progression_enabled=True,
            turn_interval_seconds=6,
        )

        assert len(combat.turn_order) == 2
        assert combat.turn_order[0] == target_data.participant_id
        assert combat.turn_order[1] == attacker_data.participant_id

    def test_create_combat_instance_turn_order_equal_dexterity(self, attacker_data, target_data):
        """Test create_combat_instance handles equal dexterity."""
        attacker_data.dexterity = 15
        target_data.dexterity = 15

        combat = CombatInitializer.create_combat_instance(
            room_id="room_001",
            attacker=attacker_data,
            target=target_data,
            current_tick=100,
            auto_progression_enabled=True,
            turn_interval_seconds=6,
        )

        assert len(combat.turn_order) == 2
        # Order should be deterministic (attacker first due to sort order)
        assert attacker_data.participant_id in combat.turn_order
        assert target_data.participant_id in combat.turn_order

    def test_create_combat_instance_auto_progression_disabled(self, attacker_data, target_data):
        """Test create_combat_instance with auto-progression disabled."""
        combat = CombatInitializer.create_combat_instance(
            room_id="room_001",
            attacker=attacker_data,
            target=target_data,
            current_tick=100,
            auto_progression_enabled=False,
            turn_interval_seconds=6,
        )

        assert combat.auto_progression_enabled is False

    def test_create_combat_instance_different_turn_interval(self, attacker_data, target_data):
        """Test create_combat_instance with different turn interval."""
        current_tick = 100
        turn_interval = 10
        combat = CombatInitializer.create_combat_instance(
            room_id="room_001",
            attacker=attacker_data,
            target=target_data,
            current_tick=current_tick,
            auto_progression_enabled=True,
            turn_interval_seconds=turn_interval,
        )

        assert combat.turn_interval_ticks == turn_interval
        assert combat.next_turn_tick == current_tick + turn_interval

    def test_create_combat_instance_damaged_participants(self, attacker_data, target_data):
        """Test create_combat_instance with damaged participants."""
        attacker_data.current_dp = 75  # Damaged
        target_data.current_dp = 30  # Damaged

        combat = CombatInitializer.create_combat_instance(
            room_id="room_001",
            attacker=attacker_data,
            target=target_data,
            current_tick=100,
            auto_progression_enabled=True,
            turn_interval_seconds=6,
        )

        attacker_participant = combat.participants[attacker_data.participant_id]
        assert attacker_participant.current_dp == 75
        assert attacker_participant.max_dp == 100

        target_participant = combat.participants[target_data.participant_id]
        assert target_participant.current_dp == 30
        assert target_participant.max_dp == 50

    def test_create_combat_instance_zero_tick(self, attacker_data, target_data):
        """Test create_combat_instance with zero tick."""
        combat = CombatInitializer.create_combat_instance(
            room_id="room_001",
            attacker=attacker_data,
            target=target_data,
            current_tick=0,
            auto_progression_enabled=True,
            turn_interval_seconds=6,
        )

        assert combat.start_tick == 0
        assert combat.last_activity_tick == 0
        assert combat.next_turn_tick == 6
