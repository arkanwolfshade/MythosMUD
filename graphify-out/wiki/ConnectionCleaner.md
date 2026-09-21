# ConnectionCleaner

> 23 nodes

## Key Concepts

- **ConnectionCleaner** (27 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Any** (14 connections)
- **.cleanup_ghost_players()** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_orphaned_data()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._close_and_remove_stale_websocket()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_online_player_ids()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._filter_actual_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_player_id_from_metadata()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_potential_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.__init__()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
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
- **Manages connection cleanup and maintenance operations. This class provides: -…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Initialize the connection cleaner. Args: memory_monitor: MemoryMonitor instance…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [UUID](UUID.md) (14 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (2 shared connections)
- [server/realtime/maintenance/__init__.py](server-realtime-maintenance-__init__.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 60 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*