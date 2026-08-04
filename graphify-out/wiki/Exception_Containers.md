# Exception Containers

> 511 nodes

## Key Concepts

- **LoggedHTTPException** (474 connections) — `server/exceptions.py`
- **ContainerServiceError** (100 connections) — `server/services/container_service.py`
- **ContainerService** (80 connections) — `server/services/container_service.py`
- **RateLimitError** (76 connections) — `server/exceptions.py`
- **test_container_service.py** (73 connections) — `server/tests/unit/services/test_container_service.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **ContainerNotFoundError** (52 connections) — `server/services/container_service.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **ContainerCapacityError** (47 connections) — `server/services/container_service.py`
- **ContainerAccessDeniedError** (47 connections) — `server/services/container_service.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **ContainerLockedError** (40 connections) — `server/services/container_service.py`
- **container_service.py** (38 connections) — `server/services/container_service.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (24 connections) — `server/api/container_exception_handlers.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **handle_close_container_exceptions()** (22 connections) — `server/api/container_exception_handlers.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- *... and 486 more nodes in this community*

## Relationships

- [task registry app](task_registry_app.md) (119 shared connections)
- [player requests schemas](player_requests_schemas.md) (110 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (68 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (41 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (41 shared connections)
- [Player Stats](Player_Stats.md) (34 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (30 shared connections)
- [profession game service](profession_game_service.md) (29 shared connections)
- [Loot Generation](Loot_Generation.md) (24 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (21 shared connections)
- [command parser helpers](command_parser_helpers.md) (19 shared connections)
- [health models rationale](health_models_rationale.md) (17 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/services/container_service.py`
- `server/services/environmental_container_loader.py`
- `server/services/user_manager.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 2391 (71%)
- INFERRED: 962 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*