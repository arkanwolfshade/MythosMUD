# NPC Definitions Admin

> 318 nodes

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **game.py** (25 connections) — `server/api/game.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
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
- *... and 293 more nodes in this community*

## Relationships

- [magic healing game](magic_healing_game.md) (43 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (19 shared connections)
- [NATS Messaging](NATS_Messaging.md) (16 shared connections)
- [character creation validate](character_creation_validate.md) (11 shared connections)
- [game rationale schemas](game_rationale_schemas.md) (8 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (8 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (8 shared connections)
- [auth users rationale](auth_users_rationale.md) (6 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (6 shared connections)
- [player model models](player_model_models.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)

## Source Files

- `server/api/game.py`
- `server/database.py`
- `server/dependencies.py`
- `server/game/level_curve.py`
- `server/game/level_service.py`
- `server/tests/unit/game/test_level_curve.py`
- `server/tests/unit/game/test_level_service.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 1109 (90%)
- INFERRED: 123 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*