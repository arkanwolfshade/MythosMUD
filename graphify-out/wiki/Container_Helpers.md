# Container Helpers

> 13 nodes

## Key Concepts

- **persistence/container_helpers.py** (24 connections) — `server/persistence/container_helpers.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **update_container_items()** (8 connections) — `server/persistence/container_helpers.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **UUID** (3 connections)
- **_metadata_dict_from_cell()** (2 connections) — `server/persistence/container_helpers.py`
- **PsycopgConnection** (2 connections)
- **PsycopgCursor** (1 connections)
- **Helper functions for container persistence operations.** (1 connections) — `server/persistence/container_helpers.py`
- **Fetch container items directly from normalized tables. Queries…** (1 connections) — `server/persistence/container_helpers.py`
- **Update container items using stored procedures. Args: cursor: Database cursor…** (1 connections) — `server/persistence/container_helpers.py`
- **Normalize quantity/position from DB row cells; bool -> 1 (not…** (1 connections) — `server/persistence/container_helpers.py`

## Relationships

- [Container Persistence](Container_Persistence.md) (10 shared connections)
- [Test Inventory Command Coercion](Test_Inventory_Command_Coercion.md) (3 shared connections)
- [Test Container Persistence Extended Crud](Test_Container_Persistence_Extended_Crud.md) (3 shared connections)
- [Item Instance Persistence](Item_Instance_Persistence.md) (2 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (1 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (1 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (1 shared connections)
- [Container Persistence Async](Container_Persistence_Async.md) (1 shared connections)
- [Container Query Helpers Async](Container_Query_Helpers_Async.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`

## Audit Trail

- EXTRACTED: 45 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*