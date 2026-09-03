# Pydantic Error Handler

> 44 nodes

## Key Concepts

- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_validation_error()** (12 connections) — `server/error_handlers/pydantic_error_handler.py`
- **MythosValidationError** (10 connections)
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
- **convert_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_error_details()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.create_handler()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._extract_error_info()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._generate_user_friendly_message()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ValidationError** (7 connections)
- **._determine_error_type()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._determine_severity()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._format_single_field_error_message()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_ExtractedFieldErrorInfo** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._get_display_field_name()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.test_handle_transfer_items_exceptions_validation_error()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **._get_field_path()** (3 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Unpack** (3 connections)
- **StandardizedErrorResponseDict** (3 connections)
- **TypedDict** (2 connections)
- **TypedDict** (1 connections)
- *... and 19 more nodes in this community*

## Relationships

- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (26 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Test Command Service](Test_Command_Service.md) (2 shared connections)
- [Test Inventory Helpers Extended](Test_Inventory_Helpers_Extended.md) (1 shared connections)
- [Test Npc Combat Integration Class](Test_Npc_Combat_Integration_Class.md) (1 shared connections)
- [Test Command Parser](Test_Command_Parser.md) (1 shared connections)
- [Test Command Processor](Test_Command_Processor.md) (1 shared connections)
- [Test Command Factories Communication](Test_Command_Factories_Communication.md) (1 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/tests/unit/api/test_container_exception_handlers.py`

## Audit Trail

- EXTRACTED: 99 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*