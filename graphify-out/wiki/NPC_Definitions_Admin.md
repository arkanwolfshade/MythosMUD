# NPC Definitions Admin

> 300 nodes

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **test_level_service.py** (16 connections) — `server/tests/unit/game/test_level_service.py`
- **total_xp_for_level()** (15 connections) — `server/game/level_curve.py`
- **test_level_curve.py** (15 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_from_total_xp()** (13 connections) — `server/game/level_curve.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **get_combat_service()** (10 connections) — `server/dependencies.py`
- **get_player_service_for_testing()** (9 connections) — `server/dependencies.py`
- **get_connection_manager()** (9 connections) — `server/dependencies.py`
- **get_async_persistence()** (9 connections) — `server/dependencies.py`
- **get_player_respawn_service()** (9 connections) — `server/dependencies.py`
- **get_player_combat_service()** (9 connections) — `server/dependencies.py`
- **get_player_death_service()** (9 connections) — `server/dependencies.py`
- **get_magic_service()** (9 connections) — `server/dependencies.py`
- **get_spell_registry()** (9 connections) — `server/dependencies.py`
- **get_spell_targeting_service()** (9 connections) — `server/dependencies.py`
- **get_spell_effects()** (9 connections) — `server/dependencies.py`
- **get_spell_learning_service()** (9 connections) — `server/dependencies.py`
- **get_mp_regeneration_service()** (9 connections) — `server/dependencies.py`
- *... and 275 more nodes in this community*

## Relationships

- [coercion int inventory](coercion_int_inventory.md) (42 shared connections)
- [room game service](room_game_service.md) (16 shared connections)
- [Loot Generation](Loot_Generation.md) (12 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (6 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (5 shared connections)
- [player service game](player_service_game.md) (5 shared connections)
- [player requests schemas](player_requests_schemas.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [profession game service](profession_game_service.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [command parser rationale](command_parser_rationale.md) (3 shared connections)

## Source Files

- `server/database.py`
- `server/dependencies.py`
- `server/game/level_curve.py`
- `server/game/level_service.py`
- `server/tests/unit/game/test_level_curve.py`
- `server/tests/unit/game/test_level_service.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 1034 (90%)
- INFERRED: 112 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*