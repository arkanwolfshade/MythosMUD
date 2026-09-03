# Container Persistence

> 77 nodes

## Key Concepts

- **test_container_persistence_extended_row_helpers.py** (54 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **container_persistence.py** (53 connections) — `server/persistence/container_persistence.py`
- **update_container()** (26 connections) — `server/persistence/container_persistence.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **delete_container()** (13 connections) — `server/persistence/container_persistence.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
- **_after_container_insert()** (11 connections) — `server/persistence/container_persistence.py`
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_insert_container_row()** (10 connections) — `server/persistence/container_persistence.py`
- **UUID** (10 connections)
- **_seed_new_container_items()** (9 connections) — `server/persistence/container_persistence.py`
- **_run_container_update_execute()** (8 connections) — `server/persistence/container_persistence.py`
- **_InsertBindSource** (7 connections) — `server/persistence/container_persistence.py`
- **validate_lock_state()** (7 connections) — `server/persistence/container_helpers.py`
- **_CreateOutcome** (6 connections) — `server/persistence/container_persistence.py`
- **_as_opt_datetime()** (6 connections) — `server/persistence/container_persistence.py`
- **_as_uuid()** (6 connections) — `server/persistence/container_persistence.py`
- **_metadata_from_row()** (6 connections) — `server/persistence/container_persistence.py`
- **ContainerData** (6 connections)
- **_allowed_roles_from_row()** (5 connections) — `server/persistence/container_persistence.py`
- **_as_opt_uuid()** (5 connections) — `server/persistence/container_persistence.py`
- **_fetch_container_row_dict()** (5 connections) — `server/persistence/container_persistence.py`
- *... and 52 more nodes in this community*

## Relationships

- [Test Container Persistence Extended Crud](Test_Container_Persistence_Extended_Crud.md) (43 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (11 shared connections)
- [Container Helpers](Container_Helpers.md) (10 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (8 shared connections)
- [Container Repository](Container_Repository.md) (7 shared connections)
- [Test Container Persistence Sql Injection](Test_Container_Persistence_Sql_Injection.md) (6 shared connections)
- [Container Persistence Async](Container_Persistence_Async.md) (4 shared connections)
- [Item Instance Persistence](Item_Instance_Persistence.md) (3 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (3 shared connections)
- [Container Query Helpers Async](Container_Query_Helpers_Async.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 272 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*