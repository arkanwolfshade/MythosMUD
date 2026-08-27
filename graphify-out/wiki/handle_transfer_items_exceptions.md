# handle_transfer_items_exceptions

> 114 nodes

## Key Concepts

- **handle_transfer_items_exceptions()** (28 connections) — `server/api/container_exception_handlers.py`
- **handle_open_container_exceptions()** (23 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (22 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **_raise_container_http()** (9 connections) — `server/api/container_exception_handlers.py`
- **_raise_unexpected_container_error()** (7 connections) — `server/api/container_exception_handlers.py`
- **Exception** (6 connections)
- **TestCreateErrorContext** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **UUID** (5 connections)
- **.test_handle_close_container_exceptions_chains_exception()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_loot_all_exceptions_chains_exception()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_open_container_exceptions_chains_exception()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_transfer_items_exceptions_chains_exception()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_close_container_exceptions_includes_context()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_loot_all_exceptions_includes_context()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_open_container_exceptions_includes_context()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_transfer_items_exceptions_includes_context()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_close_container_exceptions_invalid_token()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_close_container_exceptions_not_found()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_close_container_exceptions_service_error()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_close_container_exceptions_invalid_keyword()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_close_container_exceptions_token_keyword()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_loot_all_exceptions_access_denied()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 89 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (53 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (37 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (15 shared connections)
- [User](User.md) (6 shared connections)
- [test_containers.py](test_containers.py.md) (4 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`

## Audit Trail

- EXTRACTED: 224 (86%)
- INFERRED: 36 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*