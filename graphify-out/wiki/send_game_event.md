# send_game_event

> 29 nodes

## Key Concepts

- **send_game_event()** (28 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (16 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **resolve_connection_manager()** (14 connections) — `server/realtime/connection_manager_utils.py`
- **lazy_import_api_function()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **broadcast_game_event()** (10 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (6 connections) — `server/realtime/connection_manager_api.py`
- **__getattr__()** (5 connections) — `server/realtime/connection_manager.py`
- **UUID** (5 connections)
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **Public API utility functions for connection manager. This module provides…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a system notification to a player. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a player status update to a player. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send room description to a player. Args: player_id: The player's ID room_data:…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a game event to a specific player via WebSocket. Args: player_id: The…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Broadcast a game event to all connected players. Args: event_type: The type of…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a room event to all players in a specific room. Args: room_id: The room's…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Lazy import for API utility functions to avoid circular dependencies.** (1 connections) — `server/realtime/connection_manager.py`
- **Utility functions and module-level code for ConnectionManager. This module…** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Lazy import for API utility functions to avoid circular dependencies. Args:…** (1 connections) — `server/realtime/connection_manager_utils.py`
- *... and 4 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (8 shared connections)
- [connection_manager.py](connection_manager.py.md) (5 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [message_handlers.py](message_handlers.py.md) (2 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 84 (84%)
- INFERRED: 16 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*