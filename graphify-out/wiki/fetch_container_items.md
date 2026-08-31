# fetch_container_items

> 19 nodes

## Key Concepts

- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **update_container_items()** (8 connections) — `server/persistence/container_helpers.py`
- **_run_container_update_execute()** (8 connections) — `server/persistence/container_persistence.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **test_coerce_row_quantity()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **test_coerce_item_quantity()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **UUID** (3 connections)
- **_metadata_dict_from_cell()** (2 connections) — `server/persistence/container_helpers.py`
- **test_run_container_update_execute_no_op_when_no_fields()** (2 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **PsycopgConnection** (2 connections)
- **parametrize** (2 connections)
- **PsycopgCursor** (1 connections)
- **PsycopgCursor** (1 connections)
- **Fetch container items directly from normalized tables. Queries…** (1 connections) — `server/persistence/container_helpers.py`
- **Update container items using stored procedures. Args: cursor: Database cursor…** (1 connections) — `server/persistence/container_helpers.py`
- **Normalize quantity/position from DB row cells; bool -> 1 (not…** (1 connections) — `server/persistence/container_helpers.py`
- **Apply the items/lock/metadata update; returns (container_instance_id or None,…** (1 connections) — `server/persistence/container_persistence.py`
- **Row quantity/position coercion matches item quantity rules (PR #461 /…** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Relationships

- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (11 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (1 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (1 shared connections)
- [update_container](update_container.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*