# test_corpse_lifecycle_service.py

> 103 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (56 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **CorpseLifecycleService** (24 connections) — `server/services/corpse_lifecycle_service.py`
- **asyncio** (23 connections)
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseServiceError** (11 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (9 connections)
- **._require_corpse_container()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (7 connections)
- **CorpseNotFoundError** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._persist_corpse()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._build_corpse_component()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.can_access_corpse()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_corpse()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_success()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Any** (5 connections)
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **corpse_service()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 78 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (31 shared connections)
- [log_and_raise](log_and_raise.md) (6 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (4 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 204 (91%)
- INFERRED: 20 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*