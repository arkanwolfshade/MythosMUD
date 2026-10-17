"""Unit tests for the command-layer glue that builds an action context and runs container on_put rules."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast, override

import pytest

from server.commands import scripted_action_support as support
from server.game.scripted_actions import ScriptedActionContext
from server.models.player import Player
from server.schemas.scripted_actions import NarrateAction, ScriptedAction

ON_PUT_METADATA: dict[str, object] = {
    "name": "coffin",
    "on_put": [{"item": "jade_amulet", "actions": [{"type": "narrate", "text": "The lid settles."}]}],
}


@dataclass
class FakePersistence:
    containers: dict[uuid.UUID, dict[str, object]] = field(
        default_factory=lambda: cast(dict[uuid.UUID, dict[str, object]], {})
    )

    async def get_container(self, container_id: uuid.UUID) -> dict[str, object] | None:
        return self.containers.get(container_id)

    async def get_player_by_id(self, player_id: uuid.UUID) -> None:  # pragma: no cover - never read here
        _ = player_id

    async def save_player(self, player: Player) -> None:  # pragma: no cover - never reached here
        _ = player


def _player() -> Player:
    return Player(player_id=str(uuid.uuid4()), name="Tester")


def _app(quest_service: object | None) -> object:
    return SimpleNamespace(state=SimpleNamespace(container=SimpleNamespace(quest_service=quest_service)))


def test_action_context_wires_the_player_persistence_and_quest_service() -> None:
    player = _player()
    persistence = FakePersistence()
    quests = SimpleNamespace()

    ctx = support.action_context(_app(quests), player, persistence)

    assert ctx is not None
    assert ctx.player is player
    assert ctx.persistence is persistence
    assert ctx.quest_service is quests


def test_action_context_tolerates_an_app_without_a_quest_service() -> None:
    ctx = support.action_context(_app(None), _player(), FakePersistence())

    assert ctx is not None
    assert ctx.quest_service is None


def test_action_context_is_none_without_a_real_player_or_persistence() -> None:
    assert support.action_context(_app(None), object(), FakePersistence()) is None
    assert support.action_context(_app(None), _player(), None) is None


@pytest.fixture(name="ran")
def _ran(monkeypatch: pytest.MonkeyPatch) -> list[list[ScriptedAction]]:
    ran: list[list[ScriptedAction]] = []

    async def fake_run(actions: list[ScriptedAction], ctx: ScriptedActionContext) -> None:
        _ = ctx
        ran.append(list(actions))

    monkeypatch.setattr(support, "run_scripted_actions", fake_run)
    return ran


@pytest.mark.asyncio
async def test_run_on_put_runs_the_actions_for_the_item_put(ran: list[list[ScriptedAction]]) -> None:
    container_id = uuid.uuid4()
    persistence = FakePersistence({container_id: {"metadata_json": ON_PUT_METADATA}})

    await support.run_on_put(_app(None), persistence, _player(), container_id, "jade_amulet")

    assert ran == [[NarrateAction(text="The lid settles.")]]


@pytest.mark.asyncio
async def test_run_on_put_ignores_other_items(ran: list[list[ScriptedAction]]) -> None:
    container_id = uuid.uuid4()
    persistence = FakePersistence({container_id: {"metadata_json": ON_PUT_METADATA}})

    await support.run_on_put(_app(None), persistence, _player(), container_id, "wrench")

    assert ran == []


@pytest.mark.asyncio
async def test_run_on_put_ignores_unknown_containers_and_unidentified_items(ran: list[list[ScriptedAction]]) -> None:
    persistence = FakePersistence()

    await support.run_on_put(_app(None), persistence, _player(), uuid.uuid4(), "jade_amulet")
    await support.run_on_put(_app(None), persistence, _player(), uuid.uuid4(), None)

    assert ran == []


class ExplodingPersistence(FakePersistence):
    @override
    async def get_container(self, container_id: uuid.UUID) -> dict[str, object] | None:
        raise RuntimeError("database unavailable")


@pytest.mark.asyncio
async def test_run_on_put_swallows_a_lookup_failure_because_the_put_already_succeeded(
    ran: list[list[ScriptedAction]],
) -> None:
    await support.run_on_put(_app(None), ExplodingPersistence(), _player(), uuid.uuid4(), "jade_amulet")

    assert ran == []
