# config rationale config()

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

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (3 shared connections)
- [tick game processing](tick_game_processing.md) (3 shared connections)
- [player persistence repository](player_persistence_repository.md) (1 shared connections)
- [persistence combat handler](persistence_combat_handler.md) (1 shared connections)

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