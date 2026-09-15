# container_persistence.py

> 69 nodes

## Key Concepts

- **container_persistence.py** (53 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_row_helpers.py** (53 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **ensure_item_instance()** (12 connections) — `server/persistence/item_instance_persistence.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
- **_after_container_insert()** (11 connections) — `server/persistence/container_persistence.py`
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_insert_container_row()** (10 connections) — `server/persistence/container_persistence.py`
- **UUID** (10 connections)
- **_seed_new_container_items()** (9 connections) — `server/persistence/container_persistence.py`
- **update_container_items()** (8 connections) — `server/persistence/container_helpers.py`
- **_run_container_update_execute()** (8 connections) — `server/persistence/container_persistence.py`
- **_InsertBindSource** (7 connections) — `server/persistence/container_persistence.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **_CreateOutcome** (6 connections) — `server/persistence/container_persistence.py`
- **_as_opt_datetime()** (6 connections) — `server/persistence/container_persistence.py`
- **_as_uuid()** (6 connections) — `server/persistence/container_persistence.py`
- **_metadata_from_row()** (6 connections) — `server/persistence/container_persistence.py`
- **ContainerData** (6 connections)
- **_allowed_roles_from_row()** (5 connections) — `server/persistence/container_persistence.py`
- **_as_opt_uuid()** (5 connections) — `server/persistence/container_persistence.py`
- **_fetch_container_row_dict()** (5 connections) — `server/persistence/container_persistence.py`
- *... and 44 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (28 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (19 shared connections)
- [ContainerData](ContainerData.md) (12 shared connections)
- [ContainerRepository](ContainerRepository.md) (9 shared connections)
- [update_container](update_container.md) (9 shared connections)
- [fetch_container_items](fetch_container_items.md) (4 shared connections)
- [CreateItemInstanceInput](CreateItemInstanceInput.md) (4 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (3 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)
- [test_container_persistence_extended_parse.py](test_container_persistence_extended_parse.py.md) (1 shared connections)
- [test_persistence_container_persistence.py](test_persistence_container_persistence.py.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/persistence/item_instance_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 251 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*