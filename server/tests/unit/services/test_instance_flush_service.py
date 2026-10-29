"""Unit tests for InstanceFlushService: instance floor items -> the owner's bank box, then destroy."""

import uuid
from collections.abc import Mapping, Sequence
from uuid import UUID

import pytest

from server.exceptions import DatabaseError
from server.game.instance_manager import Instance, InstanceManager
from server.game.items.constants import INSTANCE_BOUND_FLAG
from server.game.player_registry import PlayerRegistry
from server.models.room import Room
from server.persistence.container_create_params import ContainerCreateParams
from server.realtime.room_subscription_manager import RoomSubscriptionManager
from server.services.instance_flush_service import InstanceFlushService
from server.tests.fixtures.shared.player_registry import FakeDatabase

BEDROOM_ID = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"
FOYER_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


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
    """Bank boxes keyed by owner; records update_container writes."""

    def __init__(self, boxes: dict[UUID, dict[str, object]] | None = None, *, fail: bool = False) -> None:
        self.boxes: dict[UUID, dict[str, object]] = boxes or {}
        self.fail: bool = fail

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
async def test_flush_sends_only_that_instances_drops_to_its_owners_box_then_destroys_it(box_writes: BoxWrites) -> None:
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

    moved = await InstanceFlushService(manager, drops, persistence, _registry()).flush(mine.instance_id)

    assert moved == 2
    assert manager.get_instance(mine.instance_id) is None
    assert manager.get_instance(other.instance_id) is not None
    assert next(iter(mine.rooms)) not in drops.room_drops
    assert drops.room_drops[next(iter(other.rooms))] == [_stack("someone_elses")]
    assert drops.room_drops[FOYER_ID] == [_stack("foyer_floor")]
    assert set(persistence.boxes) == {my_id}  # the other owner never got a box
    [(container_id, items)] = box_writes
    assert str(container_id) == persistence.boxes[my_id]["container_id"]
    assert items == [_stack("lantern"), _stack("bandage")]


@pytest.mark.asyncio
async def test_flush_destroys_instance_bound_stacks_instead_of_banking_them(box_writes: BoxWrites) -> None:
    """An instance_bound item (a plot token) never leaves its instance: destroyed, not sent to the owner's box."""
    manager = _instance_manager()
    owner_id = uuid.uuid4()
    instance = manager.create_instance("tutorial_sanitarium", owner_id)
    amulet = {**_stack("jade_amulet"), "flags": [INSTANCE_BOUND_FLAG]}
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("lantern"), amulet]}
    persistence = FakeBankPersistence()

    moved = await InstanceFlushService(manager, drops, persistence, _registry()).flush(instance.instance_id)

    assert moved == 1
    [(_, items)] = box_writes
    assert items == [_stack("lantern")]


@pytest.mark.asyncio
async def test_flush_with_only_instance_bound_stacks_creates_no_box(box_writes: BoxWrites) -> None:
    manager = _instance_manager()
    instance = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [{**_stack("jade_amulet"), "flags": [INSTANCE_BOUND_FLAG]}]}
    persistence = FakeBankPersistence()

    assert await InstanceFlushService(manager, drops, persistence, _registry()).flush(instance.instance_id) == 0
    assert manager.get_instance(instance.instance_id) is None
    assert persistence.boxes == {}  # nothing worth banking, so no box is created for it
    assert box_writes == []


class FakeContent:
    """Stands in for InstanceContentService.teardown; records whether the instance still existed when it ran."""

    def __init__(self, manager: InstanceManager, recovered: list[dict[str, object]]) -> None:
        self._manager: InstanceManager = manager
        self.recovered: list[dict[str, object]] = recovered
        self.torn_down: list[tuple[str, bool]] = []

    async def populate(self, instance: Instance) -> None:
        _ = instance

    async def teardown(self, instance: Instance) -> list[dict[str, object]]:
        self.torn_down.append((instance.instance_id, self._manager.get_instance(instance.instance_id) is not None))
        return self.recovered


@pytest.mark.asyncio
async def test_flush_tears_down_content_first_and_banks_what_its_containers_held(box_writes: BoxWrites) -> None:
    """Container contents are banked with the floor drops (instance-bound ones destroyed); teardown runs pre-destroy."""
    manager = _instance_manager()
    owner_id = uuid.uuid4()
    instance = manager.create_instance("tutorial_sanitarium", owner_id)
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("lantern")]}
    amulet = {**_stack("jade_amulet"), "flags": [INSTANCE_BOUND_FLAG]}
    content = FakeContent(manager, [_stack("sword"), amulet])
    persistence = FakeBankPersistence()
    flusher = InstanceFlushService(manager, drops, persistence, _registry())
    flusher.attach_content(content)

    moved = await flusher.flush(instance.instance_id)

    assert content.torn_down == [(instance.instance_id, True)]  # ran while the instance still existed
    assert manager.get_instance(instance.instance_id) is None
    assert moved == 2
    [(_, items)] = box_writes
    assert items == [_stack("lantern"), _stack("sword")]


@pytest.mark.asyncio
async def test_flush_of_an_unknown_instance_skips_content_teardown() -> None:
    manager = _instance_manager()
    content = FakeContent(manager, [_stack("sword")])
    flusher = InstanceFlushService(manager, RoomSubscriptionManager(), FakeBankPersistence(), _registry())
    flusher.attach_content(content)

    assert await flusher.flush("instance_ghost") == 0
    assert content.torn_down == []


@pytest.mark.asyncio
async def test_flush_appends_to_an_existing_box(box_writes: BoxWrites) -> None:
    manager = _instance_manager()
    owner_id = uuid.uuid4()
    instance = manager.create_instance("tutorial_sanitarium", owner_id)
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("lantern")]}
    persistence = FakeBankPersistence({owner_id: _box(100, [_stack("old_sock")])})

    _ = await InstanceFlushService(manager, drops, persistence, _registry()).flush(instance.instance_id)

    [(_, items)] = box_writes
    assert items == [_stack("old_sock"), _stack("lantern")]


@pytest.mark.asyncio
async def test_flush_never_evicts_from_a_full_box(box_writes: BoxWrites) -> None:
    """A full box is over-filled, not trimmed: the player's deposits and the new losses all survive."""
    manager = _instance_manager()
    owner_id = uuid.uuid4()
    instance = manager.create_instance("tutorial_sanitarium", owner_id)
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("d"), _stack("e")]}
    persistence = FakeBankPersistence({owner_id: _box(3, [_stack("a"), _stack("b"), _stack("c")])})

    moved = await InstanceFlushService(manager, drops, persistence, _registry()).flush(instance.instance_id)

    assert moved == 2
    [(_, items)] = box_writes
    assert items == [_stack(name) for name in "abcde"]


@pytest.mark.asyncio
async def test_flush_with_empty_floor_only_destroys(box_writes: BoxWrites) -> None:
    manager = _instance_manager()
    instance = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    persistence = FakeBankPersistence()

    assert (
        await InstanceFlushService(manager, RoomSubscriptionManager(), persistence, _registry()).flush(
            instance.instance_id
        )
        == 0
    )
    assert manager.get_instance(instance.instance_id) is None
    assert persistence.boxes == {}  # no drops, so no box is created either
    assert box_writes == []


@pytest.mark.asyncio
async def test_flush_survives_database_errors() -> None:
    """A failed deposit is logged; the instance is still gone and the caller (logout) carries on."""
    manager = _instance_manager()
    instance = manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("lantern")]}

    flusher = InstanceFlushService(manager, drops, FakeBankPersistence(fail=True), _registry())

    assert await flusher.flush(instance.instance_id) == 0
    assert manager.get_instance(instance.instance_id) is None


@pytest.mark.asyncio
async def test_flush_with_a_malformed_owner_id_loses_the_items_without_raising(box_writes: BoxWrites) -> None:
    manager = _instance_manager()
    instance = manager.create_instance("tutorial_sanitarium", "not-a-uuid")
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(instance.rooms)): [_stack("lantern")]}
    persistence = FakeBankPersistence()

    assert await InstanceFlushService(manager, drops, persistence, _registry()).flush(instance.instance_id) == 0
    assert manager.get_instance(instance.instance_id) is None
    assert box_writes == []


@pytest.mark.asyncio
async def test_flush_of_an_unknown_instance_with_leftover_drops_loses_them_without_raising(
    box_writes: BoxWrites,
) -> None:
    """No owner on record (instance already gone) means nowhere to send the stacks."""
    drops = RoomSubscriptionManager()
    drops.room_drops = {"instance_ghost_room": [_stack("lantern")]}
    persistence = FakeBankPersistence()

    assert await InstanceFlushService(_instance_manager(), drops, persistence, _registry()).flush("instance_ghost") == 0
    assert drops.room_drops == {}
    assert box_writes == []


@pytest.mark.asyncio
async def test_flush_all_flushes_every_live_instance_into_each_owners_box() -> None:
    manager = _instance_manager()
    first_owner, second_owner = uuid.uuid4(), uuid.uuid4()
    first = manager.create_instance("tutorial_sanitarium", first_owner)
    second = manager.create_instance("tutorial_sanitarium", second_owner)
    drops = RoomSubscriptionManager()
    drops.room_drops = {next(iter(first.rooms)): [_stack("a")], next(iter(second.rooms)): [_stack("b")]}
    persistence = FakeBankPersistence()

    assert await InstanceFlushService(manager, drops, persistence, _registry()).flush_all() == 2
    assert manager.list_instance_ids() == []
    assert drops.room_drops == {}
    assert set(persistence.boxes) == {first_owner, second_owner}
