"""Unit tests for InstanceFlushService: instance floor items -> the owner's bank box, then destroy."""

import uuid
from uuid import UUID

import pytest

from server.exceptions import DatabaseError
from server.game.instance_manager import InstanceManager
from server.models.room import Room
from server.persistence.container_create_params import ContainerCreateParams
from server.realtime.room_subscription_manager import RoomSubscriptionManager
from server.services.instance_flush_service import InstanceFlushService

BEDROOM_ID = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"
FOYER_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


class FakeBankPersistence:
    """Bank boxes keyed by owner; records update_container writes."""

    def __init__(self, boxes: dict[UUID, dict[str, object]] | None = None, *, fail: bool = False) -> None:
        self.boxes: dict[UUID, dict[str, object]] = boxes or {}
        self.fail: bool = fail
        self.writes: list[tuple[UUID, list[dict[str, object]] | None]] = []

    async def get_bank_container(self, owner_id: UUID) -> dict[str, object] | None:
        if self.fail:
            raise DatabaseError("database unavailable")
        return self.boxes.get(owner_id)

    async def create_container(
        self, source_type: str, params: ContainerCreateParams | None = None
    ) -> dict[str, object]:
        assert params is not None and params.owner_id is not None
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


def _stack(item_id: str) -> dict[str, object]:
    return {"item_id": item_id, "item_instance_id": f"inst-{item_id}", "item_name": item_id, "quantity": 1}


def _box(capacity: int, items: list[dict[str, object]], source_type: str = "bank") -> dict[str, object]:
    return {
        "container_id": str(uuid.uuid4()),
        "source_type": source_type,
        "capacity_slots": capacity,
        "items_json": items,
    }


def _instance_manager() -> InstanceManager:
    template = Room(
        {
            "id": BEDROOM_ID,
            "exits": {"down": FOYER_ID},
            "attributes": {"instance_template_id": "tutorial_sanitarium", "instance_exit_room_id": FOYER_ID},
        }
    )
    return InstanceManager(room_cache={BEDROOM_ID: template})


@pytest.mark.asyncio
async def test_flush_sends_only_that_instances_drops_to_its_owners_box_then_destroys_it() -> None:
    manager = _instance_manager()
    my_id, other_id = uuid.uuid4(), uuid.uuid4()
    mine = manager.create_instance("tutorial_sanitarium", my_id)
    other = manager.create_instance("tutorial_sanitarium", other_id)
    drops = RoomSubscriptionManager()
    drops.room_drops = {
        next(iter(mine.rooms)): [_stack("lantern"), _stack("bandage")],
        next(iter(other.rooms)): [_stack("someone_elses")],
        FOYER_ID: [_stack("foyer_floor")],
    }
    persistence = FakeBankPersistence()

    moved = await InstanceFlushService(manager, drops, persistence).flush(mine.instance_id)

    assert moved == 2
    assert manager.get_instance(mine.instance_id) is None
    assert manager.get_instance(other.instance_id) is not None
    assert next(iter(mine.rooms)) not in drops.room_drops
    assert drops.room_drops[next(iter(other.rooms))] == [_stack("someone_elses")]
    assert drops.room_drops[FOYER_ID] == [_stack("foyer_floor")]
    assert set(persistence.boxes) == {my_id}  # the other owner never got a box
    [(container_id, items)] = persistence.writes
    assert str(container_id) == persistence.boxes[my_id]["container_id"]
    assert items == [_stack("lantern"), _stack("bandage")]


@pytest.mark.asyncio
async def test_flush_appends_to_an_existing_box() -> None:
    manager = _instance_manager()
    owner_id = uuid.uuid4()
    instance = manager.create_instance("tutorial_sanitarium", owner_id)
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("lantern")]}
    persistence = FakeBankPersistence({owner_id: _box(100, [_stack("old_sock")])})

    _ = await InstanceFlushService(manager, drops, persistence).flush(instance.instance_id)

    [(_, items)] = persistence.writes
    assert items == [_stack("old_sock"), _stack("lantern")]


@pytest.mark.asyncio
async def test_flush_never_evicts_from_a_full_box() -> None:
    """A full box is over-filled, not trimmed: the player's deposits and the new losses all survive."""
    manager = _instance_manager()
    owner_id = uuid.uuid4()
    instance = manager.create_instance("tutorial_sanitarium", owner_id)
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("d"), _stack("e")]}
    persistence = FakeBankPersistence({owner_id: _box(3, [_stack("a"), _stack("b"), _stack("c")])})

    moved = await InstanceFlushService(manager, drops, persistence).flush(instance.instance_id)

    assert moved == 2
    [(_, items)] = persistence.writes
    assert items == [_stack(name) for name in "abcde"]


@pytest.mark.asyncio
async def test_flush_with_empty_floor_only_destroys() -> None:
    manager = _instance_manager()
    instance = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    persistence = FakeBankPersistence()

    assert await InstanceFlushService(manager, RoomSubscriptionManager(), persistence).flush(instance.instance_id) == 0
    assert manager.get_instance(instance.instance_id) is None
    assert persistence.boxes == {}  # no drops, so no box is created either
    assert persistence.writes == []


@pytest.mark.asyncio
async def test_flush_survives_database_errors() -> None:
    """A failed deposit is logged; the instance is still gone and the caller (logout) carries on."""
    manager = _instance_manager()
    instance = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("lantern")]}

    flusher = InstanceFlushService(manager, drops, FakeBankPersistence(fail=True))

    assert await flusher.flush(instance.instance_id) == 0
    assert manager.get_instance(instance.instance_id) is None


@pytest.mark.asyncio
async def test_flush_with_a_malformed_owner_id_loses_the_items_without_raising() -> None:
    manager = _instance_manager()
    instance = manager.create_instance("tutorial_sanitarium", "not-a-uuid")
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("lantern")]}
    persistence = FakeBankPersistence()

    assert await InstanceFlushService(manager, drops, persistence).flush(instance.instance_id) == 0
    assert manager.get_instance(instance.instance_id) is None
    assert persistence.writes == []


@pytest.mark.asyncio
async def test_flush_of_an_unknown_instance_with_leftover_drops_loses_them_without_raising() -> None:
    """No owner on record (instance already gone) means nowhere to send the stacks."""
    drops = RoomSubscriptionManager()
    drops.room_drops = {"instance_ghost_room": [_stack("lantern")]}
    persistence = FakeBankPersistence()

    assert await InstanceFlushService(_instance_manager(), drops, persistence).flush("instance_ghost") == 0
    assert drops.room_drops == {}
    assert persistence.writes == []


@pytest.mark.asyncio
async def test_flush_all_flushes_every_live_instance_into_each_owners_box() -> None:
    manager = _instance_manager()
    first_owner, second_owner = uuid.uuid4(), uuid.uuid4()
    first = manager.create_instance("tutorial_sanitarium", first_owner)
    second = manager.create_instance("tutorial_sanitarium", second_owner)
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(first.rooms)): [_stack("a")], next(iter(second.rooms)): [_stack("b")]}
    persistence = FakeBankPersistence()

    assert await InstanceFlushService(manager, drops, persistence).flush_all() == 2
    assert manager.list_instance_ids() == []
    assert drops.room_drops == {}
    assert set(persistence.boxes) == {first_owner, second_owner}
