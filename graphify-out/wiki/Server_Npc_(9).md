# Server Npc (9)

> 45 nodes

## Key Concepts

- **ZoneConfiguration** (53 connections) — `server/npc/zone_configuration.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **Test get_effective_spawn_probability() with no modifier.** (5 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_zone_configuration_zone_fallback()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_no_slash()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_zone_config()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_zone_configuration_init_minimal()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_init_full()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_init_partial_special_rules()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_no_modifier()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_with_modifier()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_reduced_modifier()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_caps_at_one()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_already_one()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_no_requirements()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_with_requirements_met()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_with_requirements_partial()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_with_requirements_not_met()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_empty_player_requirements()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_multiple_requirements_any()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_weather_patterns()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_description()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_zone_type()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_environment()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_zero_base()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- *... and 20 more nodes in this community*

## Relationships

- [Server Npc (15)](Server_Npc_%2815%29.md) (7 shared connections)
- [Server Npc (4)](Server_Npc_%284%29.md) (6 shared connections)
- [Server Events](Server_Events.md) (5 shared connections)
- [Server Models (3)](Server_Models_%283%29.md) (4 shared connections)
- [Server Npc (10)](Server_Npc_%2810%29.md) (4 shared connections)
- [Server Npc](Server_Npc.md) (3 shared connections)
- [Server Npc (20)](Server_Npc_%2820%29.md) (1 shared connections)
- [Server Npc (51)](Server_Npc_%2851%29.md) (1 shared connections)

## Source Files

- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 165 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*