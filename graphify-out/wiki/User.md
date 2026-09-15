# User

> 510 nodes

## Key Concepts

- **User** (310 connections) — `server/models/user.py`
- **models/user.py** (67 connections) — `server/models/user.py`
- **container_endpoints_basic.py** (62 connections) — `server/api/container_endpoints_basic.py`
- **ContainerServiceError** (49 connections) — `server/services/container_service_helpers.py`
- **RateLimitError** (44 connections) — `server/exceptions.py`
- **api/container_helpers.py** (42 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (42 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TransferContainerRequest** (41 connections) — `server/api/container_models.py`
- **container_service.py** (33 connections) — `server/services/container_service.py`
- **container_endpoints_loot.py** (31 connections) — `server/api/container_endpoints_loot.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **handle_transfer_items_exceptions()** (28 connections) — `server/api/container_exception_handlers.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **test_container_exception_handlers.py** (26 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (26 connections) — `server/tests/unit/api/test_containers.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **handle_open_container_exceptions()** (23 connections) — `server/api/container_exception_handlers.py`
- **test_container_helpers_loot.py** (22 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (21 connections) — `server/api/container_exception_handlers.py`
- **ContainerNotFoundError** (20 connections) — `server/services/container_service_helpers.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- *... and 485 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (90 shared connections)
- [get_logger](get_logger.md) (87 shared connections)
- [LootAllRequest](LootAllRequest.md) (39 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (35 shared connections)
- [players.py](players.py.md) (29 shared connections)
- [maps.py](maps.py.md) (26 shared connections)
- [container_events.py](container_events.py.md) (25 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (21 shared connections)
- [test_users.py](test_users.py.md) (20 shared connections)
- [Invite](Invite.md) (17 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (16 shared connections)
- [ContainerService](ContainerService.md) (16 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/async_persistence.py`
- `server/auth/users.py`
- `server/exceptions.py`
- `server/models/user.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/services/container_service.py`
- `server/services/container_service_helpers.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 1380 (86%)
- INFERRED: 222 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*