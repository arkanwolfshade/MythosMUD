# connection_manager_health_cleanup.py

> 79 nodes

## Key Concepts

- **connection_manager_health_cleanup.py** (29 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **delegate_error_handler()** (18 connections) — `server/realtime/connection_delegates.py`
- **test_connection_cleanup_methods.py** (17 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **delegate_connection_cleaner()** (16 connections) — `server/realtime/connection_delegates.py`
- **Any** (15 connections)
- **age_off_disconnected_sessions()** (13 connections) — `server/realtime/player_disconnect_handlers.py`
- **CleanupContext** (10 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **cleanup_dead_connections_impl()** (10 connections) — `server/realtime/connection_cleanup_methods.py`
- **check_and_cleanup_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_ghost_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **force_cleanup_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **UUID** (8 connections)
- **check_connection_health_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **Any** (6 connections)
- **check_and_cleanup_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_dead_connections_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_orphaned_data_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **detect_and_handle_error_state_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_authentication_error_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_security_violation_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_websocket_error_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **recover_from_error_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- *... and 54 more nodes in this community*

## Relationships

- [test_connection_delegates.py](test_connection_delegates.py.md) (23 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (10 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (6 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (1 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 203 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*