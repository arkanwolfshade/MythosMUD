# roomdictlist

> 113 nodes

## Key Concepts

- **RoomService** (75 connections) — `server/game/room_service.py`
- **rooms.py** (40 connections) — `server/api/rooms.py`
- **test_rooms_api.py** (24 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **Any** (13 connections)
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **.get_room()** (8 connections) — `server/game/room_service.py`
- **rooms/room.py** (8 connections) — `server/schemas/rooms/room.py`
- **asyncio** (8 connections)
- **RoomPositionUpdateResponse** (7 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (7 connections) — `server/schemas/rooms/room.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **rooms/__init__.py** (7 connections) — `server/schemas/rooms/__init__.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **RoomData** (6 connections) — `server/schemas/rooms/room_data.py`
- **_invalidate_room_cache()** (6 connections) — `server/api/rooms.py`
- *... and 88 more nodes in this community*

## Relationships

- [dependsparam](dependsparam.md) (20 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (19 shared connections)
- [server api players](server_api_players.md) (11 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (11 shared connections)
- [server services exploration service explorationservice](server_services_exploration_service_explorationservice.md) (7 shared connections)
- [server api map helpers mapzonecontext](server_api_map_helpers_mapzonecontext.md) (5 shared connections)
- [server dependencies](server_dependencies.md) (4 shared connections)
- [server api admin npc instances](server_api_admin_npc_instances.md) (4 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (3 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (3 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (2 shared connections)
- [server api player respawn](server_api_player_respawn.md) (2 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 275 (89%)
- INFERRED: 35 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*