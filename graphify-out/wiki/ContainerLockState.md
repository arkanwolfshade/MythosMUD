# ContainerLockState

> 51 nodes

## Key Concepts

- **ContainerLockState** (42 connections) — `server/models/container.py`
- **EnvironmentalContainerLoader** (18 connections) — `server/services/environmental_container_loader.py`
- **test_environmental_container_loader.py** (17 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **.load_container_from_room_json()** (7 connections) — `server/services/environmental_container_loader.py`
- **.migrate_room_container_to_postgresql()** (6 connections) — `server/services/environmental_container_loader.py`
- **test_can_access_corpse_grace_period_active()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_expired()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_type_error()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_no_grace_period_start()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_no_owner()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_owner()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_decayed()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_no_decay_time()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_not_decayed()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_uses_real_time_not_mythos_time()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **._parse_lock_state()** (4 connections) — `server/services/environmental_container_loader.py`
- **.__init__()** (3 connections) — `server/services/environmental_container_loader.py`
- **.load_containers_for_room()** (3 connections) — `server/services/environmental_container_loader.py`
- **._validate_container_capacity()** (3 connections) — `server/services/environmental_container_loader.py`
- **test_load_container_from_room_json_invalid_capacity()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_invalid_lock_state()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_success()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_containers_for_room_filters_environment()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_migrate_room_container_creates_new()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_migrate_room_container_existing()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- *... and 26 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (21 shared connections)
- [ContainerSourceType](ContainerSourceType.md) (16 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (15 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/tests/unit/services/test_environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 80 (58%)
- INFERRED: 59 (42%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*