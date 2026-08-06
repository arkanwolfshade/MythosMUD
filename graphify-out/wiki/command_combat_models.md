# command combat models

> 138 nodes

## Key Concepts

- **container_persistence.py** (42 connections) — `server/container_persistence/container_persistence.py`
- **test_container_persistence_crud.py** (42 connections) — `server/tests/unit/container_persistence/test_container_persistence_crud.py`
- **ContainerCreateParams** (34 connections) — `server/persistence/container_create_params.py`
- **container_helpers.py** (25 connections) — `server/container_persistence/container_helpers.py`
- **create_container()** (23 connections) — `server/container_persistence/container_persistence.py`
- **_container_data_from_dict()** (18 connections) — `server/container_persistence/container_persistence.py`
- **update_container()** (17 connections) — `server/container_persistence/container_persistence.py`
- **get_container()** (15 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_entity_id()** (13 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_room_id()** (12 connections) — `server/container_persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_complete_container_create()** (11 connections) — `server/container_persistence/container_persistence.py`
- **delete_container()** (11 connections) — `server/container_persistence/container_persistence.py`
- **UUID** (10 connections)
- **_execute_container_update()** (9 connections) — `server/container_persistence/container_persistence.py`
- **__init__.py** (8 connections) — `server/container_persistence/__init__.py`
- **ContainerData** (8 connections) — `server/container_persistence/container_data.py`
- **ContainerData** (8 connections)
- **validate_update_lock_state()** (7 connections) — `server/container_persistence/container_helpers.py`
- **fetch_container_items()** (7 connections) — `server/container_persistence/container_helpers.py`
- **validate_create_container_args()** (6 connections) — `server/container_persistence/container_helpers.py`
- **UUID** (6 connections)
- **as_uuid()** (6 connections) — `server/container_persistence/container_helpers.py`
- **as_opt_datetime()** (6 connections) — `server/container_persistence/container_helpers.py`
- **_map_container_content_row()** (6 connections) — `server/container_persistence/container_helpers.py`
- *... and 113 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (15 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (13 shared connections)
- [add used user](add_used_user.md) (12 shared connections)
- [commands party examples](commands_party_examples.md) (11 shared connections)
- [command inventory models](command_inventory_models.md) (9 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (1 shared connections)

## Source Files

- `server/container_persistence/__init__.py`
- `server/container_persistence/container_data.py`
- `server/container_persistence/container_helpers.py`
- `server/container_persistence/container_persistence.py`
- `server/persistence/container_create_params.py`
- `server/tests/unit/container_persistence/test_container_persistence_crud.py`

## Audit Trail

- EXTRACTED: 579 (96%)
- INFERRED: 25 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*