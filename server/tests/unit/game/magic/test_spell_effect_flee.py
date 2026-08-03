"""Unit tests for flee spell effect helpers."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic.spell_effect_flee import (
    _flee_effect_services_available,
    _flee_effect_validate_room_exits,
    run_flee_effect,
)
from server.schemas.shared import TargetMatch, TargetType


def _player_target(player_id: uuid.UUID | None = None) -> TargetMatch:
    pid = player_id or uuid.uuid4()
    return TargetMatch(
        target_type=TargetType.PLAYER,
        target_id=str(pid),
        target_name="Runner",
        room_id="room-1",
    )


def test_flee_effect_services_available() -> None:
    assert _flee_effect_services_available(None, MagicMock(), MagicMock()) is False
    assert _flee_effect_services_available(MagicMock(), MagicMock(), MagicMock()) is True


def test_flee_effect_validate_room_exits() -> None:
    combat = MagicMock()
    combat.room_id = "room-1"
    assert _flee_effect_validate_room_exits(combat, lambda _rid: None)[1] is not None

    room_no_exits = MagicMock()
    room_no_exits.exits = {}
    assert "escape" in (_flee_effect_validate_room_exits(combat, lambda _rid: room_no_exits)[1] or "").lower()

    room_ok = MagicMock()
    room_ok.exits = {"north": "room-2"}
    room_id, err = _flee_effect_validate_room_exits(combat, lambda _rid: room_ok)
    assert room_id == "room-1"
    assert err is None


@pytest.mark.asyncio
async def test_run_flee_effect_invalid_target_type() -> None:
    target = TargetMatch(
        target_type=TargetType.ROOM,
        target_id="room-1",
        target_name="Hall",
        room_id="room-1",
    )
    result = await run_flee_effect(MagicMock(), MagicMock(), MagicMock(), target)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_run_flee_effect_services_unavailable() -> None:
    result = await run_flee_effect(None, None, None, _player_target())
    assert result["success"] is False


@pytest.mark.asyncio
async def test_run_flee_effect_invalid_uuid() -> None:
    target = TargetMatch(
        target_type=TargetType.PLAYER,
        target_id="not-a-uuid",
        target_name="Bad",
        room_id="room-1",
    )
    result = await run_flee_effect(MagicMock(), MagicMock(), MagicMock(), target)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_run_flee_effect_not_in_combat() -> None:
    combat_service = MagicMock()
    combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    result = await run_flee_effect(combat_service, MagicMock(), MagicMock(), _player_target())
    assert result["success"] is False


@pytest.mark.asyncio
async def test_run_flee_effect_room_error() -> None:
    combat = MagicMock()
    combat.room_id = "room-1"
    combat_service = MagicMock()
    combat_service.get_combat_by_participant = AsyncMock(return_value=combat)
    result = await run_flee_effect(combat_service, MagicMock(), lambda _rid: None, _player_target())
    assert result["success"] is False


@pytest.mark.asyncio
async def test_run_flee_effect_success_and_failure() -> None:
    combat = MagicMock()
    combat.room_id = "room-1"
    room = MagicMock()
    room.exits = {"north": "room-2"}
    combat_service = MagicMock()
    combat_service.get_combat_by_participant = AsyncMock(return_value=combat)
    movement = MagicMock()
    get_room = MagicMock(return_value=room)

    with patch(
        "server.game.magic.spell_effect_flee.execute_voluntary_flee",
        new_callable=AsyncMock,
        return_value=True,
    ):
        ok = await run_flee_effect(combat_service, movement, get_room, _player_target())
    with patch(
        "server.game.magic.spell_effect_flee.execute_voluntary_flee",
        new_callable=AsyncMock,
        return_value=False,
    ):
        failed_roll = await run_flee_effect(combat_service, movement, get_room, _player_target())

    assert ok["success"] is True
    assert "flees" in ok["message"].lower()
    assert failed_roll["success"] is True
    assert "fails to flee" in failed_roll["message"].lower()
