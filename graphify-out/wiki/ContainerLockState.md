# ContainerLockState

> 35 nodes

## Key Concepts

- **ContainerLockState** (44 connections) — `server/models/container.py`
- **EnvironmentalContainerLoader** (18 connections) — `server/services/environmental_container_loader.py`
- **test_environmental_container_loader.py** (17 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **environmental_container_loader.py** (14 connections) — `server/services/environmental_container_loader.py`
- **.load_container_from_room_json()** (7 connections) — `server/services/environmental_container_loader.py`
- **.migrate_room_container_to_postgresql()** (6 connections) — `server/services/environmental_container_loader.py`
- **._parse_lock_state()** (4 connections) — `server/services/environmental_container_loader.py`
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
- **Any** (3 connections)
- **asyncio** (3 connections)
- **test_environmental_loader_requires_persistence()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_disabled()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_none_when_missing()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **StrEnum** (2 connections)
- **UUID** (2 connections)
- *... and 10 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (29 shared connections)
- [ContainerService](ContainerService.md) (5 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (3 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (3 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [ContainerFactoryOptions](ContainerFactoryOptions.md) (1 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (1 shared connections)
- [ContainerLockMixin](ContainerLockMixin.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 81 (71%)
- INFERRED: 33 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*