# sanitize_detail_value

> 58 nodes · cohesion 0.04

## Key Concepts

- **sanitize_detail_value()** (19 connections) — `server/legacy_error_sanitization.py`
- **legacy_error_sanitization.py** (18 connections) — `server/legacy_error_sanitization.py`
- **sanitize_context()** (11 connections) — `server/legacy_error_sanitization.py`
- **is_safe_detail_key()** (10 connections) — `server/legacy_error_sanitization.py`
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
- **.test_sanitize_html_content_with_allowed_tags()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 33 more nodes in this community*

## Relationships

- [MythosMUDError](MythosMUDError.md) (30 shared connections)
- [ErrorContext](ErrorContext.md) (5 shared connections)
- [exceptions.py](exceptions.py.md) (1 shared connections)

## Source Files

- `server/legacy_error_sanitization.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 180 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*