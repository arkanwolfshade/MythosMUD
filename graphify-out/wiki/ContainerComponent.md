# ContainerComponent

> 107 nodes

## Key Concepts

- **ContainerComponent** (147 connections) — `server/models/container.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **CorpseLifecycleService** (24 connections) — `server/services/corpse_lifecycle_service.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **._require_corpse_container()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (7 connections)
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._persist_corpse()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._build_corpse_component()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.can_access_corpse()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
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
- *... and 82 more nodes in this community*

## Relationships

- [ContainerService](ContainerService.md) (33 shared connections)
- [get_logger](get_logger.md) (25 shared connections)
- [ContainerLockState](ContainerLockState.md) (24 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (24 shared connections)
- [container_events.py](container_events.py.md) (16 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (9 shared connections)
- [.validate_entity_id](validate_entity_id.md) (8 shared connections)
- [LootAllRequest](LootAllRequest.md) (7 shared connections)
- [ContainerTransferFromMixin](ContainerTransferFromMixin.md) (5 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (5 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (5 shared connections)
- [User](User.md) (4 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/models/test_container.py`

## Audit Trail

- EXTRACTED: 287 (83%)
- INFERRED: 59 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*