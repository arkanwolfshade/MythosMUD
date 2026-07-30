# Test process exit rows with

> 6 nodes

## Key Concepts

- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **test_process_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Process status effects for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Test process_status_effects() when container is invalid.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test process_status_effects() when no online players.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`

## Relationships

- [Protocol](Protocol.md) (3 shared connections)
- [process all status effects()](process_all_status_effects%28%29.md) (3 shared connections)
- [calendar](calendar.md) (1 shared connections)
- [test container persistence sql injection](test_container_persistence_sql_injection.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*