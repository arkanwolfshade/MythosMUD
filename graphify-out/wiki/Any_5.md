# Any

> 19 nodes

## Key Concepts

- **Any** (14 connections)
- **.cleanup_ghost_players()** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_orphaned_data()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._close_and_remove_stale_websocket()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_online_player_ids()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._filter_actual_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_player_id_from_metadata()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_potential_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_ghost_players_from_room()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_connections()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return connection IDs that exceed max_connection_age.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Extract player_id from connection metadata if present.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Close stale WebSocket and remove from tracking. Handles None websocket…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up orphaned data that might accumulate over time. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return set of online player IDs as strings (room._players uses string UUIDs).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return players in room but not online. Empty if room has no get_players.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Filter to players with zero WebSocket connections (or invalid UUIDs).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove ghost players from room and log.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up ghost players from all rooms. This method removes players from room's…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [ConnectionCleaner](ConnectionCleaner.md) (16 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (2 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*