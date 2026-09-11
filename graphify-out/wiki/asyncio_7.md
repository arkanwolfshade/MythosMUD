# asyncio

> 32 nodes

## Key Concepts

- **asyncio** (18 connections)
- **disconnect_websocket_connection_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **send_personal_message_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **check_all_connections_health_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_room_occupants_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **handle_player_entered_room_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **periodic_health_check_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **subscribe_to_room_events_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **subscribe_to_room_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **unsubscribe_from_room_events_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **test_disconnect_websocket_connection_impl_missing_connection_logs_debug_not_warning()** (5 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_check_all_connections_health_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_disconnect_websocket_connection_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_get_room_occupants_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_handle_player_entered_room_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_periodic_health_check_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_safe_close_websocket_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_send_personal_message_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_subscribe_to_room_events_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_subscribe_to_room_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_unsubscribe_from_room_events_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **LogCaptureFixture** (1 connections)
- **Disconnect a specific WebSocket connection for a player.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Check health of all connections and clean up stale/dead ones.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Periodic health check task that runs continuously.** (1 connections) — `server/realtime/connection_manager_methods.py`
- *... and 7 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (16 shared connections)
- [ConnectionManager](ConnectionManager.md) (13 shared connections)
- [test_connection_manager_methods.py](test_connection_manager_methods.py.md) (11 shared connections)
- [broadcast_global_event_impl](broadcast_global_event_impl.md) (2 shared connections)
- [broadcast_to_room_impl](broadcast_to_room_impl.md) (2 shared connections)
- [get_player_impl](get_player_impl.md) (2 shared connections)
- [safe_close_websocket_impl](safe_close_websocket_impl.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*