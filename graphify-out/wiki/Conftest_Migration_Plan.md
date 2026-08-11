# Conftest Migration Plan

> 122 nodes

## Key Concepts

- **RoomCacheLoader** (29 connections) — `server/async_persistence_room_loader.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **Any** (20 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **Any** (12 connections)
- **.load()** (10 connections) — `server/async_persistence_room_loader.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **.get_player_by_id()** (6 connections) — `server/async_persistence.py`
- **datetime** (6 connections)
- **._process_combined_rows()** (6 connections) — `server/async_persistence_room_loader.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **Profession** (5 connections)
- **._build_room_data_from_row()** (5 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (5 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (4 connections) — `server/async_persistence.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence.py`
- **._query_rooms_with_exits_async()** (4 connections) — `server/async_persistence.py`
- **._parse_exits_json()** (4 connections) — `server/async_persistence.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence.py`
- **._process_combined_rows()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- *... and 97 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (52 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (17 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (2 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (1 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (1 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_room_loader.py`

## Audit Trail

- EXTRACTED: 404 (94%)
- INFERRED: 26 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*