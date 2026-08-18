# ContainerComponent

> 134 nodes

## Key Concepts

- **ContainerComponent** (100 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **_container()** (16 connections) — `server/tests/unit/services/test_container_service.py`
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
- **test_container_component_is_unlocked_when_sealed()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_unlocked_when_unlocked()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_would_exceed_capacity()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_can_access_corpse_admin()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_active()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_expired()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_type_error()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 109 more nodes in this community*

## Relationships

- [ContainerLockState](ContainerLockState.md) (36 shared connections)
- [ContainerService](ContainerService.md) (27 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (25 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (14 shared connections)
- [InventoryService](InventoryService.md) (9 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (7 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [test_container_events_loot.py](test_container_events_loot.py.md) (6 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)

## Source Files

- `server/models/container.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 251 (68%)
- INFERRED: 119 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*