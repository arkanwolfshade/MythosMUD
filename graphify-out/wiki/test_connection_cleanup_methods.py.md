# test_connection_cleanup_methods.py

> 34 nodes

## Key Concepts

- **test_connection_cleanup_methods.py** (17 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **cleanup_dead_connections_impl()** (10 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_ghost_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **force_cleanup_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **Any** (6 connections)
- **asyncio** (5 connections)
- **.cleanup_dead_connections()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_ghost_players()** (3 connections) — `server/realtime/connection_manager.py`
- **.cleanup_orphaned_data()** (3 connections) — `server/realtime/connection_manager.py`
- **.force_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **.prune_stale_players()** (3 connections) — `server/realtime/connection_manager.py`
- **test_check_and_cleanup_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_dead_connections_default_when_cleaner_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_dead_connections_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_orphaned_data_impl_ages_sessions()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_force_cleanup_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **manager()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_ghost_players_impl_delegates()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_prune_stale_players_impl_delegates()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **UUID** (2 connections)
- **fixture** (1 connections)
- **Clean up dead connections for a specific player or all players.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Force immediate cleanup of all orphaned data.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- *... and 9 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [age_off_disconnected_sessions](age_off_disconnected_sessions.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_cleanup_methods.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*