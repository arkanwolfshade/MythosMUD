# connection_cleanup_methods.py

> 46 nodes

## Key Concepts

- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **test_connection_cleanup_methods.py** (17 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **cleanup_dead_connections_impl()** (10 connections) — `server/realtime/connection_cleanup_methods.py`
- **check_and_cleanup_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **cleanup_ghost_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **force_cleanup_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **Any** (6 connections)
- **asyncio** (5 connections)
- **._check_and_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **._cleanup_ghost_players()** (3 connections) — `server/realtime/connection_manager.py`
- **.cleanup_orphaned_data()** (3 connections) — `server/realtime/connection_manager.py`
- **.force_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **.prune_stale_players()** (3 connections) — `server/realtime/connection_manager.py`
- **test_check_and_cleanup_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_dead_connections_default_when_cleaner_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_dead_connections_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_orphaned_data_impl_ages_sessions()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_force_cleanup_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_delegate_connection_cleaner_sync_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_sync_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **manager()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- *... and 21 more nodes in this community*

## Relationships

- [test_connection_delegates.py](test_connection_delegates.py.md) (11 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (3 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (3 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (2 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 105 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*