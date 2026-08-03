# Exception Containers

> 196 nodes

## Key Concepts

- **LoggedHTTPException** (409 connections) — `server/exceptions.py`
- **ContainerServiceError** (91 connections) — `server/services/container_service.py`
- **ContainerNotFoundError** (49 connections) — `server/services/container_service.py`
- **ContainerCapacityError** (45 connections) — `server/services/container_service.py`
- **ContainerAccessDeniedError** (41 connections) — `server/services/container_service.py`
- **ContainerLockedError** (38 connections) — `server/services/container_service.py`
- **container_service.py** (37 connections) — `server/services/container_service.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (24 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (22 connections) — `server/api/container_exception_handlers.py`
- **TestHelperFunctions** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestOpenContainer** (20 connections) — `server/tests/unit/api/test_containers.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **TestHandleTransferItemsExceptions** (18 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **TestCloseContainer** (17 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleOpenContainerExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleLootAllExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestRequestModels** (16 connections) — `server/tests/unit/api/test_containers.py`
- **CloseContainerRequest** (14 connections) — `server/api/container_models.py`
- **TestHandleCloseContainerExceptions** (14 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 171 more nodes in this community*

## Relationships

- [Memory Task Runtime](Memory_Task_Runtime.md) (97 shared connections)
- [Loot Generation](Loot_Generation.md) (77 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (41 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (37 shared connections)
- [alias storage commands](alias_storage_commands.md) (37 shared connections)
- [command inventory models](command_inventory_models.md) (30 shared connections)
- [admin auth service](admin_auth_service.md) (30 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (26 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (23 shared connections)
- [profession game service](profession_game_service.md) (21 shared connections)
- [Player Stats](Player_Stats.md) (19 shared connections)
- [auth users rationale](auth_users_rationale.md) (18 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 1003 (63%)
- INFERRED: 591 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*