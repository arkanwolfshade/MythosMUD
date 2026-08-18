# server realtime connection error methods

> 196 nodes

## Key Concepts

- **ConnectionManager** (168 connections) — `server/realtime/connection_manager.py`
- **connection_manager.py** (128 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_connection_error_methods.py** (15 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **connection_error_methods.py** (11 connections) — `server/realtime/connection_error_methods.py`
- **ConnectionManager** (11 connections)
- **detect_and_handle_error_state_impl()** (10 connections) — `server/realtime/connection_error_methods.py`
- **handle_authentication_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_security_violation_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_websocket_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **recover_from_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **NewGameSessionResult** (7 connections) — `server/realtime/connection_session_management.py`
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **UUID** (6 connections)
- **asyncio** (6 connections)
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Any** (5 connections)
- **Player** (5 connections)
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- *... and 171 more nodes in this community*

## Relationships

- [server api container events](server_api_container_events.md) (14 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (13 shared connections)
- [deque](deque.md) (13 shared connections)
- [server realtime connection cleanup methods](server_realtime_connection_cleanup_methods.md) (13 shared connections)
- [server realtime connection manager connectionmanager](server_realtime_connection_manager_connectionmanager.md) (11 shared connections)
- [server realtime connection helpers](server_realtime_connection_helpers.md) (10 shared connections)
- [server realtime connection delegates](server_realtime_connection_delegates.md) (10 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (9 shared connections)
- [server realtime connection disconnection](server_realtime_connection_disconnection.md) (8 shared connections)
- [server realtime player presence tracker](server_realtime_player_presence_tracker.md) (7 shared connections)
- [server container main get container](server_container_main_get_container.md) (6 shared connections)

## Source Files

- `server/realtime/__init__.py`
- `server/realtime/connection_error_methods.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_error_methods.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 487 (92%)
- INFERRED: 44 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*