# api/player_respawn.py

> 61 nodes

## Key Concepts

- **api/player_respawn.py** (29 connections) — `server/api/player_respawn.py`
- **test_player_respawn_api.py** (18 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_player_respawn_handlers.py** (16 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **rooms/room.py** (8 connections) — `server/schemas/rooms/room.py`
- **asyncio** (8 connections)
- **RoomPositionUpdateResponse** (7 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (7 connections) — `server/schemas/rooms/room.py`
- **players/player_respawn.py** (7 connections) — `server/schemas/players/player_respawn.py`
- **rooms/__init__.py** (7 connections) — `server/schemas/rooms/__init__.py`
- **RoomData** (6 connections) — `server/schemas/rooms/room_data.py`
- **test_respawn_player_from_delirium_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_validation_error()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_delirium_unexpected_error()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_from_delirium_success()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_no_session()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- *... and 36 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (40 shared connections)
- [PlayerService](PlayerService.md) (13 shared connections)
- [ValidationError](ValidationError.md) (13 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [BaseCommand](BaseCommand.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 180 (87%)
- INFERRED: 26 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*