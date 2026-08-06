# level curve game

> 140 nodes

## Key Concepts

- **test_player_repository.py** (40 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_player_repository_room.py** (14 connections) — `server/tests/unit/persistence/test_player_repository_room.py`
- **Player** (13 connections)
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **validate_and_fix_player_room()** (12 connections) — `server/persistence/repositories/player_repository_room.py`
- **_make_mock_row()** (10 connections) — `server/tests/unit/persistence/test_player_repository.py`
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
- *... and 115 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (23 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (15 shared connections)
- [add used user](add_used_user.md) (14 shared connections)
- [player room realtime](player_room_realtime.md) (10 shared connections)
- [game weapon player](game_weapon_player.md) (9 shared connections)
- [logging file setup](logging_file_setup.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [retry rationale transient()](retry_rationale_transient%28%29.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_repository_room.py`
- `server/tests/unit/persistence/test_player_repository.py`
- `server/tests/unit/persistence/test_player_repository_room.py`

## Audit Trail

- EXTRACTED: 494 (95%)
- INFERRED: 28 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*