# ContainerLockState

> 51 nodes

## Key Concepts

- **ContainerLockState** (42 connections) — `server/models/container.py`
- **models/container.py** (34 connections) — `server/models/container.py`
- **EnvironmentalContainerLoader** (18 connections) — `server/services/environmental_container_loader.py`
- **test_environmental_container_loader.py** (17 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **environmental_container_loader.py** (14 connections) — `server/services/environmental_container_loader.py`
- **.load_container_from_room_json()** (7 connections) — `server/services/environmental_container_loader.py`
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **.migrate_room_container_to_postgresql()** (6 connections) — `server/services/environmental_container_loader.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **UUID** (5 connections)
- **.create_environment()** (4 connections) — `server/models/container.py`
- **.create_equipment()** (4 connections) — `server/models/container.py`
- **._parse_lock_state()** (4 connections) — `server/services/environmental_container_loader.py`
- **.is_decayed()** (3 connections) — `server/models/container.py`
- **.__init__()** (3 connections) — `server/services/environmental_container_loader.py`
- **.load_containers_for_room()** (3 connections) — `server/services/environmental_container_loader.py`
- **._validate_container_capacity()** (3 connections) — `server/services/environmental_container_loader.py`
- **test_container_lock_state_enum_all_states()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_lock_state_enum_values()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_load_container_from_room_json_invalid_capacity()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_invalid_lock_state()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_success()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_containers_for_room_filters_environment()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_migrate_room_container_creates_new()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_migrate_room_container_existing()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- *... and 26 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (36 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (8 shared connections)
- [ContainerService](ContainerService.md) (7 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (5 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (2 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (2 shared connections)
- [InventoryService](InventoryService.md) (2 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 129 (80%)
- INFERRED: 33 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*