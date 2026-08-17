# ConnectionCleaner

> 44 nodes

## Key Concepts

- **ConnectionCleaner** (27 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Any** (14 connections)
- **UUID** (10 connections)
- **.cleanup_ghost_players()** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.prune_stale_players()** (7 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.check_and_cleanup()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_dead_connections()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._cleanup_dead_connections_for_player()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_orphaned_data()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._close_and_remove_stale_websocket()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_online_player_ids()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_stale_player_data()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **_stale_prune_max_age_seconds()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._filter_actual_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.force_cleanup()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_player_id_from_metadata()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_players_to_check()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_potential_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.__init__()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_ghost_players_from_room()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_connections()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._is_websocket_dead()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Identify players whose last_seen timestamp exceeds the max age. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove all data for a stale player. Args: pid: Player ID to remove…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- *... and 19 more nodes in this community*

## Relationships

- [MemoryMonitor](MemoryMonitor.md) (4 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (3 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 88 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*