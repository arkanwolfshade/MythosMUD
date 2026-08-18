# server error handlers pydantic error

> 46 nodes

## Key Concepts

- **create_error_context()** (35 connections) — `server/exceptions.py`
- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_validation_error()** (13 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
- **convert_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_error_details()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.create_handler()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._extract_error_info()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._generate_user_friendly_message()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ValidationError** (7 connections)
- **._determine_error_type()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._determine_severity()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._format_single_field_error_message()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_ExtractedFieldErrorInfo** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._get_display_field_name()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.__init__()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._get_field_path()** (3 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_create_error_context()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **Unpack** (3 connections)
- **StandardizedErrorResponseDict** (3 connections)
- **TypedDict** (2 connections)
- **TypedDict** (1 connections)
- *... and 21 more nodes in this community*

## Relationships

- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (27 shared connections)
- [server error types errorseverity](server_error_types_errorseverity.md) (8 shared connections)
- [server api admin subject controller](server_api_admin_subject_controller.md) (6 shared connections)
- [server monitoring exception metrics](server_monitoring_exception_metrics.md) (6 shared connections)
- [server exceptions authenticationerror init](server_exceptions_authenticationerror_init.md) (5 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (3 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (2 shared connections)
- [server tests unit test legacy](server_tests_unit_test_legacy.md) (1 shared connections)
- [server game player service playerservice](server_game_player_service_playerservice.md) (1 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 131 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*