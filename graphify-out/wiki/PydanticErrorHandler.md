# PydanticErrorHandler

> 31 nodes

## Key Concepts

- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_validation_error()** (12 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_error_details()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._extract_error_info()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._generate_user_friendly_message()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ValidationError** (7 connections)
- **._determine_error_type()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._determine_severity()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._format_single_field_error_message()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_ExtractedFieldErrorInfo** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._get_display_field_name()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._get_field_path()** (3 connections) — `server/error_handlers/pydantic_error_handler.py`
- **StandardizedErrorResponseDict** (3 connections)
- **TypedDict** (2 connections)
- **Handle a Pydantic ValidationError and convert it to a standardized response.…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Extract structured information from a Pydantic ValidationError. Args: error:…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Convert Pydantic error location to a readable field path. Args: location:…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Determine the appropriate ErrorType based on error information. Args:…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Determine the appropriate ErrorSeverity based on error information. Args:…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Generate a user-friendly message for one field validation error.** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Generate a user-friendly error message from error information. Args:…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Get a user-friendly display name for a field path. Args: field_path: Field path…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- *... and 6 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (11 shared connections)
- [ErrorType](ErrorType.md) (7 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (4 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`

## Audit Trail

- EXTRACTED: 74 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*