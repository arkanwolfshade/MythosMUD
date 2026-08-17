# asyncio

> 13 nodes

## Key Concepts

- **asyncio** (6 connections)
- **test_check_and_cleanup()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup_skips_when_not_due()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_dead_connections()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data_closes_stale_websocket()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_force_cleanup()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_orphaned_data() cleans up orphaned data.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_dead_connections() cleans up dead websocket connections.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_orphaned_data() closes stale active connections.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test check_and_cleanup() no-ops when memory monitor does not request cleanup.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test force_cleanup() performs forced cleanup.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test check_and_cleanup() performs cleanup check.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Relationships

- [test_connection_cleaner.py](test_connection_cleaner.py.md) (6 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 18 (90%)
- INFERRED: 2 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*