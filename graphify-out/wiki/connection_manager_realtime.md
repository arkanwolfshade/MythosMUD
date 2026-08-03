# connection manager realtime

> 35 nodes

## Key Concepts

- **send_game_event()** (30 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (19 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_game_event()** (12 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **__getattr__()** (9 connections) — `server/realtime/connection_manager.py`
- **send_room_event()** (8 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **_require_manager()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (6 connections)
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **.send_personal_message()** (3 connections) — `server/realtime/connection_manager_api.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **.broadcast_global()** (2 connections) — `server/realtime/connection_manager_api.py`
- **.broadcast_to_room()** (2 connections) — `server/realtime/connection_manager_api.py`
- **Lazy import for API utility functions to avoid circular dependencies.** (1 connections) — `server/realtime/connection_manager.py`
- **Protocol** (1 connections)
- **Public API utility functions for connection manager.  This module provides conve** (1 connections) — `server/realtime/connection_manager_api.py`
- **Structural type for API helpers; avoids importing ConnectionManager.** (1 connections) — `server/realtime/connection_manager_api.py`
- **Resolve manager without importing ConnectionManager (import cycle).** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a game event to a specific player via WebSocket.      Args:         player_** (1 connections) — `server/realtime/connection_manager_api.py`
- *... and 10 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (9 shared connections)
- [Database Config](Database_Config.md) (8 shared connections)
- [combat services messaging](combat_services_messaging.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [follow game service](follow_game_service.md) (4 shared connections)
- [game models player](game_models_player.md) (4 shared connections)
- [tick game processing](tick_game_processing.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (3 shared connections)
- [aggro threat services](aggro_threat_services.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)
- [magic healing game](magic_healing_game.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 150 (88%)
- INFERRED: 20 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*