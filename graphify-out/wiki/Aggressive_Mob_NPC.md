# Aggressive Mob NPC

> 203 nodes

## Key Concepts

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
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
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
- **CloseContainerRequest** (14 connections) — `server/api/container_models.py`
- *... and 178 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (178 shared connections)
- [Player Effects API](Player_Effects_API.md) (38 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (24 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (22 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (17 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (15 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (14 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (8 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (3 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (1 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (1 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 859 (69%)
- INFERRED: 390 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*