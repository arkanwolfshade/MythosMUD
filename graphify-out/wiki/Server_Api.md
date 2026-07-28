# Server Api

> 405 nodes

## Key Concepts

- **LoggedHTTPException** (401 connections) — `server/exceptions.py`
- **log_and_raise()** (164 connections) — `server/utils/error_logging.py`
- **ContainerServiceError** (91 connections) — `server/services/container_service.py`
- **ContainerService** (75 connections) — `server/services/container_service.py`
- **ContainerNotFoundError** (49 connections) — `server/services/container_service.py`
- **__init__.py** (47 connections) — `server/services/__init__.py`
- **ContainerCapacityError** (45 connections) — `server/services/container_service.py`
- **ContainerAccessDeniedError** (41 connections) — `server/services/container_service.py`
- **InventoryService** (41 connections) — `server/services/inventory_service.py`
- **ContainerLockedError** (38 connections) — `server/services/container_service.py`
- **container_service.py** (37 connections) — `server/services/container_service.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **inventory_service.py** (28 connections) — `server/services/inventory_service.py`
- **InventoryCapacityError** (27 connections) — `server/services/inventory_service.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (24 connections) — `server/api/container_exception_handlers.py`
- **WearableContainerService** (23 connections) — `server/services/wearable_container_service.py`
- **handle_close_container_exceptions()** (22 connections) — `server/api/container_exception_handlers.py`
- **SlotValidationError** (22 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **equipment_service.py** (21 connections) — `server/services/equipment_service.py`
- *... and 380 more nodes in this community*

## Relationships

- [Server Api (2)](Server_Api_%282%29.md) (230 shared connections)
- [Server Admin](Server_Admin.md) (103 shared connections)
- [Server Commands (2)](Server_Commands_%282%29.md) (36 shared connections)
- [Server Utils](Server_Utils.md) (29 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (29 shared connections)
- [Server Api (4)](Server_Api_%284%29.md) (26 shared connections)
- [Server Services (22)](Server_Services_%2822%29.md) (26 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (24 shared connections)
- [Server Auth (2)](Server_Auth_%282%29.md) (21 shared connections)
- [Server Persistence (3)](Server_Persistence_%283%29.md) (21 shared connections)
- [Server Api (5)](Server_Api_%285%29.md) (20 shared connections)
- [Server Commands](Server_Commands.md) (17 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/commands/inventory_service_helpers.py`
- `server/exceptions.py`
- `server/services/__init__.py`
- `server/services/container_service.py`
- `server/services/equipment_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/services/test_equipment_service.py`
- `server/tests/unit/services/test_inventory_service.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 2128 (73%)
- INFERRED: 804 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*