# persistence/container_helpers.py

> 16 nodes

## Key Concepts

- **persistence/container_helpers.py** (24 connections) — `server/persistence/container_helpers.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **update_container_items()** (8 connections) — `server/persistence/container_helpers.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **test_coerce_row_quantity()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **UUID** (3 connections)
- **_metadata_dict_from_cell()** (2 connections) — `server/persistence/container_helpers.py`
- **PsycopgConnection** (2 connections)
- **parametrize** (2 connections)
- **PsycopgCursor** (1 connections)
- **Helper functions for container persistence operations.** (1 connections) — `server/persistence/container_helpers.py`
- **Fetch container items directly from normalized tables. Queries…** (1 connections) — `server/persistence/container_helpers.py`
- **Update container items using stored procedures. Args: cursor: Database cursor…** (1 connections) — `server/persistence/container_helpers.py`
- **Normalize quantity/position from DB row cells; bool -> 1 (not…** (1 connections) — `server/persistence/container_helpers.py`
- **Row quantity/position coercion matches item quantity rules (PR #461 /…** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Relationships

- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [ContainerData](ContainerData.md) (3 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [container_query_helpers_async.py](container_query_helpers_async.py.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 49 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*