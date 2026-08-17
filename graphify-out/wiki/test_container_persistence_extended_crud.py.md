# test_container_persistence_extended_crud.py

> 60 nodes

## Key Concepts

- **test_container_persistence_extended_crud.py** (42 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **delete_container()** (13 connections) — `server/persistence/container_persistence.py`
- **get_decayed_containers()** (13 connections) — `server/persistence/container_query_helpers.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **test_create_container_uuid_string_conversion()** (6 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_create_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_create_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_entity_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_create_container_wraps_psycopg2_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **Any** (4 connections)
- **ContainerData** (4 connections)
- **test_delete_container_not_found()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_uuid_string_conversion()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_not_found()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_entity_id_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- *... and 35 more nodes in this community*

## Relationships

- [persistence/container_persistence.py](persistence-container_persistence.py.md) (25 shared connections)
- [get_logger](get_logger.md) (21 shared connections)
- [ContainerData](ContainerData.md) (19 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (6 shared connections)
- [test_container_persistence_crud.py](test_container_persistence_crud.py.md) (5 shared connections)
- [update_container](update_container.md) (5 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/persistence/container_persistence.py`
- `server/persistence/container_query_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 153 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*