"""Logout and quit stamp ``last_active`` through the player registry and write nothing else (ADR-029 step 8a)."""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass
from types import SimpleNamespace
from typing import cast

import pytest
from fastapi import Request

from server.commands.logout_commands import handle_logout_command, handle_quit_command
from server.game.player_registry import PlayerRegistry
from server.tests.fixtures.shared.player_registry import FakeDatabase, raw_row
from server.tests.unit.game.player_registry.fakes import FakeLoader


class _Persistence:
    """One player for any name; saving the whole row is not expected any more."""

    def __init__(self, player_id: uuid.UUID) -> None:
        self.player: SimpleNamespace = SimpleNamespace(player_id=str(player_id), name="Tester")
        self.saves: int = 0

    async def get_player_by_name(self, _name: str) -> SimpleNamespace:
        return self.player

    async def save_player(self, _player: SimpleNamespace) -> None:
        self.saves += 1


class _ConnectionManager:
    """Remembers who was marked as an intentional disconnect; its cached position says the player is standing."""

    def __init__(self, player_id: uuid.UUID) -> None:
        self.intentional_disconnects: set[uuid.UUID] = set()
        self.online_players: dict[str, dict[str, object]] = {str(player_id): {"position": "standing"}}
        self.disconnected: list[uuid.UUID] = []

    def get_online_player_by_display_name(self, _name: str) -> None:
        return None

    async def force_disconnect_player(self, player_id: uuid.UUID) -> None:
        self.disconnected.append(player_id)


@dataclass
class _Harness:
    request: Request
    registry: PlayerRegistry
    db: FakeDatabase
    persistence: _Persistence
    player_id: uuid.UUID


def _harness(*, with_registry: bool = True) -> _Harness:
    player_id = uuid.uuid4()
    db = FakeDatabase()
    registry = PlayerRegistry(
        db.session, loader=FakeLoader({player_id: raw_row(player_id, stats={"current_dp": 20, "position": "sitting"})})
    )
    persistence = _Persistence(player_id)
    connection_manager = _ConnectionManager(player_id)
    container = SimpleNamespace(
        async_persistence=persistence,
        connection_manager=connection_manager,
        player_registry=registry if with_registry else None,
    )
    state = SimpleNamespace(container=container, persistence=persistence, connection_manager=connection_manager)
    request = cast(Request, cast(object, SimpleNamespace(app=SimpleNamespace(state=state))))
    return _Harness(request, registry, db, persistence, player_id)


async def _written_changes(harness: _Harness) -> dict[str, object]:
    """What the registry's sweep would write for the player: the players-row columns and stats keys that changed."""
    assert await harness.registry.flush_dirty() == 1
    params = harness.db.executed[-1]
    assert params is not None
    return {
        "columns": json.loads(str(params["changes"])),
        "stats": json.loads(str(params["stats_changes"] or "{}")),
    }


@pytest.mark.asyncio
async def test_logout_stamps_last_active_and_leaves_the_registry_posture_alone() -> None:
    harness = _harness()

    result = await handle_logout_command({}, {"username": "tester"}, harness.request, None, "Tester")

    assert result["result"] == "Logged out successfully"
    changes = await _written_changes(harness)
    assert list(cast(dict[str, object], changes["columns"])) == ["last_active"]
    assert changes["stats"] == {}  # the connection manager's cached "standing" is not copied over "sitting"
    assert harness.persistence.saves == 0
    view = harness.registry.peek(harness.player_id)
    assert view is not None and view.row.stats["position"] == "sitting"


@pytest.mark.asyncio
async def test_quit_stamps_last_active_without_saving_the_row() -> None:
    harness = _harness()

    result = await handle_quit_command({}, {"username": "tester"}, harness.request, None, "Tester")

    assert "Goodbye" in result["result"]
    changes = await _written_changes(harness)
    assert list(cast(dict[str, object], changes["columns"])) == ["last_active"]
    assert harness.persistence.saves == 0


@pytest.mark.asyncio
async def test_logout_without_a_registry_still_logs_the_player_out() -> None:
    harness = _harness(with_registry=False)

    result = await handle_logout_command({}, {"username": "tester"}, harness.request, None, "Tester")

    assert result["result"] == "Logged out successfully"
    assert result["session_terminated"] is True
    assert harness.persistence.saves == 0
