# useGameClientV2ContainerNetworkPhase.ts

> 66 nodes · cohesion 0.06

## Key Concepts

- **room_furniture_loader.py** (32 connections) — `server/services/room_furniture_loader.py`
- **test_room_furniture_loader.py** (29 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **sync_room_furniture()** (18 connections) — `server/services/room_furniture_loader.py`
- **FakePersistence** (13 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **FakeStartupPersistence** (11 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_foyer()** (11 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **FurniturePersistence** (10 connections) — `server/services/room_furniture_loader.py`
- **initialize_room_furniture()** (10 connections) — `server/services/room_furniture_loader.py`
- **FurnitureStartupPersistence** (8 connections) — `server/services/room_furniture_loader.py`
- **_sync_entry()** (8 connections) — `server/services/room_furniture_loader.py`
- **asyncio** (8 connections)
- **PrototypeRegistry** (8 connections)
- **test_initialize_room_furniture_survives_database_error()** (8 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_skips_template_rooms_bad_entries_and_non_container_prototypes()** (8 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_undeclared_furniture_container_is_kept()** (8 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_creates_missing_furniture_container()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_initialize_room_furniture_warms_cache_and_syncs()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_refreshes_existing_container_from_prototype_without_touching_items()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_up_to_date_container_is_left_alone()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_room()** (6 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_furniture_spec()** (5 connections) — `server/services/room_furniture_loader.py`
- **_refresh_container()** (5 connections) — `server/services/room_furniture_loader.py`
- **registry()** (5 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_initialize_room_furniture_skips_without_registry()** (5 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_furniture_containers()** (4 connections) — `server/services/room_furniture_loader.py`
- *... and 41 more nodes in this community*

## Relationships

- [test_room_sync_service.py](test_room_sync_service.py.md) (15 shared connections)
- [.profession_to_dict](profession_to_dict.md) (6 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (5 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (4 shared connections)
- [test_metrics.py](test_metrics.py.md) (4 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (4 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (3 shared connections)
- [items/catalog_dml.py](items-catalog_dml.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [✅ Phase 2 Async Persistence Migration - COMPLETE](✅_Phase_2_Async_Persistence_Migration_-_COMPLETE.md) (2 shared connections)

## Source Files

- `server/services/room_furniture_loader.py`
- `server/tests/unit/services/test_room_furniture_loader.py`

## Audit Trail

- EXTRACTED: 171 (93%)
- INFERRED: 13 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*