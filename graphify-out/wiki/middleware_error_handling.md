# middleware error handling

> 62 nodes

## Key Concepts

- **test_error_handling_middleware.py** (28 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **ErrorHandlingMiddleware** (20 connections) — `server/middleware/error_handling_middleware.py`
- **error_handling_middleware.py** (19 connections) — `server/middleware/error_handling_middleware.py`
- **register_error_handlers()** (14 connections) — `server/middleware/error_handling_middleware.py`
- **._handle_exception()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **setup_error_handling()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **add_error_handling_middleware()** (8 connections) — `server/middleware/error_handling_middleware.py`
- **_http_scope()** (8 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.log_exception()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **__init__.py** (6 connections) — `server/middleware/__init__.py`
- **extract_user_id_from_non_mapping()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.__call__()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.dispatch()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **_UserWithId** (6 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_UserWithGet** (6 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_registered_exception_handlers_return_json()** (6 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_error_log_kwargs()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_levels_and_session()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_UserObjectWithId** (4 connections) — `server/middleware/error_handling_middleware.py`
- **FastAPI** (4 connections)
- **test_log_exception_adds_user_id_for_mapping_user()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_add_register_setup_error_handling()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Scope** (3 connections)
- **.__init__()** (3 connections) — `server/middleware/error_handling_middleware.py`
- *... and 37 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (11 shared connections)
- [Exception Containers](Exception_Containers.md) (6 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (4 shared connections)
- [player service game](player_service_game.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (1 shared connections)

## Source Files

- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 245 (93%)
- INFERRED: 19 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*