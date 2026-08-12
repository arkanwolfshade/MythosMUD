# Error Handling Middleware

> 54 nodes

## Key Concepts

- **error_handling_middleware.py** (19 connections) — `server/middleware/error_handling_middleware.py`
- **ErrorHandlingMiddleware** (14 connections) — `server/middleware/error_handling_middleware.py`
- **test_error_handling_middleware.py** (13 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **register_error_handlers()** (11 connections) — `server/middleware/error_handling_middleware.py`
- **._handle_exception()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **setup_error_handling()** (8 connections) — `server/middleware/error_handling_middleware.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.log_exception()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **__init__.py** (6 connections) — `server/middleware/__init__.py`
- **extract_user_id_from_non_mapping()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.__call__()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.dispatch()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **add_error_handling_middleware()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **_error_log_kwargs()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_UserObjectWithId** (4 connections) — `server/middleware/error_handling_middleware.py`
- **FastAPI** (4 connections)
- **_UserWithGet** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_adds_user_id_for_mapping_user()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Scope** (3 connections)
- **.__init__()** (3 connections) — `server/middleware/error_handling_middleware.py`
- **_UserWithId** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_request_id_from_scope()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_mapping_user_missing_id_sets_none()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Receive** (2 connections)
- *... and 29 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (6 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (3 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Command Parser](Command_Parser.md) (1 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (1 shared connections)

## Source Files

- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 180 (90%)
- INFERRED: 21 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*