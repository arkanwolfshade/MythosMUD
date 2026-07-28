# NPC Death Lifecycle

> 139 nodes · cohesion 0.02

## Key Concepts

- **ErrorContext** (54 connections) — `server/exceptions.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **create_error_context()** (33 connections) — `server/exceptions.py`
- **LoggedException** (23 connections) — `server/exceptions.py`
- **.__init__()** (16 connections) — `server/exceptions.py`
- **Any** (14 connections)
- **handle_exception()** (13 connections) — `server/exceptions.py`
- **.__init__()** (8 connections) — `server/exceptions.py`
- **.mark_logged()** (5 connections) — `server/exceptions.py`
- **test_handle_exception_standard_exception()** (5 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_logged_http_exception_initialization()** (5 connections) — `server/tests/unit/test_exceptions.py`
- **.test_mythos_exception_handler_sets_request_id()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **create_context_from_websocket()** (5 connections) — `server/utils/error_logging.py`
- **require_admin_user()** (4 connections) — `server/api/admin/subject_controller.py`
- **.__init__()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- *... and 114 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (66 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (10 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (9 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (9 shared connections)
- [Api Player](Api_Player.md) (8 shared connections)
- [WebSocket Coverage Gaps](WebSocket_Coverage_Gaps.md) (6 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (6 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (6 shared connections)
- [Game Client Container](Game_Client_Container.md) (5 shared connections)
- [API Type Guards](API_Type_Guards.md) (4 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (4 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 504 (96%)
- INFERRED: 22 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*