# Item Model Unit Tests

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

- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (8 shared connections)
- [Services Exploration Service](Services_Exploration_Service.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Archive Who Command](Archive_Who_Command.md) (1 shared connections)
- [Schemas Calendar Schedule](Schemas_Calendar_Schedule.md) (1 shared connections)
- [Community 1592](Community_1592.md) (1 shared connections)
- [Combat Results Messages](Combat_Results_Messages.md) (1 shared connections)
- [Community 1594](Community_1594.md) (1 shared connections)
- [Readme Commands](Readme_Commands.md) (1 shared connections)
- [Community 1593](Community_1593.md) (1 shared connections)
- [Community 1596](Community_1596.md) (1 shared connections)
- [Schemas Calendar Holiday](Schemas_Calendar_Holiday.md) (1 shared connections)

## Source Files

- `server/services/game_tick_service.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*