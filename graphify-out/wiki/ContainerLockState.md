# ContainerLockState

> 56 nodes

## Key Concepts

- **ContainerLockState** (44 connections) — `server/models/container.py`
- **models/container.py** (33 connections) — `server/models/container.py`
- **EnvironmentalContainerLoader** (18 connections) — `server/services/environmental_container_loader.py`
- **test_environmental_container_loader.py** (16 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **environmental_container_loader.py** (14 connections) — `server/services/environmental_container_loader.py`
- **.load_container_from_room_json()** (7 connections) — `server/services/environmental_container_loader.py`
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **.migrate_room_container_to_postgresql()** (6 connections) — `server/services/environmental_container_loader.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **test_can_access_corpse_grace_period_active()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_owner()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_uses_real_time_not_mythos_time()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
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
- *... and 31 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (24 shared connections)
- [get_logger](get_logger.md) (22 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (16 shared connections)
- [ContainerService](ContainerService.md) (12 shared connections)
- [container_events.py](container_events.py.md) (5 shared connections)
- [User](User.md) (3 shared connections)
- [.validate_entity_id](validate_entity_id.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (2 shared connections)
- [LootAllRequest](LootAllRequest.md) (2 shared connections)
- [ContainerLockMixin](ContainerLockMixin.md) (1 shared connections)
- [api/conftest.py](api-conftest.py.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/tests/unit/services/test_environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 138 (79%)
- INFERRED: 36 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*