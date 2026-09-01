# test_spawn_validator.py

> 50 nodes

## Key Concepts

- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
- **.get_population_stats()** (4 connections) — `server/npc/population_control.py`
- **mock_zone_config()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **mock_npc_definition()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **mock_population_stats()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_multiple_rules_first_passes()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_multiple_rules_second_passes()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_no_population_stats()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_not_required_no_rules()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_population_limit_exceeded()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_population_limit_ok()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_population_stats_npcs_by_definition()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_required_npc_spawns()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_conditions()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_population()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_probability()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_passes()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_uses_zone_effective_probability()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **Any** (3 connections)
- *... and 25 more nodes in this community*

## Relationships

- [ZoneConfiguration](ZoneConfiguration.md) (9 shared connections)
- [NPCDefinition](NPCDefinition.md) (7 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (7 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 99 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*