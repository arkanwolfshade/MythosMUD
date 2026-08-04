# player service game

> 146 nodes

## Key Concepts

- **Stats** (88 connections) — `server/models/game.py`
- **StatsGenerator** (48 connections) — `server/game/stats_generator.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **stats_generator.py** (15 connections) — `server/game/stats_generator.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
- **Stats** (11 connections)
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **.validate_current_vs_max_stats()** (5 connections) — `server/models/game.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **.__init__()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **.test_get_stats_generator()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **._compute_max_dp_if_missing()** (3 connections) — `server/models/game.py`
- *... and 121 more nodes in this community*

## Relationships

- [command factories communication](command_factories_communication.md) (14 shared connections)
- [profession game service](profession_game_service.md) (12 shared connections)
- [npc rationale extract](npc_rationale_extract.md) (10 shared connections)
- [room game service](room_game_service.md) (8 shared connections)
- [Loot Generation](Loot_Generation.md) (7 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (5 shared connections)
- [command commands handler](command_commands_handler.md) (5 shared connections)
- [player event state](player_event_state.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/game/test_stats_generator.py`
- `server/tests/unit/models/test_game_stats_methods.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 503 (95%)
- INFERRED: 26 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*