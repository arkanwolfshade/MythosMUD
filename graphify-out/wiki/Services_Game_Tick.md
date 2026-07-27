# Services Game Tick

> 16 nodes · cohesion 0.12

## Key Concepts

- **GameTickService** (30 connections) — `server/services/game_tick_service.py`
- **.get_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.get_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- **.__init__()** (2 connections) — `server/services/game_tick_service.py`
- **.is_service_running()** (2 connections) — `server/services/game_tick_service.py`
- **.reset_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.set_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- **.stop()** (2 connections) — `server/services/game_tick_service.py`
- **Get the current tick count.          Returns:             int: Current number of** (1 connections) — `server/services/game_tick_service.py`
- **Reset the tick count to zero.** (1 connections) — `server/services/game_tick_service.py`
- **Get the current tick interval.          Returns:             float: Current tick** (1 connections) — `server/services/game_tick_service.py`
- **Set a new tick interval.          Args:             interval: New tick interval** (1 connections) — `server/services/game_tick_service.py`
- **Check if the service is currently running.          Returns:             bool: T** (1 connections) — `server/services/game_tick_service.py`
- **Service that manages the game tick system.      The game tick system runs at reg** (1 connections) — `server/services/game_tick_service.py`
- **Initialize the GameTickService.          Args:             event_publisher: Even** (1 connections) — `server/services/game_tick_service.py`
- **Stop the game tick service.          Returns:             bool: True if stopped** (1 connections) — `server/services/game_tick_service.py`

## Relationships

- [[Services Game Tick]] (21 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/services/game_tick_service.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
