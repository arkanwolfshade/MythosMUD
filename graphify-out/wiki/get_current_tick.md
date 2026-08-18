# get_current_tick

> 12 nodes

## Key Concepts

- **get_current_tick()** (14 connections) — `server/app/game_tick_counter.py`
- **game_tick_counter.py** (8 connections) — `server/app/game_tick_counter.py`
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

- [CombatService](CombatService.md) (6 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (4 shared connections)
- [magic_service.py](magic_service.py.md) (3 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 27 (82%)
- INFERRED: 6 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*