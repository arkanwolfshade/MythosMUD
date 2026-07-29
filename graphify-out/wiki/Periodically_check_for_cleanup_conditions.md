# Periodically check for cleanup conditions

> 30 nodes

## Key Concepts

- **connection_cleanup_methods.py** (12 connections) — `server/realtime/connection_cleanup_methods.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_connections_impl()** (7 connections) — `server/realtime/connection_cleanup_methods.py`
- **Any** (6 connections)
- **check_and_cleanup_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **force_cleanup_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_ghost_players_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **test_delegate_connection_cleaner_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **.prune_stale_players()** (3 connections) — `server/realtime/connection_manager.py`
- **.cleanup_orphaned_data()** (3 connections) — `server/realtime/connection_manager.py`
- **._cleanup_ghost_players()** (3 connections) — `server/realtime/connection_manager.py`
- **._check_and_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **.force_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **UUID** (2 connections)
- **Test delegate_connection_cleaner() returns default when cleaner is None.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Cleanup method implementations for ConnectionManager.  Thin wrappers that dele** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Clean up dead connections for a specific player or all players.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Periodically check for cleanup conditions and perform cleanup if needed.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Force immediate cleanup of all orphaned data.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Clean up ghost players from all rooms.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Remove players whose presence is stale beyond the threshold.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Clean up orphaned data that might accumulate over time.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Generic delegate for connection cleaner methods.      Args:         connection_c** (1 connections) — `server/realtime/connection_delegates.py`
- *... and 5 more nodes in this community*

## Relationships

- [connection delegates](connection_delegates.md) (9 shared connections)
- [Any](Any.md) (7 shared connections)
- [Player](Player.md) (6 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 100 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*