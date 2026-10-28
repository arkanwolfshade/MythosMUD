# apiTypeGuards.ts

> 63 nodes · cohesion 0.06

## Key Concepts

- **test_error_handling_middleware.py** (28 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **error_handling_middleware.py** (19 connections) — `server/middleware/error_handling_middleware.py`
- **ErrorHandlingMiddleware** (17 connections) — `server/middleware/error_handling_middleware.py`
- **._handle_exception()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **register_error_handlers()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **setup_error_handling()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **_http_scope()** (8 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **add_error_handling_middleware()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.log_exception()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.__call__()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.dispatch()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **server/middleware/__init__.py** (6 connections) — `server/middleware/__init__.py`
- **asyncio** (6 connections)
- **test_log_exception_levels_and_session()** (6 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_registered_exception_handlers_return_json()** (6 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **extract_user_id_from_non_mapping()** (5 connections) — `server/middleware/error_handling_middleware.py`
- **test_handle_exception_fallback_when_handler_fails()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **FastAPI** (4 connections)
- **_error_log_kwargs()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_add_register_setup_error_handling()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_call_handles_exception()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_call_sets_request_id_and_success()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_dispatch_success_and_exception()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_adds_user_id_for_mapping_user()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- *... and 38 more nodes in this community*

## Relationships

- [AttributeError](AttributeError.md) (6 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (4 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (1 shared connections)

## Source Files

- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 132 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*