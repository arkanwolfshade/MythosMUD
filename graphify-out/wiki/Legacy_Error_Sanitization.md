# Legacy Error Sanitization

> 50 nodes · cohesion 0.05

## Key Concepts

- **sanitize_detail_value()** (19 connections) — `server/legacy_error_sanitization.py`
- **legacy_error_sanitization.py** (18 connections) — `server/legacy_error_sanitization.py`
- **sanitize_context()** (11 connections) — `server/legacy_error_sanitization.py`
- **sanitize_safe_details()** (6 connections) — `server/legacy_error_sanitization.py`
- **_collect_safe_context_fields()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_context_metadata()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_string()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_html_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_text_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_dict()** (4 connections) — `server/legacy_error_sanitization.py`
- **_truncate_detail_string()** (4 connections) — `server/legacy_error_sanitization.py`
- **Test sanitize_detail_value with string.** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_context_empty()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_context_with_safe_fields()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_contains_sensitive_detail_pattern()** (3 connections) — `server/legacy_error_sanitization.py`
- **ErrorContext** (3 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_list()** (3 connections) — `server/legacy_error_sanitization.py`
- **.test_sanitize_context_none()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_dict()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_int()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_list()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_long_string()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_string()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_traceback()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_html_content()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 25 more nodes in this community*

## Relationships

- [[Standardized Error Responses]] (33 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/legacy_error_sanitization.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 163 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
