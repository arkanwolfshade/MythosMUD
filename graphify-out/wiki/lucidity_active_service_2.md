# lucidity active service

> 46 nodes

## Key Concepts

- **test_connection_cleaner.py** (26 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **CleanupContext** (9 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **connection_cleaner()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup_skips_when_not_due()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_memory_monitor()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_rate_limiter()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_message_queue()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_room_manager()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_cleanup_dead_websocket()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_has_websocket_connection()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_get_async_persistence()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_connection_cleaner_init()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_not_stale()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_with_websockets()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_dead_connections()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data_closes_stale_websocket()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_ghost_players_removes_offline_room_members()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_stale_prune_max_age_local()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_ghost_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_force_cleanup()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Context for periodic cleanup checks. Groups parameters to stay under param-count** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Unit tests for connection cleaner.  Tests the ConnectionCleaner class.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- *... and 21 more nodes in this community*

## Relationships

- [taunt combat commands](taunt_combat_commands.md) (3 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (3 shared connections)
- [container service services](container_service_services.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 102 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*