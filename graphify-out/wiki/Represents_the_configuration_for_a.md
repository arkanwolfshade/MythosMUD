# Represents the configuration for a

> 49 nodes

## Key Concepts

- **ZoneConfiguration** (53 connections) — `server/npc/zone_configuration.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **Test get_effective_spawn_probability() with no modifier.** (5 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_zone_configuration_exact_match()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
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
- *... and 24 more nodes in this community*

## Relationships

- [. repr ()](_repr_%28%29.md) (9 shared connections)
- [TypedDict](TypedDict.md) (6 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (6 shared connections)
- [async load zone configurations()](async_load_zone_configurations%28%29.md) (5 shared connections)
- [.is required()](is_required%28%29.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [load zone configurations()](load_zone_configurations%28%29.md) (1 shared connections)

## Source Files

- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 172 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*