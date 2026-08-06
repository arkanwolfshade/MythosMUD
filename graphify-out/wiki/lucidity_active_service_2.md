# lucidity active service

> 38 nodes

## Key Concepts

- **test_connection_cleaner.py** (26 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
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
- **Unit tests for connection cleaner.  Tests the ConnectionCleaner class.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock memory monitor.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock rate limiter.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock message queue.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock room manager.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock cleanup_dead_websocket callback.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- *... and 13 more nodes in this community*

## Relationships

- [container service services](container_service_services.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 81 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*