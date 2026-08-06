# combat npc service

> 67 nodes

## Key Concepts

- **test_player_repository.py** (40 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **_make_mock_row()** (10 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_name_success()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **UUID** (3 connections)
- **player_repository()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **mock_player()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_player_repository_initialization()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_player_repository_initialization_with_cache()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_player_repository_initialization_with_event_bus()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_name_database_error()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_save_player_database_error()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_list_players_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_list_players_database_error()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_id_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_players_by_user_id_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_active_players_by_user_id_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_user_id_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_players_in_room_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_save_players_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_players_batch_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_validate_and_fix_player_room_valid()** (2 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_validate_and_fix_player_room_invalid()** (2 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_name_not_found()** (2 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_save_player_success()** (2 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_save_player_with_bool_is_admin()** (2 connections) — `server/tests/unit/persistence/test_player_repository.py`
- *... and 42 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (12 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (5 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_repository.py`

## Audit Trail

- EXTRACTED: 158 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*