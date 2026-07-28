# Room Exploration API

> 44 nodes · cohesion 0.08

## Key Concepts

- **rooms.py** (35 connections) — `server/api/rooms.py`
- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (10 connections) — `server/api/rooms.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (7 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (7 connections) — `server/api/rooms.py`
- **room.py** (7 connections) — `server/schemas/rooms/room.py`
- **player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **Request** (5 connections)
- **_invalidate_room_cache()** (4 connections) — `server/api/rooms.py`
- **AsyncSession** (4 connections)
- **RoomPositionUpdate** (4 connections) — `server/api/rooms.py`
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- **room_data.py** (4 connections) — `server/schemas/rooms/room_data.py`
- **BaseModel** (3 connections)
- **BaseModel** (2 connections)
- **Any** (1 connections)
- **BaseModel** (1 connections)
- **Room management API endpoints for MythosMUD server.  This module handles all roo** (1 connections) — `server/api/rooms.py`
- *... and 19 more nodes in this community*

## Relationships

- [ASCII Map API](ASCII_Map_API.md) (17 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (7 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (6 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Admin Auth Service Tests](Admin_Auth_Service_Tests.md) (2 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`

## Audit Trail

- EXTRACTED: 189 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*