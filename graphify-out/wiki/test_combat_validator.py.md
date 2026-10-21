# test_combat_validator.py

> 96 nodes · cohesion 0.03

## Key Concepts

- **ConnectionCleaner** (27 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **test_connection_cleaner.py** (26 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Any** (14 connections)
- **UUID** (10 connections)
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_ghost_players()** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **fixture** (8 connections)
- **.prune_stale_players()** (7 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.check_and_cleanup()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_dead_connections()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._cleanup_dead_connections_for_player()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_orphaned_data()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **asyncio** (6 connections)
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
- *... and 71 more nodes in this community*

## Relationships

- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (8 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [_find_item_in_inventory](_find_item_in_inventory.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/__init__.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 170 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*