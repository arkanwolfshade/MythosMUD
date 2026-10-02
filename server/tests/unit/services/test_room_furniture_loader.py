"""Unit tests for the room furniture loader (rooms.attributes.furniture -> environment containers)."""

from uuid import UUID, uuid4

import pytest

from server.exceptions import DatabaseError
from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry
from server.models.room import Room
from server.persistence.container_create_params import ContainerCreateParams
from server.services.room_furniture_loader import initialize_room_furniture, sync_room_furniture

CHEST_ID = "furniture.sanitarium.lost_and_found_chest"
ROCK_ID = "junk.rock"
FOYER_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


class FakePersistence:
    """Records container calls; rows are plain dicts shaped like AsyncPersistenceLayer's."""

    def __init__(self, rows: list[dict[str, object]] | None = None) -> None:
        self.rows: list[dict[str, object]] = rows or []
        self.created: list[tuple[str, ContainerCreateParams | None]] = []
        self.updated: list[tuple[UUID, dict[str, object] | None, int | None, object]] = []

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, object]]:
        return [row for row in self.rows if row.get("room_id") == room_id]

    async def create_container(
        self, source_type: str, params: ContainerCreateParams | None = None
    ) -> dict[str, object]:
        self.created.append((source_type, params))
        return {"container_id": str(uuid4())}

    async def update_container(
        self,
        container_id: UUID,
        items_json: list[dict[str, object]] | None = None,
        lock_state: str | None = None,
        metadata_json: dict[str, object] | None = None,
        capacity_slots: int | None = None,
    ) -> dict[str, object] | None:
        _ = lock_state
        self.updated.append((container_id, metadata_json, capacity_slots, items_json))
        return {}


def _prototype(prototype_id: str, name: str, metadata: dict[str, object]) -> ItemPrototypeModel:
    return ItemPrototypeModel.model_validate(
        {
            "prototype_id": prototype_id,
            "name": name,
            "short_description": name.lower(),
            "long_description": f"A {name.lower()}.",
            "item_type": "container",
            "weight": 1.0,
            "base_value": 0,
            "durability": None,
            "flags": [],
            "wear_slots": [],
            "stacking_rules": {},
            "usage_restrictions": {},
            "effect_components": [],
            "metadata": metadata,
            "tags": [],
        }
    )


@pytest.fixture
def registry() -> PrototypeRegistry:
    return PrototypeRegistry(
        {
            CHEST_ID: _prototype(CHEST_ID, "Lost-and-Found Chest", {"container": {"capacity_slots": 200}}),
            ROCK_ID: _prototype(ROCK_ID, "Rock", {}),
        },
        [],
    )


def _room(room_id: str, attributes: dict[str, object]) -> Room:
    return Room({"id": room_id, "attributes": attributes})


def _foyer(furniture: object) -> Room:
    return _room(FOYER_ID, {"furniture": furniture})


CHEST_FURNITURE = [{"prototype_id": CHEST_ID, "role": "lost_and_found"}]


@pytest.mark.asyncio
async def test_creates_missing_furniture_container(registry: PrototypeRegistry) -> None:
    persistence = FakePersistence()

    count = await sync_room_furniture([_foyer(CHEST_FURNITURE)], registry, persistence)

    assert count == 1
    [(source_type, params)] = persistence.created
    assert source_type == "environment"
    assert params is not None
    assert params.room_id == FOYER_ID
    assert params.capacity_slots == 200
    assert params.lock_state == "unlocked"
    assert params.metadata_json == {"name": "Lost-and-Found Chest", "prototype_id": CHEST_ID, "role": "lost_and_found"}
    assert params.items_json is None


@pytest.mark.asyncio
async def test_refreshes_existing_container_from_prototype_without_touching_items(
    registry: PrototypeRegistry,
) -> None:
    container_id = uuid4()
    persistence = FakePersistence(
        [
            {
                "container_id": str(container_id),
                "room_id": FOYER_ID,
                "source_type": "environment",
                "capacity_slots": 20,
                "items_json": [{"item_id": "lost_sock"}],
                "metadata_json": {"name": "Old Chest", "prototype_id": CHEST_ID, "role": "lost_and_found"},
            }
        ]
    )

    count = await sync_room_furniture([_foyer(CHEST_FURNITURE)], registry, persistence)

    assert count == 1
    assert persistence.created == []
    [(updated_id, metadata, capacity, items)] = persistence.updated
    assert updated_id == container_id
    assert metadata == {"name": "Lost-and-Found Chest", "prototype_id": CHEST_ID, "role": "lost_and_found"}
    assert capacity == 200
    assert items is None


@pytest.mark.asyncio
async def test_up_to_date_container_is_left_alone(registry: PrototypeRegistry) -> None:
    persistence = FakePersistence(
        [
            {
                "container_id": str(uuid4()),
                "room_id": FOYER_ID,
                "source_type": "environment",
                "capacity_slots": 200,
                "metadata_json": {"name": "Lost-and-Found Chest", "prototype_id": CHEST_ID, "role": "lost_and_found"},
            }
        ]
    )

    count = await sync_room_furniture([_foyer(CHEST_FURNITURE)], registry, persistence)

    assert count == 1
    assert persistence.created == []
    assert persistence.updated == []


@pytest.mark.asyncio
async def test_skips_template_rooms_bad_entries_and_non_container_prototypes(registry: PrototypeRegistry) -> None:
    template = _room(
        "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001",
        {"instance_template_id": "tutorial_sanitarium", "furniture": CHEST_FURNITURE},
    )
    rooms = [
        template,
        _foyer("not a list"),
        _room("room_unknown_proto", {"furniture": [{"prototype_id": "no.such.prototype"}]}),
        _room("room_not_container", {"furniture": [{"prototype_id": ROCK_ID}]}),
        _room(
            "room_malformed",
            {"furniture": [{"role": "lost_and_found"}, "chest", {"prototype_id": CHEST_ID, "role": 7}]},
        ),
        _room("room_plain", {}),
    ]
    persistence = FakePersistence()

    count = await sync_room_furniture(rooms, registry, persistence)

    assert count == 0
    assert persistence.created == []
    assert persistence.updated == []


@pytest.mark.asyncio
async def test_undeclared_furniture_container_is_kept(registry: PrototypeRegistry) -> None:
    """A container whose furniture entry was removed keeps its items: no delete, no update."""
    persistence = FakePersistence(
        [
            {
                "container_id": str(uuid4()),
                "room_id": FOYER_ID,
                "source_type": "environment",
                "capacity_slots": 10,
                "metadata_json": {"name": "Crate", "prototype_id": "furniture.old_crate"},
            }
        ]
    )

    count = await sync_room_furniture([_foyer(CHEST_FURNITURE)], registry, persistence)

    assert count == 1
    assert len(persistence.created) == 1
    assert persistence.updated == []


class FakeStartupPersistence(FakePersistence):
    """FakePersistence plus the room cache the startup hook reads."""

    def __init__(self, rooms: list[Room], *, fail: bool = False) -> None:
        super().__init__()
        self.rooms: list[Room] = rooms
        self.fail: bool = fail
        self.warmed: bool = False

    async def warmup_room_cache(self) -> None:
        if self.fail:
            raise DatabaseError("database unavailable")
        self.warmed = True

    def list_rooms(self) -> list[Room]:
        return self.rooms


@pytest.mark.asyncio
async def test_initialize_room_furniture_warms_cache_and_syncs(registry: PrototypeRegistry) -> None:
    persistence = FakeStartupPersistence([_foyer(CHEST_FURNITURE)])

    await initialize_room_furniture(persistence, registry)

    assert persistence.warmed is True
    assert len(persistence.created) == 1


@pytest.mark.asyncio
async def test_initialize_room_furniture_skips_without_registry() -> None:
    persistence = FakeStartupPersistence([_foyer(CHEST_FURNITURE)])

    await initialize_room_furniture(persistence, None)
    await initialize_room_furniture(None, None)

    assert persistence.warmed is False
    assert persistence.created == []


@pytest.mark.asyncio
async def test_initialize_room_furniture_survives_database_error(registry: PrototypeRegistry) -> None:
    """A furniture failure is logged; it must never abort server startup."""
    persistence = FakeStartupPersistence([_foyer(CHEST_FURNITURE)], fail=True)

    await initialize_room_furniture(persistence, registry)

    assert persistence.created == []
