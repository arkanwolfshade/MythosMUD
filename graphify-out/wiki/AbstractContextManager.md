# AbstractContextManager

> 190 nodes

## Key Concepts

- **LoggedHTTPException** (401 connections) — `server/exceptions.py`
- **ContainerServiceError** (91 connections) — `server/services/container_service.py`
- **ContainerNotFoundError** (49 connections) — `server/services/container_service.py`
- **ContainerCapacityError** (45 connections) — `server/services/container_service.py`
- **ContainerAccessDeniedError** (41 connections) — `server/services/container_service.py`
- **ContainerLockedError** (38 connections) — `server/services/container_service.py`
- **container_service.py** (37 connections) — `server/services/container_service.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (24 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (22 connections) — `server/api/container_exception_handlers.py`
- **TestHelperFunctions** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestOpenContainer** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleTransferItemsExceptions** (18 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **OpenContainerRequest** (17 connections) — `server/api/container_models.py`
- **TestCloseContainer** (17 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleOpenContainerExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleLootAllExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestRequestModels** (16 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleCloseContainerExceptions** (14 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleTransferItemsExceptionsEdgeCases** (14 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 165 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (128 shared connections)
- [metrics](metrics.md) (83 shared connections)
- [APIRouter](APIRouter.md) (51 shared connections)
- [. init ()](_init_%28%29.md) (35 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (35 shared connections)
- [.initialize()](initialize%28%29.md) (28 shared connections)
- [Connection Manager](Connection_Manager.md) (24 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (22 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (22 shared connections)
- [Lock](Lock.md) (20 shared connections)
- [fetch container items()](fetch_container_items%28%29.md) (19 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (12 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 970 (62%)
- INFERRED: 583 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*