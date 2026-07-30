# test container persistence sql injection

> 18 nodes

## Key Concepts

- **Any** (7 connections)
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (5 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **test_update_player_status_effects_no_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Update and save player status effects if changes occurred.      Returns:** (1 connections) — `server/app/game_tick_processing.py`
- **Validate container and retrieve player by ID.      Args:         container: Appl** (1 connections) — `server/app/game_tick_processing.py`
- **Process all status effects for a player.      Args:         app: FastAPI applica** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for a single player.      Returns:         True if player** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for a single player.      Args:         mp_service: MP r** (1 connections) — `server/app/game_tick_processing.py`
- **Cleanup a single decayed corpse.      Args:         corpse_service: Corpse lifec** (1 connections) — `server/app/game_tick_processing.py`
- **Test _update_player_status_effects() when no changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _update_player_status_effects() when changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`

## Relationships

- [Protocol](Protocol.md) (11 shared connections)
- [process all status effects()](process_all_status_effects%28%29.md) (8 shared connections)
- [Calculate max magic points (MP)](Calculate_max_magic_points_%28MP%29.md) (2 shared connections)
- [Test process exit rows with](Test_process_exit_rows_with.md) (1 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (1 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*