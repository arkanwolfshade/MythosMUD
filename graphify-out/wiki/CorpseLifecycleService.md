# CorpseLifecycleService

> 42 nodes

## Key Concepts

- **CorpseLifecycleService** (24 connections) — `server/services/corpse_lifecycle_service.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (9 connections)
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
- **Any** (5 connections)
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **corpse_service()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **._grace_period_allows_others()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_enum()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_string()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **fixture** (2 connections)
- *... and 17 more nodes in this community*

## Relationships

- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (10 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [CombatDeathHandler](CombatDeathHandler.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [ContainerLockState](ContainerLockState.md) (1 shared connections)
- [ContainerSourceType](ContainerSourceType.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 101 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*