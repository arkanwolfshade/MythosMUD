# ContainerComponent

> 111 nodes

## Key Concepts

- **ContainerComponent** (100 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
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
- **test_container_component_is_unlocked_when_sealed()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_unlocked_when_unlocked()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_would_exceed_capacity()** (5 connections) — `server/tests/unit/models/test_container.py`
- **Any** (5 connections)
- **field_validator** (5 connections)
- **UUID** (5 connections)
- **.create_environment()** (4 connections) — `server/models/container.py`
- *... and 86 more nodes in this community*

## Relationships

- [ContainerSourceType](ContainerSourceType.md) (33 shared connections)
- [ContainerLockState](ContainerLockState.md) (21 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [pytest.md](pytest.md.md) (9 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (8 shared connections)
- [InventoryService](InventoryService.md) (8 shared connections)
- [container_events.py](container_events.py.md) (7 shared connections)
- [api/conftest.py](api-conftest.py.md) (2 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/tests/unit/models/test_container.py`

## Audit Trail

- EXTRACTED: 161 (61%)
- INFERRED: 101 (39%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*