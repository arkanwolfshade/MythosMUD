"""Unit tests for the room item seeder (rooms.attributes.items -> floor drops at startup)."""

from typing import final

import pytest

from server.exceptions import DatabaseError
from server.game.items.item_factory import ItemFactory
from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry
from server.models.room import Room
from server.services.room_item_seeder import initialize_room_items, seed_room_items

TONIC_ID = "consumable.folk_tonic"
NURSES_ID = "earth_arkhamcity_sanitarium_room_nurses_001"


@final
class FakeRoomManager:
    """Records floor drops."""

    def __init__(self) -> None:
        self.drops: list[tuple[str, dict[str, object]]] = []

    def add_room_drop(self, room_id: str, stack: dict[str, object]) -> None:
        self.drops.append((room_id, stack))


@final
class FakePersistence:
    """Serves a fixed room list; optionally fails on warmup."""

    def __init__(self, rooms: list[Room], *, fail: bool = False) -> None:
        self._rooms = rooms
        self._fail = fail

    async def warmup_room_cache(self) -> None:
        if self._fail:
            raise DatabaseError("cache unavailable")

    def list_rooms(self) -> list[Room]:
        return self._rooms


@pytest.fixture
def factory() -> ItemFactory:
    tonic = ItemPrototypeModel.model_validate(
        {
            "prototype_id": TONIC_ID,
            "name": "Folk Tonic",
            "short_description": "a stoppered bottle of folk tonic",
            "long_description": "A squat brown bottle.",
            "item_type": "consumable",
            "weight": 0.3,
            "base_value": 15,
            "effect_components": ["component.lucidity_recovery"],
        }
    )
    return ItemFactory(PrototypeRegistry({TONIC_ID: tonic}, []))


def _room(room_id: str, attributes: dict[str, object]) -> Room:
    return Room({"id": room_id, "attributes": attributes})


def test_places_declared_item_on_the_floor(factory: ItemFactory) -> None:
    manager = FakeRoomManager()
    room = _room(NURSES_ID, {"items": [{"prototype_id": TONIC_ID, "quantity": 2}]})

    assert seed_room_items([room], factory, manager) == 1

    [(room_id, stack)] = manager.drops
    assert room_id == NURSES_ID
    assert stack["prototype_id"] == TONIC_ID
    assert stack["item_name"] == "Folk Tonic"
    assert stack["quantity"] == 2
    assert stack["slot_type"] == "inventory"


def test_quantity_defaults_to_one(factory: ItemFactory) -> None:
    manager = FakeRoomManager()

    _ = seed_room_items([_room(NURSES_ID, {"items": [{"prototype_id": TONIC_ID}]})], factory, manager)

    assert manager.drops[0][1]["quantity"] == 1


@pytest.mark.parametrize(
    "items",
    [
        "not-a-list",
        ["not-a-dict"],
        [{"quantity": 1}],
        [{"prototype_id": ""}],
        [{"prototype_id": TONIC_ID, "quantity": 0}],
        [{"prototype_id": TONIC_ID, "quantity": True}],
        [{"prototype_id": TONIC_ID, "quantity": "2"}],
        [{"prototype_id": "no.such.prototype"}],
    ],
)
def test_malformed_or_unknown_entries_are_skipped(factory: ItemFactory, items: object) -> None:
    manager = FakeRoomManager()

    assert seed_room_items([_room(NURSES_ID, {"items": items})], factory, manager) == 0
    assert manager.drops == []


def test_one_bad_entry_does_not_block_the_rest(factory: ItemFactory) -> None:
    manager = FakeRoomManager()
    room = _room(NURSES_ID, {"items": [{"prototype_id": "no.such.prototype"}, {"prototype_id": TONIC_ID}]})

    assert seed_room_items([room], factory, manager) == 1


def test_template_rooms_are_skipped(factory: ItemFactory) -> None:
    manager = FakeRoomManager()
    room = _room(NURSES_ID, {"instance_template_id": "tutorial", "items": [{"prototype_id": TONIC_ID}]})

    assert seed_room_items([room], factory, manager) == 0
    assert manager.drops == []


def test_rooms_without_items_are_ignored(factory: ItemFactory) -> None:
    manager = FakeRoomManager()

    assert seed_room_items([_room(NURSES_ID, {})], factory, manager) == 0


@pytest.mark.asyncio
async def test_startup_hook_seeds_cached_rooms(factory: ItemFactory) -> None:
    manager = FakeRoomManager()
    persistence = FakePersistence([_room(NURSES_ID, {"items": [{"prototype_id": TONIC_ID}]})])

    await initialize_room_items(persistence, factory, manager)

    assert len(manager.drops) == 1


@pytest.mark.asyncio
async def test_startup_hook_never_fails_startup(factory: ItemFactory) -> None:
    manager = FakeRoomManager()

    await initialize_room_items(FakePersistence([], fail=True), factory, manager)
    await initialize_room_items(None, factory, manager)
    await initialize_room_items(FakePersistence([]), object(), manager)
    await initialize_room_items(FakePersistence([]), factory, None)

    assert manager.drops == []
