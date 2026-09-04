# Container Persistence Async

> 60 nodes

## Key Concepts

- **test_container_persistence_async_helpers.py** (41 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- **container_persistence_async.py** (36 connections) — `server/persistence/container_persistence_async.py`
- **create_container_async()** (15 connections) — `server/persistence/container_persistence_async.py`
- **get_container_async()** (15 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (14 connections) — `server/persistence/container_persistence_async.py`
- **_finalize_container_creation()** (13 connections) — `server/persistence/container_persistence_async.py`
- **fetch_container_items_async()** (12 connections) — `server/persistence/container_persistence_async.py`
- **Any** (12 connections)
- **asyncio** (12 connections)
- **_container_data_from_row()** (11 connections) — `server/persistence/container_persistence_async.py`
- **delete_container_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **_populate_container_items_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **_call_create_container_procedure()** (9 connections) — `server/persistence/container_persistence_async.py`
- **AsyncSession** (9 connections)
- **_build_item_dict()** (8 connections) — `server/persistence/container_persistence_async.py`
- **_parse_jsonb()** (7 connections) — `server/persistence/container_persistence_async.py`
- **_row_to_mapping()** (7 connections) — `server/persistence/container_persistence_async.py`
- **_validate_container_create_params()** (7 connections) — `server/persistence/container_persistence_async.py`
- **_parse_item_metadata()** (6 connections) — `server/persistence/container_persistence_async.py`
- **_prepare_container_create_params()** (6 connections) — `server/persistence/container_persistence_async.py`
- **UUID** (6 connections)
- **ContainerData** (5 connections)
- **test_call_create_container_procedure_no_row()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- **test_delete_container_async_db_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- **test_populate_container_items_skips_invalid_and_failed()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- *... and 35 more nodes in this community*

## Relationships

- [Test Container Persistence Extended Crud](Test_Container_Persistence_Extended_Crud.md) (13 shared connections)
- [Container Query Helpers Async](Container_Query_Helpers_Async.md) (8 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (6 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (6 shared connections)
- [Container Repository](Container_Repository.md) (4 shared connections)
- [Container Persistence](Container_Persistence.md) (4 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (4 shared connections)
- [Item Instance Persistence](Item_Instance_Persistence.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (1 shared connections)
- [Container Helpers](Container_Helpers.md) (1 shared connections)

## Source Files

- `server/persistence/container_persistence_async.py`
- `server/tests/unit/persistence/test_container_persistence_async_helpers.py`

## Audit Trail

- EXTRACTED: 194 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*