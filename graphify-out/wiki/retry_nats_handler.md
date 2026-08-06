# retry nats handler

> 72 nodes

## Key Concepts

- **container_persistence.py** (54 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_row_helpers.py** (53 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **ContainerDataCore** (26 connections) — `server/persistence/container_data.py`
- **update_container()** (26 connections) — `server/persistence/container_persistence.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **delete_container()** (14 connections) — `server/persistence/container_persistence.py`
- **_InsertBindSource** (11 connections) — `server/persistence/container_persistence.py`
- **_insert_container_row()** (11 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **_seed_new_container_items()** (11 connections) — `server/persistence/container_persistence.py`
- **UUID** (10 connections)
- **_CreateOutcome** (10 connections) — `server/persistence/container_persistence.py`
- **_after_container_insert()** (10 connections) — `server/persistence/container_persistence.py`
- **_run_container_update_execute()** (9 connections) — `server/persistence/container_persistence.py`
- **validate_lock_state()** (8 connections) — `server/persistence/container_helpers.py`
- **_as_uuid()** (6 connections) — `server/persistence/container_persistence.py`
- **_as_opt_datetime()** (6 connections) — `server/persistence/container_persistence.py`
- **_metadata_from_row()** (6 connections) — `server/persistence/container_persistence.py`
- **_validate_new_container_params()** (6 connections) — `server/persistence/container_persistence.py`
- **ContainerData** (6 connections)
- **_as_opt_uuid()** (5 connections) — `server/persistence/container_persistence.py`
- **datetime** (5 connections)
- *... and 47 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (39 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (26 shared connections)
- [persistence container item](persistence_container_item.md) (13 shared connections)
- [commands time handle](commands_time_handle.md) (11 shared connections)
- [add used user](add_used_user.md) (6 shared connections)
- [command combat models](command_combat_models.md) (6 shared connections)
- [headers middleware security](headers_middleware_security.md) (6 shared connections)
- [commands party examples](commands_party_examples.md) (5 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (5 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [world loader room](world_loader_room.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)

## Source Files

- `server/persistence/container_data.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 468 (95%)
- INFERRED: 25 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*