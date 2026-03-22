"""
Unit tests for server.commands.combat_flee module-level helpers (not full /flee E2E).

End-to-end flee via CombatCommandHandler is covered in test_flee_command.py.
"""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.combat_flee import (
    _ensure_flee_standing,
    _get_flee_player_uuid,
    _get_flee_room_id,
    _validate_flee_combat_and_room,
)
from server.commands.combat_helpers import FleePreconditionError
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.models.game import PositionState

# pylint: disable=redefined-outer-name,protected-access
# pyright: reportPrivateUsage=false
# Reason: pytest fixture names; tests call combat_flee private helpers (no public test seam).


def test_get_flee_player_uuid_accepts_uuid() -> None:
    """UUID player_id passes through."""
    uid = uuid.uuid4()
    pl = MagicMock()
    pl.player_id = uid
    out, err = _get_flee_player_uuid(pl)
    assert err is None and out == uid


def test_get_flee_player_uuid_invalid_string() -> None:
    """Bad UUID string returns error dict."""
    pl = MagicMock()
    pl.player_id = "not-a-uuid"
    out, err = _get_flee_player_uuid(pl)
    assert out is None and err is not None


@pytest.mark.asyncio
async def test_ensure_flee_standing_when_sitting() -> None:
    """Non-standing returns scrabble message and optionally stands."""
    h = MagicMock()
    change_position: AsyncMock = AsyncMock()
    position_svc: AsyncMock = AsyncMock()
    position_svc.change_position = change_position
    h.player_position_service = position_svc
    pl = MagicMock()
    pl.get_stats = MagicMock(return_value={"position": "sitting"})
    err = await _ensure_flee_standing(h, pl, "Alice")
    assert err is not None
    assert "feet" in err["result"].lower() or "scrabble" in err["result"].lower()
    change_position.assert_awaited_once_with("Alice", "standing")


@pytest.mark.asyncio
async def test_ensure_flee_standing_when_already_standing() -> None:
    """Standing player returns no error."""
    h = MagicMock()
    h.player_position_service = None
    pl = MagicMock()
    pl.get_stats = MagicMock(return_value={"position": PositionState.STANDING})
    assert await _ensure_flee_standing(h, pl, "Bob") is None


def test_get_flee_room_id_unknown_room() -> None:
    """Missing room data yields unknown room."""
    h = MagicMock()
    h.get_room_data = MagicMock(return_value=None)
    rid, err = _get_flee_room_id(h, "missing")
    assert rid is None and err is not None
    assert "unknown" in err["result"].lower()


def test_get_flee_room_id_no_exits() -> None:
    """Room with empty exits blocks flee."""
    h = MagicMock()
    room = MagicMock()
    room.exits = {}
    h.get_room_data = MagicMock(return_value=room)
    rid, err = _get_flee_room_id(h, "r1")
    assert rid is None and err is not None
    assert "escape" in err["result"].lower()


@pytest.mark.asyncio
async def test_validate_flee_combat_and_room_no_combat_service() -> None:
    """Without combat service, combat unavailable."""
    h = MagicMock()
    h.combat_service = None
    pl = MagicMock()
    pl.current_room_id = "r1"
    c, r, err = await _validate_flee_combat_and_room(h, uuid.uuid4(), pl)
    assert c is None and r is None and err is not None


@pytest.mark.asyncio
async def test_validate_flee_combat_and_room_no_movement_service() -> None:
    """Combat resolved but movement missing."""
    h = MagicMock()
    combat_svc: AsyncMock = AsyncMock()
    h.combat_service = combat_svc
    h.movement_service = None
    pid = uuid.uuid4()
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id="r1", participants={})
    combat_svc.get_combat_by_participant = AsyncMock(return_value=combat)
    room = MagicMock()
    room.exits = {"n": "r2"}
    h.get_room_data = MagicMock(return_value=room)
    pl = MagicMock()
    pl.current_room_id = "r1"
    err = (await _validate_flee_combat_and_room(h, pid, pl))[2]
    assert err is not None
    assert "movement" in err["result"].lower()


@pytest.mark.asyncio
async def test_resolve_flee_preconditions_player_error() -> None:
    """FleePreconditionError wraps get_player_and_room error."""
    from server.commands.combat_flee import _resolve_flee_preconditions

    h = MagicMock()
    h.get_player_and_room = AsyncMock(return_value=(None, None, {"result": "no player"}))
    with pytest.raises(FleePreconditionError) as excinfo:
        _ = await _resolve_flee_preconditions(h, None, {"username": "x"}, "x")
    assert excinfo.value.error_result == {"result": "no player"}


def _participant(pid: uuid.UUID, name: str = "P") -> CombatParticipant:
    return CombatParticipant(
        participant_id=pid,
        participant_type=CombatParticipantType.PLAYER,
        name=name,
        current_dp=10,
        max_dp=10,
        dexterity=10,
        is_active=True,
    )


@pytest.mark.asyncio
async def test_validate_flee_combat_and_room_success() -> None:
    """Happy path returns combat and room_id."""
    h = MagicMock()
    combat_svc: AsyncMock = AsyncMock()
    h.combat_service = combat_svc
    h.movement_service = MagicMock()
    pid = uuid.uuid4()
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id="r1", participants={pid: _participant(pid)})
    combat_svc.get_combat_by_participant = AsyncMock(return_value=combat)
    room = MagicMock()
    room.exits = {"e": "r2"}
    h.get_room_data = MagicMock(return_value=room)
    pl = MagicMock()
    pl.current_room_id = "r1"
    c, r, err = await _validate_flee_combat_and_room(h, pid, pl)
    assert err is None
    assert c is combat and r == "r1"
