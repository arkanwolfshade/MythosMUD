# System Metrics

> 98 nodes

## Key Concepts

- **Stats** (88 connections) — `server/models/game.py`
- **StatsGenerator** (48 connections) — `server/game/stats_generator.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **stats_generator.py** (15 connections) — `server/game/stats_generator.py`
- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
- **.__init__()** (4 connections) — `server/models/game.py`
- **._compute_max_dp_if_missing()** (3 connections) — `server/models/game.py`
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **test_roll_stats_unknown_method_falls_back_to_3d6()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_passes_investigator()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_fails_occultist()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_unknown_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_available_classes_filters_by_prerequisites()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_validation_respects_required_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_check_profession_requirements_maps_wisdom_to_power()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_check_profession_requirements_unknown_stat_fails()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_stat_summary_includes_totals()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_profession_no_requirements()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_stats_validate_current_vs_max_stats_caps_dp()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_caps_magic_points()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_caps_lucidity()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_allows_valid_values()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_negative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- *... and 73 more nodes in this community*

## Relationships

- [player service game](player_service_game.md) (15 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (12 shared connections)
- [admin auth service](admin_auth_service.md) (12 shared connections)
- [persistence container extended](persistence_container_extended.md) (10 shared connections)
- [npc rationale extract](npc_rationale_extract.md) (7 shared connections)
- [services npc startup](services_npc_startup.md) (6 shared connections)
- [tick service services](tick_service_services.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [combat services turn](combat_services_turn.md) (4 shared connections)
- [schemas invite user](schemas_invite_user.md) (4 shared connections)
- [add used user](add_used_user.md) (3 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_stats_generator.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 389 (95%)
- INFERRED: 19 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*