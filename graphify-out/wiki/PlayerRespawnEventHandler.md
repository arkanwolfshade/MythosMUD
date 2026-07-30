# PlayerRespawnEventHandler

> 8 nodes

## Key Concepts

- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **test_process_heal_over_time_effect_no_healing()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Process a heal over time effect.      Returns:         True if effect was applie** (1 connections) — `server/app/game_tick_processing.py`
- **Test _process_heal_over_time_effect() with no healing.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _process_heal_over_time_effect() with no remaining duration.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _process_heal_over_time_effect() successful application.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`

## Relationships

- [process all status effects()](process_all_status_effects%28%29.md) (5 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [test container persistence sql injection](test_container_persistence_sql_injection.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*