"""Unit tests for instance_state: clearing what belongs only to a dead instance from a player."""

import json
import uuid
from collections.abc import AsyncIterator, Callable, Iterable
from typing import cast
from unittest.mock import AsyncMock, patch

import pytest

from server.constants.lucidity import STARTING_LCD
from server.game.instance_state import (
    _reset_lucidity,  # pyright: ignore[reportPrivateUsage]
    clear_lost_instance_items,
    restart_instance_run,
    strip_instance_bound_items,
)
from server.game.items.constants import INSTANCE_BOUND_FLAG
from server.game.player_registry import DbSession, PlayerAggregate, PlayerRegistry
from server.models.player import Player
from server.services.lucidity_service import resolve_tier
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, raw_row


def _player() -> Player:
    return Player(player_id=str(uuid.uuid4()), name="Tester")


def _stack(item_id: str, *flags: str) -> dict[str, object]:
    stack: dict[str, object] = {
        "item_id": item_id,
        "prototype_id": item_id,
        "item_name": item_id.replace("_", " ").title(),
        "slot_type": "inventory",
        "quantity": 1,
    }
    if flags:
        stack["flags"] = list(flags)
    return stack


def _world(
    carried: list[dict[str, object]] | None, equipped: dict[str, object] | None = None
) -> tuple[PlayerRegistry, FakeDatabase, uuid.UUID]:
    """A registry whose one player starts with ``carried`` and ``equipped`` (ADR-029); None: no such player."""
    db = FakeDatabase()
    player_id = uuid.uuid4()

    async def load(_session: DbSession, pid: uuid.UUID) -> PlayerAggregate | None:
        if carried is None:
            return None
        return aggregate(raw_row(pid, inventory=json.dumps(carried), equipped_json=json.dumps(equipped or {})))

    return PlayerRegistry(db.session, loader=load), db, player_id


def _committed(db: FakeDatabase) -> tuple[list[dict[str, object]], dict[str, object]]:
    write = db.last_inventory_write()
    assert write is not None, "nothing was committed"
    return (
        cast(list[dict[str, object]], json.loads(str(write["inventory_json"]))),
        cast(dict[str, object], json.loads(str(write["equipped_json"]))),
    )


async def test_strips_instance_bound_items_from_the_inventory_and_keeps_the_rest() -> None:
    registry, db, player_id = _world(
        [_stack("lantern"), _stack("jade_amulet", INSTANCE_BOUND_FLAG), _stack("tonic", "CONSUMABLE")]
    )

    stripped = await strip_instance_bound_items(registry, player_id)

    assert stripped.removed == 1
    carried, _equipped = _committed(db)
    assert [stack["item_id"] for stack in carried] == ["lantern", "tonic"]
    assert [stack["item_id"] for stack in stripped.carried] == ["lantern", "tonic"]  # what the caller mirrors
    assert db.commits == 1


async def test_strips_instance_bound_items_inside_a_carried_container() -> None:
    backpack = _stack("backpack")
    backpack["inner_container"] = {
        "capacity_slots": 10,
        "items": [_stack("jade_amulet", INSTANCE_BOUND_FLAG), _stack("bandage")],
    }
    registry, db, player_id = _world([backpack])

    assert (await strip_instance_bound_items(registry, player_id)).removed == 1

    [kept], _equipped = _committed(db)
    assert kept["item_id"] == "backpack"
    inner = cast(dict[str, list[dict[str, object]]], kept["inner_container"])
    assert [item["item_id"] for item in inner["items"]] == ["bandage"]


async def test_strips_instance_bound_items_that_are_equipped() -> None:
    registry, db, player_id = _world(
        [], {"amulet": _stack("jade_amulet", INSTANCE_BOUND_FLAG), "main_hand": _stack("cane")}
    )

    assert (await strip_instance_bound_items(registry, player_id)).removed == 1

    _carried, equipped = _committed(db)
    assert list(equipped) == ["main_hand"]


async def test_nothing_to_strip_writes_nothing() -> None:
    registry, db, player_id = _world([_stack("lantern")])

    stripped = await strip_instance_bound_items(registry, player_id)

    assert stripped.removed == 0
    assert db.executed == []


async def test_clearing_lost_instance_items_mirrors_the_commit_onto_the_connections_copy() -> None:
    registry, db, player_id = _world([_stack("lantern"), _stack("jade_amulet", INSTANCE_BOUND_FLAG)])
    player = Player(player_id=str(player_id), name="Restarted")
    player.set_inventory([_stack("lantern"), _stack("jade_amulet", INSTANCE_BOUND_FLAG)])

    await clear_lost_instance_items(registry, player)

    assert [stack["item_id"] for stack in _committed(db)[0]] == ["lantern"]
    assert [stack["item_id"] for stack in player.get_inventory()] == ["lantern"]


async def test_clearing_lost_instance_items_without_a_registry_or_on_failure_keeps_the_player_and_never_raises() -> (
    None
):
    player = Player(player_id=str(uuid.uuid4()), name="Restarted")
    player.set_inventory([_stack("jade_amulet", INSTANCE_BOUND_FLAG)])

    await clear_lost_instance_items(None, player)
    failing, _db, _player_id = _world(None)  # no such player: the strip raises inside
    await clear_lost_instance_items(failing, player)

    assert [stack["item_id"] for stack in player.get_inventory()] == ["jade_amulet"]


class _Quests:
    """Records the quest reset a run restart asks for."""

    calls: list[tuple[uuid.UUID, list[str]]]
    _error: Exception | None

    def __init__(self, error: Exception | None = None) -> None:
        self.calls = []
        self._error = error

    async def reset_offered_quests(self, player_id: uuid.UUID, room_ids: Iterable[str]) -> list[str]:
        self.calls.append((player_id, list(room_ids)))
        if self._error:
            raise self._error
        return []


@pytest.mark.asyncio
async def test_restart_instance_run_restores_dp_keeps_corruption_and_resets_lucidity_and_quests() -> None:
    player = _player()
    player.set_stats({"current_dp": 1, "max_dp": 100, "corruption": 3})
    quests = _Quests()

    with patch("server.game.instance_state._reset_lucidity", new=AsyncMock()) as reset_lucidity:
        await restart_instance_run(player, ["square", "walk"], quests)

    stats = player.get_stats()
    assert stats["current_dp"] == 100
    assert stats["corruption"] == 3
    reset_lucidity.assert_awaited_once_with(uuid.UUID(str(player.player_id)))
    assert quests.calls == [(uuid.UUID(str(player.player_id)), ["square", "walk"])]


class _LucidityRecord:
    current_lcd: int = 12
    current_tier: str = "fractured"


class _Session:
    commits: int = 0

    async def commit(self) -> None:
        self.commits += 1


class _LucidityRepository:
    """Stands in for LucidityRepository: hands back one record and remembers who was asked for."""

    record: _LucidityRecord
    asked_for: list[uuid.UUID]

    def __init__(self, record: _LucidityRecord) -> None:
        self.record = record
        self.asked_for = []

    async def get_or_create_player_lucidity(self, player_id: uuid.UUID) -> _LucidityRecord:
        self.asked_for.append(player_id)
        return self.record


def _repository_factory(repository: _LucidityRepository) -> Callable[[_Session], _LucidityRepository]:
    def build(_session: _Session) -> _LucidityRepository:
        return repository

    return build


@pytest.mark.asyncio
async def test_reset_lucidity_sets_the_starting_value_and_tier_and_commits() -> None:
    session = _Session()
    repository = _LucidityRepository(_LucidityRecord())
    player_id = uuid.uuid4()

    async def sessions() -> AsyncIterator[_Session]:
        yield session

    with (
        patch("server.database.get_async_session", new=sessions),
        patch("server.services.lucidity_repository.LucidityRepository", new=_repository_factory(repository)),
    ):
        await _reset_lucidity(player_id)

    assert repository.asked_for == [player_id]
    assert repository.record.current_lcd == STARTING_LCD
    assert repository.record.current_tier == resolve_tier(STARTING_LCD)
    assert session.commits == 1


@pytest.mark.asyncio
async def test_restart_instance_run_survives_a_failing_lucidity_or_quest_reset() -> None:
    player = _player()
    player.set_stats({"current_dp": 1, "max_dp": 100})
    quests = _Quests(error=RuntimeError("db down"))

    with patch("server.game.instance_state._reset_lucidity", new=AsyncMock(side_effect=RuntimeError("db down"))):
        await restart_instance_run(player, ["square"], quests)

    assert player.get_stats()["current_dp"] == 100
    assert len(quests.calls) == 1  # the quest reset still ran after the lucidity failure


@pytest.mark.asyncio
async def test_restart_instance_run_without_a_quest_service_still_restores_dp() -> None:
    player = _player()
    player.set_stats({"current_dp": 1, "max_dp": 100})

    with patch("server.game.instance_state._reset_lucidity", new=AsyncMock()):
        await restart_instance_run(player, ["square"], None)

    assert player.get_stats()["current_dp"] == 100
