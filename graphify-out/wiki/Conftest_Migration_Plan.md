# Conftest Migration Plan

> 95 nodes

## Key Concepts

- **Player** (22 connections)
- **UUID** (21 connections)
- **Any** (20 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (6 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **._process_exit_rows()** (4 connections) — `server/async_persistence.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence.py`
- **._query_rooms_with_exits_async()** (4 connections) — `server/async_persistence.py`
- **._parse_exits_json()** (4 connections) — `server/async_persistence.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence.py`
- **._process_combined_rows()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (4 connections) — `server/async_persistence.py`
- **.apply_fear()** (4 connections) — `server/async_persistence.py`
- **.apply_corruption()** (4 connections) — `server/async_persistence.py`
- **.heal_player()** (4 connections) — `server/async_persistence.py`
- **.async_heal_player()** (4 connections) — `server/async_persistence.py`
- *... and 70 more nodes in this community*

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (47 shared connections)
- [Persistence Item Instance](Persistence_Item_Instance.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Container System Architecture](Container_System_Architecture.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 287 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*