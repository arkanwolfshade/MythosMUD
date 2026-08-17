# ConnectionManager

> 151 nodes

## Key Concepts

- **ConnectionManager** (255 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **NewGameSessionResult** (7 connections) — `server/realtime/connection_session_management.py`
- **get_connection_id_from_websocket_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **._get_player()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **convert_room_players_uuids_to_names_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_dual_connection_stats_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **handle_player_left_room_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **stop_health_checks_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **.broadcast_to_room()** (4 connections) — `server/realtime/connection_manager.py`
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket_connection()** (4 connections) — `server/realtime/connection_manager.py`
- *... and 126 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (76 shared connections)
- [container_events.py](container_events.py.md) (31 shared connections)
- [connection_manager.py](connection_manager.py.md) (26 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (10 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (8 shared connections)
- [EventHandler](EventHandler.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [RateLimiter](RateLimiter.md) (6 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (6 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (4 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (4 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (4 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 420 (91%)
- INFERRED: 44 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*