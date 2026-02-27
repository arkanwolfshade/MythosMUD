"""
Unit tests for combat flee handler (voluntary flee roll and execute_voluntary_flee).
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services.combat_flee_handler import try_voluntary_flee_roll

# pylint: disable=protected-access  # Reason: Test file - accessing for test setup


def _make_participant(participant_id: uuid.UUID, name: str = "Test", dp: int = 100) -> CombatParticipant:
    """Create a combat participant that can act."""
    return CombatParticipant(
        participant_id=participant_id,
        participant_type=CombatParticipantType.PLAYER,
        name=name,
        current_dp=dp,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )


def test_try_voluntary_flee_roll_zero_exits_returns_false():
    """With zero exits, flee always fails."""
    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_1", participants={fleeing_id: _make_participant(fleeing_id)}
    )
    assert try_voluntary_flee_roll(combat, fleeing_id, 0) is False


def test_try_voluntary_flee_roll_roll_above_chance_fails():
    """When random() returns above computed chance, flee fails."""
    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_1", participants={fleeing_id: _make_participant(fleeing_id)}
    )
    # Base 0.5 + 0.1*4 exits - 0 = 0.9. Roll 0.95 should fail.
    with patch("server.services.combat_flee_handler.random.random", return_value=0.95):
        assert try_voluntary_flee_roll(combat, fleeing_id, 4) is False


def test_try_voluntary_flee_roll_roll_below_chance_succeeds():
    """When random() returns below computed chance, flee succeeds."""
    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_1", participants={fleeing_id: _make_participant(fleeing_id)}
    )
    with patch("server.services.combat_flee_handler.random.random", return_value=0.3):
        assert try_voluntary_flee_roll(combat, fleeing_id, 4) is True


def test_try_voluntary_flee_roll_opponents_reduce_chance():
    """More opponents reduce flee chance."""
    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    opp_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id,
        room_id="room_1",
        participants={
            fleeing_id: _make_participant(fleeing_id),
            opp_id: _make_participant(opp_id, "Opponent"),
        },
    )
    # Base 0.5 + 0.1*2 - 0.1*1 = 0.6. Roll 0.55 succeeds.
    with patch("server.services.combat_flee_handler.random.random", return_value=0.55):
        assert try_voluntary_flee_roll(combat, fleeing_id, 2) is True
    # Roll 0.65 fails.
    with patch("server.services.combat_flee_handler.random.random", return_value=0.65):
        assert try_voluntary_flee_roll(combat, fleeing_id, 2) is False


def test_try_voluntary_flee_roll_dead_opponent_not_counted():
    """Dead or inactive opponents do not reduce chance."""
    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    dead_id = uuid.uuid4()
    dead_participant = _make_participant(dead_id, "Dead", dp=0)
    dead_participant.is_active = False
    combat = CombatInstance(
        combat_id=combat_id,
        room_id="room_1",
        participants={fleeing_id: _make_participant(fleeing_id), dead_id: dead_participant},
    )
    # Only fleeing participant is "alive and can act", so 0 opponents. Chance = 0.5 + 0.1*1 = 0.6.
    with patch("server.services.combat_flee_handler.random.random", return_value=0.55):
        assert try_voluntary_flee_roll(combat, fleeing_id, 1) is True


@pytest.mark.asyncio
async def test_execute_voluntary_flee_no_room_returns_false():
    """execute_voluntary_flee returns False when get_room_by_id returns None."""
    from server.services.combat_flee_handler import execute_voluntary_flee

    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_1", participants={fleeing_id: _make_participant(fleeing_id)}
    )
    combat_service = AsyncMock()
    get_room = MagicMock(return_value=None)
    movement_service = AsyncMock()
    with patch("server.services.combat_flee_handler.try_voluntary_flee_roll", return_value=True):
        result = await execute_voluntary_flee(combat_service, get_room, movement_service, combat, fleeing_id)
    assert result is False
    movement_service.move_player.assert_not_awaited()


@pytest.mark.asyncio
async def test_execute_voluntary_flee_no_exits_returns_false():
    """execute_voluntary_flee returns False when room has no exits."""
    from server.services.combat_flee_handler import execute_voluntary_flee

    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_1", participants={fleeing_id: _make_participant(fleeing_id)}
    )
    combat_service = AsyncMock()
    room = MagicMock()
    room.exits = {}
    get_room = MagicMock(return_value=room)
    movement_service = AsyncMock()
    result = await execute_voluntary_flee(combat_service, get_room, movement_service, combat, fleeing_id)
    assert result is False
    combat_service.end_combat.assert_not_awaited()
