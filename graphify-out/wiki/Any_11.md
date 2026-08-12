# Any

> 11 nodes

## Key Concepts

- **Any** (8 connections)
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (4 connections) — `server/app/game_tick_processing.py`
- **test_update_player_status_effects_changes()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_no_changes()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Update and save player status effects if changes occurred. Returns: True if…** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for a single player. Args: mp_service: MP regeneration…** (1 connections) — `server/app/game_tick_processing.py`
- **Cleanup a single decayed corpse. Args: corpse_service: Corpse lifecycle service…** (1 connections) — `server/app/game_tick_processing.py`
- **Test _update_player_status_effects() when no changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _update_player_status_effects() when changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`

## Relationships

- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (8 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (6 shared connections)
- [_process_session_dp_decay_and_death](_process_session_dp_decay_and_death.md) (2 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*