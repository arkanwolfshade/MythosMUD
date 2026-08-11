# Inventory Service Helpers

> 79 nodes

## Key Concepts

- **RoomService** (72 connections) — `server/game/room_service.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **Any** (13 connections)
- **.get_room()** (11 connections) — `server/game/room_service.py`
- **TestGetContainer** (8 connections) — `server/tests/unit/test_dependency_injection.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **TestGetPlayerService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetRoomService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetStatsGenerator** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **.filter_rooms_by_exploration()** (6 connections) — `server/game/room_service.py`
- **.get_room_occupants()** (5 connections) — `server/game/room_service.py`
- **.list_rooms()** (5 connections) — `server/game/room_service.py`
- **room_service()** (5 connections) — `server/tests/unit/game/test_room_service.py`
- **.get_local_chat_scope()** (4 connections) — `server/game/room_service.py`
- **.get_room_exits()** (4 connections) — `server/game/room_service.py`
- **._lookup_explored_stable_ids()** (4 connections) — `server/game/room_service.py`
- **.test_get_room_service_success()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.get_room_by_name()** (3 connections) — `server/game/room_service.py`
- **.list_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **.validate_room_exists()** (3 connections) — `server/game/room_service.py`
- **.validate_exit_exists()** (3 connections) — `server/game/room_service.py`
- *... and 54 more nodes in this community*

## Relationships

- [Mythos Time HUD](Mythos_Time_HUD.md) (16 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (16 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (10 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (9 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (8 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (4 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (3 shared connections)
- [ASCII Map Exit Tests](ASCII_Map_Exit_Tests.md) (3 shared connections)
- [Combat Messaging Base](Combat_Messaging_Base.md) (3 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [NATS Subject Patterns](NATS_Subject_Patterns.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)

## Source Files

- `server/game/room_service.py`
- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 266 (87%)
- INFERRED: 40 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*