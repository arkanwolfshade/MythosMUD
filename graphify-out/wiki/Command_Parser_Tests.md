# Command Parser Tests

> 115 nodes

## Key Concepts

- **NPCSpawnRule** (57 connections) — `server/models/npc.py`
- **ZoneConfiguration** (55 connections) — `server/npc/zone_configuration.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_population()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_conditions()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_probability()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_multiple_rules_first_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_multiple_rules_second_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_uses_zone_effective_probability()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_population_stats_npcs_by_definition()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **.set_spawn_conditions()** (3 connections) — `server/models/npc.py`
- **.load_spawn_rules()** (3 connections) — `server/npc/population_control.py`
- **Any** (3 connections)
- **.__init__()** (3 connections) — `server/npc/zone_configuration.py`
- **test_load_spawn_rules()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_exact_match()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_zone_fallback()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- *... and 90 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (37 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (14 shared connections)
- [FastAPI App Factory](FastAPI_App_Factory.md) (9 shared connections)
- [NATS Subject Metrics](NATS_Subject_Metrics.md) (9 shared connections)
- [Cursor Plans Best](Cursor_Plans_Best.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (2 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (2 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 403 (94%)
- INFERRED: 28 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*