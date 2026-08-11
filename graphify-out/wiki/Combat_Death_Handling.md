# Combat Death Handling

> 43 nodes

## Key Concepts

- **PydanticErrorHandler** (23 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_validation_error()** (14 connections) — `server/error_handlers/pydantic_error_handler.py`
- **__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **handle_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **convert_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
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
- **Keyword arguments accepted by create_error_context and ErrorContext().** (2 connections) — `server/exceptions.py`
- **Error handlers package for MythosMUD.  This package provides specialized error h** (1 connections) — `server/error_handlers/__init__.py`
- *... and 18 more nodes in this community*

## Relationships

- [Container API Endpoints](Container_API_Endpoints.md) (17 shared connections)
- [Player Position Service](Player_Position_Service.md) (9 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (3 shared connections)
- [Archive Planning E 2 E](Archive_Planning_E_2_E.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (1 shared connections)
- [Mythos Time HUD](Mythos_Time_HUD.md) (1 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`

## Audit Trail

- EXTRACTED: 183 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*