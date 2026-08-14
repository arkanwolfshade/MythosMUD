# Stats

> 112 nodes

## Key Concepts

- **Stats** (77 connections) — `server/models/game.py`
- **StatsGenerator** (47 connections) — `server/game/stats_generator.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **stats_generator.py** (15 connections) — `server/game/stats_generator.py`
- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
- **.validate_current_vs_max_stats()** (6 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **._compute_max_dp_if_missing()** (4 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/game.py`
- **.max_lucidity()** (4 connections) — `server/models/game.py`
- **.max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **test_check_profession_requirements_maps_wisdom_to_power()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_check_profession_requirements_unknown_stat_fails()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_available_classes_filters_by_prerequisites()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_stat_summary_includes_totals()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_profession_no_requirements()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_validation_respects_required_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_fails_occultist()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_passes_investigator()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_unknown_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- *... and 87 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (13 shared connections)
- [Stats](Stats.md) (12 shared connections)
- [server/models/game.py](server-models-game.py.md) (11 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (9 shared connections)
- [CharacterCreationService](CharacterCreationService.md) (6 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [test_player_schemas.py](test_player_schemas.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [player_schema_converter.py](player_schema_converter.py.md) (3 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/game/test_stats_generator.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 249 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*