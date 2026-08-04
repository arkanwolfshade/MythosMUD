# realtime monitoring statistics

> 45 nodes

## Key Concepts

- **send_game_event()** (30 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (21 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_game_event()** (12 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **test_connection_manager_api.py** (10 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
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
- *... and 20 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (9 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [party service game](party_service_game.md) (5 shared connections)
- [room look commands](room_look_commands.md) (4 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (3 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`

## Audit Trail

- EXTRACTED: 171 (90%)
- INFERRED: 20 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*