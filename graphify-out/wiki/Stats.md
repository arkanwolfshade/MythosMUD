# Stats

> 205 nodes

## Key Concepts

- **Stats** (77 connections) — `server/models/game.py`
- **StatsGenerator** (43 connections) — `server/game/stats_generator.py`
- **test_character_creation_service.py** (33 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_generator.py** (20 connections) — `server/tests/unit/game/test_stats_generator.py`
- **stats_generator.py** (16 connections) — `server/game/stats_generator.py`
- **character_creation_service.py** (15 connections) — `server/game/character_creation_service.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
- **Stats** (11 connections)
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **.create_character_with_stats()** (6 connections) — `server/game/character_creation_service.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **.validate_current_vs_max_stats()** (6 connections) — `server/models/game.py`
- **.validate_character_stats()** (5 connections) — `server/game/character_creation_service.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **Any** (5 connections)
- **.get_available_classes_info()** (4 connections) — `server/game/character_creation_service.py`
- **.__init__()** (4 connections) — `server/game/character_creation_service.py`
- **.roll_character_stats()** (4 connections) — `server/game/character_creation_service.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- *... and 180 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (15 shared connections)
- [PlayerService](PlayerService.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [ValidationError](ValidationError.md) (8 shared connections)
- [server/models/game.py](server-models-game.py.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_player_service.py](test_player_service.py.md) (4 shared connections)
- [models/player.py](models-player.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [.create_player_read_from_object](create_player_read_from_object.md) (2 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/game/test_stats_generator.py`
- `server/tests/unit/models/test_game_stats_methods.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 371 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*