# NPC Spawn Validator

> 39 nodes · cohesion 0.07

## Key Concepts

- **should_spawn_npc()** (22 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (21 connections) — `server/tests/unit/npc/test_spawn_validator.py`
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
- **mock_npc_definition()** (2 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **mock_population_stats()** (2 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **mock_zone_config()** (2 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **Test should_spawn_npc() returns True when spawn rule passes.** (2 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **Any** (2 connections) — `server/npc/spawn_validator.py`
- **NPCDefinition** (2 connections) — `server/npc/spawn_validator.py`
- **NPCSpawnRule** (2 connections) — `server/npc/spawn_validator.py`
- **ZoneConfiguration** (2 connections) — `server/npc/spawn_validator.py`
- **Determine if an NPC should spawn based on conditions.      Args:         definit** (1 connections) — `server/npc/spawn_validator.py`
- **Unit tests for spawn validator.  Tests the should_spawn_npc function.** (1 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- *... and 14 more nodes in this community*

## Relationships

- [[Zone Config Loader]] (6 shared connections)
- [[NPC Definition Schemas]] (2 shared connections)
- [[Distributed Event Bus]] (1 shared connections)
- [[NPC Services Bundle]] (1 shared connections)

## Source Files

- `server/npc/spawn_validator.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 110 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
