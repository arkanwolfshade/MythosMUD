# Exception Containers

> 501 nodes

## Key Concepts

- **LoggedHTTPException** (474 connections) — `server/exceptions.py`
- **ContainerServiceError** (100 connections) — `server/services/container_service.py`
- **ContainerService** (80 connections) — `server/services/container_service.py`
- **test_container_service.py** (73 connections) — `server/tests/unit/services/test_container_service.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **ContainerNotFoundError** (52 connections) — `server/services/container_service.py`
- **__init__.py** (47 connections) — `server/services/__init__.py`
- **ContainerCapacityError** (47 connections) — `server/services/container_service.py`
- **ContainerAccessDeniedError** (47 connections) — `server/services/container_service.py`
- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **ContainerLockedError** (40 connections) — `server/services/container_service.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **container_service.py** (38 connections) — `server/services/container_service.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **ContainerSourceType** (28 connections) — `server/models/container.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **container.py** (26 connections) — `server/models/container.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (24 connections) — `server/api/container_exception_handlers.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 476 more nodes in this community*

## Relationships

- [commands follow rationale](commands_follow_rationale.md) (190 shared connections)
- [player requests schemas](player_requests_schemas.md) (81 shared connections)
- [task registry app](task_registry_app.md) (43 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (37 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (36 shared connections)
- [Loot Generation](Loot_Generation.md) (35 shared connections)
- [auth rationale access](auth_rationale_access.md) (32 shared connections)
- [Player Stats](Player_Stats.md) (32 shared connections)
- [profession game service](profession_game_service.md) (31 shared connections)
- [player preferences services](player_preferences_services.md) (19 shared connections)
- [command parser helpers](command_parser_helpers.md) (19 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (19 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/models/container.py`
- `server/services/__init__.py`
- `server/services/container_service.py`
- `server/services/environmental_container_loader.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 2330 (72%)
- INFERRED: 914 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*