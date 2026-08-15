# test_game_tick_processing_async.py

> 41 nodes

## Key Concepts

- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **asyncio** (15 connections)
- **_process_single_effect()** (13 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (12 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (10 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (9 connections) — `server/app/game_tick_processing.py`
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
- **test_process_combat_tick_calls_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_damage_over_time_zero_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_heal_over_time_effect()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_single_effect_heal_expires()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Process a damage over time effect. Returns: True if effect was applied, False…** (1 connections) — `server/app/game_tick_processing.py`
- **Process a heal over time effect. Returns: True if effect was applied, False…** (1 connections) — `server/app/game_tick_processing.py`
- *... and 16 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (12 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [_update_player_status_effects](_update_player_status_effects.md) (5 shared connections)
- [_process_mortally_wounded_player](_process_mortally_wounded_player.md) (3 shared connections)
- [mock_app](mock_app.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 102 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*