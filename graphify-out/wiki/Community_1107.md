# Community 1107

> 12 nodes

## Key Concepts

- **game_tick_counter.py** (9 connections) — `server/app/game_tick_counter.py`
- **get_current_tick()** (8 connections) — `server/app/game_tick_counter.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_counter.py`
- **set_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Shared game tick counter. Kept in a leaf module so combat services can read the…** (1 connections) — `server/app/game_tick_counter.py`
- **Get the current game tick.** (1 connections) — `server/app/game_tick_counter.py`
- **Set the current game tick (game tick loop).** (1 connections) — `server/app/game_tick_counter.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_counter.py`
- **Test get_current_tick returns the current tick value.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test reset_current_tick resets the tick counter.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`

## Relationships

- [Community 550](Community_550.md) (4 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 380](Community_380.md) (2 shared connections)
- [Magic & Tick Services](Magic_&_Tick_Services.md) (1 shared connections)
- [Community 46](Community_46.md) (1 shared connections)
- [Community 893](Community_893.md) (1 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 23 (82%)
- INFERRED: 5 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*