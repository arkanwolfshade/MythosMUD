# ContainerComponent

> 117 nodes

## Key Concepts

- **ContainerComponent** (147 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **ContainerLockState** (44 connections) — `server/models/container.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
- **.can_access_corpse()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **test_container_component_default_lock_state()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots_full()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_used_slots()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_capacity_when_full()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_room_for_additional_items()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_room_for_exceeds_capacity()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_locked_when_locked()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_locked_when_sealed()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_locked_when_unlocked()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_unlocked_when_locked()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_unlocked_when_sealed()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_unlocked_when_unlocked()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_would_exceed_capacity()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_can_access_corpse_admin()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_active()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_expired()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_type_error()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_invalid_grace_period()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 92 more nodes in this community*

## Relationships

- [container_events.py](container_events.py.md) (30 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (27 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (26 shared connections)
- [User](User.md) (24 shared connections)
- [ContainerService](ContainerService.md) (16 shared connections)
- [ContainerFactoryOptions](ContainerFactoryOptions.md) (14 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (13 shared connections)
- [InventoryService](InventoryService.md) (9 shared connections)
- [EnvironmentalContainerLoader](EnvironmentalContainerLoader.md) (8 shared connections)
- [._validate_container_access](_validate_container_access.md) (6 shared connections)
- [WearableContainerService](WearableContainerService.md) (5 shared connections)
- [models/player.py](models-player.py.md) (3 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 276 (70%)
- INFERRED: 119 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*