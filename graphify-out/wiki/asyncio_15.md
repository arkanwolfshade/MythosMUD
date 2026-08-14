# asyncio

> 17 nodes

## Key Concepts

- **asyncio** (24 connections)
- **test_delete_player_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_delete_player_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_user_id_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_save_players_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_soft_delete_player_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_update_player_last_active_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_update_player_last_active_with_timestamp()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_id returns None when player not found.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_user_id returns None when no players.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test save_players successfully saves multiple players.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test soft_delete_player successfully soft deletes player.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test delete_player successfully deletes player.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test delete_player returns False when player not found.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test update_player_last_active successfully updates timestamp.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test update_player_last_active with provided timestamp.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`

## Relationships

- [test_player_repository.py](test_player_repository.py.md) (10 shared connections)
- [_make_mock_row](_make_mock_row.md) (6 shared connections)
- [test_get_player_by_name_database_error](test_get_player_by_name_database_error.md) (1 shared connections)
- [test_get_player_by_user_id_success](test_get_player_by_user_id_success.md) (1 shared connections)
- [test_get_players_batch_success](test_get_players_batch_success.md) (1 shared connections)
- [test_list_players_database_error](test_list_players_database_error.md) (1 shared connections)
- [test_save_player_database_error](test_save_player_database_error.md) (1 shared connections)
- [test_save_player_success](test_save_player_success.md) (1 shared connections)
- [test_save_player_with_bool_is_admin](test_save_player_with_bool_is_admin.md) (1 shared connections)
- [test_soft_delete_player_not_found](test_soft_delete_player_not_found.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_repository.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*