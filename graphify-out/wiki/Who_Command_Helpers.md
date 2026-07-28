# Who Command Helpers

> 38 nodes · cohesion 0.05

## Key Concepts

- **test_connection_cleaner.py** (22 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **connection_cleaner()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_cleanup_dead_websocket()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_get_async_persistence()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_has_websocket_connection()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_memory_monitor()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_message_queue()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_rate_limiter()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_room_manager()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_dead_connections()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_ghost_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_connection_cleaner_init()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_force_cleanup()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_not_stale()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_with_websockets()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Context for periodic cleanup checks. Groups parameters to stay under param-count** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Unit tests for connection cleaner.  Tests the ConnectionCleaner class.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() does not remove recent players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() preserves players with active websockets.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_orphaned_data() cleans up orphaned data.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_dead_connections() cleans up dead connections.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- *... and 13 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Realtime Maintenance Connection](Realtime_Maintenance_Connection.md) (3 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (2 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 84 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*