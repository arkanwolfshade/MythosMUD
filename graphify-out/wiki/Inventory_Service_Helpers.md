# Inventory Service Helpers

> 51 nodes

## Key Concepts

- **RoomService** (72 connections) — `server/game/room_service.py`
- **Any** (13 connections)
- **.get_room()** (11 connections) — `server/game/room_service.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **.filter_rooms_by_exploration()** (6 connections) — `server/game/room_service.py`
- **.get_room_occupants()** (5 connections) — `server/game/room_service.py`
- **.list_rooms()** (5 connections) — `server/game/room_service.py`
- **.get_local_chat_scope()** (4 connections) — `server/game/room_service.py`
- **.get_room_exits()** (4 connections) — `server/game/room_service.py`
- **._lookup_explored_stable_ids()** (4 connections) — `server/game/room_service.py`
- **.test_get_room_service_success()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.get_room_by_name()** (3 connections) — `server/game/room_service.py`
- **.list_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **.validate_room_exists()** (3 connections) — `server/game/room_service.py`
- **.validate_exit_exists()** (3 connections) — `server/game/room_service.py`
- **._extract_occupants_from_room()** (3 connections) — `server/game/room_service.py`
- **.validate_player_in_room()** (3 connections) — `server/game/room_service.py`
- **._room_matches_zone_filters()** (3 connections) — `server/game/room_service.py`
- **._prepare_room_for_list()** (3 connections) — `server/game/room_service.py`
- **UUID** (3 connections)
- **.get_environment_state()** (3 connections) — `server/game/room_service.py`
- **.search_rooms_by_name()** (3 connections) — `server/game/room_service.py`
- **.get_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **room_service_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- *... and 26 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (22 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (7 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (7 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (3 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (2 shared connections)
- [ASCII Map Exit Tests](ASCII_Map_Exit_Tests.md) (2 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (1 shared connections)

## Source Files

- `server/game/room_service.py`
- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 189 (90%)
- INFERRED: 21 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*