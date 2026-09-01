# test_connection_cleaner.py

> 29 nodes

## Key Concepts

- **test_connection_cleaner.py** (27 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **asyncio** (6 connections)
- **test_check_and_cleanup()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup_skips_when_not_due()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
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
- **Context for periodic cleanup checks. Groups parameters to stay under param-…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Unit tests for connection cleaner. Tests the ConnectionCleaner class.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() does not remove recent players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() preserves players with active websockets.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_orphaned_data() cleans up orphaned data.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_dead_connections() cleans up dead websocket connections.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_orphaned_data() closes stale active connections.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_ghost_players() removes players not in online_players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test check_and_cleanup() no-ops when memory monitor does not request cleanup.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_ghost_players() removes ghost players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- *... and 4 more nodes in this community*

## Relationships

- [fixture](fixture.md) (8 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (2 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 50 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*