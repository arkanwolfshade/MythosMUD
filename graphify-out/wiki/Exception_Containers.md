# Exception Containers

> 517 nodes

## Key Concepts

- **LoggedHTTPException** (474 connections) — `server/exceptions.py`
- **User** (325 connections) — `server/models/user.py`
- **ContainerServiceError** (100 connections) — `server/services/container_service.py`
- **ContainerService** (80 connections) — `server/services/container_service.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **ContainerNotFoundError** (52 connections) — `server/services/container_service.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **ContainerCapacityError** (47 connections) — `server/services/container_service.py`
- **ContainerAccessDeniedError** (47 connections) — `server/services/container_service.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **ContainerLockedError** (40 connections) — `server/services/container_service.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **container_service.py** (38 connections) — `server/services/container_service.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **ContainerSourceType** (28 connections) — `server/models/container.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **container.py** (26 connections) — `server/models/container.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (24 connections) — `server/api/container_exception_handlers.py`
- *... and 492 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (88 shared connections)
- [alias storage commands](alias_storage_commands.md) (77 shared connections)
- [Player Stats](Player_Stats.md) (57 shared connections)
- [container events rationale](container_events_rationale.md) (54 shared connections)
- [admin auth service](admin_auth_service.md) (43 shared connections)
- [command inventory models](command_inventory_models.md) (40 shared connections)
- [game models stats](game_models_stats.md) (38 shared connections)
- [task registry app](task_registry_app.md) (37 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (36 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (35 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (35 shared connections)
- [command inventory factories](command_inventory_factories.md) (31 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/models/container.py`
- `server/models/user.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 2706 (73%)
- INFERRED: 1023 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*