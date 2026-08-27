# item_instance_persistence.py

> 25 nodes

## Key Concepts

- **item_instance_persistence.py** (21 connections) — `server/persistence/item_instance_persistence.py`
- **test_item_instance_persistence.py** (17 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **create_item_instance()** (12 connections) — `server/persistence/item_instance_persistence.py`
- **ensure_item_instance()** (12 connections) — `server/persistence/item_instance_persistence.py`
- **get_item_instance()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **Any** (7 connections)
- **_execute_item_instance_upsert()** (6 connections) — `server/persistence/item_instance_persistence.py`
- **_handle_item_instance_db_error()** (5 connections) — `server/persistence/item_instance_persistence.py`
- **_item_instance_row_values()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **test_create_item_instance_db_error()** (3 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_create_item_instance_missing_id()** (3 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_create_item_instance_success()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_ensure_item_instance_calls_create()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_get_item_instance_found()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_get_item_instance_not_found()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_item_instance_exists_false()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_item_instance_exists_true()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **Exception** (1 connections)
- **Item instance persistence operations. As documented in the restricted archives,…** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Create a new item instance in the database.** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Retrieve an item instance by ID.** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Check if an item instance exists in the database.** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Ensure an item instance exists in the database, creating it if necessary.** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Unit tests for item_instance_persistence helpers.** (1 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`

## Relationships

- [DatabaseError](DatabaseError.md) (8 shared connections)
- [item_instance_persistence_async.py](item_instance_persistence_async.py.md) (7 shared connections)
- [ContainerData](ContainerData.md) (5 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [persistence/container_helpers.py](persistence-container_helpers.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/persistence/item_instance_persistence.py`
- `server/tests/unit/persistence/test_item_instance_persistence.py`

## Audit Trail

- EXTRACTED: 75 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*