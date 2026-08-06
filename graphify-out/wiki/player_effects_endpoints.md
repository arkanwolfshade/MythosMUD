# player effects endpoints

> 93 nodes

## Key Concepts

- **container_service.py** (33 connections) — `server/services/container_service.py`
- **container_service_transfer_to.py** (33 connections) — `server/services/container_service_transfer_to.py`
- **container_service_transfer_from.py** (26 connections) — `server/services/container_service_transfer_from.py`
- **container_service_helpers.py** (23 connections) — `server/services/container_service_helpers.py`
- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **ContainerSessionMixin** (18 connections) — `server/services/container_service_session.py`
- **ContainerTransferFromMixin** (18 connections) — `server/services/container_service_transfer_from.py`
- **filter_container_data()** (14 connections) — `server/services/container_service_helpers.py`
- **audit_logger.py** (14 connections) — `server/utils/audit_logger.py`
- **as_object_dict()** (12 connections) — `server/services/container_service_helpers.py`
- **._execute_transfer_from_container()** (12 connections) — `server/services/container_service_transfer_from.py`
- **._require_container_component()** (12 connections) — `server/services/container_service_transfer_to.py`
- **._execute_transfer_to_container()** (12 connections) — `server/services/container_service_transfer_to.py`
- **get_enum_value()** (11 connections) — `server/services/container_service_helpers.py`
- **.open_container()** (11 connections) — `server/services/container_service_session.py`
- **._raise_if_cannot_open_locks()** (10 connections) — `server/services/container_service_session.py`
- **UUID** (10 connections)
- **._finalize_loot_all()** (10 connections) — `server/services/container_service_transfer_from.py`
- **UUID** (9 connections)
- **._add_item_to_player_inventory()** (9 connections) — `server/services/container_service_transfer_from.py`
- **._persist_and_audit_transfer_from_container()** (9 connections) — `server/services/container_service_transfer_from.py`
- **UUID** (9 connections)
- **.transfer_to_container()** (9 connections) — `server/services/container_service_transfer_to.py`
- **player_inventory_for_response()** (8 connections) — `server/services/container_service_helpers.py`
- **InventoryStack** (8 connections)
- *... and 68 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (36 shared connections)
- [add used user](add_used_user.md) (34 shared connections)
- [task registry app](task_registry_app.md) (20 shared connections)
- [alias storage commands](alias_storage_commands.md) (12 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (10 shared connections)
- [player event handlers](player_event_handlers.md) (8 shared connections)
- [Exception Containers](Exception_Containers.md) (4 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [command inventory models](command_inventory_models.md) (3 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (3 shared connections)
- [player room realtime](player_room_realtime.md) (2 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/container_service_helpers.py`
- `server/services/container_service_session.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`
- `server/tests/unit/services/test_container_service.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 507 (92%)
- INFERRED: 44 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*