# Container API Endpoints

> 229 nodes · cohesion 0.02

## Key Concepts

- **LoggedHTTPException** (401 connections) — `server/exceptions.py`
- **ContainerServiceError** (91 connections) — `server/services/container_service.py`
- **ContainerNotFoundError** (49 connections) — `server/services/container_service.py`
- **ContainerCapacityError** (45 connections) — `server/services/container_service.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **ContainerAccessDeniedError** (41 connections) — `server/services/container_service.py`
- **ContainerLockedError** (38 connections) — `server/services/container_service.py`
- **container_service.py** (37 connections) — `server/services/container_service.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (24 connections) — `server/api/container_exception_handlers.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **handle_close_container_exceptions()** (22 connections) — `server/api/container_exception_handlers.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **TestHandleTransferItemsExceptions** (18 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestHandleLootAllExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleOpenContainerExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleContainerServiceErrorEdgeCases** (15 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestExceptionChaining** (14 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestExceptionHandlerContext** (14 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 204 more nodes in this community*

## Relationships

- [Inventory Service Helpers](Inventory_Service_Helpers.md) (160 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (82 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (60 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (35 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (34 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (31 shared connections)
- [Communication Command Handlers](Communication_Command_Handlers.md) (30 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (20 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (18 shared connections)
- [Player Effects API](Player_Effects_API.md) (17 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (15 shared connections)
- [Services Inventory Mutation](Services_Inventory_Mutation.md) (14 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/exceptions.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 1186 (68%)
- INFERRED: 557 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*