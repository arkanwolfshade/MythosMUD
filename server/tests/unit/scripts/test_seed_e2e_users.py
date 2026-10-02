"""Regression tests for scripts/seed_e2e_users.py deterministic account ids (#969).

make test-playwright's integration stage deletes users/players under a still-running E2E server. Re-seeding
with fresh uuid4s left that server holding ids that no longer existed, so the seeded ids must be stable.
"""

# pylint: disable=protected-access
# pyright: reportPrivateUsage=false
# Reason: this module tests the seed script's private _ensure_player_for_user directly.

from __future__ import annotations

import importlib.util
import sys
import uuid
from collections.abc import Awaitable, Callable
from datetime import UTC, datetime
from pathlib import Path
from typing import Protocol, cast

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "seed_e2e_users.py"


class _SeedScript(Protocol):
    """Attributes of scripts/seed_e2e_users.py read after dynamic import (not on the ModuleType stub)."""

    e2e_user_id: Callable[[str], uuid.UUID]
    e2e_player_id: Callable[[str], uuid.UUID]
    _ensure_player_for_user: Callable[..., Awaitable[None]]


def _load_script() -> _SeedScript:
    """Import a fresh copy of the script, like a new seed process would."""
    name = f"seed_e2e_users_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(name, SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    # @dataclass resolves its module through sys.modules during class creation.
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        del sys.modules[name]
    return cast(_SeedScript, cast(object, module))


class _RecordingConnection:
    """Stands in for asyncpg.Connection: no existing character, records every execute()."""

    def __init__(self) -> None:
        self.executed: list[tuple[object, ...]] = []

    async def fetchrow(self, _query: str, *_args: object) -> None:
        return None

    async def execute(self, _query: str, *args: object) -> str:
        self.executed.append(args)
        return "CALL"


def test_ids_are_stable_across_imports() -> None:
    """A fresh process (fresh import) must derive the same ids, or a re-seed creates new identities."""
    first, second = _load_script(), _load_script()
    assert first.e2e_user_id("ArkanWolfshade") == second.e2e_user_id("ArkanWolfshade")
    assert first.e2e_player_id("Ithaqua") == second.e2e_player_id("Ithaqua")


def test_ids_are_distinct_per_account_and_kind() -> None:
    script = _load_script()
    ids = {
        script.e2e_user_id("ArkanWolfshade"),
        script.e2e_user_id("Ithaqua"),
        script.e2e_player_id("ArkanWolfshade"),
        script.e2e_player_id("Ithaqua"),
    }
    assert len(ids) == 4


async def test_reseeding_a_deleted_character_reuses_its_player_id() -> None:
    """The #969 scenario: the character row is gone, the seed recreates it, the player_id must not change."""
    script = _load_script()
    user_id = script.e2e_user_id("ArkanWolfshade")
    now = datetime.now(UTC)
    first, second = _RecordingConnection(), _RecordingConnection()

    for conn in (first, second):
        await script._ensure_player_for_user(
            conn, user_id=user_id, character_name="ArkanWolfshade", player_is_admin=1, now=now
        )

    assert len(first.executed) == len(second.executed) == 1
    first_player_id, first_user_id = first.executed[0][:2]
    assert first_player_id == second.executed[0][0] == script.e2e_player_id("ArkanWolfshade")
    assert first_user_id == user_id
