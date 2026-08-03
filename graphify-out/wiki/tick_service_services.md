# tick service services

> 16 nodes

## Key Concepts

- **GameTickService** (30 connections) — `server/services/game_tick_service.py`
- **.__init__()** (2 connections) — `server/services/game_tick_service.py`
- **.stop()** (2 connections) — `server/services/game_tick_service.py`
- **.get_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.reset_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.get_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- **.set_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- **.is_service_running()** (2 connections) — `server/services/game_tick_service.py`
- **Service that manages the game tick system.      The game tick system runs at reg** (1 connections) — `server/services/game_tick_service.py`
- **Initialize the GameTickService.          Args:             event_publisher: Even** (1 connections) — `server/services/game_tick_service.py`
- **Stop the game tick service.          Returns:             bool: True if stopped** (1 connections) — `server/services/game_tick_service.py`
- **Get the current tick count.          Returns:             int: Current number of** (1 connections) — `server/services/game_tick_service.py`
- **Reset the tick count to zero.** (1 connections) — `server/services/game_tick_service.py`
- **Get the current tick interval.          Returns:             float: Current tick** (1 connections) — `server/services/game_tick_service.py`
- **Set a new tick interval.          Args:             interval: New tick interval** (1 connections) — `server/services/game_tick_service.py`
- **Check if the service is currently running.          Returns:             bool: T** (1 connections) — `server/services/game_tick_service.py`

## Relationships

- [tick game service](tick_game_service.md) (8 shared connections)
- [tick services game](tick_services_game.md) (6 shared connections)
- [services game tick](services_game_tick.md) (4 shared connections)
- [npc realtime event](npc_realtime_event.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [player realtime event](player_realtime_event.md) (1 shared connections)

## Source Files

- `server/services/game_tick_service.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*