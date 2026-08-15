# PydanticErrorHandler

> 64 nodes

## Key Concepts

- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_validation_error()** (13 connections) — `server/error_handlers/pydantic_error_handler.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **MythosValidationError** (10 connections)
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
- **convert_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_error_details()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.create_handler()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._extract_error_info()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._generate_user_friendly_message()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ValidationError** (7 connections)
- **._determine_error_type()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._determine_severity()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._format_single_field_error_message()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_process_validated_command_validation_error()** (5 connections) — `server/tests/unit/commands/test_command_service.py`
- **_ExtractedFieldErrorInfo** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_SampleModel** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **._get_display_field_name()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.__init__()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.test_handle_transfer_items_exceptions_validation_error()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- *... and 39 more nodes in this community*

## Relationships

- [MythosMUDError](MythosMUDError.md) (31 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (2 shared connections)
- [test_command_service.py](test_command_service.py.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [ErrorContext](ErrorContext.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (1 shared connections)
- [test_command_processor.py](test_command_processor.py.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 132 (89%)
- INFERRED: 16 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*