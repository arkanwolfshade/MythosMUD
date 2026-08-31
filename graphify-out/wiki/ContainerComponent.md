# ContainerComponent

> 154 nodes

## Key Concepts

- **ContainerComponent** (147 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **CorpseLifecycleService** (24 connections) — `server/services/corpse_lifecycle_service.py`
- **_container()** (15 connections) — `server/tests/unit/services/test_container_service.py`
- **._validate_container_access()** (8 connections) — `server/services/container_service_access.py`
- **._require_corpse_container()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (7 connections)
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._persist_corpse()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._raise_corpse_grace_denied()** (5 connections) — `server/services/container_service_access.py`
- **._validate_corpse_grace_period()** (5 connections) — `server/services/container_service_access.py`
- **._validate_ownership()** (5 connections) — `server/services/container_service_access.py`
- **._validate_proximity()** (5 connections) — `server/services/container_service_access.py`
- **._validate_role_access()** (5 connections) — `server/services/container_service_access.py`
- **._build_corpse_component()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.can_access_corpse()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **test_container_component_default_lock_state()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots_full()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_used_slots()** (5 connections) — `server/tests/unit/models/test_container.py`
- *... and 129 more nodes in this community*

## Relationships

- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (36 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (35 shared connections)
- [ContainerLockState](ContainerLockState.md) (29 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (26 shared connections)
- [ContainerService](ContainerService.md) (23 shared connections)
- [ContainerFactoryOptions](ContainerFactoryOptions.md) (13 shared connections)
- [LootAllRequest](LootAllRequest.md) (11 shared connections)
- [log_and_raise](log_and_raise.md) (8 shared connections)
- [pytest.md](pytest.md.md) (7 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (7 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (7 shared connections)
- [transfer_all_items_from_container](transfer_all_items_from_container.md) (3 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/container_service_access.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 358 (74%)
- INFERRED: 123 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*