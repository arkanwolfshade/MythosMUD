# NPC Combat Handler Tests

> 27 nodes · cohesion 0.14

## Key Concepts

- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (16 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **resolve_connection_manager()** (14 connections) — `server/realtime/connection_manager_utils.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **lazy_import_api_function()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (5 connections)
- **_coerce_connection_manager()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **Public API utility functions for connection manager.  This module provides conve** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a system notification to a player.      Args:         player_id: The player** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a player status update to a player.      Args:         player_id: The playe** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send room description to a player.      Args:         player_id: The player's ID** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a game event to a specific player via WebSocket.      Args:         player_** (1 connections) — `server/realtime/connection_manager_api.py`
- **Broadcast a game event to all connected players.      Args:         event_type:** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a room event to all players in a specific room.      Args:         room_id:** (1 connections) — `server/realtime/connection_manager_api.py`
- **Utility functions and module-level code for ConnectionManager.  This module cont** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Lazy import for API utility functions to avoid circular dependencies.      Args:** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Narrow container or test doubles to ConnectionManager for static typing.** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Wrap a sync or async callable so callers can always await it.** (1 connections) — `server/realtime/connection_manager_utils.py`
- *... and 2 more nodes in this community*

## Relationships

- [Realtime Connection Impl](Realtime_Connection_Impl.md) (7 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (7 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (4 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (3 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (2 shared connections)
- [Magic Game Healing](Magic_Game_Healing.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (2 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (2 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 122 (80%)
- INFERRED: 31 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*