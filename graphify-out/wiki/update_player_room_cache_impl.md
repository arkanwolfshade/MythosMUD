# update_player_room_cache_impl

> 6 nodes

## Key Concepts

- **update_player_room_cache_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **test_update_player_room_cache_impl_player_not_online_is_a_noop()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_update_player_room_cache_impl_refreshes_existing_entry()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **Keep online_players[...]['current_room_id'] in sync with an actual room move.…** (1 connections) — `server/realtime/connection_manager_methods.py`
- **#297/#610: online_players[...]['current_room_id'] is written once at connect…** (1 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **A player absent from online_players (e.g. NPC-driven room event, or a race with…** (1 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`

## Relationships

- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [test_connection_manager_methods.py](test_connection_manager_methods.py.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*