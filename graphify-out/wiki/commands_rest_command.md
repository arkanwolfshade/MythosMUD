# commands rest command

> 7 nodes

## Key Concepts

- **process_combat_tick()** (9 connections) — `server/app/game_tick_processing.py`
- **test_process_combat_tick_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_calls_service()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Process combat auto-progression.** (1 connections) — `server/app/game_tick_processing.py`
- **Test process_combat_tick() when combat service is not available.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test process_combat_tick() successful execution.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`

## Relationships

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (4 shared connections)
- [command helpers functions](command_helpers_functions.md) (3 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*