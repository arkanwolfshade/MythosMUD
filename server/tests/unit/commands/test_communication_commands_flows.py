# pyright: reportPrivateUsage=false
# Tests target flow helpers in communication_commands_flows (module-private by convention).
"""Unit tests for communication_commands_flows (bundles, message parsing, whisper IDs, room send)."""

from __future__ import annotations

import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.communication_commands_flows import (
    _chat_send_with_room_bundle,
    _global_player_bundle,
    _message_from_command,
    _player_id_bundle,
    _room_player_bundle,
    _RoomChannelOutcomeConfig,
    _str_error_from_chat_result,
    _whisper_id_pair_or_error,
)


def test_str_error_from_chat_result_string() -> None:
    assert _str_error_from_chat_result({"error": "boom"}) == "boom"


def test_str_error_from_chat_result_non_string_defaults() -> None:
    assert _str_error_from_chat_result({"error": 123}) == "Unknown error"
    assert _str_error_from_chat_result({}) == "Unknown error"


def test_message_from_command_missing_message() -> None:
    out = _message_from_command(
        {},
        "p",
        strip=True,
        usage="USAGE",
        empty_log="empty",
    )
    assert out == {"result": "USAGE"}


def test_message_from_command_empty_after_strip() -> None:
    out = _message_from_command(
        {"message": "   "},
        "p",
        strip=True,
        usage="USAGE",
        empty_log="empty",
    )
    assert out == {"result": "USAGE"}


def test_message_from_command_strip_true() -> None:
    out = _message_from_command(
        {"message": "  hi  "},
        "p",
        strip=True,
        usage="USAGE",
        empty_log="empty",
    )
    assert out == "hi"


def test_message_from_command_strip_false() -> None:
    out = _message_from_command(
        {"message": "  hi  "},
        "p",
        strip=False,
        usage="USAGE",
        empty_log="empty",
    )
    assert out == "  hi  "


def test_whisper_id_pair_self_whisper() -> None:
    pid = uuid.uuid4()
    a = SimpleNamespace(player_id=pid)
    b = SimpleNamespace(player_id=pid)
    out = _whisper_id_pair_or_error(a, b)
    assert out == {"result": "You cannot whisper to yourself"}


def test_whisper_id_pair_missing_id() -> None:
    a = SimpleNamespace()
    b = SimpleNamespace(player_id=uuid.uuid4())
    out = _whisper_id_pair_or_error(a, b)
    assert out == {"result": "Player ID not found."}


def test_whisper_id_pair_ok() -> None:
    sid = uuid.uuid4()
    tid = uuid.uuid4()
    a = SimpleNamespace(player_id=sid)
    b = SimpleNamespace(player_id=tid)
    pair = _whisper_id_pair_or_error(a, b)
    assert pair == (sid, tid)


@pytest.mark.asyncio
async def test_room_player_bundle_not_found() -> None:
    ps = MagicMock()
    ps.resolve_player_name = AsyncMock(return_value=None)
    assert await _room_player_bundle(ps, "ghost") == "Player not found."


@pytest.mark.asyncio
async def test_room_player_bundle_no_room() -> None:
    ps = MagicMock()
    po = MagicMock()
    po.current_room_id = None
    ps.resolve_player_name = AsyncMock(return_value=po)
    assert await _room_player_bundle(ps, "x") == "You are not in a room."


@pytest.mark.asyncio
async def test_room_player_bundle_no_primary_id() -> None:
    ps = MagicMock()
    po = SimpleNamespace(current_room_id="r1")
    ps.resolve_player_name = AsyncMock(return_value=po)
    assert await _room_player_bundle(ps, "x") == "Player ID not found."


@pytest.mark.asyncio
async def test_room_player_bundle_success() -> None:
    ps = MagicMock()
    pid = uuid.uuid4()
    po = SimpleNamespace(current_room_id="room_a", player_id=pid)
    ps.resolve_player_name = AsyncMock(return_value=po)
    bundle = await _room_player_bundle(ps, "x")
    assert isinstance(bundle, tuple)
    _o, rid, got_pid = bundle
    assert rid == "room_a"
    assert got_pid == pid


@pytest.mark.asyncio
async def test_global_player_bundle_level_too_low() -> None:
    ps = MagicMock()
    po = SimpleNamespace(level=0, player_id=uuid.uuid4())
    ps.resolve_player_name = AsyncMock(return_value=po)
    assert await _global_player_bundle(ps, "x") == "You must be at least level 1 to use global chat."


@pytest.mark.asyncio
async def test_global_player_bundle_non_int_level_coerced() -> None:
    ps = MagicMock()
    po = SimpleNamespace(level="bad", player_id=uuid.uuid4())
    ps.resolve_player_name = AsyncMock(return_value=po)
    out = await _global_player_bundle(ps, "x")
    assert out == "You must be at least level 1 to use global chat."


@pytest.mark.asyncio
async def test_global_player_bundle_success() -> None:
    ps = MagicMock()
    pid = uuid.uuid4()
    po = SimpleNamespace(level=5, player_id=pid)
    ps.resolve_player_name = AsyncMock(return_value=po)
    bundle = await _global_player_bundle(ps, "x")
    assert isinstance(bundle, tuple)
    _o, lvl, got = bundle
    assert lvl == 5
    assert got == pid


@pytest.mark.asyncio
async def test_player_id_bundle_success() -> None:
    ps = MagicMock()
    pid = uuid.uuid4()
    po = SimpleNamespace(player_id=pid)
    ps.resolve_player_name = AsyncMock(return_value=po)
    bundle = await _player_id_bundle(ps, "x")
    assert bundle == (po, pid)


@pytest.mark.asyncio
async def test_chat_send_with_room_bundle_success() -> None:
    ps = MagicMock()
    pid = uuid.uuid4()
    po = SimpleNamespace(current_room_id="r1", player_id=pid)
    ps.resolve_player_name = AsyncMock(return_value=po)
    cs = MagicMock()

    async def send(_c: object, _pid: object, m: str) -> object:
        assert m == "hello"
        return {"success": True}

    cfg = _RoomChannelOutcomeConfig(
        success_fmt="OK: {0}",
        success_log="ok",
        fail_log="fail",
        err_label="ERR ",
    )
    out = await _chat_send_with_room_bundle(
        {"message": "x"},
        "alice",
        ps,
        cs,
        "hello",
        send,
        cfg,
    )
    assert out == {"result": "OK: hello"}


@pytest.mark.asyncio
async def test_chat_send_with_room_bundle_chat_failure() -> None:
    ps = MagicMock()
    po = SimpleNamespace(current_room_id="r1", player_id=uuid.uuid4())
    ps.resolve_player_name = AsyncMock(return_value=po)
    cs = MagicMock()

    async def send(_c: object, _pid: object, _m: str) -> object:
        return {"success": False, "error": "nope"}

    cfg = _RoomChannelOutcomeConfig(
        success_fmt="OK: {0}",
        success_log="ok",
        fail_log="fail",
        err_label="ERR ",
    )
    out = await _chat_send_with_room_bundle(
        {},
        "alice",
        ps,
        cs,
        "hello",
        send,
        cfg,
    )
    assert out == {"result": "ERR nope"}


@pytest.mark.asyncio
async def test_chat_send_with_room_bundle_exception_returns_generic_message() -> None:
    """Unexpected exceptions must not leak str(e) to the client (PR #461)."""
    ps = MagicMock()
    po = SimpleNamespace(current_room_id="r1", player_id=uuid.uuid4())
    ps.resolve_player_name = AsyncMock(return_value=po)
    cs = MagicMock()

    async def send(_c: object, _pid: object, _m: str) -> object:
        raise RuntimeError("internal connection reset by peer")

    cfg = _RoomChannelOutcomeConfig(
        success_fmt="OK: {0}",
        success_log="ok",
        fail_log="fail",
        err_label="ERR ",
    )
    out = await _chat_send_with_room_bundle(
        {"message": "x"},
        "alice",
        ps,
        cs,
        "hello",
        send,
        cfg,
    )
    assert out == {"result": "ERR Something went wrong. Please try again later."}
    assert "internal connection" not in out["result"]
