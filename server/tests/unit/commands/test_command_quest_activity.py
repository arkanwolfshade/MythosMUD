"""Unit tests for cmd_<name> quest activity: commands typed inside an instance count toward quest goals."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast

import pytest

from server.commands.command_quest_activity import record_command_activity

INSTANCE_ROOM = f"instance_{uuid.uuid4()}_earth_arkham_dusk_room_001"
WORLD_ROOM = "earth_arkhamcity_downtown_001"


@dataclass
class FakeQuests:
    activity: list[tuple[uuid.UUID, str]] = field(default_factory=lambda: cast(list[tuple[uuid.UUID, str]], []))

    async def record_complete_activity(self, player_id: uuid.UUID, activity_target: str) -> None:
        self.activity.append((player_id, activity_target))


@dataclass
class FakePersistence:
    room_id: str | None
    player_id: uuid.UUID = field(default_factory=uuid.uuid4)
    lookups: list[str] = field(default_factory=lambda: cast(list[str], []))
    fail: bool = False

    async def get_player_by_name(self, name: str) -> SimpleNamespace | None:
        self.lookups.append(name)
        if self.fail:
            raise RuntimeError("database unavailable")
        if self.room_id is None:
            return None
        return SimpleNamespace(player_id=str(self.player_id), current_room_id=self.room_id)


@dataclass
class FakeInstances:
    ids: list[str]

    def list_instance_ids(self) -> list[str]:
        return self.ids


def _request(persistence: FakePersistence | None, quests: FakeQuests | None, instances: FakeInstances | None) -> object:
    container = SimpleNamespace(async_persistence=persistence, quest_service=quests, instance_manager=instances)
    return SimpleNamespace(app=SimpleNamespace(state=SimpleNamespace(container=container)))


@pytest.mark.asyncio
async def test_a_command_typed_inside_an_instance_is_recorded_as_cmd_activity() -> None:
    persistence, quests = FakePersistence(INSTANCE_ROOM), FakeQuests()

    await record_command_activity("look", "Tester", _request(persistence, quests, FakeInstances(["i1"])))

    assert quests.activity == [(persistence.player_id, "cmd_look")]
    assert persistence.lookups == ["Tester"]


@pytest.mark.asyncio
async def test_nothing_is_looked_up_while_no_instance_is_live() -> None:
    persistence, quests = FakePersistence(INSTANCE_ROOM), FakeQuests()

    await record_command_activity("look", "Tester", _request(persistence, quests, FakeInstances([])))

    assert persistence.lookups == []
    assert quests.activity == []


@pytest.mark.asyncio
async def test_a_command_typed_in_the_ordinary_world_is_not_recorded() -> None:
    persistence, quests = FakePersistence(WORLD_ROOM), FakeQuests()

    await record_command_activity("look", "Tester", _request(persistence, quests, FakeInstances(["i1"])))

    assert quests.activity == []


@pytest.mark.asyncio
async def test_an_unknown_player_is_not_recorded() -> None:
    quests = FakeQuests()

    await record_command_activity("look", "Ghost", _request(FakePersistence(None), quests, FakeInstances(["i1"])))

    assert quests.activity == []


@pytest.mark.asyncio
@pytest.mark.parametrize("missing", ["request", "persistence", "quests", "instances"])
async def test_missing_services_are_a_quiet_no_op(missing: str) -> None:
    persistence, quests, instances = FakePersistence(INSTANCE_ROOM), FakeQuests(), FakeInstances(["i1"])
    request: object | None = _request(
        None if missing == "persistence" else persistence,
        None if missing == "quests" else quests,
        None if missing == "instances" else instances,
    )
    if missing == "request":
        request = None

    await record_command_activity("look", "Tester", request)

    assert quests.activity == []


@pytest.mark.asyncio
async def test_a_failure_while_recording_never_reaches_the_command() -> None:
    persistence, quests = FakePersistence(INSTANCE_ROOM, fail=True), FakeQuests()

    await record_command_activity("look", "Tester", _request(persistence, quests, FakeInstances(["i1"])))

    assert quests.activity == []
