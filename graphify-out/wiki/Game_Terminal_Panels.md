# Game Terminal Panels

> 72 nodes

## Key Concepts

- **__init__.py** (70 connections) — `server/schemas/__init__.py`
- **rooms.py** (35 connections) — `server/api/rooms.py`
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **AdminSession** (14 connections) — `server/schemas/admin/admin_data.py`
- **AuditLogEntry** (14 connections) — `server/schemas/admin/admin_data.py`
- **__init__.py** (13 connections) — `server/schemas/admin/__init__.py`
- **list_rooms()** (10 connections) — `server/api/rooms.py`
- **BaseModel** (10 connections)
- **NPCSpawnResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCDespawnResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCMoveResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCStatsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCPopulationStatsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCZoneStatsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCSystemStatusResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **AdminSessionsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **AdminAuditLogResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **AdminCleanupSessionsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **_validate_room_position_update()** (7 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (7 connections) — `server/api/rooms.py`
- *... and 47 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (35 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (18 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (6 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (6 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (6 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (6 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (5 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (4 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (4 shared connections)
- [Schedule Service Loader](Schedule_Service_Loader.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (3 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/__init__.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`

## Audit Trail

- EXTRACTED: 375 (89%)
- INFERRED: 47 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*