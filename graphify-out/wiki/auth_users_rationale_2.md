# auth users rationale

> 70 nodes

## Key Concepts

- **test_container_persistence_extended_crud.py** (41 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **ContainerData** (35 connections) — `server/persistence/container_data.py`
- **__init__.py** (32 connections) — `server/persistence/__init__.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **get_decayed_containers()** (13 connections) — `server/persistence/container_query_helpers.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **test_create_container_uuid_string_conversion()** (6 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_create_container_success()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Any** (4 connections)
- **ContainerData** (4 connections)
- **test_create_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_entity_id_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_entity_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_not_found()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- *... and 45 more nodes in this community*

## Relationships

- [retry nats handler](retry_nats_handler.md) (39 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (23 shared connections)
- [persistence container item](persistence_container_item.md) (12 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (4 shared connections)
- [command combat models](command_combat_models.md) (4 shared connections)
- [world loader room](world_loader_room.md) (4 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (4 shared connections)
- [persistence protocols rationale](persistence_protocols_rationale.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (3 shared connections)
- [commands time handle](commands_time_handle.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [add used user](add_used_user.md) (1 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/container_data.py`
- `server/persistence/container_query_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Audit Trail

- EXTRACTED: 287 (92%)
- INFERRED: 24 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*