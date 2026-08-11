# Command Parser Tests

> 84 nodes

## Key Concepts

- **NPCSpawnRule** (57 connections) — `server/models/npc.py`
- **npc.py** (37 connections) — `server/models/npc.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **Base** (6 connections) — `server/models/npc.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
- **.check_spawn_conditions()** (4 connections) — `server/models/npc.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- **test_should_spawn_npc_spawn_rule_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_population()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_conditions()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_probability()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_multiple_rules_first_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_multiple_rules_second_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_uses_zone_effective_probability()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_population_stats_npcs_by_definition()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **._check_missing_key_condition()** (3 connections) — `server/models/npc.py`
- *... and 59 more nodes in this community*

## Relationships

- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (17 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (14 shared connections)
- [FastAPI App Factory](FastAPI_App_Factory.md) (12 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (9 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (9 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (7 shared connections)
- [AnyIO vs Asyncio Guide](AnyIO_vs_Asyncio_Guide.md) (6 shared connections)
- [Mythos Calendar Time Service](Mythos_Calendar_Time_Service.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (3 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (3 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (3 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc_metadata.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 332 (94%)
- INFERRED: 20 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*