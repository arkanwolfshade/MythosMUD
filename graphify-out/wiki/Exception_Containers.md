# Exception Containers

> 504 nodes

## Key Concepts

- **LoggedHTTPException** (408 connections) — `server/exceptions.py`
- **ContainerServiceError** (91 connections) — `server/services/container_service.py`
- **ContainerService** (78 connections) — `server/services/container_service.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **ContainerNotFoundError** (49 connections) — `server/services/container_service.py`
- **ContainerCapacityError** (45 connections) — `server/services/container_service.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **ContainerAccessDeniedError** (41 connections) — `server/services/container_service.py`
- **ContainerLockedError** (38 connections) — `server/services/container_service.py`
- **container_service.py** (37 connections) — `server/services/container_service.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (24 connections) — `server/api/container_exception_handlers.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **handle_close_container_exceptions()** (22 connections) — `server/api/container_exception_handlers.py`
- **TestHelperFunctions** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestOpenContainer** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestTransferItems** (20 connections) — `server/tests/unit/api/test_containers.py`
- *... and 479 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (128 shared connections)
- [auth users rationale](auth_users_rationale.md) (114 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (90 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (40 shared connections)
- [Player Stats](Player_Stats.md) (39 shared connections)
- [health models rationale](health_models_rationale.md) (34 shared connections)
- [command inventory factories](command_inventory_factories.md) (33 shared connections)
- [admin auth service](admin_auth_service.md) (30 shared connections)
- [NATS Messaging](NATS_Messaging.md) (21 shared connections)
- [respawn player handlers](respawn_player_handlers.md) (18 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (16 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (14 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/exceptions.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 2355 (73%)
- INFERRED: 872 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*