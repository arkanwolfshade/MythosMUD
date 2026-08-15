# AttributeError

> 157 nodes

## Key Concepts

- **AttributeError** (45 connections)
- **test_websocket_room_updates.py** (34 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (30 connections) — `server/realtime/websocket_room_updates.py`
- **format_room_drop_lines()** (25 connections) — `server/utils/room_renderer.py`
- **test_room_renderer.py** (25 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **asyncio** (24 connections)
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **clone_room_drops()** (18 connections) — `server/utils/room_renderer.py`
- **test_room_renderer_functions.py** (14 connections) — `server/tests/unit/utils/test_room_renderer_functions.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **build_room_drop_summary()** (13 connections) — `server/utils/room_renderer.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **room_renderer.py** (10 connections) — `server/utils/room_renderer.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_build_event.py** (6 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_broadcast_room_update_fallback_npc_method()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **_resolve_room_with_fallback()** (4 connections) — `server/realtime/websocket_room_updates.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_broadcast_room_update_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- *... and 132 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (5 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [test_look_room.py](test_look_room.py.md) (4 shared connections)
- [occupant_display.py](occupant_display.py.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (3 shared connections)
- [look_command.py](look_command.py.md) (3 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (3 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (2 shared connections)
- [test_status_commands.py](test_status_commands.py.md) (2 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/services/test_room_sync_service.py`
- `server/tests/unit/utils/test_room_renderer.py`
- `server/tests/unit/utils/test_room_renderer_functions.py`
- `server/utils/room_renderer.py`

## Audit Trail

- EXTRACTED: 305 (87%)
- INFERRED: 44 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*