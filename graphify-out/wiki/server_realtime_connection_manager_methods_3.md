# server realtime connection manager methods

> 34 nodes

## Key Concepts

- **asyncio** (17 connections)
- **broadcast_to_room_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **check_all_connections_health_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **get_room_occupants_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **handle_player_entered_room_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **periodic_health_check_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **subscribe_to_room_events_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **unsubscribe_from_room_events_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **test_broadcast_global_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_global_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_room_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_to_room_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_check_all_connections_health_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_disconnect_websocket_connection_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_get_room_occupants_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_handle_player_entered_room_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_periodic_health_check_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_subscribe_to_room_events_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_unsubscribe_from_room_events_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **Broadcast a message to all players in a room.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Broadcast a message to all connected players.** (1 connections) — `server/realtime/connection_manager_methods.py`
- *... and 9 more nodes in this community*

## Relationships

- [server realtime connection manager methods](server_realtime_connection_manager_methods.md) (29 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server realtime connection websocket close](server_realtime_connection_websocket_close.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 76 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*