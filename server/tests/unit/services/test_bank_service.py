"""Unit tests for bank_service: lazy per-player deposit boxes, over-fill forwarding, bank-room flag."""

import asyncio
import uuid
from collections.abc import Mapping, Sequence
from uuid import UUID

import pytest

from server.exceptions import DatabaseError
from server.game.player_registry import PlayerRegistry
from server.models.room import Room
from server.persistence.container_create_params import ContainerCreateParams
from server.services.bank_service import (
    BANK_BOX_CAPACITY,
    forward_to_bank_box,
    get_or_create_bank_box,
    is_bank_room,
)
from server.tests.fixtures.shared.player_registry import FakeDatabase

BoxWrites = list[tuple[UUID, list[dict[str, object]]]]


@pytest.fixture
def box_writes(monkeypatch: pytest.MonkeyPatch) -> BoxWrites:
    """The bank box writes the registry committed, as (container_id, items), in place of the database's."""
    writes: BoxWrites = []

    async def record(_session: object, container_id: UUID, items_json: Sequence[Mapping[str, object]]) -> None:
        writes.append((container_id, [dict(item) for item in items_json]))

    monkeypatch.setattr("server.services.bank_service.write_container_items_async", record)
    return writes


def _registry() -> PlayerRegistry:
    return PlayerRegistry(FakeDatabase().session)


class FakeBankPersistence:
    """In-memory bank boxes. `race_winner` simulates losing a create race to a concurrent creator."""

    def __init__(self, *, race_winner: bool = False, race_leaves_nothing: bool = False) -> None:
        self.boxes: dict[UUID, dict[str, object]] = {}
        self.created: list[ContainerCreateParams] = []
        self._race_winner: bool = race_winner
        self._race_leaves_nothing: bool = race_leaves_nothing

    async def get_bank_container(self, owner_id: UUID) -> dict[str, object] | None:
        return self.boxes.get(owner_id)

    async def create_container(
        self, source_type: str, params: ContainerCreateParams | None = None
    ) -> dict[str, object]:
        assert params is not None and params.owner_id is not None
        self.created.append(params)
        if self._race_winner or self._race_leaves_nothing:
            if self._race_winner:
                self.boxes[params.owner_id] = _box(params.capacity_slots, [])
            raise DatabaseError("duplicate key value violates unique constraint uq_containers_bank_owner")
        box = _box(params.capacity_slots, [], source_type=source_type)
        self.boxes[params.owner_id] = box
        return box


def _box(capacity: int, items: list[dict[str, object]], source_type: str = "bank") -> dict[str, object]:
    return {
        "container_id": str(uuid.uuid4()),
        "source_type": source_type,
        "capacity_slots": capacity,
        "items_json": items,
    }


def _stack(item_id: str) -> dict[str, object]:
    return {"item_id": item_id, "item_instance_id": f"inst-{item_id}", "item_name": item_id, "quantity": 1}


@pytest.mark.asyncio
async def test_first_use_creates_a_bank_box_owned_by_the_player() -> None:
    persistence = FakeBankPersistence()
    owner_id = uuid.uuid4()

    box = await get_or_create_bank_box(persistence, owner_id)

    assert box["source_type"] == "bank"
    [params] = persistence.created
    assert params.owner_id == owner_id
    assert params.capacity_slots == BANK_BOX_CAPACITY == 100
    assert params.room_id is None  # a bank box lives in no room: look and room lookups never see it


@pytest.mark.asyncio
async def test_second_use_returns_the_same_box_instead_of_creating_another() -> None:
    persistence = FakeBankPersistence()
    owner_id = uuid.uuid4()

    first = await get_or_create_bank_box(persistence, owner_id)
    second = await get_or_create_bank_box(persistence, owner_id)

    assert second is first
    assert len(persistence.created) == 1


@pytest.mark.asyncio
async def test_each_player_gets_their_own_box() -> None:
    persistence = FakeBankPersistence()

    mine = await get_or_create_bank_box(persistence, uuid.uuid4())
    theirs = await get_or_create_bank_box(persistence, uuid.uuid4())

    assert mine["container_id"] != theirs["container_id"]


@pytest.mark.asyncio
async def test_losing_a_create_race_uses_the_winners_box() -> None:
    """uq_containers_bank_owner rejects the second creator; it must pick up the winner's box, not fail."""
    persistence = FakeBankPersistence(race_winner=True)
    owner_id = uuid.uuid4()

    box = await get_or_create_bank_box(persistence, owner_id)

    assert box is persistence.boxes[owner_id]


@pytest.mark.asyncio
async def test_a_create_failure_with_no_box_to_fall_back_on_is_raised() -> None:
    """If the create failed for a real reason (no winner exists), the error must not be swallowed."""
    persistence = FakeBankPersistence(race_leaves_nothing=True)

    with pytest.raises(DatabaseError):
        _ = await get_or_create_bank_box(persistence, uuid.uuid4())


@pytest.mark.asyncio
async def test_forward_creates_the_box_when_the_player_has_none(box_writes: BoxWrites) -> None:
    persistence = FakeBankPersistence()
    owner_id = uuid.uuid4()

    await forward_to_bank_box(persistence, _registry(), owner_id, [_stack("lantern")])

    [(container_id, items)] = box_writes
    assert str(container_id) == persistence.boxes[owner_id]["container_id"]
    assert items == [_stack("lantern")]


@pytest.mark.asyncio
async def test_forward_over_fills_a_full_box_rather_than_evicting(box_writes: BoxWrites) -> None:
    persistence = FakeBankPersistence()
    owner_id = uuid.uuid4()
    persistence.boxes[owner_id] = _box(2, [_stack("a"), _stack("b")])

    await forward_to_bank_box(persistence, _registry(), owner_id, [_stack("c"), _stack("d")])

    [(_, items)] = box_writes
    assert items == [_stack(name) for name in "abcd"]  # 4 stacks in a 2-slot box: nothing lost


@pytest.mark.parametrize(
    ("attributes", "expected"),
    [
        ({"bank": True}, True),
        ({"bank": False}, False),
        ({"bank": "true"}, False),  # only a literal JSON true counts
        ({"bank": 1}, False),
        ({"environment": "indoors"}, False),
        ({}, False),
    ],
)
def test_is_bank_room_only_for_a_literal_true_flag(attributes: dict[str, object], expected: bool) -> None:
    assert is_bank_room(Room({"id": "some_room", "attributes": attributes})) is expected


def test_is_bank_room_is_false_for_no_room() -> None:
    assert is_bank_room(None) is False


@pytest.mark.asyncio
async def test_forward_waits_for_a_unit_holding_the_box_then_appends_to_what_it_wrote(box_writes: BoxWrites) -> None:
    """A deposit (a registry unit holding the box's lock) and a forward can never overwrite each other (ADR-029)."""
    persistence = FakeBankPersistence()
    owner_id = uuid.uuid4()
    persistence.boxes[owner_id] = _box(100, [_stack("a")])
    box_id = UUID(str(persistence.boxes[owner_id]["container_id"]))
    registry = _registry()

    async with registry.mutate_many([], containers=[box_id]):
        forward = asyncio.create_task(forward_to_bank_box(persistence, registry, owner_id, [_stack("c")]))
        for _ in range(5):
            await asyncio.sleep(0)
        assert not forward.done()  # waiting for the box's lock
        persistence.boxes[owner_id] = {**persistence.boxes[owner_id], "items_json": [_stack("a"), _stack("b")]}
    await forward

    [(_, items)] = box_writes
    assert items == [_stack(name) for name in "abc"]  # read again under the lock: the deposit's "b" survives
