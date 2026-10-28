"""Unit tests for bank_service: lazy per-player deposit boxes, over-fill forwarding, bank-room flag."""

import uuid
from uuid import UUID

import pytest

from server.exceptions import DatabaseError
from server.models.room import Room
from server.persistence.container_create_params import ContainerCreateParams
from server.services.bank_service import (
    BANK_BOX_CAPACITY,
    forward_to_bank_box,
    get_or_create_bank_box,
    is_bank_room,
)


class FakeBankPersistence:
    """In-memory bank boxes. `race_winner` simulates losing a create race to a concurrent creator."""

    def __init__(self, *, race_winner: bool = False, race_leaves_nothing: bool = False) -> None:
        self.boxes: dict[UUID, dict[str, object]] = {}
        self.created: list[ContainerCreateParams] = []
        self.writes: list[tuple[UUID, list[dict[str, object]] | None]] = []
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

    async def update_container(
        self,
        container_id: UUID,
        items_json: list[dict[str, object]] | None = None,
        lock_state: str | None = None,
        metadata_json: dict[str, object] | None = None,
        capacity_slots: int | None = None,
    ) -> dict[str, object] | None:
        _ = (lock_state, metadata_json, capacity_slots)
        self.writes.append((container_id, items_json))
        return {}


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
async def test_forward_creates_the_box_when_the_player_has_none() -> None:
    persistence = FakeBankPersistence()
    owner_id = uuid.uuid4()

    await forward_to_bank_box(persistence, owner_id, [_stack("lantern")])

    [(container_id, items)] = persistence.writes
    assert str(container_id) == persistence.boxes[owner_id]["container_id"]
    assert items == [_stack("lantern")]


@pytest.mark.asyncio
async def test_forward_over_fills_a_full_box_rather_than_evicting() -> None:
    persistence = FakeBankPersistence()
    owner_id = uuid.uuid4()
    persistence.boxes[owner_id] = _box(2, [_stack("a"), _stack("b")])

    await forward_to_bank_box(persistence, owner_id, [_stack("c"), _stack("d")])

    [(_, items)] = persistence.writes
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
