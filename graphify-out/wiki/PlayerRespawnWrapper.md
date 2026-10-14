# PlayerRespawnWrapper

> 31 nodes

## Key Concepts

- **PlayerRespawnWrapper** (18 connections) — `server/game/player_respawn_wrapper.py`
- **test_player_respawn_wrapper.py** (14 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **.respawn_player_by_user_id()** (7 connections) — `server/game/player_respawn_wrapper.py`
- **asyncio** (7 connections)
- **.respawn_player_from_delirium_by_user_id()** (6 connections) — `server/game/player_respawn_wrapper.py`
- **_select_dead_player_for_respawn()** (6 connections) — `server/game/player_respawn_wrapper.py`
- **._load_active_players()** (5 connections) — `server/game/player_respawn_wrapper.py`
- **._load_player_for_delirium_respawn()** (5 connections) — `server/game/player_respawn_wrapper.py`
- **_resolve_respawn_room_data()** (5 connections) — `server/game/player_respawn_wrapper.py`
- **_is_eligible_for_respawn()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **_dead_player()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_not_delirious()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_player_not_found()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_multiple_dead_picks_most_recent()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_no_players()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_not_dead()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **Any** (4 connections)
- **Player** (4 connections)
- **.__init__()** (3 connections) — `server/game/player_respawn_wrapper.py`
- **Respawn a dead player by user ID. This method handles the complete respawn…** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Load the user's character and validate delirium eligibility (lucidity <= -10).** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Respawn a delirious player by user ID. This method handles the complete…** (1 connections) — `server/game/player_respawn_wrapper.py`
- **A player is eligible for respawn if dead, or stranded in limbo.** (1 connections) — `server/game/player_respawn_wrapper.py`
- *... and 6 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (5 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 63 (84%)
- INFERRED: 12 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*