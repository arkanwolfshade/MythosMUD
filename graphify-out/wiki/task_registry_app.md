# task registry app

> 121 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **CorpseServiceError** (13 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (10 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseNotFoundError** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (5 connections)
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (4 connections)
- **.can_access_corpse()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **test_corpse_not_found_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Any** (3 connections)
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **test_get_enum_value_enum()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_string()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **corpse_service()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_service_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_success()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_not_found()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 96 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (18 shared connections)
- [NPC Combat](NPC_Combat.md) (12 shared connections)
- [container events rationale](container_events_rationale.md) (9 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 305 (94%)
- INFERRED: 21 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*