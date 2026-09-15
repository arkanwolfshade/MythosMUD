# asyncio

> 21 nodes

## Key Concepts

- **asyncio** (26 connections)
- **test_get_player_by_name_database_error()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_user_id_success()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_list_players_database_error()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_save_player_database_error()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_name_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_user_id_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_soft_delete_player_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_soft_delete_player_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_update_player_last_active_with_timestamp()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_name returns None when player not found.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_name handles database errors.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test save_player handles database errors.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test list_players handles database errors.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_id returns None when player not found.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_user_id returns first active player.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_user_id returns None when no players.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test soft_delete_player successfully soft deletes player.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test soft_delete_player returns False when player not found.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test update_player_last_active with provided timestamp.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`

## Relationships

- [test_player_repository.py](test_player_repository.py.md) (12 shared connections)
- [_make_mock_row](_make_mock_row.md) (7 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [_ScalarResult](_ScalarResult.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [test_delete_player_success](test_delete_player_success.md) (1 shared connections)
- [test_list_players_empty](test_list_players_empty.md) (1 shared connections)
- [test_save_player_with_bool_is_admin](test_save_player_with_bool_is_admin.md) (1 shared connections)
- [test_save_players_success](test_save_players_success.md) (1 shared connections)
- [test_update_player_last_active_success](test_update_player_last_active_success.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_repository.py`

## Audit Trail

- EXTRACTED: 46 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*