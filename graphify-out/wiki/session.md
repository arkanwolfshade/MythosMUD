# session

> 109 nodes

## Key Concepts

- **session()** (39 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **PlayerRepository** (35 connections) — `server/persistence/repositories/player_repository.py`
- **CreateItemInstanceInput** (18 connections) — `server/async_persistence_constants.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **ItemRepository** (17 connections) — `server/persistence/repositories/item_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **create_item_instance_async()** (13 connections) — `server/persistence/item_instance_persistence_async.py`
- **test_item_instance_persistence_async.py** (13 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **ensure_item_instance_async()** (12 connections) — `server/persistence/item_instance_persistence_async.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **.get_player_by_id()** (10 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **_delete_mutable_integration_test_rows()** (8 connections) — `server/tests/fixtures/integration/__init__.py`
- **_should_preserve_table_on_cleanup()** (8 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_cleanup_deletes_rows_from_mutable_tables()** (8 connections) — `server/tests/integration/test_integration_cleanup.py`
- **item_instance_exists_async()** (7 connections) — `server/persistence/item_instance_persistence_async.py`
- **.get_bank_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.save_player()** (7 connections) — `server/persistence/repositories/player_repository.py`
- *... and 84 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (75 shared connections)
- [ContainerRepository](ContainerRepository.md) (11 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (5 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (5 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (4 shared connections)
- [_ScalarResult](_ScalarResult.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [session_factory](session_factory.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [test_room_write_procedures.py](test_room_write_procedures.py.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [retry.py](retry.py.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/container_repository.py`
- `server/persistence/repositories/item_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/tests/fixtures/integration/__init__.py`
- `server/tests/integration/test_integration_cleanup.py`
- `server/tests/unit/game/items/test_item_effects.py`
- `server/tests/unit/persistence/repositories/test_item_repository.py`
- `server/tests/unit/persistence/test_item_instance_persistence_async.py`

## Audit Trail

- EXTRACTED: 281 (84%)
- INFERRED: 54 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*