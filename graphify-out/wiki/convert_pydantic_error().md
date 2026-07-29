# convert pydantic error()

> 38 nodes

## Key Concepts

- **PydanticErrorHandler** (23 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_validation_error()** (14 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **convert_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ValidationError** (7 connections)
- **._extract_error_info()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._generate_user_friendly_message()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_error_details()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.create_handler()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._determine_error_type()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._determine_severity()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._format_single_field_error_message()** (5 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_ExtractedFieldErrorInfo** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._get_display_field_name()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **StandardizedErrorResponseDict** (3 connections)
- **._get_field_path()** (3 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Unpack** (3 connections)
- **TypedDict** (2 connections)
- **Intermediate field error extracted from a Pydantic ValidationError.** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Structured information extracted from a Pydantic ValidationError.** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Handler for processing Pydantic validation errors into user-friendly messages.** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Handle a Pydantic ValidationError and convert it to a standardized response.** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- *... and 13 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (29 shared connections)
- [MythosValidationError](MythosValidationError.md) (2 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`

## Audit Trail

- EXTRACTED: 162 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*