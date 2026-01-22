"""
Unit tests for combat models.

Tests the combat system models including enums, dataclasses, and their methods.
"""  # pylint: disable=too-many-lines  # Reason: Comprehensive test suite for combat models - splitting would reduce cohesion and make related tests harder to find

from datetime import UTC, datetime
from unittest.mock import patch
from uuid import UUID, uuid4

from server.models.combat import (
    CombatInstance,
    CombatParticipant,
    CombatParticipantType,
    CombatStatus,
    _get_default_damage,
)

# --- Tests for _get_default_damage function ---


def test_get_default_damage_from_config():
    """Test _get_default_damage retrieves value from config."""
    with patch("server.models.combat.get_config") as mock_config:
        mock_config_instance = type("Config", (), {"game": type("Game", (), {"basic_unarmed_damage": 15})()})()
        mock_config.return_value = mock_config_instance

        result = _get_default_damage()

        assert result == 15
        assert isinstance(result, int)


def test_get_default_damage_fallback_on_error():
    """Test _get_default_damage falls back to 10 on config error."""
    with patch("server.models.combat.get_config", side_effect=ImportError("Config error")):
        result = _get_default_damage()

        assert result == 10
        assert isinstance(result, int)


# --- Tests for CombatStatus enum ---


def test_combat_status_enum_values():
    """Test CombatStatus enum contains expected values."""
    assert CombatStatus.ACTIVE.value == "active"
    assert CombatStatus.ENDED.value == "ended"
    assert CombatStatus.TIMEOUT.value == "timeout"


def test_combat_status_enum_all_statuses():
    """Test CombatStatus enum contains all expected statuses."""
    expected_statuses = {"active", "ended", "timeout"}
    actual_statuses = {s.value for s in CombatStatus}
    assert actual_statuses == expected_statuses


# --- Tests for CombatParticipantType enum ---


def test_combat_participant_type_enum_values():
    """Test CombatParticipantType enum contains expected values."""
    assert CombatParticipantType.PLAYER.value == "player"
    assert CombatParticipantType.NPC.value == "npc"


def test_combat_participant_type_enum_all_types():
    """Test CombatParticipantType enum contains all expected types."""
    expected_types = {"player", "npc"}
    actual_types = {t.value for t in CombatParticipantType}
    assert actual_types == expected_types


# --- Tests for CombatParticipant dataclass ---


def test_combat_participant_is_alive_player_positive_dp():
    """Test is_alive returns True for player with positive DP."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=50,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    assert participant.is_alive() is True


def test_combat_participant_is_alive_player_zero_dp():
    """Test is_alive returns True for player with 0 DP (mortally wounded but still in combat)."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=0,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    assert participant.is_alive() is True


def test_combat_participant_is_alive_player_negative_dp_above_threshold():
    """Test is_alive returns True for player with negative DP above -10."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=-5,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    assert participant.is_alive() is True


def test_combat_participant_is_alive_player_negative_dp_at_threshold():
    """Test is_alive returns False for player with DP at -10 threshold."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=-10,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    assert participant.is_alive() is False


def test_combat_participant_is_alive_player_negative_dp_below_threshold():
    """Test is_alive returns False for player with DP below -10."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=-15,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    assert participant.is_alive() is False


def test_combat_participant_is_alive_player_inactive():
    """Test is_alive returns False for inactive player even with positive DP."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=50,
        max_dp=100,
        dexterity=10,
        is_active=False,
    )

    assert participant.is_alive() is False


def test_combat_participant_is_alive_npc_positive_dp():
    """Test is_alive returns True for NPC with positive DP."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.NPC,
        name="TestNPC",
        current_dp=50,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    assert participant.is_alive() is True


def test_combat_participant_is_alive_npc_zero_dp():
    """Test is_alive returns False for NPC with 0 DP."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.NPC,
        name="TestNPC",
        current_dp=0,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    assert participant.is_alive() is False


def test_combat_participant_is_alive_npc_negative_dp():
    """Test is_alive returns False for NPC with negative DP."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.NPC,
        name="TestNPC",
        current_dp=-5,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    assert participant.is_alive() is False


def test_combat_participant_is_alive_npc_inactive():
    """Test is_alive returns False for inactive NPC even with positive DP."""
    participant = CombatParticipant(
        participant_id=uuid4(),
        participant_type=CombatParticipantType.NPC,
        name="TestNPC",
        current_dp=50,
        max_dp=100,
        dexterity=10,
        is_active=False,
    )

    assert participant.is_alive() is False


# --- Tests for CombatInstance dataclass ---


def test_combat_instance_default_values():
    """Test CombatInstance has correct default values."""
    instance = CombatInstance()

    assert isinstance(instance.combat_id, UUID)
    assert instance.room_id == ""
    assert not instance.participants
    assert not instance.turn_order
    assert instance.current_turn == 0
    assert instance.status == CombatStatus.ACTIVE
    assert instance.start_tick == 0
    assert instance.last_activity_tick == 0
    assert isinstance(instance.last_activity, datetime)
    assert instance.combat_round == 0
    assert instance.auto_progression_enabled is True
    assert instance.turn_interval_ticks == 100  # Round interval (100 ticks = 10 seconds)
    assert instance.next_turn_tick == 0
    assert not instance.queued_actions
    assert not instance.round_actions


def test_combat_instance_get_current_turn_participant_with_valid_turn():
    """Test get_current_turn_participant returns participant when turn is valid."""
    participant_id = uuid4()
    participant = CombatParticipant(
        participant_id=participant_id,
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=50,
        max_dp=100,
        dexterity=10,
    )

    instance = CombatInstance()
    instance.participants[participant_id] = participant
    instance.turn_order = [participant_id]
    instance.current_turn = 0

    result = instance.get_current_turn_participant()

    assert result == participant


def test_combat_instance_get_current_turn_participant_no_turn_order():
    """Test get_current_turn_participant returns None when no turn order."""
    instance = CombatInstance()
    instance.turn_order = []

    result = instance.get_current_turn_participant()

    assert result is None


def test_combat_instance_get_current_turn_participant_turn_out_of_range():
    """Test get_current_turn_participant returns None when turn index out of range."""
    participant_id = uuid4()
    instance = CombatInstance()
    instance.turn_order = [participant_id]
    instance.current_turn = 10  # Out of range

    result = instance.get_current_turn_participant()

    assert result is None


def test_combat_instance_get_current_turn_participant_missing_participant():
    """Test get_current_turn_participant returns None when participant not in participants dict."""
    participant_id = uuid4()
    instance = CombatInstance()
    instance.turn_order = [participant_id]
    instance.current_turn = 0
    # Don't add participant to participants dict

    result = instance.get_current_turn_participant()

    assert result is None


def test_combat_instance_is_combat_over_when_active():
    """Test is_combat_over returns False when status is ACTIVE and multiple participants alive."""
    participant1_id = uuid4()
    participant1 = CombatParticipant(
        participant_id=participant1_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Player1",
        current_dp=50,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    participant2_id = uuid4()
    participant2 = CombatParticipant(
        participant_id=participant2_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Player2",
        current_dp=50,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    instance = CombatInstance()
    instance.status = CombatStatus.ACTIVE
    instance.participants[participant1_id] = participant1
    instance.participants[participant2_id] = participant2

    assert instance.is_combat_over() is False


def test_combat_instance_is_combat_over_when_ended():
    """Test is_combat_over returns True when status is ENDED."""
    instance = CombatInstance()
    instance.status = CombatStatus.ENDED

    assert instance.is_combat_over() is True


def test_combat_instance_is_combat_over_when_timeout():
    """Test is_combat_over returns True when status is TIMEOUT."""
    instance = CombatInstance()
    instance.status = CombatStatus.TIMEOUT

    assert instance.is_combat_over() is True


def test_combat_instance_get_alive_participants():
    """Test get_alive_participants returns only alive participants."""
    participant1_id = uuid4()
    participant1 = CombatParticipant(
        participant_id=participant1_id,
        participant_type=CombatParticipantType.PLAYER,
        name="AlivePlayer",
        current_dp=50,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    participant2_id = uuid4()
    participant2 = CombatParticipant(
        participant_id=participant2_id,
        participant_type=CombatParticipantType.PLAYER,
        name="DeadPlayer",
        current_dp=-15,  # Dead
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    instance = CombatInstance()
    instance.participants[participant1_id] = participant1
    instance.participants[participant2_id] = participant2

    result = instance.get_alive_participants()

    assert len(result) == 1
    assert result[0] == participant1


def test_combat_instance_get_alive_participants_empty():
    """Test get_alive_participants returns empty list when no alive participants."""
    participant_id = uuid4()
    participant = CombatParticipant(
        participant_id=participant_id,
        participant_type=CombatParticipantType.PLAYER,
        name="DeadPlayer",
        current_dp=-15,  # Dead
        max_dp=100,
        dexterity=10,
        is_active=True,
    )

    instance = CombatInstance()
    instance.participants[participant_id] = participant

    result = instance.get_alive_participants()

    assert result == []


def test_combat_instance_update_activity():
    """Test update_activity updates last_activity_tick and last_activity."""
    instance = CombatInstance()
    instance.last_activity_tick = 0
    original_activity = instance.last_activity

    import time

    time.sleep(0.01)

    instance.update_activity(current_tick=100)

    assert instance.last_activity_tick == 100
    assert instance.last_activity > original_activity
    assert instance.last_activity.tzinfo == UTC


def test_combat_instance_advance_turn():
    """Test advance_turn increments combat_round and updates next_turn_tick."""
    participant_id = uuid4()
    instance = CombatInstance()
    instance.turn_order = [participant_id, uuid4()]
    instance.current_turn = 0
    instance.next_turn_tick = 0
    instance.turn_interval_ticks = 100
    instance.combat_round = 0

    instance.advance_turn(current_tick=10)

    assert instance.combat_round == 1  # Round increments
    assert instance.current_turn == 0  # Reset to 0 (may be repurposed)
    assert instance.next_turn_tick == 110  # 10 + 100


def test_combat_instance_advance_turn_increments_round():
    """Test advance_turn increments combat_round (round-based system)."""
    participant1_id = uuid4()
    participant2_id = uuid4()
    instance = CombatInstance()
    instance.turn_order = [participant1_id, participant2_id]
    instance.current_turn = 1
    instance.combat_round = 0
    instance.next_turn_tick = 10
    instance.turn_interval_ticks = 100

    instance.advance_turn(current_tick=20)

    assert instance.combat_round == 1  # Round increments
    assert instance.current_turn == 0  # Reset to 0
    assert instance.next_turn_tick == 120  # 20 + 100


def test_combat_instance_advance_turn_always_increments_round():
    """Test advance_turn always increments combat_round in round-based system."""
    participant_id = uuid4()
    instance = CombatInstance()
    instance.turn_order = [participant_id]
    instance.current_turn = 0
    instance.combat_round = 5
    instance.turn_interval_ticks = 100

    instance.advance_turn(current_tick=1000)

    assert instance.combat_round == 6  # Round increments
    assert instance.current_turn == 0  # Reset to 0
    assert instance.next_turn_tick == 1100  # 1000 + 100


def test_combat_instance_queue_action():
    """Test queue_action queues an action for the next round."""
    from server.models.combat import CombatAction

    participant_id = uuid4()
    instance = CombatInstance()
    instance.combat_round = 5
    instance.participants[participant_id] = CombatParticipant(
        participant_id=participant_id,
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=50,
        max_dp=100,
        dexterity=10,
    )

    action = CombatAction(action_type="attack", damage=10)
    instance.queue_action(participant_id, action)

    assert len(instance.queued_actions[participant_id]) == 1
    assert instance.queued_actions[participant_id][0] == action
    assert action.round == 6  # Next round (5 + 1)
    assert action.queued is True


def test_combat_instance_get_queued_actions():
    """Test get_queued_actions returns queued actions for a participant."""
    from server.models.combat import CombatAction

    participant_id = uuid4()
    instance = CombatInstance()
    action1 = CombatAction(action_type="attack", damage=10)
    action2 = CombatAction(action_type="spell", spell_name="heal")

    instance.queue_action(participant_id, action1)
    instance.queue_action(participant_id, action2)

    queued = instance.get_queued_actions(participant_id)
    assert len(queued) == 2
    assert action1 in queued
    assert action2 in queued


def test_combat_instance_clear_queued_actions():
    """Test clear_queued_actions clears actions for a participant."""
    from server.models.combat import CombatAction

    participant_id = uuid4()
    instance = CombatInstance()
    action = CombatAction(action_type="attack", damage=10)
    instance.queue_action(participant_id, action)

    instance.clear_queued_actions(participant_id)

    assert participant_id not in instance.queued_actions
    assert instance.get_queued_actions(participant_id) == []


def test_combat_instance_clear_queued_actions_specific_round():
    """Test clear_queued_actions clears only actions for a specific round."""
    from server.models.combat import CombatAction

    participant_id = uuid4()
    instance = CombatInstance()
    instance.combat_round = 5
    action1 = CombatAction(action_type="attack", damage=10)
    action2 = CombatAction(action_type="spell", spell_name="heal")
    instance.queue_action(participant_id, action1)  # Queued for round 6
    instance.combat_round = 6
    instance.queue_action(participant_id, action2)  # Queued for round 7

    instance.clear_queued_actions(participant_id, round_number=6)

    queued = instance.get_queued_actions(participant_id)
    assert len(queued) == 1
    assert action2 in queued  # Only action2 remains (round 7)
    assert action1 not in queued  # action1 cleared (round 6)


def test_combat_instance_get_participants_by_initiative():
    """Test get_participants_by_initiative returns participants sorted by dexterity."""
    participant1_id = uuid4()
    participant1 = CombatParticipant(
        participant_id=participant1_id,
        participant_type=CombatParticipantType.PLAYER,
        name="LowDex",
        current_dp=50,
        max_dp=100,
        dexterity=30,
    )

    participant2_id = uuid4()
    participant2 = CombatParticipant(
        participant_id=participant2_id,
        participant_type=CombatParticipantType.NPC,
        name="HighDex",
        current_dp=50,
        max_dp=100,
        dexterity=90,
    )

    participant3_id = uuid4()
    participant3 = CombatParticipant(
        participant_id=participant3_id,
        participant_type=CombatParticipantType.PLAYER,
        name="MidDex",
        current_dp=50,
        max_dp=100,
        dexterity=60,
    )

    instance = CombatInstance()
    instance.participants[participant1_id] = participant1
    instance.participants[participant2_id] = participant2
    instance.participants[participant3_id] = participant3

    result = instance.get_participants_by_initiative()

    assert len(result) == 3
    assert result[0] == participant2  # Highest dexterity (90)
    assert result[1] == participant3  # Mid dexterity (60)
    assert result[2] == participant1  # Lowest dexterity (30)
