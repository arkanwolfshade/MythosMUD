# container service services

> 34 nodes

## Key Concepts

- **connection_cleanup_methods.py** (18 connections) — `server/realtime/connection_cleanup_methods.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **cleanup_dead_connections_impl()** (7 connections) — `server/realtime/connection_cleanup_methods.py`
- **check_and_cleanup_impl()** (7 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (7 connections) — `server/realtime/connection_cleanup_methods.py`
- **Any** (6 connections)
- **force_cleanup_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_ghost_players_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **.prune_stale_players()** (3 connections) — `server/realtime/connection_manager.py`
- **.cleanup_orphaned_data()** (3 connections) — `server/realtime/connection_manager.py`
- **._cleanup_ghost_players()** (3 connections) — `server/realtime/connection_manager.py`
- **._check_and_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **.force_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **test_delegate_connection_cleaner_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **UUID** (2 connections)
- **Cleanup method implementations for ConnectionManager.  Thin wrappers that delega** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Clean up dead connections for a specific player or all players.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Periodically check for cleanup conditions and perform cleanup if needed.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Force immediate cleanup of all orphaned data.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Clean up ghost players from all rooms.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Remove players whose presence is stale beyond the threshold.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Clean up orphaned data that might accumulate over time.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- *... and 9 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (15 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (9 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (1 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 120 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*