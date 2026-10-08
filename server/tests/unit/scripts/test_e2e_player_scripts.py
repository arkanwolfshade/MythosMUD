"""Tests for scripts/e2e_player_state.py and scripts/e2e_place_player.py (Playwright setup/assertion helpers)."""

# pylint: disable=protected-access
# pyright: reportPrivateUsage=false
# Reason: this module tests the scripts' private async entry points directly.

from __future__ import annotations

import importlib.util
import json
import sys
import uuid
from collections.abc import Awaitable, Callable
from pathlib import Path
from typing import Protocol, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPTS = PROJECT_ROOT / "scripts"

PLAYER_ID = uuid.uuid4()
ROW: dict[str, object] = {
    "player_id": PLAYER_ID,
    "current_room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
    "respawn_room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
    "tutorial_instance_id": None,
}


class _StateScript(Protocol):
    _print_state: Callable[[str], Awaitable[None]]


class _PlaceScript(Protocol):
    _place: Callable[[str, str], Awaitable[None]]


def _load(script: str) -> object:
    name = f"{script}_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{script}.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        del sys.modules[name]
    return module


class _FakeConnection:
    """Stands in for asyncpg.Connection; answers by the query's text and records what it was asked."""

    def __init__(
        self,
        *,
        row: dict[str, object] | None = None,
        contents: str | None = None,
        room_exists: bool = True,
        player_exists: bool = True,
    ) -> None:
        self.row: dict[str, object] | None = row
        self.contents: str | None = contents
        self.room_exists: bool = room_exists
        self.player_exists: bool = player_exists
        self.queries: list[tuple[str, tuple[object, ...]]] = []
        self.closed: bool = False

    async def fetchrow(self, query: str, *args: object) -> dict[str, object] | None:
        self.queries.append((" ".join(query.split()), args))
        return self.row

    async def fetchval(self, query: str, *args: object) -> object:
        flat = " ".join(query.split())
        self.queries.append((flat, args))
        if "get_container_contents_json" in flat:
            return self.contents
        if flat.startswith("SELECT 1 FROM rooms"):
            return 1 if self.room_exists else None
        if flat.startswith("UPDATE players"):
            return PLAYER_ID if self.player_exists else None
        raise AssertionError(f"unexpected query: {flat}")

    async def close(self) -> None:
        self.closed = True


def _connect_to(monkeypatch: pytest.MonkeyPatch, conn: _FakeConnection) -> None:
    async def fake_connect(*_args: object, **_kwargs: object) -> _FakeConnection:
        return conn

    monkeypatch.setattr("asyncpg.connect", fake_connect)


async def test_state_reports_location_and_what_is_in_the_bank_box(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    script = cast(_StateScript, _load("e2e_player_state"))
    stacks = [{"item_name": "Sling", "quantity": 1}, {"item_name": "Oil Lamp", "quantity": 2}]
    conn = _FakeConnection(row=ROW, contents=json.dumps(stacks))
    _connect_to(monkeypatch, conn)

    await script._print_state("E2ETutorial")

    state = cast(dict[str, object], json.loads(capsys.readouterr().out))
    assert state == {
        "current_room_id": ROW["current_room_id"],
        "respawn_room_id": ROW["respawn_room_id"],
        "tutorial_instance_id": None,
        "bank_items": ["Sling", "Oil Lamp"],
    }
    # The box is looked up by this player's id, never by name or room.
    bank_query = next(query for query in conn.queries if "get_container_contents_json" in query[0])
    assert "source_type = 'bank'" in bank_query[0]
    assert bank_query[1] == (PLAYER_ID,)
    assert conn.closed


async def test_state_reports_an_empty_list_when_the_character_has_no_box(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    script = cast(_StateScript, _load("e2e_player_state"))
    _connect_to(monkeypatch, _FakeConnection(row=ROW, contents=None))

    await script._print_state("E2ETutorial")

    assert cast(dict[str, object], json.loads(capsys.readouterr().out))["bank_items"] == []


async def test_state_exits_nonzero_for_an_unknown_character(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    script = cast(_StateScript, _load("e2e_player_state"))
    conn = _FakeConnection(row=None)
    _connect_to(monkeypatch, conn)

    with pytest.raises(SystemExit) as raised:
        await script._print_state("Nobody")

    assert raised.value.code == 1
    assert "No player named Nobody" in capsys.readouterr().err
    assert conn.closed
    assert all(
        "get_container_contents_json" not in query[0] for query in conn.queries
    )  # no box lookup without a player


async def test_place_moves_the_named_character_to_the_room(monkeypatch: pytest.MonkeyPatch) -> None:
    script = cast(_PlaceScript, _load("e2e_place_player"))
    conn = _FakeConnection()
    _connect_to(monkeypatch, conn)

    await script._place("E2ETutorial", "earth_arkhamcity_downtown_room_arkham_savings_001")

    [update] = [query for query in conn.queries if query[0].startswith("UPDATE players")]
    assert "current_room_id = $2" in update[0]
    assert update[1] == ("E2ETutorial", "earth_arkhamcity_downtown_room_arkham_savings_001")
    assert conn.closed


async def test_place_refuses_a_room_that_does_not_exist_and_moves_nobody(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """A typo must fail loudly, not strand the character in a room the server cannot load."""
    script = cast(_PlaceScript, _load("e2e_place_player"))
    conn = _FakeConnection(room_exists=False)
    _connect_to(monkeypatch, conn)

    with pytest.raises(SystemExit) as raised:
        await script._place("E2ETutorial", "no_such_room")

    assert raised.value.code == 1
    assert "No room with stable id no_such_room" in capsys.readouterr().err
    assert all(not query[0].startswith("UPDATE") for query in conn.queries)
    assert conn.closed


async def test_place_exits_nonzero_for_an_unknown_character(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    script = cast(_PlaceScript, _load("e2e_place_player"))
    _connect_to(monkeypatch, _FakeConnection(player_exists=False))

    with pytest.raises(SystemExit) as raised:
        await script._place("Nobody", "earth_arkhamcity_downtown_room_arkham_savings_001")

    assert raised.value.code == 1
    assert "No player named Nobody" in capsys.readouterr().err
