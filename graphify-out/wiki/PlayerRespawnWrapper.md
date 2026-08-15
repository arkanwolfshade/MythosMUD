# PlayerRespawnWrapper

> 19 nodes

## Key Concepts

- **PlayerRespawnWrapper** (15 connections) — `server/game/player_respawn_wrapper.py`
- **test_player_respawn_wrapper.py** (13 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **asyncio** (6 connections)
- **.respawn_player_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **.respawn_player_from_delirium_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **test_respawn_from_delirium_not_delirious()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_player_not_found()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_no_players()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_not_dead()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **.__init__()** (3 connections) — `server/game/player_respawn_wrapper.py`
- **_dead_player()** (3 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **Any** (3 connections)
- **Respawn a delirious player by user ID. This method handles the complete…** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Wrapper service for player respawn operations.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Initialize with a persistence layer.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Respawn a dead player by user ID. This method handles the complete respawn…** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Unit tests for PlayerRespawnWrapper.** (1 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`

## Relationships

- [ValidationError](ValidationError.md) (7 shared connections)
- [Player](Player.md) (3 shared connections)
- [PlayerStateService](PlayerStateService.md) (1 shared connections)
- [Stats](Stats.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 36 (77%)
- INFERRED: 11 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*