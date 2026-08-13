# CorpseLifecycleService

> 37 nodes

## Key Concepts

- **CorpseLifecycleService** (27 connections) — `server/services/corpse_lifecycle_service.py`
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
- **._grace_period_allows_others()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_enum()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_string()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Create a corpse container when a player dies.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **True if player may access corpse (owner/admin always; others after grace).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Check if a corpse container has decayed. Args: corpse: Corpse container to…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- *... and 12 more nodes in this community*

## Relationships

- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (6 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 84 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*