# UUID

> 15 nodes

## Key Concepts

- **UUID** (10 connections)
- **.prune_stale_players()** (7 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_dead_connections()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._cleanup_dead_connections_for_player()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_stale_player_data()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_players_to_check()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._is_websocket_dead()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Identify players whose last_seen timestamp exceeds the max age. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove all data for a stale player. Args: pid: Player ID to remove…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove players whose presence is stale beyond the threshold. Args: last_seen:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return True if websocket appears dead (should be cleaned up).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return list of player IDs to check (single player or all).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up dead connections for a single player.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up dead connections for a specific player or all players. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [ConnectionCleaner](ConnectionCleaner.md) (14 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*