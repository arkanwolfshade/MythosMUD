# test_spawn_validator.py

> 37 nodes · cohesion 0.07

## Key Concepts

- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (22 connections) — `server/npc/spawn_validator.py`
- **test_should_spawn_npc_multiple_rules_first_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_multiple_rules_second_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_population_stats_npcs_by_definition()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_conditions()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_population()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_probability()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_uses_zone_effective_probability()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **mock_npc_definition()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **mock_zone_config()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_no_population_stats()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_not_required_no_rules()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_population_limit_exceeded()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_population_limit_ok()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_required_npc_spawns()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **mock_population_stats()** (2 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **Any** (1 connections)
- **Determine if an NPC should spawn based on conditions.      Args:         definit** (1 connections) — `server/npc/spawn_validator.py`
- **Unit tests for spawn validator.  Tests the should_spawn_npc function.** (1 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **Test should_spawn_npc() skips rule when population check fails.** (1 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **Test should_spawn_npc() skips rule when spawn conditions fail.** (1 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **Test should_spawn_npc() returns False when probability roll fails.** (1 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **Test should_spawn_npc() returns True for required NPC.** (1 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- *... and 12 more nodes in this community*

## Relationships

- [NPCSpawnRule](NPCSpawnRule.md) (10 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (3 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (1 shared connections)

## Source Files

- `server/npc/spawn_validator.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 110 (92%)
- INFERRED: 10 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*