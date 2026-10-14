# ItemFactory

> 36 nodes

## Key Concepts

- **ItemFactory** (35 connections) — `server/game/items/item_factory.py`
- **test_room_item_seeder.py** (26 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **seed_room_items()** (15 connections) — `server/services/room_item_seeder.py`
- **FakeRoomManager** (11 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **_room()** (10 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **FakePersistence** (9 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **initialize_room_items()** (9 connections) — `server/services/room_item_seeder.py`
- **factory()** (7 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_startup_hook_never_fails_startup()** (7 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_startup_hook_seeds_cached_rooms()** (7 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_malformed_or_unknown_entries_are_skipped()** (6 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_one_bad_entry_does_not_block_the_rest()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_places_declared_item_on_the_floor()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_quantity_defaults_to_one()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_rooms_without_items_are_ignored()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_template_rooms_are_skipped()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **_item_entries()** (4 connections) — `server/services/room_item_seeder.py`
- **.__init__()** (3 connections) — `server/game/items/item_factory.py`
- **Room** (3 connections)
- **_as_entry()** (2 connections) — `server/services/room_item_seeder.py`
- **.__init__()** (2 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **.list_rooms()** (2 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **.warmup_room_cache()** (2 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **asyncio** (2 connections)
- **.add_room_drop()** (1 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- *... and 11 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (17 shared connections)
- [test_item_factory.py](test_item_factory.py.md) (6 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (5 shared connections)
- [initialize_components](initialize_components.md) (4 shared connections)
- [Room](Room.md) (3 shared connections)
- [RoomListPersistence](RoomListPersistence.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [items/__init__.py](items-__init__.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (2 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (2 shared connections)
- [items/catalog_dml.py](items-catalog_dml.py.md) (1 shared connections)

## Source Files

- `server/game/items/item_factory.py`
- `server/services/room_item_seeder.py`
- `server/tests/unit/services/test_room_item_seeder.py`

## Audit Trail

- EXTRACTED: 101 (81%)
- INFERRED: 24 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*