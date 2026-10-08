"""Tests for scripts/e2e_reset_players.py --tutorial (puts E2ETutorial back at the start of the tutorial)."""

# pylint: disable=protected-access
# pyright: reportPrivateUsage=false
# Reason: this module tests the reset script's private _reset_tutorial_character directly.

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


class _ResetScript(Protocol):
    """Attributes of scripts/e2e_reset_players.py read after dynamic import."""

    TUTORIAL_BEDROOM: str
    TUTORIAL_ITEM_PROTOTYPE: str
    FOLK_TONIC_COOLDOWN_KEY: str
    _reset_tutorial_character: Callable[[object], Awaitable[None]]
    _clear_folk_tonic_cooldowns: Callable[[object], Awaitable[None]]


class _SeedSpec(Protocol):
    username: str


class _SeedScript(Protocol):
    E2E_USER_SPECS: tuple[_SeedSpec, ...]


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


class _RecordingConnection:
    """Stands in for asyncpg.Connection: returns a player id (or None) and records every execute()."""

    def __init__(self, player_id: uuid.UUID | None) -> None:
        self.player_id: uuid.UUID | None = player_id
        self.executed: list[tuple[str, tuple[object, ...]]] = []

    async def fetchval(self, _query: str, *_args: object) -> uuid.UUID | None:
        return self.player_id

    async def execute(self, query: str, *args: object) -> str:
        self.executed.append((" ".join(query.split()), args))
        return "OK"


async def test_reset_tutorial_character_restores_tutorial_start_state() -> None:
    script = cast(_ResetScript, _load("e2e_reset_players"))
    player_id = uuid.uuid4()
    conn = _RecordingConnection(player_id)

    await script._reset_tutorial_character(conn)

    [player_update, quest_delete, inventory, chest_clear, bank_clear] = conn.executed
    assert "tutorial_instance_id = NULL" in player_update[0]
    assert player_update[1][:2] == (player_id, script.TUTORIAL_BEDROOM)
    # Player.get_inventory() reads players.inventory: both copies must carry the same Sling.
    assert player_update[1][2] == inventory[1][1]
    assert quest_delete == ("DELETE FROM quest_instances WHERE player_id = $1", (player_id,))
    stacks = cast(list[dict[str, object]], json.loads(cast(str, inventory[1][1])))
    assert [stack["item_id"] for stack in stacks] == [script.TUTORIAL_ITEM_PROTOTYPE]
    assert "clear_container_contents" in chest_clear[0]
    assert "lost_and_found" in chest_clear[0]
    # What the tutorial leaves behind lands in the leaver's deposit box; it must not carry over into
    # the next test, and only the tutorial character's own box may be emptied.
    assert "clear_container_contents" in bank_clear[0]
    assert "source_type = 'bank'" in bank_clear[0]
    assert bank_clear[1] == (player_id,)


async def test_clear_folk_tonic_cooldowns_targets_the_shared_players_only() -> None:
    script = cast(_ResetScript, _load("e2e_reset_players"))
    conn = _RecordingConnection(None)

    await script._clear_folk_tonic_cooldowns(conn)

    [(query, args)] = conn.executed
    assert query.startswith("DELETE FROM lucidity_cooldowns WHERE action_code = $1")
    assert "'ArkanWolfshade', 'Ithaqua'" in query
    assert args == (script.FOLK_TONIC_COOLDOWN_KEY,)
    assert script.FOLK_TONIC_COOLDOWN_KEY == "folk_tonic"


async def test_reset_tutorial_character_requires_the_seeded_character() -> None:
    script = cast(_ResetScript, _load("e2e_reset_players"))

    with pytest.raises(RuntimeError, match="E2ETutorial is not seeded"):
        await script._reset_tutorial_character(_RecordingConnection(None))


def test_seed_includes_the_tutorial_account() -> None:
    seed = cast(_SeedScript, _load("seed_e2e_users"))

    assert "E2ETutorial" in [spec.username for spec in seed.E2E_USER_SPECS]
