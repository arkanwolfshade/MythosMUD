# .check_and_cleanup

> 8 nodes

## Key Concepts

- **.check_and_cleanup()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **_stale_prune_max_age_seconds()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.force_cleanup()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **test_stale_prune_max_age_local()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Stale-prune threshold (seconds). Higher in e2e/local to avoid mid-run drops.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Force immediate cleanup of all orphaned data. Args: cleanup_stats: Cleanup…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Periodically check for cleanup conditions and perform cleanup if needed. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Test _stale_prune_max_age_seconds uses longer threshold in local env.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Relationships

- [ConnectionCleaner](ConnectionCleaner.md) (4 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*