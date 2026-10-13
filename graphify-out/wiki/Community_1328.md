# Community 1328

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

- [Community 788](Community_788.md) (3 shared connections)
- [Community 843](Community_843.md) (2 shared connections)
- [Community 591](Community_591.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*