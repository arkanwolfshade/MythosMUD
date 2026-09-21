# PlayerRespawnWrapper

> 13 nodes

## Key Concepts

- **PlayerRespawnWrapper** (18 connections) — `server/game/player_respawn_wrapper.py`
- **test_player_respawn_wrapper.py** (14 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **asyncio** (7 connections)
- **_dead_player()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_not_delirious()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_player_not_found()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_multiple_dead_picks_most_recent()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_no_players()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_not_dead()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **Wrapper service for player respawn operations.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Unit tests for PlayerRespawnWrapper.** (1 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [.respawn_player_by_user_id](respawn_player_by_user_id.md) (5 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [models/player.py](models-player.py.md) (1 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 33 (73%)
- INFERRED: 12 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*