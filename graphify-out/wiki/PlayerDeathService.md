# PlayerDeathService

> 39 nodes · cohesion 0.09

## Key Concepts

- **test_room_item_seeder.py** (26 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **seed_room_items()** (15 connections) — `server/services/room_item_seeder.py`
- **FakeRoomManager** (11 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **_room()** (10 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **initialize_room_items()** (9 connections) — `server/services/room_item_seeder.py`
- **FakePersistence** (9 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **RoomListPersistence** (7 connections) — `server/services/room_item_seeder.py`
- **factory()** (7 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_startup_hook_never_fails_startup()** (7 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_startup_hook_seeds_cached_rooms()** (7 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_malformed_or_unknown_entries_are_skipped()** (6 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **RoomDropSink** (5 connections) — `server/services/room_item_seeder.py`
- **test_one_bad_entry_does_not_block_the_rest()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_places_declared_item_on_the_floor()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_quantity_defaults_to_one()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_rooms_without_items_are_ignored()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **test_template_rooms_are_skipped()** (5 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **Room** (3 connections)
- **Protocol** (2 connections)
- **Room** (2 connections)
- **.add_room_drop()** (2 connections) — `server/services/room_item_seeder.py`
- **.list_rooms()** (2 connections) — `server/services/room_item_seeder.py`
- **.warmup_room_cache()** (2 connections) — `server/services/room_item_seeder.py`
- **.__init__()** (2 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- **.list_rooms()** (2 connections) — `server/tests/unit/services/test_room_item_seeder.py`
- *... and 14 more nodes in this community*

## Relationships

- [test_metrics.py](test_metrics.py.md) (18 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (3 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (3 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [items/catalog_dml.py](items-catalog_dml.py.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (1 shared connections)

## Source Files

- `server/services/room_item_seeder.py`
- `server/tests/unit/services/test_room_item_seeder.py`

## Audit Trail

- EXTRACTED: 93 (86%)
- INFERRED: 15 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*