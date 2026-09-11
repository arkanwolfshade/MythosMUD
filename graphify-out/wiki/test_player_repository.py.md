# test_player_repository.py

> 137 nodes

## Key Concepts

- **test_player_repository.py** (47 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **PlayerRepository** (32 connections) — `server/persistence/repositories/player_repository.py`
- **asyncio** (26 connections)
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **retry_with_backoff()** (14 connections) — `server/utils/retry.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **_make_mock_row()** (10 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **_ScalarResult** (6 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **_SessionCM** (6 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **.save_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.update_player_last_active()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **test_save_player_allows_new_player()** (6 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_save_player_refuses_deleted_player()** (6 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **UUID** (6 connections)
- **.delete_player()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.save_players()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.soft_delete_player()** (5 connections) — `server/persistence/repositories/player_repository.py`
- *... and 112 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (26 shared connections)
- [Player](Player.md) (13 shared connections)
- [get_session_maker](get_session_maker.md) (12 shared connections)
- [retry.py](retry.py.md) (7 shared connections)
- [Room](Room.md) (4 shared connections)
- [PlayerInventory](PlayerInventory.md) (3 shared connections)
- [item_instance_persistence_async.py](item_instance_persistence_async.py.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (1 shared connections)
- [test_player_repository_room.py](test_player_repository_room.py.md) (1 shared connections)
- [_StubPlayerRepo](_StubPlayerRepo.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/tests/unit/persistence/test_player_repository.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 273 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*