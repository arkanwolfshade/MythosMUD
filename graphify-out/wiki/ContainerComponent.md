# ContainerComponent

> 233 nodes

## Key Concepts

- **ContainerComponent** (147 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **test_corpse_lifecycle_service.py** (56 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **ContainerLockState** (44 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **CorpseLifecycleService** (24 connections) — `server/services/corpse_lifecycle_service.py`
- **asyncio** (23 connections)
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseServiceError** (11 connections) — `server/services/corpse_lifecycle_service.py`
- **._require_corpse_container()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (7 connections)
- **CorpseNotFoundError** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._persist_corpse()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.validate_entity_id()** (5 connections) — `server/models/container.py`
- **.validate_lock_state()** (5 connections) — `server/models/container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
- **._build_corpse_component()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.can_access_corpse()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **test_container_component_default_lock_state()** (5 connections) — `server/tests/unit/models/test_container.py`
- *... and 208 more nodes in this community*

## Relationships

- [LootAllRequest](LootAllRequest.md) (33 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (32 shared connections)
- [ContainerService](ContainerService.md) (17 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (15 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (9 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (7 shared connections)
- [EnvironmentalContainerLoader](EnvironmentalContainerLoader.md) (5 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (5 shared connections)
- [ContainerFactoryOptions](ContainerFactoryOptions.md) (5 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 470 (79%)
- INFERRED: 127 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*