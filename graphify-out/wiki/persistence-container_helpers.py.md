# persistence/container_helpers.py

> 17 nodes

## Key Concepts

- **persistence/container_helpers.py** (26 connections) — `server/persistence/container_helpers.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **update_container_items()** (8 connections) — `server/persistence/container_helpers.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **build_update_query()** (6 connections) — `server/persistence/container_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **UUID** (3 connections)
- **_metadata_dict_from_cell()** (2 connections) — `server/persistence/container_helpers.py`
- **datetime** (2 connections)
- **PsycopgConnection** (2 connections)
- **Composed** (1 connections)
- **PsycopgCursor** (1 connections)
- **Helper functions for container persistence operations.** (1 connections) — `server/persistence/container_helpers.py`
- **Fetch container items directly from normalized tables. Queries…** (1 connections) — `server/persistence/container_helpers.py`
- **Update container items using stored procedures. Args: cursor: Database cursor…** (1 connections) — `server/persistence/container_helpers.py`
- **Build SQL update query for container. Args: updates: List of update clauses…** (1 connections) — `server/persistence/container_helpers.py`
- **Normalize quantity/position from DB row cells; bool -> 1 (not…** (1 connections) — `server/persistence/container_helpers.py`

## Relationships

- [persistence/container_persistence.py](persistence-container_persistence.py.md) (11 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (3 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (2 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (2 shared connections)
- [container_query_helpers_async.py](container_query_helpers_async.py.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`

## Audit Trail

- EXTRACTED: 52 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*