# TransferContainerRequest

> 98 nodes

## Key Concepts

- **TransferContainerRequest** (39 connections) — `server/api/container_models.py`
- **test_containers.py** (29 connections) — `server/tests/unit/api/test_containers.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **asyncio** (17 connections)
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **OpenContainerRequest** (13 connections) — `server/api/container_models.py`
- **TestOpenContainer** (11 connections) — `server/tests/unit/api/test_containers.py`
- **TestTransferItems** (11 connections) — `server/tests/unit/api/test_containers.py`
- **CloseContainerRequest** (10 connections) — `server/api/container_models.py`
- **TestHelperFunctions** (10 connections) — `server/tests/unit/api/test_containers.py`
- **get_current_user()** (9 connections) — `docs/examples/logging/fastapi_integration.py`
- **TestCloseContainer** (8 connections) — `server/tests/unit/api/test_containers.py`
- **register_basic_endpoints()** (6 connections) — `server/api/container_endpoints_basic.py`
- **.test_close_container_rate_limit()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_access_denied()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_locked()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_not_found()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_rate_limit()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_transfer_items_capacity_error()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_transfer_items_rate_limit()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_transfer_items_stale_token()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **TestRequestModels** (5 connections) — `server/tests/unit/api/test_containers.py`
- **.test_close_container_not_authenticated()** (5 connections) — `server/tests/unit/api/test_containers.py`
- *... and 73 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (56 shared connections)
- [container_events.py](container_events.py.md) (16 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [User](User.md) (7 shared connections)
- [ContainerComponent](ContainerComponent.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [general_exception_handler](general_exception_handler.md) (1 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 252 (88%)
- INFERRED: 33 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*