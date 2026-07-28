# Server (4)

> 35 nodes

## Key Concepts

- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_map_error_type()** (15 connections) — `server/legacy_error_handlers.py`
- **_get_status_code_for_error()** (11 connections) — `server/legacy_error_handlers.py`
- **.test_map_error_type_authentication()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_validation()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_not_found()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_rate_limit()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_game_logic()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_database()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_network()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_configuration()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_map_error_type_unknown()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_severity_for_error_database()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_authentication()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_validation()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_not_found()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_rate_limit()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_database()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_get_status_code_for_error_unknown()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test _map_error_type for AuthenticationError.** (2 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test _map_error_type for RateLimitError.** (2 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test _get_status_code_for_error for AuthenticationError.** (2 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Map MythosMUD error types to standardized error types.** (1 connections) — `server/legacy_error_handlers.py`
- **Get appropriate HTTP status code for error type.** (1 connections) — `server/legacy_error_handlers.py`
- **Test error type and status code mapping functions.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 10 more nodes in this community*

## Relationships

- [Server Error Handlers](Server_Error_Handlers.md) (33 shared connections)
- [Server Persistence](Server_Persistence.md) (4 shared connections)
- [Server Utils](Server_Utils.md) (3 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (3 shared connections)
- [Server Api](Server_Api.md) (1 shared connections)

## Source Files

- `server/legacy_error_handlers.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 130 (90%)
- INFERRED: 14 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*