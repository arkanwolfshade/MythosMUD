# respawn player handlers

> 61 nodes

## Key Concepts

- **rooms.py** (35 connections) — `server/api/rooms.py`
- **player_respawn.py** (24 connections) — `server/api/player_respawn.py`
- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **respawn_player_from_delirium()** (9 connections) — `server/api/player_respawn.py`
- **respawn_player()** (9 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (8 connections) — `server/schemas/players/player_respawn.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_validate_room_position_update()** (7 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (7 connections) — `server/api/rooms.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **room.py** (7 connections) — `server/schemas/rooms/room.py`
- **player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **Request** (5 connections)
- **test_handle_respawn_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_must_be_dead()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- *... and 36 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (18 shared connections)
- [auth users rationale](auth_users_rationale.md) (12 shared connections)
- [command inventory factories](command_inventory_factories.md) (12 shared connections)
- [Player Stats](Player_Stats.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (6 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (5 shared connections)
- [admin auth service](admin_auth_service.md) (5 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (4 shared connections)
- [magic healing game](magic_healing_game.md) (3 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/api/rooms.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 294 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*