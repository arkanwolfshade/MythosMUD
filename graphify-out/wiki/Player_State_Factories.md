# Player State Factories

> 31 nodes

## Key Concepts

- **CorpseLifecycleService** (27 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (9 connections)
- **._require_corpse_container()** (9 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (9 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (8 connections) — `server/services/corpse_lifecycle_service.py`
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
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **._grace_period_allows_others()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **Safely get enum value, handling both enum instances and string values.      When** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Filter out database-specific fields that are not part of the ContainerComponent** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Service for managing corpse container lifecycle.      Handles creation on death,** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Initialize the corpse lifecycle service.          Args:             persistence:** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Create a corpse container when a player dies.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **True if player may access corpse (owner/admin always; others after grace).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (6 shared connections)
- [Archive Npc Population](Archive_Npc_Population.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (3 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (3 shared connections)
- [test_get_enum_value_string](test_get_enum_value_string.md) (1 shared connections)
- [corpse_service](corpse_service.md) (1 shared connections)
- [test_corpse_lifecycle_service_init_no_persistence](test_corpse_lifecycle_service_init_no_persistence.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 137 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*