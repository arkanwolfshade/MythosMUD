# Realtime Maintenance Connection

> 6 nodes · cohesion 0.33

## Key Concepts

- **.check_and_cleanup()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.force_cleanup()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **_stale_prune_max_age_seconds()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Stale-prune threshold (seconds). Higher in e2e/local to avoid mid-run drops.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Force immediate cleanup of all orphaned data.          Args:             cleanup** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Periodically check for cleanup conditions and perform cleanup if needed.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [[Realtime Maintenance Connection]] (5 shared connections)
- [[Room Occupant Events]] (2 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
