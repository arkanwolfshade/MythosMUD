# ZoneConfiguration

> 64 nodes

## Key Concepts

- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
- **mock_zone_config()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_check_spawn_requirements_for_room_with_definitions()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_exact_match()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_no_slash()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_zone_fallback()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
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
- *... and 39 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (30 shared connections)
- [test_zone_configuration.py](test_zone_configuration.py.md) (22 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (10 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (5 shared connections)
- [ZoneConfigurationData](ZoneConfigurationData.md) (3 shared connections)
- [load_zone_configurations](load_zone_configurations.md) (1 shared connections)
- [._get_zone_key_from_room_id](_get_zone_key_from_room_id.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 128 (78%)
- INFERRED: 37 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*