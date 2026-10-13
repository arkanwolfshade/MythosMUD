# Community 818

> 20 nodes

## Key Concepts

- **GameTickService** (11 connections) — `server/services/game_tick_service.py`
- **.start()** (4 connections) — `server/services/game_tick_service.py`
- **._tick_loop()** (3 connections) — `server/services/game_tick_service.py`
- **.get_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.get_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- **.__init__()** (2 connections) — `server/services/game_tick_service.py`
- **.is_service_running()** (2 connections) — `server/services/game_tick_service.py`
- **.reset_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.set_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- **.stop()** (2 connections) — `server/services/game_tick_service.py`
- **Get the current tick count. Returns: int: Current number of ticks processed** (1 connections) — `server/services/game_tick_service.py`
- **Reset the tick count to zero.** (1 connections) — `server/services/game_tick_service.py`
- **Get the current tick interval. Returns: float: Current tick interval in seconds** (1 connections) — `server/services/game_tick_service.py`
- **Set a new tick interval. Args: interval: New tick interval in seconds** (1 connections) — `server/services/game_tick_service.py`
- **Check if the service is currently running. Returns: bool: True if running,…** (1 connections) — `server/services/game_tick_service.py`
- **Service that manages the game tick system. The game tick system runs at regular…** (1 connections) — `server/services/game_tick_service.py`
- **Initialize the GameTickService. Args: event_publisher: EventPublisher instance…** (1 connections) — `server/services/game_tick_service.py`
- **Start the game tick service. Returns: bool: True if started successfully, False…** (1 connections) — `server/services/game_tick_service.py`
- **Stop the game tick service. Returns: bool: True if stopped successfully, False…** (1 connections) — `server/services/game_tick_service.py`
- **Main tick loop that runs at the specified interval.** (1 connections) — `server/services/game_tick_service.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Community 404](Community_404.md) (1 shared connections)

## Source Files

- `server/services/game_tick_service.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*