# TestSanitization

> 60 nodes

## Key Concepts

- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **legacy_error_sanitization.py** (18 connections) — `server/legacy_error_sanitization.py`
- **sanitize_detail_value()** (16 connections) — `server/legacy_error_sanitization.py`
- **sanitize_context()** (11 connections) — `server/legacy_error_sanitization.py`
- **is_safe_detail_key()** (8 connections) — `server/legacy_error_sanitization.py`
- **sanitize_safe_details()** (6 connections) — `server/legacy_error_sanitization.py`
- **_collect_safe_context_fields()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_context_metadata()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_string()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_html_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_text_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_dict()** (4 connections) — `server/legacy_error_sanitization.py`
- **_truncate_detail_string()** (4 connections) — `server/legacy_error_sanitization.py`
- **.test_sanitize_context_empty()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_context_with_safe_fields()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_contains_sensitive_detail_pattern()** (3 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_list()** (3 connections) — `server/legacy_error_sanitization.py`
- **.test_sanitize_context_none()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_dict()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_int()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_list()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_long_string()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_string()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_traceback()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_html_content()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 35 more nodes in this community*

## Relationships

- [MythosMUDError](MythosMUDError.md) (21 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [ErrorContext](ErrorContext.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/legacy_error_sanitization.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 105 (88%)
- INFERRED: 14 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*