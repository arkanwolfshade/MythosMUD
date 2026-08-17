# test_websocket_room_updates.py

> 83 nodes

## Key Concepts

- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (30 connections) — `server/realtime/websocket_room_updates.py`
- **asyncio** (24 connections)
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **occupant_display.py** (11 connections) — `server/realtime/occupant_display.py`
- **format_occupant_display_name()** (10 connections) — `server/realtime/occupant_display.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_build_event.py** (7 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **test_broadcast_room_update_fallback_npc_method()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **_resolve_room_with_fallback()** (4 connections) — `server/realtime/websocket_room_updates.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_broadcast_room_update_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- *... and 58 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (5 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [mock_connection_manager](mock_connection_manager.md) (4 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [.__post_init__](__post_init__.md) (2 shared connections)

## Source Files

- `server/realtime/occupant_display.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`

## Audit Trail

- EXTRACTED: 210 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*