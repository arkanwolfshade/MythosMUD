# container_persistence.py

> 165 nodes · cohesion 0.03

## Key Concepts

- **container_persistence.py** (54 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_row_helpers.py** (53 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **test_container_persistence_extended_crud.py** (41 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **ContainerData** (34 connections) — `server/persistence/container_data.py`
- **container_helpers.py** (26 connections) — `server/persistence/container_helpers.py`
- **update_container()** (26 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_parse.py** (26 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **delete_container()** (14 connections) — `server/persistence/container_persistence.py`
- **get_decayed_containers()** (13 connections) — `server/persistence/container_query_helpers.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
- **_insert_container_row()** (11 connections) — `server/persistence/container_persistence.py`
- **_InsertBindSource** (11 connections) — `server/persistence/container_persistence.py`
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_seed_new_container_items()** (11 connections) — `server/persistence/container_persistence.py`
- **update_container_items()** (10 connections) — `server/persistence/container_helpers.py`
- **_after_container_insert()** (10 connections) — `server/persistence/container_persistence.py`
- *... and 140 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (47 shared connections)
- [container_persistence_async.py](container_persistence_async.py.md) (38 shared connections)
- [test_container_persistence.py](test_container_persistence.py.md) (19 shared connections)
- [__init__.py](__init__.py.md) (13 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (9 shared connections)
- [ValidationError](ValidationError.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_container_persistence_sql_injection.py](test_container_persistence_sql_injection.py.md) (6 shared connections)
- [exceptions.py](exceptions.py.md) (5 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)

## Source Files

- `server/persistence/container_data.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/persistence/container_query_helpers.py`
- `server/persistence/item_instance_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 852 (94%)
- INFERRED: 51 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*