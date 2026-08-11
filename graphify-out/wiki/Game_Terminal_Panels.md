# Game Terminal Panels

> 36 nodes

## Key Concepts

- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **list_rooms()** (10 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **_update_room_position_in_db()** (7 connections) — `server/api/rooms.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **room.py** (7 connections) — `server/schemas/rooms/room.py`
- **player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **Request** (5 connections)
- **AsyncSession** (4 connections)
- **_invalidate_room_cache()** (4 connections) — `server/api/rooms.py`
- **RoomPositionUpdate** (4 connections) — `server/api/rooms.py`
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- **room_data.py** (4 connections) — `server/schemas/rooms/room_data.py`
- **BaseModel** (3 connections)
- **BaseModel** (2 connections)
- **BaseModel** (1 connections)
- **Update room position in database and verify the update succeeded.** (1 connections) — `server/api/rooms.py`
- **Invalidate room cache to force reload.** (1 connections) — `server/api/rooms.py`
- **List rooms filtered by plane, zone, and optionally sub_zone.      Returns room d** (1 connections) — `server/api/rooms.py`
- **Request model for updating room map coordinates.** (1 connections) — `server/api/rooms.py`
- **Update room map coordinates (admin only).      Updates the map_x and map_y colum** (1 connections) — `server/api/rooms.py`
- *... and 11 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (20 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (4 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (4 shared connections)
- [Mythos Time HUD](Mythos_Time_HUD.md) (2 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (2 shared connections)
- [Postgres Adapter Infrastructure](Postgres_Adapter_Infrastructure.md) (1 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`

## Audit Trail

- EXTRACTED: 129 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*