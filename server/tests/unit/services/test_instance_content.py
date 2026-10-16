"""Unit tests for InstanceContentService: furniture, floor items and NPCs of an instance, created and torn down."""

from typing import final
from uuid import UUID, uuid4

import pytest

from server.exceptions import DatabaseError
from server.game.instance_manager import Instance, InstanceManager
from server.game.items.item_factory import ItemFactory
from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry
from server.models.room import Room
from server.persistence.container_create_params import ContainerCreateParams
from server.services.instance_content import InstanceContentService

CHEST_ID = "furniture.demo.chest"
TONIC_ID = "consumable.folk_tonic"
TEMPLATE_ID = "demo"
SQUARE_ID = "earth_demo_zone_room_square_001"
WALK_ID = "earth_demo_zone_room_walk_001"


@final
class FakeContainerPersistence:
    """Container rows keyed like AsyncPersistenceLayer's; records deletions."""

    def __init__(self, *, fail_on_delete: bool = False) -> None:
        self.rows: list[dict[str, object]] = []
        self.deleted: list[UUID] = []
        self.fail_on_delete: bool = fail_on_delete

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, object]]:
        return [row for row in self.rows if row.get("room_id") == room_id]

    async def create_container(
        self, source_type: str, params: ContainerCreateParams | None = None
    ) -> dict[str, object]:
        assert params is not None
        row: dict[str, object] = {
            "container_id": str(uuid4()),
            "room_id": params.room_id,
            "source_type": source_type,
            "items_json": list(params.items_json or []),
            "metadata_json": dict(params.metadata_json or {}),
        }
        self.rows.append(row)
        return row

    async def update_container(
        self,
        container_id: UUID,
        items_json: list[dict[str, object]] | None = None,
        lock_state: str | None = None,
        metadata_json: dict[str, object] | None = None,
        capacity_slots: int | None = None,
    ) -> dict[str, object] | None:
        _ = (container_id, items_json, lock_state, metadata_json, capacity_slots)
        return {}

    async def delete_container(self, container_id: UUID) -> bool:
        if self.fail_on_delete:
            raise DatabaseError("database unavailable")
        self.deleted.append(container_id)
        self.rows = [row for row in self.rows if row["container_id"] != str(container_id)]
        return True


@final
class FakeDrops:
    """Records floor drops."""

    def __init__(self) -> None:
        self.drops: list[tuple[str, dict[str, object]]] = []

    def add_room_drop(self, room_id: str, stack: dict[str, object]) -> None:
        self.drops.append((room_id, stack))


@final
class FakeNpcHost:
    """Records NPC spawns and despawns; names in `unknown` fail to spawn."""

    def __init__(self, unknown: frozenset[str] | None = None) -> None:
        self.spawned: list[tuple[str, str]] = []
        self.despawned_prefixes: list[str] = []
        self.unknown: frozenset[str] = unknown or frozenset()

    def spawn(self, definition_name: str, room_id: str) -> str | None:
        if definition_name in self.unknown:
            return None
        self.spawned.append((definition_name, room_id))
        return f"npc-{len(self.spawned)}"

    def despawn_in_rooms(self, room_prefix: str) -> int:
        self.despawned_prefixes.append(room_prefix)
        return 1


def _prototype(prototype_id: str, name: str, item_type: str, metadata: dict[str, object]) -> ItemPrototypeModel:
    return ItemPrototypeModel.model_validate(
        {
            "prototype_id": prototype_id,
            "name": name,
            "short_description": name.lower(),
            "long_description": f"A {name.lower()}.",
            "item_type": item_type,
            "weight": 1.0,
            "base_value": 0,
            "metadata": metadata,
        }
    )


@pytest.fixture
def registry() -> PrototypeRegistry:
    return PrototypeRegistry(
        {
            CHEST_ID: _prototype(CHEST_ID, "Chest", "container", {"container": {"capacity_slots": 20}}),
            TONIC_ID: _prototype(TONIC_ID, "Folk Tonic", "consumable", {}),
        },
        [],
    )


def _instance(owner: UUID | None = None) -> Instance:
    """A two-room instance: the square carries furniture, a floor item and an NPC; the walk is bare."""
    square = Room(
        {
            "id": SQUARE_ID,
            "attributes": {
                "instance_template_id": TEMPLATE_ID,
                "instance_start": True,
                "furniture": [{"prototype_id": CHEST_ID}],
                "items": [{"prototype_id": TONIC_ID, "quantity": 1}],
                "instance_npcs": ["Lamplighter"],
            },
        }
    )
    walk = Room({"id": WALK_ID, "attributes": {"instance_template_id": TEMPLATE_ID}})
    manager = InstanceManager(room_cache={SQUARE_ID: square, WALK_ID: walk})
    return manager.create_instance(TEMPLATE_ID, owner or uuid4())


def _service(
    registry: PrototypeRegistry,
    persistence: FakeContainerPersistence,
    drops: FakeDrops,
    npcs: FakeNpcHost | None,
) -> InstanceContentService:
    return InstanceContentService(persistence, registry, ItemFactory(registry), drops, npcs)


@pytest.mark.asyncio
async def test_populate_places_furniture_items_and_npcs_in_the_instance_rooms(registry: PrototypeRegistry) -> None:
    instance = _instance()
    square_id = f"{instance.instance_id}_{SQUARE_ID}"
    persistence, drops, npcs = FakeContainerPersistence(), FakeDrops(), FakeNpcHost()

    await _service(registry, persistence, drops, npcs).populate(instance)

    [chest] = persistence.rows
    assert chest["room_id"] == square_id
    [(drop_room, stack)] = drops.drops
    assert drop_room == square_id
    assert stack["prototype_id"] == TONIC_ID
    assert npcs.spawned == [("Lamplighter", square_id)]


@pytest.mark.asyncio
async def test_populate_survives_an_npc_that_cannot_spawn(registry: PrototypeRegistry) -> None:
    """A missing NPC definition must not stop the rest of the instance from being populated."""
    instance = _instance()
    persistence, drops = FakeContainerPersistence(), FakeDrops()
    npcs = FakeNpcHost(unknown=frozenset({"Lamplighter"}))

    await _service(registry, persistence, drops, npcs).populate(instance)

    assert npcs.spawned == []
    assert len(persistence.rows) == 1
    assert len(drops.drops) == 1


@pytest.mark.asyncio
async def test_populate_without_an_npc_host_still_places_furniture_and_items(registry: PrototypeRegistry) -> None:
    instance = _instance()
    persistence, drops = FakeContainerPersistence(), FakeDrops()

    await _service(registry, persistence, drops, None).populate(instance)

    assert len(persistence.rows) == 1
    assert len(drops.drops) == 1


@pytest.mark.asyncio
async def test_populate_skips_malformed_npc_entries(registry: PrototypeRegistry) -> None:
    instance = _instance()
    square = instance.rooms[f"{instance.instance_id}_{SQUARE_ID}"]
    square.attributes["instance_npcs"] = ["Lamplighter", 7, "", None]
    npcs = FakeNpcHost()

    await _service(registry, FakeContainerPersistence(), FakeDrops(), npcs).populate(instance)

    assert [name for name, _ in npcs.spawned] == ["Lamplighter"]


@pytest.mark.asyncio
async def test_teardown_despawns_npcs_deletes_containers_and_returns_their_contents(
    registry: PrototypeRegistry,
) -> None:
    mine, other = _instance(), _instance()
    persistence, drops, npcs = FakeContainerPersistence(), FakeDrops(), FakeNpcHost()
    service = _service(registry, persistence, drops, npcs)
    await service.populate(mine)
    await service.populate(other)
    kept = {"item_id": "lantern", "item_name": "Lantern", "quantity": 1}
    for row in persistence.rows:
        if str(row["room_id"]).startswith(mine.instance_id):
            row["items_json"] = [kept]

    recovered = await service.teardown(mine)

    assert npcs.despawned_prefixes == [f"{mine.instance_id}_"]
    assert recovered == [kept]
    assert [row["room_id"] for row in persistence.rows] == [f"{other.instance_id}_{SQUARE_ID}"]
    assert len(persistence.deleted) == 1


@pytest.mark.asyncio
async def test_teardown_survives_a_database_error(registry: PrototypeRegistry) -> None:
    """A failed container delete is logged; teardown still finishes so the instance can be destroyed."""
    instance = _instance()
    persistence = FakeContainerPersistence(fail_on_delete=True)
    service = _service(registry, persistence, FakeDrops(), FakeNpcHost())
    await service.populate(instance)

    assert await service.teardown(instance) == []
