# memory leak metrics

> 41 nodes

## Key Concepts

- **rooms.py** (35 connections) — `server/api/rooms.py`
- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **list_rooms()** (10 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **_validate_room_position_update()** (7 connections) — `server/api/rooms.py`
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
- **Room management API endpoints for MythosMUD server.  This module handles all roo** (1 connections) — `server/api/rooms.py`
- **Validate authentication and admin permissions for room position update.** (1 connections) — `server/api/rooms.py`
- **Update room position in database and verify the update succeeded.** (1 connections) — `server/api/rooms.py`
- *... and 16 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (13 shared connections)
- [metrics](metrics.md) (12 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (6 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (2 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)
- [test player preferences service](test_player_preferences_service.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [test security headers](test_security_headers.md) (1 shared connections)
- [.mock cursor()](mock_cursor%28%29.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`

## Audit Trail

- EXTRACTED: 174 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*