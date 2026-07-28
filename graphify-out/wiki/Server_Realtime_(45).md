# Server Realtime (45)

> 46 nodes

## Key Concepts

- **ConnectionCleaner** (28 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Any** (15 connections)
- **UUID** (12 connections)
- **.cleanup_ghost_players()** (9 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.prune_stale_players()** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_orphaned_data()** (7 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_dead_connections()** (7 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._close_and_remove_stale_websocket()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._cleanup_dead_connections_for_player()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.check_and_cleanup()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_stale_player_data()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_online_player_ids()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._filter_actual_ghost_players()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.force_cleanup()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **_stale_prune_max_age_seconds()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.__init__()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_player_id_from_metadata()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_players_to_check()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_potential_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_ghost_players_from_room()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **__init__.py** (3 connections) — `server/realtime/maintenance/__init__.py`
- **._identify_stale_connections()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._is_websocket_dead()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Maintenance components for connection management.  This package provides modular** (1 connections) — `server/realtime/maintenance/__init__.py`
- *... and 21 more nodes in this community*

## Relationships

- [Server Persistence](Server_Persistence.md) (9 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (2 shared connections)
- [Server Realtime (43)](Server_Realtime_%2843%29.md) (1 shared connections)
- [Server Realtime (64)](Server_Realtime_%2864%29.md) (1 shared connections)
- [Server Realtime (69)](Server_Realtime_%2869%29.md) (1 shared connections)
- [Server Realtime (134)](Server_Realtime_%28134%29.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/__init__.py`
- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 174 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*