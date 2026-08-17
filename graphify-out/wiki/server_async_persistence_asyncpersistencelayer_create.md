# server async persistence asyncpersistencelayer create

> 76 nodes

## Key Concepts

- **item_instance_persistence.py** (21 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_persistence_async.py** (20 connections) — `server/persistence/item_instance_persistence_async.py`
- **CreateItemInstanceInput** (18 connections) — `server/async_persistence_constants.py`
- **ItemRepository** (17 connections) — `server/persistence/repositories/item_repository.py`
- **test_item_instance_persistence.py** (17 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **item_repository.py** (15 connections) — `server/persistence/repositories/item_repository.py`
- **test_item_instance_persistence_async.py** (14 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **create_item_instance_async()** (13 connections) — `server/persistence/item_instance_persistence_async.py`
- **ensure_item_instance_async()** (12 connections) — `server/persistence/item_instance_persistence_async.py`
- **create_item_instance()** (12 connections) — `server/persistence/item_instance_persistence.py`
- **ensure_item_instance()** (12 connections) — `server/persistence/item_instance_persistence.py`
- **EnsureItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **test_item_repository.py** (8 connections) — `server/tests/unit/persistence/repositories/test_item_repository.py`
- **item_instance_exists_async()** (7 connections) — `server/persistence/item_instance_persistence_async.py`
- **get_item_instance()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **async_persistence_constants.py** (7 connections) — `server/async_persistence_constants.py`
- **Any** (7 connections)
- **_metadata_from_options()** (6 connections) — `server/persistence/item_instance_persistence_async.py`
- **_execute_item_instance_upsert()** (6 connections) — `server/persistence/item_instance_persistence.py`
- **_item_instance_upsert_params()** (5 connections) — `server/persistence/item_instance_persistence_async.py`
- **_run_item_instance_upsert()** (5 connections) — `server/persistence/item_instance_persistence_async.py`
- **_handle_item_instance_db_error()** (5 connections) — `server/persistence/item_instance_persistence.py`
- **.create_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **.ensure_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- *... and 51 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (25 shared connections)
- [server persistence container data](server_persistence_container_data.md) (6 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (6 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (6 shared connections)
- [composed](composed.md) (5 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (4 shared connections)
- [characterinfo](characterinfo.md) (3 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (2 shared connections)
- [server persistence container persistence async](server_persistence_container_persistence_async.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/persistence/item_instance_persistence.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/item_repository.py`
- `server/tests/unit/persistence/repositories/test_item_repository.py`
- `server/tests/unit/persistence/test_item_instance_persistence.py`
- `server/tests/unit/persistence/test_item_instance_persistence_async.py`

## Audit Trail

- EXTRACTED: 201 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*