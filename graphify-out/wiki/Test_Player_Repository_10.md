# Test Player Repository

> 17 nodes

## Key Concepts

- **asyncio** (24 connections)
- **test_save_players_success()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_delete_player_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_delete_player_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_user_id_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
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

- [Test Player Repository](Test_Player_Repository.md) (24 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_repository.py`

## Audit Trail

- EXTRACTED: 40 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*