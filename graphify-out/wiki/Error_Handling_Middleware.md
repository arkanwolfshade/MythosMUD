# Error Handling Middleware

> 72 nodes

## Key Concepts

- **test_error_handling_middleware.py** (30 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **error_handling_middleware.py** (20 connections) — `server/middleware/error_handling_middleware.py`
- **ErrorHandlingMiddleware** (17 connections) — `server/middleware/error_handling_middleware.py`
- **._handle_exception()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **register_error_handlers()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **setup_error_handling()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **_http_scope()** (8 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **http_exception_handler()** (7 connections) — `docs/examples/logging/fastapi_integration.py`
- **add_error_handling_middleware()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.log_exception()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **general_exception_handler()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **.__call__()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.dispatch()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **test_registered_exception_handlers_return_json()** (6 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **server/middleware/__init__.py** (6 connections) — `server/middleware/__init__.py`
- **asyncio** (6 connections)
- **extract_user_id_from_non_mapping()** (5 connections) — `server/middleware/error_handling_middleware.py`
- **_error_log_kwargs()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_levels_and_session()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **log_api_requests()** (4 connections) — `docs/examples/logging/fastapi_integration.py`
- **test_add_register_setup_error_handling()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_call_handles_exception()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_call_sets_request_id_and_success()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_dispatch_success_and_exception()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- *... and 47 more nodes in this community*

## Relationships

- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (13 shared connections)
- [Fastapi Integration](Fastapi_Integration.md) (5 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (3 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Test Security Headers](Test_Security_Headers.md) (1 shared connections)
- [Test Openapi Tags](Test_Openapi_Tags.md) (1 shared connections)
- [Test Command Factories Utility](Test_Command_Factories_Utility.md) (1 shared connections)
- [Websocket Integration](Websocket_Integration.md) (1 shared connections)
- [Command Aliases](Command_Aliases.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 152 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*