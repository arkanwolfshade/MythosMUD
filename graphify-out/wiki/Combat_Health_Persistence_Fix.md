# Combat Health Persistence Fix

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

- [AnyIO Code Review](AnyIO_Code_Review.md) (8 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (3 shared connections)
- [Components Panels Monitoringpaneltestfixtures](Components_Panels_Monitoringpaneltestfixtures.md) (2 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Cursor Plans Postgresql](Cursor_Plans_Postgresql.md) (1 shared connections)
- [Realtime Player Event](Realtime_Player_Event.md) (1 shared connections)
- [Realtime Websocket Handler](Realtime_Websocket_Handler.md) (1 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (1 shared connections)
- [Realtime Nats Message](Realtime_Nats_Message.md) (1 shared connections)
- [Persistence Repositories Skill](Persistence_Repositories_Skill.md) (1 shared connections)

## Source Files

- `server/services/game_tick_service.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*