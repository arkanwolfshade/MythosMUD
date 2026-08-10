# Aggressive Mob NPC

> 598 nodes

## Key Concepts

- **LoggedHTTPException** (405 connections) — `server/exceptions.py`
- **ContainerComponent** (104 connections) — `server/models/container.py`
- **ContainerServiceError** (91 connections) — `server/services/container_service.py`
- **ContainerService** (78 connections) — `server/services/container_service.py`
- **LootAllRequest** (63 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (49 connections) — `server/api/container_endpoints_basic.py`
- **ContainerNotFoundError** (49 connections) — `server/services/container_service.py`
- **__init__.py** (47 connections) — `server/services/__init__.py`
- **ContainerCapacityError** (45 connections) — `server/services/container_service.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **ContainerAccessDeniedError** (41 connections) — `server/services/container_service.py`
- **ContainerLockedError** (38 connections) — `server/services/container_service.py`
- **container_service.py** (37 connections) — `server/services/container_service.py`
- **loot_all_items()** (35 connections) — `server/api/container_endpoints_loot.py`
- **handle_transfer_items_exceptions()** (33 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **container_endpoints_loot.py** (30 connections) — `server/api/container_endpoints_loot.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **handle_open_container_exceptions()** (27 connections) — `server/api/container_exception_handlers.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **container_exception_handlers.py** (26 connections) — `server/api/container_exception_handlers.py`
- **container.py** (26 connections) — `server/models/container.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- *... and 573 more nodes in this community*

## Relationships

- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (129 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (81 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (74 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (47 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (44 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (36 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (35 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (33 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (30 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (28 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (26 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (19 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/auth/dependencies.py`
- `server/exceptions.py`
- `server/models/container.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/services/__init__.py`
- `server/services/container_service.py`
- `server/services/inventory_service.py`
- `server/services/passive_lucidity_flux_service.py`
- `server/services/user_manager.py`
- `server/tests/unit/api/conftest.py`

## Audit Trail

- EXTRACTED: 2878 (77%)
- INFERRED: 867 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*