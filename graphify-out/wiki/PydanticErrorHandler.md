# PydanticErrorHandler

> 41 nodes

## Key Concepts

- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_validation_error()** (13 connections) — `server/error_handlers/pydantic_error_handler.py`
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
- **_ExtractedFieldErrorInfo** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._get_display_field_name()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._get_field_path()** (3 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Unpack** (3 connections)
- **StandardizedErrorResponseDict** (3 connections)
- **TypedDict** (2 connections)
- **TypedDict** (1 connections)
- **Handle a Pydantic ValidationError and convert it to a standardized response.…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Extract structured information from a Pydantic ValidationError. Args: error:…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- *... and 16 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (16 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [MythosValidationError](MythosValidationError.md) (2 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`

## Audit Trail

- EXTRACTED: 98 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*