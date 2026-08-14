# test_corpse_lifecycle_service.py

> 103 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **CorpseLifecycleService** (27 connections) — `server/services/corpse_lifecycle_service.py`
- **asyncio** (23 connections)
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (9 connections)
- **._require_corpse_container()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (7 connections)
- **CorpseServiceError** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._persist_corpse()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseNotFoundError** (5 connections) — `server/services/corpse_lifecycle_service.py`
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
- *... and 78 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (16 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [ContainerService](ContainerService.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (2 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (2 shared connections)
- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [LootAllRequest](LootAllRequest.md) (2 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 207 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*