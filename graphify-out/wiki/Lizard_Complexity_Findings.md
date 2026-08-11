# Lizard Complexity Findings

> 12 nodes

## Key Concepts

- **test_player_repository.py** (40 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_user_id_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_list_players_empty()** (2 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_id_not_found()** (2 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_delete_player_not_found()** (2 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_update_player_last_active_success()** (2 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Unit tests for player repository.  Tests the PlayerRepository class which handle** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test list_players returns empty list when no players.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_id returns None when player not found.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_user_id returns first active player.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test delete_player returns False when player not found.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test update_player_last_active successfully updates timestamp.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`

## Relationships

- [Logging Structured Setup](Logging_Structured_Setup.md) (8 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Migration Verification](Migration_Verification.md) (2 shared connections)
- [Commands Go Command](Commands_Go_Command.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [test_process_exit_rows_missing_direction](test_process_exit_rows_missing_direction.md) (1 shared connections)
- [test_process_exit_rows_missing_zone](test_process_exit_rows_missing_zone.md) (1 shared connections)
- [Services Player Respawn](Services_Player_Respawn.md) (1 shared connections)
- [test_get_user_role_with_dict_is_admin](test_get_user_role_with_dict_is_admin.md) (1 shared connections)
- [test_get_valid_exits_empty_room](test_get_valid_exits_empty_room.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_repository.py`

## Audit Trail

- EXTRACTED: 56 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*