# CreateItemInstanceInput

> 61 nodes

## Key Concepts

- **CreateItemInstanceInput** (18 connections) — `server/async_persistence_constants.py`
- **ItemRepository** (17 connections) — `server/persistence/repositories/item_repository.py`
- **test_item_instance_persistence.py** (16 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **create_item_instance_async()** (13 connections) — `server/persistence/item_instance_persistence_async.py`
- **test_item_instance_persistence_async.py** (13 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **ensure_item_instance_async()** (12 connections) — `server/persistence/item_instance_persistence_async.py`
- **create_item_instance()** (12 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists_async()** (7 connections) — `server/persistence/item_instance_persistence_async.py`
- **get_item_instance()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **Any** (7 connections)
- **test_item_repository.py** (7 connections) — `server/tests/unit/persistence/repositories/test_item_repository.py`
- **_metadata_from_options()** (6 connections) — `server/persistence/item_instance_persistence_async.py`
- **_execute_item_instance_upsert()** (6 connections) — `server/persistence/item_instance_persistence.py`
- **_item_instance_upsert_params()** (5 connections) — `server/persistence/item_instance_persistence_async.py`
- **_run_item_instance_upsert()** (5 connections) — `server/persistence/item_instance_persistence_async.py`
- **_handle_item_instance_db_error()** (5 connections) — `server/persistence/item_instance_persistence.py`
- **.create_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **.ensure_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **asyncio** (5 connections)
- **_item_instance_row_values()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **.item_instance_exists()** (4 connections) — `server/persistence/repositories/item_repository.py`
- **test_create_item_instance_async_db_error()** (4 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **test_create_item_instance_async_missing_id()** (4 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **AsyncSession** (4 connections)
- *... and 36 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (44 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (4 shared connections)
- [container_persistence.py](container_persistence.py.md) (4 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (2 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (1 shared connections)

## Source Files

- `server/async_persistence_constants.py`
- `server/persistence/item_instance_persistence.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/item_repository.py`
- `server/tests/unit/persistence/repositories/test_item_repository.py`
- `server/tests/unit/persistence/test_item_instance_persistence.py`
- `server/tests/unit/persistence/test_item_instance_persistence_async.py`

## Audit Trail

- EXTRACTED: 152 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*