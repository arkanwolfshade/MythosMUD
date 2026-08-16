# reset_current_tick

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

- [get_current_tick](get_current_tick.md) (4 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 12 (75%)
- INFERRED: 4 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*