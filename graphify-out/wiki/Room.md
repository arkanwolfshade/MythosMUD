# Room

> 180 nodes

## Key Concepts

- **Room** (132 connections) — `server/models/room.py`
- **test_room_class.py** (34 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_furniture_loader.py** (29 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **sync_room_furniture()** (18 connections) — `server/services/room_furniture_loader.py`
- **FakePersistence** (13 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **FakeStartupPersistence** (11 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_foyer()** (11 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **FurniturePersistence** (10 connections) — `server/services/room_furniture_loader.py`
- **initialize_room_furniture()** (10 connections) — `server/services/room_furniture_loader.py`
- **test_furniture_container_created_once_then_refreshed_in_place()** (10 connections) — `server/tests/integration/test_room_furniture_persistence.py`
- **FurnitureStartupPersistence** (8 connections) — `server/services/room_furniture_loader.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **_sync_entry()** (8 connections) — `server/services/room_furniture_loader.py`
- **test_initialize_room_furniture_survives_database_error()** (8 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_skips_template_rooms_bad_entries_and_non_container_prototypes()** (8 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_undeclared_furniture_container_is_kept()** (8 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **asyncio** (8 connections)
- **PrototypeRegistry** (8 connections)
- **test_creates_missing_furniture_container()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_initialize_room_furniture_warms_cache_and_syncs()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_refreshes_existing_container_from_prototype_without_touching_items()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_up_to_date_container_is_left_alone()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_room_map_coordinates.py** (7 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **_as_float()** (6 connections) — `server/models/room.py`
- **.__init__()** (6 connections) — `server/models/room.py`
- *... and 155 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (45 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (10 shared connections)
- [test_instance_manager.py](test_instance_manager.py.md) (9 shared connections)
- [ContainerCreateParams](ContainerCreateParams.md) (8 shared connections)
- [ValueError](ValueError.md) (8 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (4 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [_room](_room.md) (3 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (3 shared connections)
- [ItemFactory](ItemFactory.md) (3 shared connections)

## Source Files

- `server/models/room.py`
- `server/services/room_furniture_loader.py`
- `server/tests/integration/test_room_furniture_persistence.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/models/test_room_map_coordinates.py`
- `server/tests/unit/services/test_room_furniture_loader.py`

## Audit Trail

- EXTRACTED: 387 (92%)
- INFERRED: 34 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*