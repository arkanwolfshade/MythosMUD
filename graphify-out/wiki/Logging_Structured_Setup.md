# Logging Structured Setup

> 15 nodes

## Key Concepts

- **_make_mock_row()** (10 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_player_by_name_success()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **UUID** (3 connections)
- **test_list_players_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_players_by_user_id_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_active_players_by_user_id_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_players_in_room_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_get_players_batch_success()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Create a mock procedure result row for row_to_player.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_player_by_name successfully retrieves player.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test list_players successfully retrieves players.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_players_by_user_id successfully retrieves players.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_active_players_by_user_id successfully retrieves active players.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_players_in_room successfully retrieves players.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Test get_players_batch successfully retrieves multiple players.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`

## Relationships

- [Lizard Complexity Findings](Lizard_Complexity_Findings.md) (8 shared connections)
- [Services Player Respawn](Services_Player_Respawn.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_repository.py`

## Audit Trail

- EXTRACTED: 37 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*