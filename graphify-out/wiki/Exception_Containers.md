# Exception Containers

> 257 nodes

## Key Concepts

- **container_endpoints_basic.py** (62 connections) — `server/api/container_endpoints_basic.py`
- **TransferContainerRequest** (56 connections) — `server/api/container_models.py`
- **container_helpers.py** (42 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (42 connections) — `server/tests/unit/api/test_container_helpers.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **test_containers.py** (26 connections) — `server/tests/unit/api/test_containers.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **OpenContainerRequest** (17 connections) — `server/api/container_models.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **TestHelperFunctions** (15 connections) — `server/tests/unit/api/test_containers.py`
- **TestOpenContainer** (15 connections) — `server/tests/unit/api/test_containers.py`
- **TestTransferItems** (15 connections) — `server/tests/unit/api/test_containers.py`
- **CloseContainerRequest** (14 connections) — `server/api/container_models.py`
- **container_models.py** (13 connections) — `server/api/container_models.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **execute_transfer()** (12 connections) — `server/api/container_helpers.py`
- **TestCloseContainer** (12 connections) — `server/tests/unit/api/test_containers.py`
- **Request** (11 connections)
- **ContainerOpenResponse** (11 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (11 connections) — `server/schemas/containers/container.py`
- **TestCreateErrorContext** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- *... and 232 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (89 shared connections)
- [player event handlers](player_event_handlers.md) (50 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (44 shared connections)
- [player requests schemas](player_requests_schemas.md) (37 shared connections)
- [alias storage commands](alias_storage_commands.md) (28 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (10 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (7 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (4 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (4 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (3 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 1084 (85%)
- INFERRED: 198 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*