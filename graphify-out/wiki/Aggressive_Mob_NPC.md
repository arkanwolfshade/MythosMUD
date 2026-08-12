# Aggressive Mob NPC

> 242 nodes

## Key Concepts

- **LoggedHTTPException** (405 connections) — `server/exceptions.py`
- **ContainerServiceError** (91 connections) — `server/services/container_service.py`
- **ContainerNotFoundError** (49 connections) — `server/services/container_service.py`
- **ContainerCapacityError** (45 connections) — `server/services/container_service.py`
- **ContainerAccessDeniedError** (41 connections) — `server/services/container_service.py`
- **ContainerLockedError** (38 connections) — `server/services/container_service.py`
- **container_service.py** (37 connections) — `server/services/container_service.py`
- **handle_transfer_items_exceptions()** (33 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **handle_open_container_exceptions()** (27 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (26 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (23 connections) — `server/api/container_exception_handlers.py`
- **TestHelperFunctions** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestOpenContainer** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestTransferItems** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleTransferItemsExceptions** (18 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **OpenContainerRequest** (17 connections) — `server/api/container_models.py`
- **TestCloseContainer** (17 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleOpenContainerExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleLootAllExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestRequestModels** (16 connections) — `server/tests/unit/api/test_containers.py`
- **.open_container()** (15 connections) — `server/services/container_service.py`
- *... and 217 more nodes in this community*

## Relationships

- [NPC Service Tests](NPC_Service_Tests.md) (98 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (76 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (68 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (55 shared connections)
- [Player Effects API](Player_Effects_API.md) (50 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (25 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (24 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (24 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (23 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (20 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (19 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (16 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/services/container_service.py`
- `server/services/user_manager.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 1160 (65%)
- INFERRED: 631 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*