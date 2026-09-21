# server/exceptions.py

> 271 nodes

## Key Concepts

- **server/exceptions.py** (250 connections) — `server/exceptions.py`
- **error_logging.py** (61 connections) — `server/utils/error_logging.py`
- **MythosMUDError** (53 connections) — `server/exceptions.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **ErrorContext** (40 connections) — `server/exceptions.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **standardized_responses.py** (32 connections) — `server/error_handlers/standardized_responses.py`
- **create_error_context()** (29 connections) — `server/exceptions.py`
- **test_standardized_responses.py** (29 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (22 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **LoggedException** (20 connections) — `server/exceptions.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **.__init__()** (15 connections) — `server/exceptions.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **ResourceNotFoundError** (13 connections) — `server/exceptions.py`
- **Any** (13 connections)
- **NetworkError** (12 connections) — `server/exceptions.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **emote_repository.py** (12 connections) — `server/persistence/repositories/emote_repository.py`
- **handle_exception()** (11 connections) — `server/exceptions.py`
- **log_structured_error()** (11 connections) — `server/utils/enhanced_error_logging.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **._handle_mythos_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- *... and 246 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (50 shared connections)
- [ValidationError](ValidationError.md) (50 shared connections)
- [DatabaseError](DatabaseError.md) (34 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (14 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (12 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (12 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (11 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (11 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (10 shared connections)
- [DatabaseManager](DatabaseManager.md) (10 shared connections)
- [subject_controller.py](subject_controller.py.md) (8 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/exceptions.py`
- `server/persistence/repositories/emote_repository.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 934 (97%)
- INFERRED: 29 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*