# APIRouter

> 635 nodes

## Key Concepts

- **LoggedHTTPException** (401 connections) — `server/exceptions.py`
- **User** (306 connections) — `server/models/user.py`
- **ContainerServiceError** (91 connections) — `server/services/container_service.py`
- **ContainerService** (78 connections) — `server/services/container_service.py`
- **RateLimitError** (76 connections) — `server/exceptions.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **user.py** (57 connections) — `server/models/user.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **ContainerNotFoundError** (49 connections) — `server/services/container_service.py`
- **ContainerCapacityError** (45 connections) — `server/services/container_service.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **ContainerAccessDeniedError** (41 connections) — `server/services/container_service.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **ContainerLockedError** (38 connections) — `server/services/container_service.py`
- **container_service.py** (37 connections) — `server/services/container_service.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- *... and 610 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (133 shared connections)
- [BaseUserManager](BaseUserManager.md) (82 shared connections)
- [character creation](character_creation.md) (77 shared connections)
- [main()](main%28%29.md) (73 shared connections)
- [Request](Request.md) (65 shared connections)
- [Connection Manager](Connection_Manager.md) (56 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (54 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (34 shared connections)
- [metrics](metrics.md) (32 shared connections)
- [player respawn](player_respawn.md) (31 shared connections)
- [ContainerComponent](ContainerComponent.md) (26 shared connections)
- [monitoring](monitoring.md) (18 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/api/player_helpers.py`
- `server/auth/dependencies.py`
- `server/exceptions.py`
- `server/models/container.py`
- `server/models/user.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/services/container_service.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/api/conftest.py`

## Audit Trail

- EXTRACTED: 3324 (76%)
- INFERRED: 1052 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*