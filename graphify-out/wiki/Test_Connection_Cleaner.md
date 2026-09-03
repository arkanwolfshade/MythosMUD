# Test Connection Cleaner

> 44 nodes

## Key Concepts

- **test_connection_cleaner.py** (27 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **fixture** (8 connections)
- **asyncio** (6 connections)
- **connection_cleaner()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup_skips_when_not_due()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_cleanup_dead_websocket()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_get_async_persistence()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_has_websocket_connection()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_memory_monitor()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_message_queue()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_rate_limiter()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_room_manager()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_dead_connections()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data_closes_stale_websocket()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_force_cleanup()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_ghost_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_ghost_players_removes_offline_room_members()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_connection_cleaner_init()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_not_stale()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_with_websockets()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Unit tests for connection cleaner. Tests the ConnectionCleaner class.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() does not remove recent players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- *... and 19 more nodes in this community*

## Relationships

- [Connection Cleaner](Connection_Cleaner.md) (3 shared connections)
- [Connection Cleanup Methods](Connection_Cleanup_Methods.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 61 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*