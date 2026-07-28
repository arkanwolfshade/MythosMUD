# Server Persistence (2)

> 88 nodes

## Key Concepts

- **test_container_persistence_extended_crud.py** (41 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **ContainerData** (34 connections) — `server/persistence/container_data.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **ContainerDataExtras** (18 connections) — `server/persistence/container_data.py`
- **delete_container()** (14 connections) — `server/persistence/container_persistence.py`
- **get_decayed_containers()** (13 connections) — `server/persistence/container_query_helpers.py`
- **container_data.py** (12 connections) — `server/persistence/container_data.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **test_create_container_uuid_string_conversion()** (6 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_create_container_success()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_uuid_string_conversion()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_items_missing_item_instance_id()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_items_only_prototype_id()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_container_data_to_dict()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_container_data_to_dict_none_values()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **Any** (4 connections)
- **ContainerData** (4 connections)
- **test_create_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- *... and 63 more nodes in this community*

## Relationships

- [Server Persistence (5)](Server_Persistence_%285%29.md) (43 shared connections)
- [Server Persistence](Server_Persistence.md) (14 shared connections)
- [Server Persistence (9)](Server_Persistence_%289%29.md) (10 shared connections)
- [Server Persistence (7)](Server_Persistence_%287%29.md) (10 shared connections)
- [Server Persistence (16)](Server_Persistence_%2816%29.md) (7 shared connections)
- [Server Persistence (6)](Server_Persistence_%286%29.md) (7 shared connections)
- [Server Api](Server_Api.md) (5 shared connections)
- [Server Admin](Server_Admin.md) (3 shared connections)
- [Server Persistence (15)](Server_Persistence_%2815%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Container Persistence](Server_Container_Persistence.md) (1 shared connections)

## Source Files

- `server/persistence/container_data.py`
- `server/persistence/container_persistence.py`
- `server/persistence/container_query_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 357 (92%)
- INFERRED: 32 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*