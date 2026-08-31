# test_websocket_room_updates.py

> 74 nodes

## Key Concepts

- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **broadcast_room_update()** (24 connections) — `server/realtime/websocket_room_updates.py`
- **asyncio** (24 connections)
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **test_warded_indicator_in_websocket_room_updates()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_broadcast_room_update_fallback_npc_method()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **_resolve_room_with_fallback()** (4 connections) — `server/realtime/websocket_room_updates.py`
- **test_broadcast_room_update_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event_with_drops()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_filters_dead()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_no_service()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_filters_dead()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- *... and 49 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (5 shared connections)
- [test_look_room.py](test_look_room.py.md) (5 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (4 shared connections)
- [connection_manager_from_running_app](connection_manager_from_running_app.md) (3 shared connections)
- [test_websocket_room_updates_build_event.py](test_websocket_room_updates_build_event.py.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [occupant_display.py](occupant_display.py.md) (3 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (3 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`

## Audit Trail

- EXTRACTED: 182 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*