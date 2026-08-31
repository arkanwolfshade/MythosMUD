"""Unit tests for unified posture notification."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.posture_notify import (
    emit_posture_change,
    format_room_posture_message,
    normalize_posture,
)


def test_normalize_posture_enum_value() -> None:
    """Enum-like values normalize to lowercase string."""

    class _Pos:
        value: str = "LYING"

    assert normalize_posture(_Pos()) == "lying"


def test_format_room_posture_message_standing_from_lying() -> None:
    result = format_room_posture_message("Ada", "lying", "standing")
    assert "Ada" in result
    assert "pushes" in result.lower() or "stands" in result.lower()


@pytest.mark.asyncio
async def test_emit_posture_change_no_op_when_unchanged() -> None:
    broadcast_to_room: AsyncMock = AsyncMock()
    cm: MagicMock = MagicMock()
    cm.broadcast_to_room = broadcast_to_room
    result = await emit_posture_change(
        cm,
        player_id=uuid.uuid4(),
        display_name="Test",
        room_id="room_a",
        previous_position="standing",
        new_position="standing",
    )
    assert result is None
    broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_emit_posture_change_broadcasts_room_and_sends_personal() -> None:
    broadcast_to_room: AsyncMock = AsyncMock()
    send_personal_message: AsyncMock = AsyncMock(return_value={"success": True})
    cm: MagicMock = MagicMock()
    cm.broadcast_to_room = broadcast_to_room
    cm.send_personal_message = send_personal_message
    player_id = uuid.uuid4()
    self_msg = await emit_posture_change(
        cm,
        player_id=player_id,
        display_name="TestPlayer",
        room_id="room_a",
        previous_position="standing",
        new_position="sitting",
        include_self_message=True,
        send_personal_update=True,
    )
    assert self_msg is not None
    assert "seat" in self_msg.lower()
    broadcast_to_room.assert_awaited_once()
    send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_posture_change_room_only_skips_personal() -> None:
    broadcast_to_room: AsyncMock = AsyncMock()
    send_personal_message: AsyncMock = AsyncMock()
    cm: MagicMock = MagicMock()
    cm.broadcast_to_room = broadcast_to_room
    cm.send_personal_message = send_personal_message
    result = await emit_posture_change(
        cm,
        player_id=uuid.uuid4(),
        display_name="TestPlayer",
        room_id="room_a",
        previous_position="lying",
        new_position="standing",
        include_self_message=False,
    )
    assert result is None
    broadcast_to_room.assert_awaited_once()
    send_personal_message.assert_not_called()


@pytest.mark.asyncio
async def test_emit_posture_change_attach_only_returns_message() -> None:
    broadcast_to_room: AsyncMock = AsyncMock()
    send_personal_message: AsyncMock = AsyncMock()
    cm: MagicMock = MagicMock()
    cm.broadcast_to_room = broadcast_to_room
    cm.send_personal_message = send_personal_message
    self_msg = await emit_posture_change(
        cm,
        player_id=uuid.uuid4(),
        display_name="TestPlayer",
        room_id="room_a",
        previous_position="standing",
        new_position="lying",
        include_self_message=True,
        send_personal_update=False,
    )
    assert self_msg is not None
    assert "lie" in self_msg.lower()
    send_personal_message.assert_not_called()
