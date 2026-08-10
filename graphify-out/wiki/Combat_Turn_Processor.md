# Combat Turn Processor

> 22 nodes

## Key Concepts

- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **resolve_connection_manager()** (14 connections) — `server/realtime/connection_manager_utils.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **lazy_import_api_function()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **__getattr__()** (5 connections) — `server/realtime/connection_manager.py`
- **_coerce_connection_manager()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **Lazy import for API utility functions to avoid circular dependencies.** (1 connections) — `server/realtime/connection_manager.py`
- **Send a game event to a specific player via WebSocket.      Args:         player_** (1 connections) — `server/realtime/connection_manager_api.py`
- **Broadcast a game event to all connected players.      Args:         event_type:** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a room event to all players in a specific room.      Args:         room_id:** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a player status update to a player.      Args:         player_id: The playe** (1 connections) — `server/realtime/connection_manager_api.py`
- **Utility functions and module-level code for ConnectionManager.  This module cont** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Narrow container or test doubles to ConnectionManager for static typing.** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Wrap a sync or async callable so callers can always await it.** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Ensure connection manager methods are awaitable.      Wraps synchronous callable** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Resolve a connection manager instance.      Prefers explicitly supplied candidat** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Lazy import for API utility functions to avoid circular dependencies.      Args:** (1 connections) — `server/realtime/connection_manager_utils.py`

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (12 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (8 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (4 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (3 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (2 shared connections)
- [Database Error Handling](Database_Error_Handling.md) (2 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (2 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (2 shared connections)
- [Security Headers Middleware](Security_Headers_Middleware.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 93 (77%)
- INFERRED: 28 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*