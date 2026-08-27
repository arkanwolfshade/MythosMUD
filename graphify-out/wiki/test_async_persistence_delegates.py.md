# test_async_persistence_delegates.py

> 93 nodes

## Key Concepts

- **ZoneConfiguration** (49 connections) — `server/npc/zone_configuration.py`
- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
- **Test get_effective_spawn_probability() with no modifier.** (5 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **ZoneConfigurationData** (4 connections) — `server/npc/zone_configuration.py`
- **mock_zone_config()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **ZoneSpecialRules** (3 connections) — `server/npc/zone_configuration.py`
- **.__init__()** (3 connections) — `server/npc/zone_configuration.py`
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
- *... and 68 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (16 shared connections)
- [ErrorType](ErrorType.md) (6 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (6 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (4 shared connections)
- [Invite](Invite.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (3 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/npc/spawn_validator.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 174 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*