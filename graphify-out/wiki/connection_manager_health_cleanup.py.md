# connection_manager_health_cleanup.py

> 43 nodes

## Key Concepts

- **connection_manager_health_cleanup.py** (29 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **delegate_connection_cleaner()** (16 connections) — `server/realtime/connection_delegates.py`
- **Any** (15 connections)
- **delegate_connection_cleaner_sync()** (12 connections) — `server/realtime/connection_delegates.py`
- **UUID** (8 connections)
- **check_connection_health_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **check_and_cleanup_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_dead_connections_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_orphaned_data_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **detect_and_handle_error_state_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_authentication_error_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_security_violation_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_websocket_error_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **recover_from_error_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_ghost_players_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **force_cleanup_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **_periodic_health_check_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **prune_stale_players_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **start_health_checks_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **stop_health_checks_impl()** (3 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **test_delegate_connection_cleaner_sync_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_sync_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Generic delegate for connection cleaner methods. Args: connection_cleaner:…** (1 connections) — `server/realtime/connection_delegates.py`
- **Generic delegate for synchronous connection cleaner methods. Args:…** (1 connections) — `server/realtime/connection_delegates.py`
- **Health checks, error handling, and cleanup helpers for ConnectionManager.…** (1 connections) — `server/realtime/connection_manager_health_cleanup.py`
- *... and 18 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (16 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [delegate_error_handler](delegate_error_handler.md) (6 shared connections)
- [test_connection_cleanup_methods.py](test_connection_cleanup_methods.py.md) (5 shared connections)
- [age_off_disconnected_sessions](age_off_disconnected_sessions.md) (2 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 107 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*