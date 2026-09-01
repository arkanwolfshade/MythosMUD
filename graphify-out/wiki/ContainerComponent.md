# ContainerComponent

> 254 nodes

## Key Concepts

- **ContainerComponent** (147 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **test_corpse_lifecycle_service.py** (56 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **ContainerLockState** (44 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **CorpseLifecycleService** (24 connections) — `server/services/corpse_lifecycle_service.py`
- **asyncio** (23 connections)
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **test_container_endpoints_loot_register.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **CorpseServiceError** (11 connections) — `server/services/corpse_lifecycle_service.py`
- **._validate_container_access()** (8 connections) — `server/services/container_service_access.py`
- **._require_corpse_container()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (7 connections)
- **CorpseNotFoundError** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **register_loot_endpoints()** (6 connections) — `server/api/container_endpoints_loot.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._persist_corpse()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.validate_entity_id()** (5 connections) — `server/models/container.py`
- **.validate_lock_state()** (5 connections) — `server/models/container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
- *... and 229 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (38 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (25 shared connections)
- [LootAllRequest](LootAllRequest.md) (18 shared connections)
- [ContainerService](ContainerService.md) (17 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (8 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (7 shared connections)
- [EnvironmentalContainerLoader](EnvironmentalContainerLoader.md) (5 shared connections)
- [ContainerTransferFromMixin](ContainerTransferFromMixin.md) (5 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (5 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (5 shared connections)
- [ContainerFactoryOptions](ContainerFactoryOptions.md) (5 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/models/container.py`
- `server/services/container_service_access.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 515 (80%)
- INFERRED: 131 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*