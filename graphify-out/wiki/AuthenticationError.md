# AuthenticationError

> 72 nodes

## Key Concepts

- **AuthenticationError** (46 connections) — `server/exceptions.py`
- **TestErrorMapping** (32 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_map_error_type()** (23 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (22 connections) — `server/exceptions.py`
- **_get_status_code_for_error()** (19 connections) — `server/legacy_error_handlers.py`
- **_get_severity_for_error()** (18 connections) — `server/legacy_error_handlers.py`
- **ConfigurationError** (17 connections) — `server/exceptions.py`
- **GameLogicError** (16 connections) — `server/exceptions.py`
- **.test_get_severity_for_error_authentication()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_severity_for_error_configuration()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_severity_for_error_database()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_severity_for_error_unknown()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_authentication()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_database()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_not_found()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_rate_limit()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_unknown()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_validation()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_authentication()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_configuration()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_database()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_game_logic()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_network()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_not_found()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_rate_limit()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 47 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (25 shared connections)
- [DatabaseError](DatabaseError.md) (22 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (22 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (16 shared connections)
- [MythosMUDError](MythosMUDError.md) (11 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (6 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (6 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (3 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (3 shared connections)

## Source Files

- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 164 (73%)
- INFERRED: 62 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*