# npc_combat_grace.py

> 12 nodes

## Key Concepts

- **get_current_tick()** (11 connections) — `server/app/game_tick_counter.py`
- **game_tick_counter.py** (9 connections) — `server/app/game_tick_counter.py`
- **reset_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **set_current_tick()** (3 connections) — `server/app/game_tick_counter.py`
- **Shared game tick counter. Kept in a leaf module so combat services can read the…** (1 connections) — `server/app/game_tick_counter.py`
- **Get the current game tick.** (1 connections) — `server/app/game_tick_counter.py`
- **Set the current game tick (game tick loop).** (1 connections) — `server/app/game_tick_counter.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_counter.py`
- **Test get_current_tick returns the current tick value.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test reset_current_tick resets the tick counter.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`

## Relationships

- [test_logging_handlers.py](test_logging_handlers.py.md) (4 shared connections)
- [Any](Any.md) (2 shared connections)
- [Memory Leak Prevention System - Implementation Summary](Memory_Leak_Prevention_System_-_Implementation_Summary.md) (2 shared connections)
- [test_metrics.py](test_metrics.py.md) (1 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (1 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (1 shared connections)
- [RoomInfoPanel.tsx](RoomInfoPanel.tsx.md) (1 shared connections)
- [inventory_get_command.py](inventory_get_command.py.md) (1 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 22 (79%)
- INFERRED: 6 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*