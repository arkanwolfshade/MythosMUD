# Community 422

> 42 nodes

## Key Concepts

- **rooms.py** (60 connections) — `server/api/rooms.py`
- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **_validate_admin_room_action()** (12 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (10 connections) — `server/api/rooms.py`
- **Request** (10 connections)
- **_update_room_position_in_db()** (9 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (9 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **asyncio** (8 connections)
- **RoomPositionUpdateResponse** (7 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (7 connections) — `server/schemas/rooms/room.py`
- **rooms/room.py** (7 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **test_update_room_position_room_missing()** (6 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_get_room_not_found()** (5 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_get_room_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_invalidate_room_cache()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_list_rooms_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_not_found()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_validate_room_position_update_requires_auth()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_success()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **BaseModel** (3 connections)
- *... and 17 more nodes in this community*

## Relationships

- [Community 179](Community_179.md) (38 shared connections)
- [Community 320](Community_320.md) (12 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (11 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (11 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (8 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (4 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (3 shared connections)
- [Community 1191](Community_1191.md) (3 shared connections)
- [Community 855](Community_855.md) (3 shared connections)
- [Admin NPC Management API](Admin_NPC_Management_API.md) (3 shared connections)
- [Community 45](Community_45.md) (3 shared connections)
- [Community 98](Community_98.md) (2 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/rooms/room.py`
- `server/tests/unit/api/test_rooms_api.py`

## Audit Trail

- EXTRACTED: 177 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*