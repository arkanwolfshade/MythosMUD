# connection_manager.py

> 161 nodes · cohesion 0.02

## Key Concepts

- **connection_manager.py** (165 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (89 connections) — `server/realtime/connection_manager_methods.py`
- **Any** (60 connections)
- **UUID** (27 connections)
- **safe_close_websocket_impl()** (10 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_to_room_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **check_connection_health_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **check_and_cleanup_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **cleanup_dead_connections_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **cleanup_orphaned_data_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **detect_and_handle_error_state_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **force_disconnect_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_message_delivery_stats_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_next_sequence_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_presence_info_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **handle_authentication_error_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **handle_security_violation_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **handle_websocket_error_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- *... and 136 more nodes in this community*

## Relationships

- [UUID](UUID.md) (44 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (40 shared connections)
- [get_logger](get_logger.md) (29 shared connections)
- [ConnectionManager](ConnectionManager.md) (29 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (10 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (8 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (8 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (7 shared connections)
- [.__init__](__init__.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 853 (100%)
- INFERRED: 4 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*