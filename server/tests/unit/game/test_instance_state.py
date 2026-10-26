"""Unit tests for instance_state: clearing what belongs only to a dead instance from a player."""

import uuid
from collections.abc import AsyncIterator, Callable, Iterable
from typing import cast
from unittest.mock import AsyncMock, patch

import pytest

from server.constants.lucidity import STARTING_LCD
from server.game.instance_state import (
    INSTANCE_SCOPED_EFFECT_KEY,
    _reset_lucidity,  # pyright: ignore[reportPrivateUsage]
    reset_instance_scoped_state,
    restart_instance_run,
    strip_instance_bound_items,
    strip_instance_scoped_effects,
)
from server.game.items.constants import INSTANCE_BOUND_FLAG
from server.models.player import Player
from server.services.lucidity_service import resolve_tier


def _player() -> Player:
    return Player(player_id=str(uuid.uuid4()), name="Tester")


def _stack(item_id: str, *flags: str) -> dict[str, object]:
    stack: dict[str, object] = {"item_id": item_id, "prototype_id": item_id, "quantity": 1}
    if flags:
        stack["flags"] = list(flags)
    return stack


def test_strips_instance_bound_items_from_the_inventory_and_keeps_the_rest() -> None:
    player = _player()
    player.set_inventory([_stack("lantern"), _stack("jade_amulet", INSTANCE_BOUND_FLAG), _stack("tonic", "CONSUMABLE")])

    removed = strip_instance_bound_items(player)

    assert removed == 1
    assert [stack["item_id"] for stack in player.get_inventory()] == ["lantern", "tonic"]


def test_strips_instance_bound_items_inside_a_carried_container() -> None:
    backpack = _stack("backpack")
    backpack["inner_container"] = {"items": [_stack("jade_amulet", INSTANCE_BOUND_FLAG), _stack("bandage")]}
    player = _player()
    player.set_inventory([backpack])

    assert strip_instance_bound_items(player) == 1

    [kept] = player.get_inventory()
    assert kept["item_id"] == "backpack"
    inner = cast(dict[str, list[dict[str, object]]], kept["inner_container"])
    assert [item["item_id"] for item in inner["items"]] == ["bandage"]


def test_strips_instance_bound_items_that_are_equipped() -> None:
    player = _player()
    player.set_equipped_items(
        {"amulet": _stack("jade_amulet", INSTANCE_BOUND_FLAG), "main_hand": _stack("cane")}  # type: ignore[arg-type]
    )

    assert strip_instance_bound_items(player) == 1

    assert list(player.get_equipped_items()) == ["main_hand"]


def test_nothing_to_strip_changes_nothing() -> None:
    player = _player()
    player.set_inventory([_stack("lantern")])

    assert strip_instance_bound_items(player) == 0
    assert player.get_inventory() == [_stack("lantern")]


def test_strips_instance_scoped_status_effects_and_keeps_the_rest() -> None:
    player = _player()
    player.set_status_effects(
        [
            {"type": "lucidity_drain_over_time", INSTANCE_SCOPED_EFFECT_KEY: True},
            {"type": "heal_over_time", "healing": 1},
        ]
    )

    assert strip_instance_scoped_effects(player) == 1

    assert [effect["type"] for effect in player.get_status_effects()] == ["heal_over_time"]


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


def test_reset_instance_scoped_state_clears_items_and_effects_together() -> None:
    player = _player()
    player.set_inventory([_stack("jade_amulet", INSTANCE_BOUND_FLAG)])
    player.set_status_effects([{"type": "lucidity_drain_over_time", INSTANCE_SCOPED_EFFECT_KEY: True}])

    assert reset_instance_scoped_state(player) == 2

    assert player.get_inventory() == []
    assert player.get_status_effects() == []
