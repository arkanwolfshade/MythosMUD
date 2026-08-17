# server realtime connection cleanup methods

> 28 nodes

## Key Concepts

- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **test_connection_cleanup_methods.py** (17 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **cleanup_dead_connections_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **check_and_cleanup_impl()** (7 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (7 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_ghost_players_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **force_cleanup_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
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

- [server realtime connection delegates delegate](server_realtime_connection_delegates_delegate.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server realtime maintenance connection cleaner](server_realtime_maintenance_connection_cleaner.md) (2 shared connections)
- [server realtime connection delegates](server_realtime_connection_delegates.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/tests/unit/realtime/test_connection_cleanup_methods.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*