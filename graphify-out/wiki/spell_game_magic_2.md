# spell game magic

> 54 nodes

## Key Concepts

- **ZoneConfiguration** (53 connections) — `server/npc/zone_configuration.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
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
- **test_get_effective_spawn_probability_zero_base()** (3 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- *... and 29 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [npc idle movement](npc_idle_movement.md) (7 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (6 shared connections)
- [npc realtime occupant](npc_realtime_occupant.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [combat services rationale](combat_services_rationale.md) (1 shared connections)
- [services npc combat](services_npc_combat.md) (1 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)

## Source Files

- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 169 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*