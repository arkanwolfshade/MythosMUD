# .cleanup dead connections()

> 11 nodes

## Key Concepts

- **UUID** (12 connections)
- **.cleanup_dead_connections()** (7 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._cleanup_dead_connections_for_player()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.__init__()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_players_to_check()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._is_websocket_dead()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Initialize the connection cleaner.          Args:             memory_monitor: Me** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return True if websocket appears dead (should be cleaned up).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return list of player IDs to check (single player or all).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up dead connections for a single player.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up dead connections for a specific player or all players.          Args:** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [ConnectionCleaner](ConnectionCleaner.md) (11 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [. identify stale players()](_identify_stale_players%28%29.md) (3 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 39 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*