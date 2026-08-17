# server app game tick counter

> 8 nodes

## Key Concepts

- **reset_current_tick()** (6 connections) — `server/app/game_tick_counter.py`
- **set_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Set the current game tick (game tick loop).** (1 connections) — `server/app/game_tick_counter.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_counter.py`
- **Test get_current_tick returns the current tick value.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test reset_current_tick resets the tick counter.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`

## Relationships

- [server app game tick counter](server_app_game_tick_counter.md) (4 shared connections)
- [server app game tick processing](server_app_game_tick_processing.md) (2 shared connections)
- [server app game tick status](server_app_game_tick_status.md) (2 shared connections)
- [corpselifecycleservice](corpselifecycleservice.md) (1 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 12 (75%)
- INFERRED: 4 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*