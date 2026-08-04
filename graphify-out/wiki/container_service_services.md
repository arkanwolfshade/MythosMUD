# container service services

> 38 nodes

## Key Concepts

- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **test_connection_cleanup_methods.py** (16 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **cleanup_dead_connections_impl()** (10 connections) — `server/realtime/connection_cleanup_methods.py`
- **check_and_cleanup_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **CleanupContext** (9 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **force_cleanup_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_ghost_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **Any** (6 connections)
- **.prune_stale_players()** (3 connections) — `server/realtime/connection_manager.py`
- **.cleanup_orphaned_data()** (3 connections) — `server/realtime/connection_manager.py`
- **._cleanup_ghost_players()** (3 connections) — `server/realtime/connection_manager.py`
- **._check_and_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **.force_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **UUID** (2 connections)
- **test_cleanup_dead_connections_impl_delegates()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_check_and_cleanup_impl_delegates()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_force_cleanup_impl_delegates()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_ghost_players_impl_delegates()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_prune_stale_players_impl_delegates()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_orphaned_data_impl_ages_sessions()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_dead_connections_default_when_cleaner_missing()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **Cleanup method implementations for ConnectionManager.  Thin wrappers that delega** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- **Clean up dead connections for a specific player or all players.** (1 connections) — `server/realtime/connection_cleanup_methods.py`
- *... and 13 more nodes in this community*

## Relationships

- [connection realtime delegates](connection_realtime_delegates.md) (9 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (7 shared connections)
- [Room Broadcast](Room_Broadcast.md) (6 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (3 shared connections)
- [lucidity active service](lucidity_active_service.md) (3 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (1 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_manager.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_cleanup_methods.py`

## Audit Trail

- EXTRACTED: 147 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*