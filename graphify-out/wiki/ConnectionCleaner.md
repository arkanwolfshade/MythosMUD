# ConnectionCleaner

> 34 nodes

## Key Concepts

- **ConnectionCleaner** (27 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Any** (14 connections)
- **UUID** (10 connections)
- **.cleanup_ghost_players()** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.prune_stale_players()** (7 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_dead_connections()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._cleanup_dead_connections_for_player()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._close_and_remove_stale_websocket()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_online_player_ids()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_stale_player_data()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._filter_actual_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_player_id_from_metadata()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_players_to_check()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_potential_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.__init__()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_ghost_players_from_room()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._is_websocket_dead()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Identify players whose last_seen timestamp exceeds the max age. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove all data for a stale player. Args: pid: Player ID to remove…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove players whose presence is stale beyond the threshold. Args: last_seen:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Extract player_id from connection metadata if present.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Close stale WebSocket and remove from tracking. Handles None websocket…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return True if websocket appears dead (should be cleaned up).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return list of player IDs to check (single player or all).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- *... and 9 more nodes in this community*

## Relationships

- [.check_and_cleanup](check_and_cleanup.md) (8 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (2 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (2 shared connections)
- [server/realtime/maintenance/__init__.py](server-realtime-maintenance-__init__.py.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 76 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*