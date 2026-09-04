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


@pytest.mark.asyncio
async def test_execute_voluntary_flee_missing_participant_returns_false():
    """execute_voluntary_flee returns False when participant not in combat."""
    from server.services.combat_flee_handler import execute_voluntary_flee

    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    other_id = uuid.uuid4()
    combat = CombatInstance(combat_id=combat_id, room_id="room_1", participants={other_id: _make_participant(other_id)})
    room = MagicMock()
    room.exits = {"north": "room_2"}
    get_room = MagicMock(return_value=room)
    result = await execute_voluntary_flee(AsyncMock(), get_room, AsyncMock(), combat, fleeing_id)
    assert result is False


@pytest.mark.asyncio
async def test_execute_voluntary_flee_roll_fail_consumes_action():
    """Failed flee roll queues skip action and runs free hits."""
    from server.services.combat_flee_handler import execute_voluntary_flee

    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_1", participants={fleeing_id: _make_participant(fleeing_id)}
    )
    room = MagicMock()
    room.exits = {"north": "room_2"}
    get_room = MagicMock(return_value=room)
    combat_service = AsyncMock()
    with patch("server.services.combat_flee_handler.try_voluntary_flee_roll", return_value=False):
        result = await execute_voluntary_flee(combat_service, get_room, AsyncMock(), combat, fleeing_id)
    assert result is False
    combat_service.execute_flee_failed_free_hits.assert_awaited_once_with(combat_id, fleeing_id)


@pytest.mark.asyncio
async def test_execute_voluntary_flee_success_moves_player():
    """Successful flee ends combat and moves player."""
    from server.services.combat_flee_handler import execute_voluntary_flee

    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_1", participants={fleeing_id: _make_participant(fleeing_id)}
    )
    room = MagicMock()
    room.exits = {"north": "room_2"}
    get_room = MagicMock(return_value=room)
    combat_service = AsyncMock()
    movement_service = AsyncMock()
    movement_service.move_player = AsyncMock(return_value=True)
    with patch("server.services.combat_flee_handler.try_voluntary_flee_roll", return_value=True):
        with patch("server.services.combat_flee_handler.secrets.choice", return_value="room_2"):
            result = await execute_voluntary_flee(combat_service, get_room, movement_service, combat, fleeing_id)
    assert result is True
    combat_service.end_combat.assert_awaited_once()
    movement_service.move_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_check_involuntary_flee_zero_max_dp_returns_false():
    """check_involuntary_flee returns False when max_dp is zero."""
    from server.services.combat_flee_handler import check_involuntary_flee

    participant = _make_participant(uuid.uuid4(), dp=0)
    participant.max_dp = 0
    assert await check_involuntary_flee(participant, 10) is False


@pytest.mark.asyncio
async def test_involuntary_flee_on_cooldown_active():
    """_involuntary_flee_on_cooldown returns True when cooldown not expired."""
    from datetime import UTC, datetime, timedelta

    from server.services.combat_flee_handler import _involuntary_flee_on_cooldown

    lucidity_service = AsyncMock()
    cooldown = MagicMock()
    cooldown.cooldown_expires_at = datetime.now(UTC) + timedelta(minutes=1)
    lucidity_service.get_cooldown = AsyncMock(return_value=cooldown)
    player_id = uuid.uuid4()
    assert await _involuntary_flee_on_cooldown(lucidity_service, player_id, "involuntary_flee") is True


@pytest.mark.asyncio
async def test_involuntary_flee_on_cooldown_expired():
    """_involuntary_flee_on_cooldown returns False when cooldown expired."""
    from datetime import UTC, datetime, timedelta

    from server.services.combat_flee_handler import _involuntary_flee_on_cooldown

    lucidity_service = AsyncMock()
    cooldown = MagicMock()
    cooldown.cooldown_expires_at = datetime.now(UTC) - timedelta(minutes=1)
    lucidity_service.get_cooldown = AsyncMock(return_value=cooldown)
    player_id = uuid.uuid4()
    assert await _involuntary_flee_on_cooldown(lucidity_service, player_id, "involuntary_flee") is False


@pytest.mark.asyncio
async def test_involuntary_flee_on_cooldown_naive_datetime():
    """Naive cooldown_expires_at is treated as UTC."""
    from datetime import datetime

    from server.services.combat_flee_handler import _involuntary_flee_on_cooldown

    lucidity_service = AsyncMock()
    cooldown = MagicMock()
    cooldown.cooldown_expires_at = datetime(2099, 1, 1)
    lucidity_service.get_cooldown = AsyncMock(return_value=cooldown)
    player_id = uuid.uuid4()
    assert await _involuntary_flee_on_cooldown(lucidity_service, player_id, "involuntary_flee") is True


@pytest.mark.asyncio
async def test_involuntary_flee_on_cooldown_no_expiry():
    """Missing cooldown_expires_at is not on cooldown."""
    from server.services.combat_flee_handler import _involuntary_flee_on_cooldown

    lucidity_service = AsyncMock()
    cooldown = MagicMock()
    cooldown.cooldown_expires_at = None
    lucidity_service.get_cooldown = AsyncMock(return_value=cooldown)
    player_id = uuid.uuid4()
    assert await _involuntary_flee_on_cooldown(lucidity_service, player_id, "involuntary_flee") is False


@pytest.mark.asyncio
async def test_execute_voluntary_flee_free_hits_error_logged():
    """Free hit execution errors are logged but flee still fails."""
    from server.services.combat_flee_handler import execute_voluntary_flee

    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_1", participants={fleeing_id: _make_participant(fleeing_id)}
    )
    room = MagicMock()
    room.exits = {"north": "room_2"}
    combat_service = AsyncMock()
    combat_service.execute_flee_failed_free_hits = AsyncMock(side_effect=RuntimeError("boom"))
    with patch("server.services.combat_flee_handler.try_voluntary_flee_roll", return_value=False):
        result = await execute_voluntary_flee(
            combat_service, MagicMock(return_value=room), AsyncMock(), combat, fleeing_id
        )
    assert result is False


@pytest.mark.asyncio
async def test_execute_voluntary_flee_move_fails_returns_false():
    """Successful roll but failed move returns False."""
    from server.services.combat_flee_handler import execute_voluntary_flee

    combat_id = uuid.uuid4()
    fleeing_id = uuid.uuid4()
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_1", participants={fleeing_id: _make_participant(fleeing_id)}
    )
    room = MagicMock()
    room.exits = {"north": "room_2"}
    movement_service = AsyncMock()
    movement_service.move_player = AsyncMock(return_value=False)
    with patch("server.services.combat_flee_handler.try_voluntary_flee_roll", return_value=True):
        with patch("server.services.combat_flee_handler.secrets.choice", return_value="room_2"):
            result = await execute_voluntary_flee(
                AsyncMock(), MagicMock(return_value=room), movement_service, combat, fleeing_id
            )
    assert result is False


@pytest.mark.asyncio
async def test_check_involuntary_flee_with_session_tier_blocks():
    """Involuntary flee blocked when tier/damage threshold not met."""
    from server.services.combat_flee_handler import _check_involuntary_flee_with_session

    participant = _make_participant(uuid.uuid4())
    session = AsyncMock()
    with patch("server.services.combat_flee_handler.LucidityService") as mock_svc_cls:
        mock_svc = mock_svc_cls.return_value
        mock_svc.get_player_lucidity = AsyncMock(return_value=MagicMock(current_tier="lucid"))
        with patch("server.services.combat_flee_handler.should_involuntary_flee", return_value=False):
            result = await _check_involuntary_flee_with_session(session, participant, 0.05, 5)
    assert result is False


@pytest.mark.asyncio
async def test_check_involuntary_flee_with_session_sets_cooldown():
    """Involuntary flee allowed sets cooldown and commits."""
    from server.services.combat_flee_handler import _check_involuntary_flee_with_session

    participant = _make_participant(uuid.uuid4())
    session = AsyncMock()
    with patch("server.services.combat_flee_handler.LucidityService") as mock_svc_cls:
        mock_svc = mock_svc_cls.return_value
        mock_svc.get_player_lucidity = AsyncMock(return_value=MagicMock(current_tier="deranged"))
        mock_svc.get_cooldown = AsyncMock(return_value=None)
        mock_svc.set_cooldown = AsyncMock()
        with patch("server.services.combat_flee_handler.should_involuntary_flee", return_value=True):
            result = await _check_involuntary_flee_with_session(session, participant, 0.20, 20)
    assert result is True
    mock_svc.set_cooldown.assert_awaited_once()
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_check_involuntary_flee_session_path():
    """check_involuntary_flee delegates to session helper."""
    from server.services.combat_flee_handler import check_involuntary_flee

    participant = _make_participant(uuid.uuid4())
    session = AsyncMock()

    async def fake_session_gen():
        yield session

    with patch("server.services.combat_flee_handler.get_async_session", return_value=fake_session_gen()):
        with patch(
            "server.services.combat_flee_handler._check_involuntary_flee_with_session",
            new_callable=AsyncMock,
            return_value=True,
        ) as mock_check:
            result = await check_involuntary_flee(participant, 20)
    assert result is True
    mock_check.assert_awaited_once()
