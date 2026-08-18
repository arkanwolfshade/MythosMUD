# computed field

> 113 nodes

## Key Concepts

- **Stats** (77 connections) — `server/models/game.py`
- **StatsGenerator** (43 connections) — `server/game/stats_generator.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_generator.py** (20 connections) — `server/tests/unit/game/test_stats_generator.py`
- **stats_generator.py** (16 connections) — `server/game/stats_generator.py`
- **character_creation_service.py** (15 connections) — `server/game/character_creation_service.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
- **AttributeType** (8 connections) — `server/models/game.py`
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
- *... and 88 more nodes in this community*

## Relationships

- [server api character creation](server_api_character_creation.md) (20 shared connections)
- [server game stats generator py](server_game_stats_generator_py.md) (12 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (10 shared connections)
- [server game character creation service](server_game_character_creation_service.md) (6 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (6 shared connections)
- [server dependencies](server_dependencies.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [fixturerequest](fixturerequest.md) (4 shared connections)
- [server api players](server_api_players.md) (3 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (3 shared connections)
- [server tests unit test dependency](server_tests_unit_test_dependency.md) (1 shared connections)
- [server async persistence](server_async_persistence.md) (1 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/game/test_stats_generator.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 259 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*