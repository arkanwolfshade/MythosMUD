# connection_manager_health_cleanup.py

> 66 nodes

## Key Concepts

- **connection_manager_health_cleanup.py** (30 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **Any** (15 connections)
- **Any** (13 connections)
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (9 connections) — `server/realtime/connection_delegates.py`
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **delegate_health_monitor_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **check_connection_health_impl()** (8 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **UUID** (8 connections)
- **check_and_cleanup_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_dead_connections_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_orphaned_data_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **detect_and_handle_error_state_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_authentication_error_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_security_violation_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_websocket_error_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **recover_from_error_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_ghost_players_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **force_cleanup_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **_periodic_health_check_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **prune_stale_players_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **start_health_checks_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **stop_health_checks_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- *... and 41 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (28 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (17 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)
- [time.py](time.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (1 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 175 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*