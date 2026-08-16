# PlayerRepository

> 106 nodes

## Key Concepts

- **PlayerRepository** (30 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository.py** (29 connections) — `server/persistence/repositories/player_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_player_repository_room.py** (15 connections) — `server/tests/unit/persistence/test_player_repository_room.py`
- **validate_and_fix_player_room()** (13 connections) — `server/persistence/repositories/player_repository_room.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **player_repository_save.py** (12 connections) — `server/persistence/repositories/player_repository_save.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **should_skip_room_validation()** (10 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room_with_persistence()** (10 connections) — `server/persistence/repositories/player_repository_room.py`
- **.prepare()** (10 connections) — `server/persistence/repositories/player_repository_save.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **_player()** (9 connections) — `server/tests/unit/persistence/test_player_repository_room.py`
- **player_repository_room.py** (9 connections) — `server/persistence/repositories/player_repository_room.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **._prepare_inventory_payload()** (7 connections) — `server/persistence/repositories/player_repository_save.py`
- **Any** (7 connections)
- **Player** (7 connections)
- *... and 81 more nodes in this community*

## Relationships

- [Player](Player.md) (22 shared connections)
- [log_and_raise](log_and_raise.md) (14 shared connections)
- [get_session_maker](get_session_maker.md) (13 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (6 shared connections)
- [retry.py](retry.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (5 shared connections)
- [persistence/repositories/__init__.py](persistence-repositories-__init__.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_repository_room.py`
- `server/persistence/repositories/player_repository_save.py`
- `server/tests/unit/persistence/test_player_repository_room.py`

## Audit Trail

- EXTRACTED: 265 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*