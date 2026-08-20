# connection_cleanup_methods.py

> 28 nodes

## Key Concepts

- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **test_connection_cleanup_methods.py** (17 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **cleanup_dead_connections_impl()** (10 connections) — `server/realtime/connection_cleanup_methods.py`
- **check_and_cleanup_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_ghost_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **force_cleanup_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **Any** (6 connections)
- **asyncio** (5 connections)
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
- **Cleanup method implementations for ConnectionManager. Thin wrappers that…** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Clean up dead connections for a specific player or all players.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Periodically check for cleanup conditions and perform cleanup if needed.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Force immediate cleanup of all orphaned data.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Clean up ghost players from all rooms.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- *... and 3 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (11 shared connections)
- [connection_manager.py](connection_manager.py.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/tests/unit/realtime/test_connection_cleanup_methods.py`

## Audit Trail

- EXTRACTED: 81 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*