# Mythos Time HUD

> 44 nodes

## Key Concepts

- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **LoggedException** (23 connections) — `server/exceptions.py`
- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_StubBoundLogger** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_logged_http_exception_initialization()** (5 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_http_exception_inheritance()** (4 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_already_logged()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_mark_logged()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_authentication_error_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_database_error_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_database_error_without_table()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_validation_error_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_validation_error_without_field()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_rate_limit_error_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_rate_limit_error_without_retry_after()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_http_exception_with_logger_name()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **.already_logged()** (2 connections) — `server/exceptions.py`
- **BoundLogger** (2 connections)
- **Marker base class indicating an exception has already produced a log entry.** (1 connections) — `server/exceptions.py`
- **Return True if this exception instance has already been logged.** (1 connections) — `server/exceptions.py`
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- *... and 19 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (19 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (12 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (6 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (5 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (3 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (3 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/exceptions.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_exceptions.py`

## Audit Trail

- EXTRACTED: 160 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*