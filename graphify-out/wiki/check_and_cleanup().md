# .check and cleanup()

> 6 nodes

## Key Concepts

- **.check_and_cleanup()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.force_cleanup()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **_stale_prune_max_age_seconds()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Stale-prune threshold (seconds). Higher in e2e/local to avoid mid-run drops.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Force immediate cleanup of all orphaned data.          Args:             cleanup** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Periodically check for cleanup conditions and perform cleanup if needed.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [ConnectionCleaner](ConnectionCleaner.md) (4 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [. identify stale players()](_identify_stale_players%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 17 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*