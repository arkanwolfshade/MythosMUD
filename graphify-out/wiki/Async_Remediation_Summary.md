# Async Remediation Summary

> 56 nodes · cohesion 0.05

## Key Concepts

- **ZoneConfiguration** (53 connections) — `server/npc/zone_configuration.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **.__init__()** (3 connections) — `server/npc/zone_configuration.py`
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

- [Distributed Event Bus](Distributed_Event_Bus.md) (15 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (12 shared connections)
- [NPC Spawn Validator](NPC_Spawn_Validator.md) (3 shared connections)

## Source Files

- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 173 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*