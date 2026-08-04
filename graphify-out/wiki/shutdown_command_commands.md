# shutdown command commands

> 73 nodes

## Key Concepts

- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_player_repository_room.py** (14 connections) — `server/tests/unit/persistence/test_player_repository_room.py`
- **Player** (13 connections)
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **validate_and_fix_player_room()** (12 connections) — `server/persistence/repositories/player_repository_room.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **should_skip_room_validation()** (9 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room_with_persistence()** (9 connections) — `server/persistence/repositories/player_repository_room.py`
- **_player()** (9 connections) — `server/tests/unit/persistence/test_player_repository_room.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository_room.py** (8 connections) — `server/persistence/repositories/player_repository_room.py`
- **UUID** (7 connections)
- **.update_player_last_active()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.save_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.save_players()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.soft_delete_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.delete_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **Any** (5 connections)
- *... and 48 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (32 shared connections)
- [Database Config](Database_Config.md) (13 shared connections)
- [combat models rationale](combat_models_rationale.md) (12 shared connections)
- [combat npc service](combat_npc_service.md) (6 shared connections)
- [npc population stats](npc_population_stats.md) (5 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_repository_room.py`
- `server/tests/unit/persistence/test_player_repository_room.py`

## Audit Trail

- EXTRACTED: 336 (94%)
- INFERRED: 20 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*