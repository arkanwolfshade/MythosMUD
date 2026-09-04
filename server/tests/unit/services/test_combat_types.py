"""
Unit tests for combat type definitions.

Tests the CombatParticipantData dataclass used across combat services.
"""

import uuid

from server.models.combat import CombatParticipantType
from server.services.combat_types import CombatParticipantData


class TestCombatParticipantData:
    """Test suite for CombatParticipantData dataclass."""

    def test_combat_participant_data_creation(self):
        """Test CombatParticipantData can be created with required fields."""
        participant_id = uuid.uuid4()
        data = CombatParticipantData(
            participant_id=participant_id,
            name="TestPlayer",
            current_dp=50,
            max_dp=100,
            dexterity=10,
        )
        assert data.participant_id == participant_id
        assert data.name == "TestPlayer"
        assert data.current_dp == 50
        assert data.max_dp == 100
        assert data.dexterity == 10
        assert data.participant_type == CombatParticipantType.PLAYER

    def test_combat_participant_data_with_participant_type(self):
        """Test CombatParticipantData with explicit participant type."""
        participant_id = uuid.uuid4()
        data = CombatParticipantData(
            participant_id=participant_id,
            name="TestNPC",
            current_dp=30,
            max_dp=60,
            dexterity=8,
            participant_type=CombatParticipantType.NPC,
        )
        assert data.participant_type == CombatParticipantType.NPC

    def test_combat_participant_data_default_participant_type(self):
        """Test CombatParticipantData defaults to PLAYER type."""
        participant_id = uuid.uuid4()
        data = CombatParticipantData(
            participant_id=participant_id,
            name="TestPlayer",
            current_dp=50,
            max_dp=100,
            dexterity=10,
        )
        assert data.participant_type == CombatParticipantType.PLAYER

    def test_combat_participant_data_equality(self):
        """Test CombatParticipantData equality comparison."""
        participant_id = uuid.uuid4()
        data1 = CombatParticipantData(
            participant_id=participant_id,
            name="TestPlayer",
            current_dp=50,
            max_dp=100,
            dexterity=10,
        )
        data2 = CombatParticipantData(
            participant_id=participant_id,
            name="TestPlayer",
            current_dp=50,
            max_dp=100,
            dexterity=10,
        )
        assert data1 == data2

    def test_combat_participant_data_inequality(self):
        """Test CombatParticipantData inequality comparison."""
        participant_id1 = uuid.uuid4()
        participant_id2 = uuid.uuid4()
        data1 = CombatParticipantData(
            participant_id=participant_id1,
            name="TestPlayer1",
            current_dp=50,
            max_dp=100,
            dexterity=10,
        )
        data2 = CombatParticipantData(
            participant_id=participant_id2,
            name="TestPlayer2",
            current_dp=50,
            max_dp=100,
            dexterity=10,
        )
        assert data1 != data2

    def test_combat_participant_data_with_zero_dp(self):
        """Test CombatParticipantData with zero determination points."""
        participant_id = uuid.uuid4()
        data = CombatParticipantData(
            participant_id=participant_id,
            name="DefeatedPlayer",
            current_dp=0,
            max_dp=100,
            dexterity=10,
        )
        assert data.current_dp == 0
        assert data.max_dp == 100

    def test_combat_participant_data_with_high_values(self):
        """Test CombatParticipantData with high stat values."""
        participant_id = uuid.uuid4()
        data = CombatParticipantData(
            participant_id=participant_id,
            name="PowerfulPlayer",
            current_dp=999,
            max_dp=1000,
            dexterity=99,
        )
        assert data.current_dp == 999
        assert data.max_dp == 1000
        assert data.dexterity == 99

    def test_combat_participant_data_current_exceeds_max(self):
        """Test CombatParticipantData allows current_dp to exceed max_dp."""
        participant_id = uuid.uuid4()
        data = CombatParticipantData(
            participant_id=participant_id,
            name="BoostedPlayer",
            current_dp=150,
            max_dp=100,
            dexterity=10,
        )
        assert data.current_dp == 150
        assert data.max_dp == 100

    def test_combat_participant_data_immutability(self):
        """Test CombatParticipantData fields can be accessed but are not frozen."""
        participant_id = uuid.uuid4()
        data = CombatParticipantData(
            participant_id=participant_id,
            name="TestPlayer",
            current_dp=50,
            max_dp=100,
            dexterity=10,
        )
        # Dataclass fields are mutable by default
        data.current_dp = 75
        assert data.current_dp == 75
