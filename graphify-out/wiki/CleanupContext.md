# CleanupContext

> 15 nodes

## Key Concepts

- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **asyncio** (6 connections)
- **test_check_and_cleanup()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup_skips_when_not_due()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_dead_connections()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data_closes_stale_websocket()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_force_cleanup()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Context for periodic cleanup checks. Groups parameters to stay under param-…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Test cleanup_orphaned_data() cleans up orphaned data.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_dead_connections() cleans up dead websocket connections.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_orphaned_data() closes stale active connections.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test check_and_cleanup() no-ops when memory monitor does not request cleanup.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test force_cleanup() performs forced cleanup.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test check_and_cleanup() performs cleanup check.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Relationships

- [test_connection_cleaner.py](test_connection_cleaner.py.md) (7 shared connections)
- [test_connection_cleanup_methods.py](test_connection_cleanup_methods.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 24 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*