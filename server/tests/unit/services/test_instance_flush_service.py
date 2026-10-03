"""Unit tests for InstanceFlushService: instance floor items -> lost-and-found chest, then destroy."""

import uuid
from uuid import UUID

import pytest

from server.exceptions import DatabaseError
from server.game.instance_manager import InstanceManager
from server.models.room import Room
from server.realtime.room_subscription_manager import RoomSubscriptionManager
from server.services.instance_flush_service import InstanceFlushService, deposit_in_lost_and_found

BEDROOM_ID = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"
FOYER_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


class FakeChestPersistence:
    """Container rows for one room; records update_container writes."""

    def __init__(self, rows: list[dict[str, object]], *, fail: bool = False) -> None:
        self.rows: list[dict[str, object]] = rows
        self.fail: bool = fail
        self.writes: list[tuple[UUID, list[dict[str, object]] | None]] = []

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, object]]:
        if self.fail:
            raise DatabaseError("database unavailable")
        return [row for row in self.rows if row.get("room_id") == room_id]

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


def _chest(capacity: int, items: list[dict[str, object]], role: str = "lost_and_found") -> dict[str, object]:
    return {
        "container_id": str(uuid.uuid4()),
        "room_id": FOYER_ID,
        "source_type": "environment",
        "capacity_slots": capacity,
        "items_json": items,
        "metadata_json": {"name": "Lost-and-Found Chest", "role": role},
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
async def test_deposit_appends_to_the_lost_and_found_chest() -> None:
    chest = _chest(10, [_stack("old_sock")])
    persistence = FakeChestPersistence([_chest(10, [], role="decor"), chest])

    await deposit_in_lost_and_found(persistence, FOYER_ID, [_stack("lantern")])

    [(container_id, items)] = persistence.writes
    assert str(container_id) == chest["container_id"]
    assert items == [_stack("old_sock"), _stack("lantern")]


@pytest.mark.asyncio
async def test_deposit_evicts_oldest_stacks_when_full() -> None:
    """FIFO: the chest keeps the newest `capacity` stacks."""
    persistence = FakeChestPersistence([_chest(3, [_stack("a"), _stack("b"), _stack("c")])])

    await deposit_in_lost_and_found(persistence, FOYER_ID, [_stack("d"), _stack("e")])

    [(_, items)] = persistence.writes
    assert items == [_stack("c"), _stack("d"), _stack("e")]


@pytest.mark.asyncio
async def test_deposit_without_a_chest_writes_nothing() -> None:
    persistence = FakeChestPersistence([_chest(10, [], role="decor")])

    await deposit_in_lost_and_found(persistence, FOYER_ID, [_stack("lantern")])

    assert persistence.writes == []


@pytest.mark.asyncio
async def test_flush_moves_only_that_instances_drops_then_destroys_it() -> None:
    manager = _instance_manager()
    mine = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    other = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    drops = RoomSubscriptionManager()
    drops.room_drops = {
        next(iter(mine.rooms)): [_stack("lantern"), _stack("bandage")],
        next(iter(other.rooms)): [_stack("someone_elses")],
        FOYER_ID: [_stack("foyer_floor")],
    }
    persistence = FakeChestPersistence([_chest(200, [])])
    flusher = InstanceFlushService(manager, drops, persistence)

    moved = await flusher.flush(mine.instance_id)

    assert moved == 2
    assert manager.get_instance(mine.instance_id) is None
    assert manager.get_instance(other.instance_id) is not None
    assert next(iter(mine.rooms)) not in drops.room_drops
    assert drops.room_drops[next(iter(other.rooms))] == [_stack("someone_elses")]
    assert drops.room_drops[FOYER_ID] == [_stack("foyer_floor")]
    [(_, items)] = persistence.writes
    assert items == [_stack("lantern"), _stack("bandage")]


@pytest.mark.asyncio
async def test_flush_with_empty_floor_only_destroys() -> None:
    manager = _instance_manager()
    instance = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    persistence = FakeChestPersistence([_chest(200, [])])

    assert await InstanceFlushService(manager, RoomSubscriptionManager(), persistence).flush(instance.instance_id) == 0
    assert manager.get_instance(instance.instance_id) is None
    assert persistence.writes == []


@pytest.mark.asyncio
async def test_flush_survives_database_errors() -> None:
    """A failed deposit is logged; the instance is still gone and the caller (logout) carries on."""
    manager = _instance_manager()
    instance = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("lantern")]}

    flusher = InstanceFlushService(manager, drops, FakeChestPersistence([], fail=True))

    assert await flusher.flush(instance.instance_id) == 0
    assert manager.get_instance(instance.instance_id) is None


@pytest.mark.asyncio
async def test_flush_all_flushes_every_live_instance() -> None:
    manager = _instance_manager()
    first = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    second = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(first.rooms)): [_stack("a")], next(iter(second.rooms)): [_stack("b")]}
    persistence = FakeChestPersistence([_chest(200, [])])

    assert await InstanceFlushService(manager, drops, persistence).flush_all() == 2
    assert manager.list_instance_ids() == []
    assert drops.room_drops == {}
