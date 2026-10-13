# NPC Definition JSON

> 151 nodes

## Key Concepts

- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._execute_create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **AsyncSession** (6 connections)
- **.get_spawn_conditions()** (5 connections) — `server/models/npc.py`
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
- **.get_spawn_rule()** (5 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.get_spawn_rules()** (5 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._validate_spawn_rule_inputs()** (5 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Test get_effective_spawn_probability() with no modifier.** (5 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- *... and 126 more nodes in this community*

## Relationships

- [NPC Behavior Engine](NPC_Behavior_Engine.md) (30 shared connections)
- [Community 161](Community_161.md) (14 shared connections)
- [Community 276](Community_276.md) (8 shared connections)
- [NPC Population Stats](NPC_Population_Stats.md) (8 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (5 shared connections)
- [Community 40](Community_40.md) (5 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 193](Community_193.md) (1 shared connections)
- [Community 1124](Community_1124.md) (1 shared connections)
- [Community 482](Community_482.md) (1 shared connections)
- [Community 113](Community_113.md) (1 shared connections)
- [Community 985](Community_985.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/zone_configuration.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 304 (96%)
- INFERRED: 13 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*