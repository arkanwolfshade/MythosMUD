# Standardized Error Responses

> 186 nodes

## Key Concepts

- **MythosMUDError** (55 connections) — `server/exceptions.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **ErrorContext** (40 connections) — `server/exceptions.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **create_error_context()** (30 connections) — `server/exceptions.py`
- **standardized_responses.py** (26 connections) — `server/error_handlers/standardized_responses.py`
- **LoggedException** (20 connections) — `server/exceptions.py`
- **error_handling_middleware.py** (19 connections) — `server/middleware/error_handling_middleware.py`
- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **.__init__()** (15 connections) — `server/exceptions.py`
- **ResourceNotFoundError** (13 connections) — `server/exceptions.py`
- **Any** (13 connections)
- **NetworkError** (12 connections) — `server/exceptions.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **handle_exception()** (11 connections) — `server/exceptions.py`
- **GameLogicError** (9 connections) — `server/exceptions.py`
- **ConfigurationError** (8 connections) — `server/exceptions.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **.__init__()** (7 connections) — `server/exceptions.py`
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **.mark_logged()** (5 connections) — `server/exceptions.py`
- **test_handle_exception_standard_exception()** (5 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_logged_http_exception_initialization()** (5 connections) — `server/tests/unit/test_exceptions.py`
- **CombatMessages** (5 connections)
- **.__init__()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- *... and 161 more nodes in this community*

## Relationships

- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (27 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (27 shared connections)
- [Community 205](Community_205.md) (20 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (19 shared connections)
- [Container API Models](Container_API_Models.md) (18 shared connections)
- [Community 445](Community_445.md) (11 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (11 shared connections)
- [Community 116](Community_116.md) (8 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (4 shared connections)
- [Community 444](Community_444.md) (4 shared connections)
- [Community 411](Community_411.md) (4 shared connections)
- [API Response Models](API_Response_Models.md) (3 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/exceptions.py`
- `server/middleware/error_handling_middleware.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 442 (97%)
- INFERRED: 14 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*