# TestLegacyHandlerSecurity

> 5 nodes

## Key Concepts

- **TestLegacyHandlerSecurity** (6 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_logged_http_exception_does_not_expose_raw_detail()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **._response_message()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_http_exception_does_not_expose_raw_detail()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Public error.message must not echo HTTPException detail with internal paths.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (1 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*