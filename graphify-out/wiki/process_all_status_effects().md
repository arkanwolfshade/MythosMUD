# process all status effects()

> 36 nodes

## Key Concepts

- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **_process_damage_over_time_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **test_process_damage_over_time_effect_no_damage()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_healing()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_damage_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_heal_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_expired()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_app()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_container()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_player()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Process a damage over time effect.      Returns:         True if effect was appl** (1 connections) — `server/app/game_tick_processing.py`
- **Process a heal over time effect.      Returns:         True if effect was applie** (1 connections) — `server/app/game_tick_processing.py`
- **Process a single status effect.      Returns:         Tuple of (updated_effect_d** (1 connections) — `server/app/game_tick_processing.py`
- **Unit tests for game tick processing async functions.  Tests the async game tick** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Create a mock FastAPI app.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Create a mock ApplicationContainer.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Create a mock player.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- *... and 11 more nodes in this community*

## Relationships

- [Protocol](Protocol.md) (9 shared connections)
- [test container persistence sql injection](test_container_persistence_sql_injection.md) (8 shared connections)
- [Test process exit rows with](Test_process_exit_rows_with.md) (3 shared connections)
- [login grace period](login_grace_period.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 113 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*