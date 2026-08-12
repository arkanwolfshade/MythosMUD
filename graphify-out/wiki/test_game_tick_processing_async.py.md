# test_game_tick_processing_async.py

> 35 nodes

## Key Concepts

- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **asyncio** (15 connections)
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (10 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **test_process_combat_tick_no_service()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_damage()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_remaining()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_healing()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_remaining()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_damage_over_time()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_expired()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_heal_over_time()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_container()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_online_players()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Process a damage over time effect. Returns: True if effect was applied, False…** (1 connections) — `server/app/game_tick_processing.py`
- **Process a heal over time effect. Returns: True if effect was applied, False…** (1 connections) — `server/app/game_tick_processing.py`
- **Process a single status effect. Returns: Tuple of (updated_effect_dict or None…** (1 connections) — `server/app/game_tick_processing.py`
- **Unit tests for game tick processing async functions. Tests the async game tick…** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _process_single_effect() with damage_over_time effect.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _process_single_effect() with heal_over_time effect.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _process_single_effect() with expired effect.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- *... and 10 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (13 shared connections)
- [Any](Any.md) (8 shared connections)
- [mock_app](mock_app.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 139 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*