# Combat Turn Processor

> 29 nodes

## Key Concepts

- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (16 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **resolve_connection_manager()** (14 connections) — `server/realtime/connection_manager_utils.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **lazy_import_api_function()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **__getattr__()** (5 connections) — `server/realtime/connection_manager.py`
- **UUID** (5 connections)
- **_coerce_connection_manager()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **Lazy import for API utility functions to avoid circular dependencies.** (1 connections) — `server/realtime/connection_manager.py`
- **Public API utility functions for connection manager.  This module provides conve** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a game event to a specific player via WebSocket.      Args:         player_** (1 connections) — `server/realtime/connection_manager_api.py`
- **Broadcast a game event to all connected players.      Args:         event_type:** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a room event to all players in a specific room.      Args:         room_id:** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a system notification to a player.      Args:         player_id: The player** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a player status update to a player.      Args:         player_id: The playe** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send room description to a player.      Args:         player_id: The player's ID** (1 connections) — `server/realtime/connection_manager_api.py`
- **Utility functions and module-level code for ConnectionManager.  This module cont** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Narrow container or test doubles to ConnectionManager for static typing.** (1 connections) — `server/realtime/connection_manager_utils.py`
- *... and 4 more nodes in this community*

## Relationships

- [Schemas Maps Map](Schemas_Maps_Map.md) (8 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (5 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (4 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (3 shared connections)
- [Command Alias Handling](Command_Alias_Handling.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)
- [Architecture Review Plan](Architecture_Review_Plan.md) (2 shared connections)
- [Server Process Termination](Server_Process_Termination.md) (2 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (2 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 127 (80%)
- INFERRED: 32 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*