# ConnectionManager

> 41 nodes

## Key Concepts

- **ConnectionManager** (64 connections) — `server/realtime/connection_manager_methods.py`
- **UUID** (24 connections)
- **get_message_delivery_stats_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **check_connection_health_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_count_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_pending_messages_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_session_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_websocket_connection_id_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_rate_limit_info_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **has_websocket_connection_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **validate_session_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **unsubscribe_from_room_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **test_check_connection_health_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **.disconnect_websocket()** (2 connections) — `server/realtime/connection_manager_methods.py`
- **.has_websocket_connection()** (2 connections) — `server/realtime/connection_manager_methods.py`
- **.track_player_disconnected()** (2 connections) — `server/realtime/connection_manager_methods.py`
- **test_get_connection_count_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_get_message_delivery_stats_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_get_pending_messages_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_get_player_session_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_get_player_websocket_connection_id_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_get_rate_limit_info_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_has_websocket_connection_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_validate_session_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **.canonical_room_id()** (1 connections) — `server/realtime/connection_manager_methods.py`
- *... and 16 more nodes in this community*

## Relationships

- [test_connection_manager_methods.py](test_connection_manager_methods.py.md) (19 shared connections)
- [connection_manager.py](connection_manager.py.md) (16 shared connections)
- [asyncio](asyncio.md) (13 shared connections)
- [get_player_impl](get_player_impl.md) (6 shared connections)
- [broadcast_to_room_impl](broadcast_to_room_impl.md) (3 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (3 shared connections)
- [broadcast_global_event_impl](broadcast_global_event_impl.md) (2 shared connections)
- [get_active_connection_count_impl](get_active_connection_count_impl.md) (2 shared connections)
- [update_player_room_cache_impl](update_player_room_cache_impl.md) (2 shared connections)
- [validate_player_presence_impl](validate_player_presence_impl.md) (2 shared connections)
- [get_connection_id_from_websocket_impl](get_connection_id_from_websocket_impl.md) (1 shared connections)
- [get_dual_connection_stats_impl](get_dual_connection_stats_impl.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 123 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*