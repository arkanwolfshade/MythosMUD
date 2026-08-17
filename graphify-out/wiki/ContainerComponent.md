# ContainerComponent

> 206 nodes

## Key Concepts

- **ContainerComponent** (100 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **test_corpse_lifecycle_service.py** (56 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **ContainerLockState** (42 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **asyncio** (23 connections)
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **CorpseServiceError** (11 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **CorpseNotFoundError** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **.validate_entity_id()** (5 connections) — `server/models/container.py`
- **.validate_lock_state()** (5 connections) — `server/models/container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
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
- *... and 181 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (53 shared connections)
- [ContainerService](ContainerService.md) (17 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (9 shared connections)
- [emit_loot_all_event](emit_loot_all_event.md) (9 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (7 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [LootAllRequest](LootAllRequest.md) (5 shared connections)
- [loot_all_items](loot_all_items.md) (4 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)
- [EnvironmentalContainerLoader](EnvironmentalContainerLoader.md) (2 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (2 shared connections)
- [fixture](fixture.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 322 (65%)
- INFERRED: 172 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*