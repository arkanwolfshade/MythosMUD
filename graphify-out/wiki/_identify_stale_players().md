# . identify stale players()

> 6 nodes

## Key Concepts

- **.prune_stale_players()** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_stale_player_data()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Identify players whose last_seen timestamp exceeds the max age.          Args:** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove all data for a stale player.          Args:             pid: Player ID to** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove players whose presence is stale beyond the threshold.          Args:** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [ConnectionCleaner](ConnectionCleaner.md) (5 shared connections)
- [.cleanup dead connections()](cleanup_dead_connections%28%29.md) (3 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [.check and cleanup()](check_and_cleanup%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 19 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*