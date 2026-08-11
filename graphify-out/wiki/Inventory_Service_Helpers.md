# Inventory Service Helpers

> 49 nodes

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
- **.__init__()** (2 connections) — `server/game/room_service.py`
- *... and 24 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (13 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (10 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (8 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (6 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (4 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (4 shared connections)
- [ASCII Map Exit Tests](ASCII_Map_Exit_Tests.md) (2 shared connections)
- [Config Model Tests](Config_Model_Tests.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)

## Source Files

- `server/game/room_service.py`
- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 185 (90%)
- INFERRED: 20 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*