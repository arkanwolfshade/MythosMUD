# ZoneConfiguration

> 56 nodes

## Key Concepts

- **ZoneConfiguration** (52 connections) — `server/npc/zone_configuration.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_check_spawn_requirements_for_room_with_definitions()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_exact_match()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_no_slash()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_zone_fallback()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_can_access_empty_player_requirements()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_multiple_requirements_any()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_no_requirements()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_with_requirements_met()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_with_requirements_not_met()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_can_access_with_requirements_partial()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_already_one()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_caps_at_one()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_no_modifier()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_reduced_modifier()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_very_high_modifier()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_with_modifier()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_get_effective_spawn_probability_zero_base()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_description()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_environment()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_init_full()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_init_minimal()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_init_partial_special_rules()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **test_zone_configuration_weather_patterns()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- *... and 31 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (10 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (8 shared connections)
- [test_population_control.py](test_population_control.py.md) (6 shared connections)
- [load_zone_configurations](load_zone_configurations.md) (1 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (1 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [_PopulationLifecycleManager](_PopulationLifecycleManager.md) (1 shared connections)

## Source Files

- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 100 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*