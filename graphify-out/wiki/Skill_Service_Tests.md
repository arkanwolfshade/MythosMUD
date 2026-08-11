# Skill Service Tests

> 132 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **CorpseLifecycleService** (27 connections) — `server/services/corpse_lifecycle_service.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseServiceError** (15 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerLockState** (10 connections) — `server/models/container.py`
- **ContainerComponent** (9 connections)
- **._require_corpse_container()** (9 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (9 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseNotFoundError** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (7 connections)
- **._persist_corpse()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **Any** (5 connections)
- **._build_corpse_component()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.can_access_corpse()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **test_corpse_not_found_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **._grace_period_allows_others()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- *... and 107 more nodes in this community*

## Relationships

- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (24 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (5 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (5 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (4 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (1 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 394 (93%)
- INFERRED: 29 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*