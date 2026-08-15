# should_spawn_npc

> 39 nodes

## Key Concepts

- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
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
- **Spawn Validator Module. This module provides logic for validating whether NPCs…** (1 connections) — `server/npc/spawn_validator.py`
- **Determine if an NPC should spawn based on conditions. Args: definition: NPC…** (1 connections) — `server/npc/spawn_validator.py`
- **Return False when zone population blocks this NPC definition.** (1 connections) — `server/npc/spawn_validator.py`
- **Evaluate one spawn rule; return True when probability roll succeeds.** (1 connections) — `server/npc/spawn_validator.py`
- **Return True when any spawn rule passes probability checks.** (1 connections) — `server/npc/spawn_validator.py`
- *... and 14 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (5 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (5 shared connections)
- [mock_zone_config](mock_zone_config.md) (3 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (2 shared connections)

## Source Files

- `server/npc/spawn_validator.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 82 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*