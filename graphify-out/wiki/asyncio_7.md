# asyncio

> 38 nodes

## Key Concepts

- **asyncio** (18 connections)
- **broadcast_to_room_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **send_personal_message_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **check_all_connections_health_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **handle_player_entered_room_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **periodic_health_check_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **subscribe_to_room_events_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **unsubscribe_from_room_events_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **test_disconnect_websocket_connection_impl_missing_connection_logs_debug_not_warning()** (5 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_global_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_global_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_room_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_to_room_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_check_all_connections_health_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_disconnect_websocket_connection_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_handle_player_entered_room_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_periodic_health_check_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_safe_close_websocket_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_send_personal_message_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_subscribe_to_room_events_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_unsubscribe_from_room_events_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- *... and 13 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (31 shared connections)
- [connection_manager.py](connection_manager.py.md) (11 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (6 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [test_connection_event_helpers.py](test_connection_event_helpers.py.md) (2 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (1 shared connections)
- [delegate_game_state_provider](delegate_game_state_provider.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 94 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*