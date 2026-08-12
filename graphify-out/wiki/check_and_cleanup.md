# .check_and_cleanup

> 10 nodes

## Key Concepts

- **.check_and_cleanup()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_orphaned_data()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.force_cleanup()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **_stale_prune_max_age_seconds()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_connections()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return connection IDs that exceed max_connection_age.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up orphaned data that might accumulate over time. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Stale-prune threshold (seconds). Higher in e2e/local to avoid mid-run drops.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Force immediate cleanup of all orphaned data. Args: cleanup_stats: Cleanup…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Periodically check for cleanup conditions and perform cleanup if needed. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [ConnectionCleaner](ConnectionCleaner.md) (7 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (1 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*